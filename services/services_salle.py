from Data.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or not str(salle.capacite):
            return False, " les champs sont obligatoires"

        if int(salle.capacite) < 1:
            return False, "La capacité doit être >= 1"

        if self.dao_salle.get_salle(salle.code):
            return False, "Le code existe déjà"
        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutée"

    def modifier_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or not str(salle.capacite):
            return False, " les champs sont obligatoires"

        if int(salle.capacite) < 1:
            return False, "La capacité doit >= 1"

        self.dao_salle.update_salle(salle)
        return True, "Salle modifiée "

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)

    def rechercher_salle(self, code):
        return self.dao_salle.get_salle(code)



    def recuperer_salles(self):
        return self.dao_salle.get_salles()