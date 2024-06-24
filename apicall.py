from flask import Flask, request, redirect, url_for, render_template,jsonify

app = Flask(__name__)

cart = []

@app.route('/')
def index():
    return render_template('index.html', cart=cart)

@app.route('/api/add', methods=['POST'])
def add_to_cart():
    product = {
        'name': request.form['name'],
    }
    cart.append(product)
    return jsonify({'message': 'Product added to cart', 'cart': cart}), 201

    return redirect(url_for('index'))

@app.route('/api/delete/<string:product_name>', methods=['DELETE'])
def delete_from_cart(product_name):
    global cart
    cart = [product for product in cart if product['name'] != product_name]
    return jsonify({'message': 'Product deleted ', 'cart': cart}), 201

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
