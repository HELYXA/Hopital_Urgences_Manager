"""
Système de gestion des urgences hospitalières
Permet de prioriser et suivre les patients d'un service d'urgences (POO).
"""

PRIORITES = {
    1: "Non urgent",
    2: "Peu urgent",
    3: "Urgent",
    4: "Très urgent",
    5: "Urgence vitale",
}


class Patient:
    def __init__(self, nom="", age=0, priorite=0):
        self.nom = nom
        self.age = age
        self.priorite = priorite

    def __str__(self):
        return f"Nom : {self.nom}, Âge : {self.age}, Priorité : {self.priorite} ({self.get_description_priorite()})"

    def get_description_priorite(self):
        return PRIORITES.get(self.priorite, "Priorité non définie")


class GestionUrgences:
    def __init__(self):
        # Quelques patients de demonstration
        self.liste_patients = [
            Patient("Alice", 34, 5),   # Urgence vitale
            Patient("Bob", 40, 3),     # Urgent
            Patient("Charlie", 29, 4),  # Très urgent
        ]

    @staticmethod
    def _demander_priorite_valide(message="Entrez la priorité (1 à 5, 5 étant la plus haute) : "):
        """Redemande tant que la priorité saisie n'est pas comprise entre 1 et 5."""
        while True:
            try:
                priorite = int(input(message))
            except ValueError:
                print("Erreur : veuillez entrer un nombre entier.")
                continue
            if 1 <= priorite <= 5:
                return priorite
            print("Erreur : la priorité doit être comprise entre 1 et 5.")

    def ajout_patient(self):
        nom = input("Entrez le nom du patient : ")
        age = int(input("Entrez l'âge du patient : "))
        priorite = self._demander_priorite_valide()
        self.liste_patients.append(Patient(nom, age, priorite))
        print("Patient ajouté avec succès.")

    def afficher_patients(self):
        if not self.liste_patients:
            print("Aucun patient enregistré.")
            return
        # Par defaut, sorted() trie en ordre croissant ; reverse=True inverse l'ordre
        patients_tries = sorted(self.liste_patients, key=lambda p: p.priorite, reverse=True)
        print("Liste des patients triée par priorité :")
        for patient in patients_tries:
            print(patient)

    def rechercher_patient(self):
        nom_recherche = input("Entrez le nom du patient à rechercher : ")
        for patient in self.liste_patients:
            if patient.nom.lower() == nom_recherche.lower():
                print("Patient trouvé :")
                print(patient)
                return
        print("Patient non trouvé.")

    def supprimer_patient(self):
        nom_supprimer = input("Entrez le nom du patient à supprimer : ")
        for patient in self.liste_patients:
            if patient.nom.lower() == nom_supprimer.lower():
                self.liste_patients.remove(patient)
                print("Patient supprimé avec succès.")
                return
        print("Patient non trouvé.")

    def modifier_patient(self):
        nom_recherche = input("Entrez le nom du patient à modifier : ")
        for patient in self.liste_patients:
            if patient.nom.lower() == nom_recherche.lower():
                patient.nom = input("Entrez le nouveau nom : ")
                patient.age = int(input("Entrez le nouvel âge : "))
                # Bug corrige : on valide la priorite AVANT de l'assigner au patient,
                # pour ne jamais laisser l'objet dans un etat invalide.
                patient.priorite = self._demander_priorite_valide(
                    "Entrez la nouvelle priorité (1 à 5) : "
                )
                print("Patient mis à jour avec succès.")
                return
        print("Patient non trouvé.")


def menu_principal():
    gestion_urgences = GestionUrgences()

    while True:
        print("\n--- Système de gestion des urgences hospitalières ---")
        print("1. Ajouter un patient")
        print("2. Afficher la liste des patients")
        print("3. Rechercher un patient")
        print("4. Supprimer un patient")
        print("5. Mettre à jour un patient")
        print("6. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            gestion_urgences.ajout_patient()
        elif choix == "2":
            gestion_urgences.afficher_patients()
        elif choix == "3":
            gestion_urgences.rechercher_patient()
        elif choix == "4":
            gestion_urgences.supprimer_patient()
        elif choix == "5":
            gestion_urgences.modifier_patient()
        elif choix == "6":
            print("Quitter le système.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    menu_principal()
