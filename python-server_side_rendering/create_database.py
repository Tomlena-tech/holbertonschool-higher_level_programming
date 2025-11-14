#!/usr/bin/python3
"""
Script to create the products.db SQLite database
Task 04: Database Integration
"""

import sqlite3

def create_database():
    """Create products.db database with Products table and sample data"""
    
    print("🔧 Création de la base de données...")
    
    # 1. Connexion à la base de données
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    print("✅ Connexion établie")
    
    # 2. Supprimer la table si elle existe
    cursor.execute('DROP TABLE IF EXISTS Products')
    print("✅ Ancienne table supprimée (si existante)")
    
    # 3. Créer la table Products
    cursor.execute('''
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    print("✅ Table Products créée")
    
    # 4. Insérer les données
    products_data = [
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Headphones', 'Electronics', 49.99),
        (4, 'Notebook', 'Stationery', 5.99),
        (5, 'Desk Lamp', 'Home Goods', 24.99),
        (6, 'Backpack', 'Accessories', 39.99)
    ]
    
    cursor.executemany('''
        INSERT INTO Products (id, name, category, price)
        VALUES (?, ?, ?, ?)
    ''', products_data)
    print(f"✅ {len(products_data)} produits insérés")
    
    # 5. IMPORTANT : Sauvegarder !
    conn.commit()
    print("✅ Changements sauvegardés")
    
    # 6. Vérifier
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]
    print(f"\n📊 Résultat : {count} produits dans la base")
    
    # 7. Afficher les produits
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    
    print("\n📦 Contenu de la base de données :")
    print("─" * 65)
    print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Price':>10}")
    print("─" * 65)
    for product in products:
        print(f"{product[0]:<5} {product[1]:<20} {product[2]:<15} {product[3]:>10.2f}€")
    print("─" * 65)
    
    # 8. Fermer
    conn.close()
    print("\n✅ Base de données products.db créée avec succès !\n")


if __name__ == '__main__':
    create_database()
