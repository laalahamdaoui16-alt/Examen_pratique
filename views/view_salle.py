import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from models.salle import Salle
from services.services_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()

        self.cadreInfo = ctk.CTkFrame(self)
        self.cadreInfo.pack(pady=10, padx=10)
        ctk.CTkLabel(self.cadreInfo, text="Code").grid(row=0, column=0, padx=5, pady=5)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Libellé").grid(row=1, column=0, padx=5, pady=5)
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo)
        self.entry_libelle.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Type").grid(row=2, column=0, padx=5, pady=5)
        self.entry_type = ctk.CTkEntry(self.cadreInfo)
        self.entry_type.grid(row=2, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Capacité").grid(row=3, column=0, padx=5, pady=5)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1, padx=5, pady=5)

        self.cadreAction = ctk.CTkFrame(self)
        self.cadreAction.pack(pady=10)

        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=5, pady=5)

        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=5, pady=5)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=5, pady=5)

        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=5, pady=5)

        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "libelle", "type", "capacite"), show="headings")
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")

        self.treeList.column("code", width=80)
        self.treeList.column("libelle", width=150)
        self.treeList.column("type", width=120)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        self.lister_salles()

    def ajouter_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            self.entry_capacite.get()
        )
        succes, message = self.service_salle.ajouter_salle(salle)
        messagebox.showinfo("Résultat", message)
        if succes:
            self.lister_salles()

    def modifier_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            self.entry_capacite.get()
        )
        succes, message = self.service_salle.modifier_salle(salle)
        messagebox.showinfo("Résultat", message)
        if succes:
            self.lister_salles()

    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service_salle.supprimer_salle(code)
        messagebox.showinfo("Résultat", "Salle supprimée")
        self.lister_salles()

    def rechercher_salle(self):
        code = self.entry_code.get()
        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entry_libelle.delete(0, "end")
            self.entry_libelle.insert(0, salle.libelle)
            self.entry_type.delete(0, "end")
            self.entry_type.insert(0, salle.type)

            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, salle.capacite)
        else:
            messagebox.showerror("Erreur", "Salle introuvable")


    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))