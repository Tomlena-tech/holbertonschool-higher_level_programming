#!/usr/bin/env python3
"""
Module pour interagir avec l'API JSONPlaceholder
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Récupère tous les posts depuis JSONPlaceholder et affiche leurs titres
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Erreur lors de la récupération des données")


def fetch_and_save_posts():
    """
    Récupère tous les posts et les sauvegarde dans un fichier CSV
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Structurer les données
        posts_data = []
        for post in posts:
            posts_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
        
        # Écrire dans un fichier CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
        
        print("Données sauvegardées dans posts.csv")
    else:
        print("Erreur lors de la récupération des données")
