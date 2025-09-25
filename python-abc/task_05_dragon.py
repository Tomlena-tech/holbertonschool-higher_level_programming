#!/usr/bin/env python3

class SwimMixin:
    """Mixin who's added swimm skill."""
    
    def swim(self):
        """Way to swimm"""
        print("The creature swims!")


class FlyMixin:
    """Mixin add flying skill to the class."""
    
    def fly(self):
        """how to fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Classe Dragon inherits of mixins SwimMixin and FlyMixin.
    """
    
    def roar(self):
        """Méthod to roars."""
        print("The dragon roars!")
