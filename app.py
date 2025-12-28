from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Simple in-memory storage (for demonstration)
products = [
    {
        'id': 1,
        'name': 'Fresh Tomatoes',
        'category': 'Vegetables',
        'quantity': 500,
        'unit': 'kg',
        'price': 2.50,
        'farmer': 'Green Valley Farm',
        'updated': datetime.now().strftime('%Y-%m-%d %H:%M')
    },
    {
        'id': 2,
        'name': 'Organic Wheat',
        'category': 'Grains',
        'quantity': 2000,
        'unit': 'kg',
        'price': 1.80,
        'farmer': 'Sunny Fields',
        'updated': datetime.now().strftime('%Y-%m-%d %H:%M')
    },
    {
    'id': 3,
    'name': 'Fresh Apples',
    'category': 'Fruits',
    'quantity': 1200,
    'unit': 'kg',
    'price': 1.60,
    'farmer': 'Golden Orchard',
    'updated': datetime.now().strftime('%Y-%m-%d %H:%M')
}
]

@app.route('/')
def index():
    """Homepage - displays all products"""
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    """Add new product"""
    if request.method == 'POST':
        new_product = {
            'id': len(products) + 1,
            'name': request.form['name'],
            'category': request.form['category'],
            'quantity': float(request.form['quantity']),
            'unit': request.form['unit'],
            'price': float(request.form['price']),
            'farmer': request.form['farmer'],
            'updated': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        products.append(new_product)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/api/products')
def api_products():
    """API endpoint for products"""
    return jsonify(products)

@app.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'products_count': len(products)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
