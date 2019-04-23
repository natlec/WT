
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

    # Get cart contents from database
    cart = session.get_cart_contents(db)

    # Info relative to page
    info = {
        'page': '',
        'title': 'All products',
        'description': 'Explore our entire range of products for both men & women. ',
        'cart': 0
    }

    # Get cart items count
    if cart:
        for item in cart:
            info['cart'] += int(item['quantity'])

    # Get products list
    info['products'] = model.product_list(db)

    return template('index', info)


# Homepage / Products by category page
@app.route('/<category>')
def products(db, category):

    # Get or set session cookie
    session.get_or_create_session(db)

    # Get cart contents from database
    cart = session.get_cart_contents(db)

    # Check if category exists
    if category == 'men' or category == 'women':

        # Info relative to page
        info = {
            'page': category,
            'title': "%s's products" % category,
            'description': "Explore our entire range of %s's products." % category,
            'cart': 0
        }

        # Get cart items count
        if cart:
            for item in cart:
                info['cart'] += int(item['quantity'])

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

    # Get cart contents from database
    cart = session.get_cart_contents(db)

    # Info relative to page
    info = {
        'page': 'cart',
        'title': 'Shopping cart',
        'description': "You've added the following items to your shopping cart:",
        'cart': 0,
        'total': 0
    }

    # Get item list for cart
    info['products'] = cart

    # Get cart items count & total cost
    if cart:
        for item in cart:
            info['cart'] += int(item['quantity'])
            info['total'] += (float(item['cost'])*float(item['quantity']))

    return template('cart', info)


# Add to cart request
@app.post('/cart')
def addToCart(db):

    # Get or set session cookie
    session.get_or_create_session(db)

    # Add item to cart
    session.add_to_cart(db, request.forms.get('product'), request.forms.get('quantity'))

    # Redirect to cart page
    return redirect('cart')


# Empty cart request
@app.post('/empty_cart')
def emptyCart(db):

    # Get or set session cookie
    session.get_or_create_session(db)

    # Add item to cart
    session.empty_cart(db)

    # Redirect to cart page
    return redirect('cart')


# Product page
@app.route('/product/<id>')
def product(db, id):

    # Get or set session cookie
    session.get_or_create_session(db)

    # Get cart contents from database
    cart = session.get_cart_contents(db)

    # Info relative to page
    info = {
        'page': 'product',
        'cart': 0
    }

    # Get cart items count
    if cart:
        for item in cart:
            info['cart'] += int(item['quantity'])

    # Get product data
    info['product'] = model.product_get(db, id)

    # Check if product exists
    if info['product'] is not None:
        return template('product', info)
    else:
        return HTTPResponse(status=404)


# Static files (CSS / Fonts / Images)
@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


# Favicon image
@app.route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='static', mimetype='image/x-icon')


# Start Bottle on port 8010
if __name__ == '__main__':

    import bottle_sqlite as sqlite
    from dbschema import DATABASE_NAME
    # Install database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
