import json
import pathlib
from contacts import Contact


class ContactManager:
    def __init__(self , fichier="contacts.json"):
        self.fichier = pathlib.Path(fichier)
        self.contacts = []
        self.charger_contacts()
    
    def charger_contacts(self):
        if self.fichier.exists():
            with open(self.fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.contacts = [Contact(**contact) for contact in data]
        else:
            self.contacts = []

    def sauvegarder_contacts(self):
        with open(self.fichier, 'w', encoding='utf-8') as f:
            json.dump([contact.to_dict() for contact in self.contacts], f, ensure_ascii=False, indent=4)
    
    def ajouter_contact(self, contact):
        self.contacts.append(contact)
        self.sauvegarder_contacts()
    
    def supprimer_contact(self, contact):
        self.contacts.remove(contact)
        self.sauvegarder_contacts()
    
    def rechercher_contact(self, nom):
        return [contact for contact in self.contacts if contact.nom.lower() == nom.lower()]

    def afficher_contacts(self):
        if not self.contacts:
            print("Aucun contact trouvé.")
        else:
            for contact in self.contacts:
                print(contact)