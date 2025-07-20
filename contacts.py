class Contact:
    def __init__(self, nom, telephone, email):
        self.nom = nom
        self.telephone = telephone
        self.email = email
    def to_dict(self):
        return {
            'nom': self.nom,
            'telephone': self.telephone,
            'email': self.email
        }
    def __str__(self):
        return f"Nom: {self.nom}, Téléphone: {self.telephone}, Email: {self.email}"