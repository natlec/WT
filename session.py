"""
Code for handling sessions in our web application
"""

from bottle import request, response
import uuid
import json
import datetime

import model
import dbschema

from bisect import bisect_left

COOKIE_NAME = 'session'


def get_or_create_session(db):
    """Get the current sessionid either from a
    cookie in the current request or by creating a
    new session if none are present.

    If a new session is created, a cookie is set in the response.

    Returns the session key (string)
    """

    cur = db.cursor()

    # Get sessionid from cookie
    sessionid = request.get_cookie(COOKIE_NAME)
    cur.execute("""SELECT sessionid FROM sessions WHERE sessionid=?""", (sessionid,))

    # If no existing session: create new session
    if not cur.fetchone():
        # Use uuid library to generate random sessionid
        sessionid = str(uuid.uuid4())

        # Store new sessionid in database
        cur.execute("""INSERT INTO sessions VALUES (?, '[]')""", (sessionid,))
        db.commit()

        # Set cookie expiry time to 1 week
        expiry = datetime.datetime.now() + datetime.timedelta(days=7)

        # Set cookie
        response.set_cookie(COOKIE_NAME, sessionid, path="/", expires=expiry)

    # Return sessionid
    return sessionid


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""

    cur = db.cursor()

    # Get sessionid from cookie
    sessionid = request.get_cookie(COOKIE_NAME)

    # Get data of item to add
    product = model.product_get(db, itemid)

    # Get cart list
    cart = get_cart_contents(db)
    if cart == None:
        cart = []

    # Create new item to add
    item = {'id': itemid, 'quantity': int(quantity), 'name': product['name'], 'cost': float(product['unit_cost']), 'image': product['image_url']}

    # Check if item exists
    exists = False
    for i in cart:
        if i['id'] == itemid:
            # Update existing item quantity
            i['quantity'] += int(quantity)
            exists = True
            break
    if not exists:
        # Add new item to cart list
        cart.append(item)    

    # Add new cart list to database for this session
    cur.execute("""UPDATE sessions SET data=? WHERE sessionid=?""", (json.dumps(cart), sessionid,))
    db.commit()


def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """

    cur = db.cursor()
    
    # Get sessionid from cookie
    sessionid = request.get_cookie(COOKIE_NAME)

    # Get cart items from sessions table in database (only for this session)
    cur.execute("""SELECT data FROM sessions WHERE sessionid=? AND data<>''""", (sessionid,))
    row = cur.fetchone()

    # Return cart items
    return json.loads(row['data']) if row != None else None
