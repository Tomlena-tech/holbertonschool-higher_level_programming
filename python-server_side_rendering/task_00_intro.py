#!/usr/bin/python3
"""Module de génération d'invitations personnalisées"""

import os
import re


def generate_invitations(template, attendees):
    """Génère des fichiers d'invitation personnalisés"""
    
    # Validations
    if not isinstance(template, str):
        print("Erreur : Le template doit être une chaîne de caractères")
        return
    
    if not isinstance(attendees, list):
        print("Erreur : attendees doit être une liste")
        return
    
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Extraire les placeholders
    placeholders = re.findall(r'\{(\w+)\}', template)
    
    # Traiter chaque participant
    for index, attendee in enumerate(attendees, start=1):  # ✅ Virgule
        try:  # ✅ try au bon endroit
            # Vérifier que c'est un dictionnaire
            if not isinstance(attendee, dict):
                print(f"Erreur : L'invité {index} n'est pas un dictionnaire")
                continue
            
            # Commencer avec le template
            invitation = template
            
            # Remplacer chaque placeholder
            for placeholder_key in placeholders:  # ✅ Deux-points
                placeholder = f"{{{placeholder_key}}}"
                value = attendee.get(placeholder_key)
                
                if value is None:
                    value = "N/A"
                
                invitation = invitation.replace(placeholder, str(value))
            
            # Créer le fichier
            filename = f"output_{index}.txt"  # ✅ "output"
            
            if os.path.exists(filename):
                print(f"Le fichier '{filename}' existe déjà, il sera écrasé")
            
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(invitation)
            
            print(f"Fichier '{filename}' créé avec succès")
            
        except IOError as e:  # ✅ Aligné avec try
            print(f"Erreur d'écriture : {e}")
        except Exception as e:  # ✅ Aligné avec except précédent
            print(f"Erreur inattendue : {e}")
