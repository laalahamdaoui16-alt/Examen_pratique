import mysql.connector
import json
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r") as f:
            config = json.load(f)

        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connexion

    def insert_salle(self, salle):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        requete = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)
        curseur.execute(requete, valeurs)
        connexion.commit()
        curseur.close()
        connexion.close()

    def update_salle(self, salle):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        requete = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        valeurs = (salle.libelle, salle.type, salle.capacite, salle.code)
        curseur.execute(requete, valeurs)
        connexion.commit()
        curseur.close()
        connexion.close()

    def delete_salle(self, code):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        requete = "DELETE FROM salle WHERE code=%s"
        curseur.execute(requete, (code,))
        connexion.commit()
        curseur.close()
        connexion.close()

    def get_salle(self, code):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        requete = "SELECT * FROM salle WHERE code=%s"
        curseur.execute(requete, (code,))
        ligne = curseur.fetchone()
        curseur.close()
        connexion.close()

        if ligne:
            return Salle(ligne[0], ligne[1], ligne[2], ligne[3])
        return None

    def get_salles(self):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        requete = "SELECT * FROM salle"
        curseur.execute(requete)
        lignes = curseur.fetchall()
        curseur.close()
        connexion.close()

        liste = []
        for ligne in lignes:
            liste.append(Salle(ligne[0], ligne[1], ligne[2], ligne[3]))
        return liste