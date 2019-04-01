
import random
from bottle import Bottle, template, static_file, request, redirect, HTTPError, HTTPResponse, response

import model
import session

app = Bottle()


# Homepage / All products page
@app.route('/')
def index(db):

    # Get or set session cookie
    session.get_or_create_session(db)

    # Info relative to page
    info = {
        'page': '',
        'title': 'All products',
        'description': 'Explore our entire range of products for both men & women. ',
        'cart': 0
    }

    # Get products list
    info['products'] = model.product_list(db)

    return template('index', info)


# Homepage / Products by category page
@app.route('/<category>')
def products(db, category):

    # Get or set session cookie
    session.get_or_create_session(db)

    # Check if category exists
    if category == 'men' or category == 'women':

        # Info relative to page
        info = {
            'page': category,
            'title': "%s's products" % category,
            'description': "Explore our entire range of %s's products." % category,
            'cart': 0
        }

        # Get products list
        info['products'] = model.product_list(db, category)

        return template('index', info)
    else:
        return HTTPResponse(status=404)


# Cart page
@app.route('/cart')
def cart(db):

    # Get or set session cookie
    session.get_or_create_session(db)

    # Info relative to page
    info = {
        'page': 'cart',
        'title': 'Shopping cart',
        'cart': 0
    }

    return template('cart', info)


# Add to cart request
@app.post('/cart')
def addToCart(db):

    # Get or set session cookie
    session.get_or_create_session(db)

    # Info relative to page
    info = {
        'page': 'cart',
        'title': 'Shopping cart',
        'cart': 0
    }
    
    return template('cart', info)


# Product page
@app.route('/product/<id>')
def product(db, id):

    # Get or set session cookie
    session.get_or_create_session(db)

    # Info relative to page
    info = {
        'page': 'product',
        'cart': 0
    }

    # Get product data
    info['product'] = model.product_get(db, id)

    # Check if product exists
    if info['product'] != None:
        return template('product', info)
    else:
        return HTTPResponse(status=404)


# Static files (CSS / Fonts / Images)
@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


# Start Bottle on port 8010
if __name__ == '__main__':

    import bottle_sqlite as sqlite
    from dbschema import DATABASE_NAME
    # Install database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
