from models.salle import Salle
from Data.dao_salle import DataSalle

dao = DataSalle()

connexion = dao.get_connection()
print("Connexion réussie")
connexion.close()

s1 = Salle("S01", "Salle reseau", "Laboratoire", 20)
dao.insert_salle(s1)

s1.libelle = "Salle informatique"
dao.update_salle(s1)

salle = dao.get_salle("S01")
if salle:
    print(salle.afficher_infos())

for s in dao.get_salles():
    print(s.afficher_infos())

dao.delete_salle("S01")
print("Salle supprimée")