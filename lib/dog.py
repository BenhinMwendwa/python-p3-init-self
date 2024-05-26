#!/usr/bin/env python3

class Dog:
    def __init__ (self,name,breed="Mutt"):
        self.name = name
        self.Breed = breed

fido = Dog("Fido","Dalmatian")
print(fido.Breed =="Dalmatian")
print(fido.name)