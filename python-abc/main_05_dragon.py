#!/usr/bin/env python3
from task_05_dragon import Dragon

dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!

print()
print("Draco peut faire tout ça grâce aux mixins !")
print(f"Classes parentes de Dragon: {Dragon.__bases__}")
print(f"MRO (Method Resolution Order): {Dragon.__mro__}")
