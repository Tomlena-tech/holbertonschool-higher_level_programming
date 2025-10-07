#!/usr/bin/env python3
# Exercice 0 : Bases de HTTP/HTTPS

## 1. Différences entre HTTP et HTTPS

Les differences entre HTTP et le HTTPS : 
- les premier n'est pas sécurisé. le HTTPS oui.
- HTTP : Port 80 - HTTPS : Port 443
- CERTIFICAT
   - HTTP : Pas de certificat nécessaire
   - HTTPS : Nécessite un certificat SSL/TLS

- CADENAS
   - HTTP : Pas de cadenas dans le navigateur
   - HTTPS : Cadenas 🔒 visible dans la barre d'adresse


   
## 2. Structure des Requêtes et Réponses HTTP

### Structure d'une Requête
STRUCTURE D'UNE REQUÊTE HTTP OBSERVÉE :

Ligne de requête :
┌─────────────────────────────────┐
│ GET /https://chatgpt.com/c/68e282f6-c86c-832b-b57a-a0db45107f7d
         │
└─────────────────────────────────┘

En-têtes de requête :
┌─────────────────────────────────┐
│ Host: chatgpt.com│
│ User-Agent: Mozilla/5.0 │
│ Accept: text/html               │
│ Accept-Language: fr-FR          │
│ Connection: keep-alive          │
└─────────────────────────────────┘

Corps (si POST) :
┌─────────────────────────────────┐
└─────────────────────────────────┘

---

STRUCTURE D'UNE RÉPONSE HTTP OBSERVÉE :

Ligne de statut :
┌─────────────────────────────────┐
│ HTTP/1.1 200 OK                 │
└─────────────────────────────────┘

En-têtes de réponse :
┌─────────────────────────────────┐
│ Date:  │Mon, 06 Oct 2025 12:03:32 GMT
│ Server: cloudflare          │
│ Content-Type: text/html; charset=utf-8         │
│ Content-Length:            │
│ Set-Cookie: __cf_bm=Qk40E__cMZaZ9ZoGk7Ai7PL0ykFaeQ0tYPS4SgYrJVA-1759752212-1.0.1.1-rWRqI9QXNMFR3RXqWy9L.APpc9lyorU_XpKRxYhNscTjsQwY4hiJrXzKncH6uXEVauEv9OZVYwPdiRez1mMFLsHfu615pOS5mr2iiXUFYXI; path=/; expires=Mon, 06-Oct-25 12:33:32 GMT; domain=.chatgpt.com; HttpOnly; Secure; SameSite=None.         │
└─────────────────────────────────┘

Corps :
┌─────────────────────────────────┐
│<!DOCTYPE html>
<html lang="fr-FR" data-build="prod-544ef7a65f3ef03d172b84cc0b5cd60b865d8802" dir="ltr" class="">
    <head>
        <meta charSet="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"/>
        <meta name="description" content="ChatGPT vous aide à obtenir des réponses, à trouver des idées et à gagner en productivité. Son utilisation est gratuite et conviviale. Il vous suffit de lui poser une question pour que ChatGPT vous aide dans vos tâches de rédaction, d’apprentissage, de brainstorming et plus encore."/>
        <meta name="keyword" content="chat ia,ia,chap gpt,chat gbt,chat gpt 3,connexion chat gpt,site web chat gpt,chat gpt,chat gtp,chat openai,chat,chatia,chatbot gpt,chatg,connexion chatgpt,chatgpt,gpt chat,open ai,openai chat,openai chatgpt,openai"/>
        <meta property="og:description" content="Un système d’IA conversationnel qui écoute, apprend et vous pousse à réfléchir"/>
        <meta property="og:url" content="https://chatgpt.com/fr-FR"/>
        <meta property="og:site_name" content="ChatGPT"/>
        <link r           │
└─────────────────────────────────┘

### Structure d'une Réponse
[Votre schéma ou description]

## 3. Méthodes HTTP Courantes

## 3. Méthodes HTTP Courantes

| Méthode | Description | Cas d'utilisation |
|---------|-------------|-------------------|
| GET     | Récupère des données du serveur | Charger une page web, obtenir des infos |
| POST    | Envoie des données pour créer une ressource | S'inscrire, publier un commentaire |
| PUT     | Met à jour complètement une ressource | Modifier tout son profil utilisateur |
| DELETE  | Supprime une ressource | Supprimer un compte, effacer un post |
| PATCH   | Modification partielle d'une ressource | Changer uniquement son email |
## 4. Codes de Statut HTTP Courants

## 4. Codes de Statut HTTP Courants

| Code | Nom | Description | Scénario |
|------|-----|-------------|----------|
| 200  | OK  | Requête réussie | Page web chargée normalement |
| 201  | Created | Ressource créée avec succès | Compte utilisateur créé |
| 404  | Not Found | Ressource introuvable | URL incorrecte ou page supprimée |
| 401  | Unauthorized | Authentification requise | Accéder à son profil sans être connecté |
| 500  | Internal Server Error | Erreur interne du serveur | Bug dans le code du serveur |
