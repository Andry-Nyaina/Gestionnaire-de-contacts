from contacts import Contact
from contact_manager import ContactManager


def menu():
    print("\n --- Gestionnaire de Contacts ---")
    print("1. Ajouter un contact")
    print("2. Supprimer un contact")
    print("3. Rechercher un contact")
    print("4. Afficher tous les contacts")
    print("5. Quitter")
    return input("Choisissez une option: ")


manager = ContactManager()

while True:
    choix = menu()
    
    if choix == '1':
        nom = input("Nom: ")
        telephone = input("Téléphone: ")
        email = input("Email: ")
        contact = Contact(nom, telephone, email)
        manager.ajouter_contact(contact)
        print("Contact ajouté avec succès.")
    
    elif choix == '2':
        nom = input("Nom du contact à supprimer: ")
        contacts = manager.rechercher_contact(nom)
        if contacts:
            for i, contact in enumerate(contacts):
                print(f"{i + 1}. {contact}")
            index = int(input("Sélectionnez le numéro du contact à supprimer: ")) - 1
            if 0 <= index < len(contacts):
                manager.supprimer_contact(contacts[index])
                print("Contact supprimé avec succès.")
            else:
                print("Numéro invalide.")
        else:
            print("Aucun contact trouvé avec ce nom.")
    
    elif choix == '3':
        nom = input("Nom du contact à rechercher: ")
        contacts = manager.rechercher_contact(nom)
        if contacts:
            for contact in contacts:
                print(contact)
        else:
            print("Aucun contact trouvé avec ce nom.")
    
    elif choix == '4':
        manager.afficher_contacts()
    
    elif choix == '5':
        print("Au revoir!")
        break
    
    else:
        print("Option invalide, veuillez réessayer.")

    print("-" * 50)