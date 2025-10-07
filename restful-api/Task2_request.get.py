#!/usr/bin/env python3
"""
Script basique pour récupérer des posts depuis JSONPlaceholder
"""
import requests

# URL de l'API
url = "https://jsonplaceholder.typicode.com/posts"

# Faire la requête GET
response = requests.get(url)

# Afficher le résultat
print(response.json())
