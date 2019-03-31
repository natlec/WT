"""
Code for handling sessions in our web application
"""

from bottle import request, response
import uuid
import json
import datetime

import model
import dbschema

COOKIE_NAME = 'session'


def get_or_create_session(db):
    """Get the current sessionid either from a
    cookie in the current request or by creating a
    new session if none are present.

    If a new session is created, a cookie is set in the response.

    Returns the session key (string)
    """

    # Create session table
    cur = db.cursor()
    cur.execute("DROP TABLE IF EXISTS session")
    cur.execute("""
    CREATE TABLE session (
        key text unique primary key
    )
    """)

    # Get session key from cookie
    key = request.get_cookie(COOKIE_NAME)
    cur.execute("SELECT key FROM session WHERE key=?", (key,))
    row = cur.fetchone()

    # If no existing session: create new session instead
    if not row:
        # Use uuid library to generate random key
        key = str(uuid.uuid4())

        # Store new session key in database
        cur.execute("INSERT INTO session VALUES (?)", (key,))
        db.commit()

        # Set cookie expiry time
        expiry = datetime.datetime.now() + datetime.timedelta(days=1)

        # Set cookie
        response.set_cookie(COOKIE_NAME, key, path="/", expires=expiry)

    # Return session key
    return key


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""


def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """


