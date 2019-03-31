
import random
from bottle import Bottle, template, static_file, request, redirect, HTTPError

import model
import session

app = Bottle()

# Homepage / All products page
@app.route('/')
def index(db):

    info = {
        'page': '',
        'title': 'All products',
        'cart': 0
    }

    info['products'] = model.product_list(db)

    return template('index', info)


# Cart page
@app.route('/cart')
def cart(db):

    info = {
        'page': 'cart',
        'title': 'Shopping cart',
        'cart': 20
    }

    return template('cart', info)


# Product page
@app.route('/product/<id>')
def product(db, id):

    info = {
        'page': 'product',
        'cart': 5
    }

    info['product'] = model.product_get(db, id)

    return template('product', info)


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
