import requests

# URL de l'API JSONPlaceholder
url = "https://jsonplaceholder.typicode.com/posts"

# Faire la requête GET
response = requests.get(url)

# Afficher le code de statut
print("Status Code:", response.status_code)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Parser la réponse en JSON
    posts = response.json()

    # Afficher les titres des 5 premiers posts (par exemple)
    for post in posts[:5]:
        print(post["title"])
else:
    print("Erreur lors de la récupération des données.")
