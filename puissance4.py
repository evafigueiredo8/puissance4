import numpy as np
from joueur import Joueur

class Puissance4:  
    def __init__(self):
        self.grille = self.creer_grille()
        self.joueurs = [Joueur(1), Joueur(2)]
        self.partie_en_cours = True
        self.joueur_actuel = self.joueurs[0]  # Joueur 1 commence
        
    def creer_grille(self):
        # cette fonction créait une matrice 6 x 7 de 0
        return np.zeros((6, 7), dtype=int)

    def afficher_grille(self, grille):
        # cette fonction affiche le numéro de chaque colonne pour que le joueur puisse choisir ooù positionner son pion
        for ligne in range(6):
            for colonne in range(7):
                print(grille[5 - ligne][colonne], end=" ")
            print()
        print("1 2 3 4 5 6 7")

    def jouer_coup(self, grille, colonne, joueur):
        # vérifie si le joueur peut placer son pion dans la colonne qu'il a choisi
        for ligne in range(6):
            if grille[ligne][colonne] == 0:
                grille[ligne][colonne] = joueur
                return True
        return False

    def verifier_victoire(self, grille, joueur):
        # fonction qui vérifie si le joueur actuel a gagné
        # vérifie si 4 pions sont allignés sur une ligne
        for ligne in range(6):
            for colonne in range(4):
                if grille[ligne][colonne] == joueur and grille[ligne][colonne+1] == joueur and grille[ligne][colonne+2] == joueur and grille[ligne][colonne+3] == joueur:
                    return True
        # vérifie si 4 pions sont allignés sur une colonne
        for ligne in range(3):
            for colonne in range(7):
                if grille[ligne][colonne] == joueur and grille[ligne+1][colonne] == joueur and grille[ligne+2][colonne] == joueur and grille[ligne+3][colonne] == joueur:
                    return True
        # vérifie en diagonale /
        for ligne in range(3):
            for colonne in range(4):
                if grille[ligne][colonne] == joueur and grille[ligne+1][colonne+1] == joueur and grille[ligne+2][colonne+2] == joueur and grille[ligne+3][colonne+3] == joueur:
                    return True
        # vérifie diagonale \
        for ligne in range(3):
            for colonne in range(3, 7):
                if grille[ligne][colonne] == joueur and grille[ligne+1][colonne-1] == joueur and grille[ligne+2][colonne-2] == joueur and grille[ligne+3][colonne-3] == joueur:
                    return True
        return False

    def puissance4(self):
        # fonction principale
        partie = True
        grille = self.creer_grille()
        joueur = ""
        while joueur != "1" and joueur != "2":
            joueur = input("Choisissez le joueur qui commence (1 ou 2) : ")
            if joueur != "1" and joueur != "2":
                print("Veuillez entrer un chiffre entre 1 et 2.")
        while partie:
            self.afficher_grille(grille)
            colonne = input(f"Joueur {joueur}, choisissez une colonne (1-7) : ")
            if colonne.isdigit() and 1 <= int(colonne) <= 7: # vérifier si le joueur a bien choisi un chiffre (isdigit) entre 1 et 7
                colonne = int(colonne) - 1 # on enlève 1 car les colonnes vont de 0 à 6
                if self.jouer_coup(grille, colonne, joueur):
                    if self.verifier_victoire(grille, joueur):
                        self.afficher_grille(grille)
                        print(f"Le joueur {joueur} a gagné !")
                        partie = False
                    elif np.count_nonzero(grille == 0) == 0:
                        self.afficher_grille(grille)
                        print("La grille est pleine, c'est un match nul !")
                        partie = False
                    joueur = 3 - joueur
                else:
                    print("La colonne est pleine, veuillez choisir une autre colonne.")
            else:
                print("Entrée invalide. Veuillez choisir un chiffre de 1 à 7.")
