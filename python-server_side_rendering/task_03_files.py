#!/usr/bin/python3
"""
Flask application to display products from JSON or CSV
Task 03: Reading and Displaying Data from Multiple Sources
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')


@app.route('/products')
def products():
    """
    Display products from JSON or CSV based on query parameter
    URL examples:
    - /products?source=json
    - /products?source=csv
    - /products?source=json&id=1
    """
    
    # 1. Récupérer les query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # 2. Valider le paramètre 'source'
    if not source:
        error = "Error: No source specified. Please use ?source=json or ?source=csv"
        return render_template('product_display.html', error=error)
    
    if source not in ['json', 'csv']:
        error = "Wrong source"
        return render_template('product_display.html', error=error)
    
    # 3. Lire les données selon la source
    products_list = []  
    
    try:
        if source == 'json':
            # Lire depuis products.json
            with open('products.json', 'r') as f:
                products_list = json.load(f)
        
        elif source == 'csv':
            # Lire depuis products.csv
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                products_list = list(reader)
                
                # Convertir les types (CSV lit tout en string)
                for product in products_list:
                    product['id'] = int(product['id'])
                    product['price'] = float(product['price'])
    
    except FileNotFoundError:
        error = f"Error: {source.upper()} file not found."
        return render_template('product_display.html', error=error)
    
    except json.JSONDecodeError:
        error = "Error: Invalid JSON format."
        return render_template('product_display.html', error=error)
    
    except Exception as e:
        error = f"Error: {str(e)}"
        return render_template('product_display.html', error=error)
    
    # 4. Filtrer par ID si spécifié
    if product_id:
        try:
            product_id = int(product_id)
            # Chercher le produit avec cet ID
            filtered_product = next(
                (p for p in products_list if p['id'] == product_id), 
                None
            )
            
            if filtered_product:
                products_list = [filtered_product]
            else:
                error = f"Product not found"
                return render_template('product_display.html', error=error)
        
        except ValueError:
            error = "Error: Invalid id format. ID must be a number."
            return render_template('product_display.html', error=error)
    
    # 5. Passer les données au template
    return render_template(
        'product_display.html', 
        products=products_list,
        source=source
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
