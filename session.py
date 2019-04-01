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

    # Get sessionid from cookie
    sessionid = request.get_cookie(COOKIE_NAME)
    cur.execute("SELECT sessionid FROM sessions WHERE sessionid=?", (sessionid,))

    # If no existing session: create new session
    if not cur.fetchone():
        # Use uuid library to generate random sessionid
        sessionid = str(uuid.uuid4())

        # Store new sessionid in database
        cur.execute("INSERT INTO sessions VALUES (?, '')", (sessionid,))
        db.commit()

        # Set cookie expiry time to 1 week
        expiry = datetime.datetime.now() + datetime.timedelta(days=7)

        # Set cookie
        response.set_cookie(COOKIE_NAME, sessionid, path="/", expires=expiry)

    # Return sessionid
    return sessionid


def add_to_cart(db, itemid, quantity):
    """Add an item to the shopping cart"""


def get_cart_contents(db):
    """Return the contents of the shopping cart as
    a list of dictionaries:
    [{'id': <id>, 'quantity': <qty>, 'name': <name>, 'cost': <cost>}, ...]
    """


