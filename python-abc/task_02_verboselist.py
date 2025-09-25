#!/usr/bin/env python3
"""Defines a VerboseList class"""


class VerboseList(list):  # ← Hérite de list
    """Create a list who's talking"""
    
    def append(self, item):
        """Override of method append"""
        print(f"Ajout de {item} à la liste")
        super().append(item)  
    
    def extend(self, item):
        """Override de la méthode extend"""
        print(f"Extension de la liste avec {item}")
        super().extend(item)
    
    def remove(self, item):
        """Override de la méthode remove"""
        print(f"Suppression de {item} de la liste")
        super().remove(item)
    
    def pop(self, index=-1):
        """Override de la méthode pop"""
        if index == -1:
            print(f"Suppression du dernier élément")
        else:
            print(f"Suppression de l'élément à l'index {index}")
        return super().pop(index)
    
ma_liste_bavarde = VerboseList(["chat", "chien"])
ma_liste_bavarde.append("oiseau")        # "Ajout de oiseau à la liste"
ma_liste_bavarde.remove("chat")          # "Suppression de chat de la liste" 
ma_liste_bavarde.extend(["poisson"])     # "Extension de la liste avec ['poisson']"
animal = ma_liste_bavarde.pop()          # "Suppression du dernier élément"
