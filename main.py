import tkinter as tk
from sympy import sympify

class CalculatriceGraphique:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Calculatrice Graphique")

        self.expression_var = tk.StringVar()
        self.resultat_var = tk.StringVar()


        # Champ d'affichage
        champ_affichage = tk.Entry(fenetre, textvariable=self.expression_var, font=('Arial', 14))
        champ_affichage.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Boutons pour les chiffres
        chiffres = "7894561230"
        row_val = 1
        col_val = 0
        for chiffre in chiffres:
            tk.Button(fenetre, text=chiffre, command=lambda c=chiffre: self.ajouter_caractere(c)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

        # Boutons pour les opérations mathématiques
        operations = "+-*/"
        row_op = 1
        col_op = 3
        for operation in operations:
            tk.Button(fenetre, text=operation, command=lambda o=operation: self.ajouter_caractere(o)).grid(row=row_op, column=col_op, sticky="nsew")
            row_op += 1

        # Bouton égal
        tk.Button(fenetre, text="=", command=self.evaluer_expression).grid(row=4, column=3, sticky="nsew")

        # Bouton Clear
        tk.Button(fenetre, text="C", command=self.clear).grid(row=4, column=0, columnspan=2, sticky="nsew")

        # Bouton Backspace
        tk.Button(fenetre, text="←", command=self.backspace).grid(row=4, column=2, sticky="nsew")

        # Configuration du redimensionnement des boutons
        for i in range(5):
            fenetre.grid_rowconfigure(i, weight=1)
            fenetre.grid_columnconfigure(i, weight=1)

    def ajouter_caractere(self, caractere):
        current_expression = self.expression_var.get()
        self.expression_var.set(current_expression + caractere)

    def evaluer_expression(self):
        try:
            expression = self.expression_var.get()
            resultat = sympify(expression)
            self.resultat_var.set(resultat)
            self.expression_var.set(resultat)
        except Exception as e:
            self.resultat_var.set("Erreur")
            self.expression_var.set("Erreur")

    def clear(self):
        self.expression_var.set("")
        self.resultat_var.set("")

    def backspace(self):
        current_expression = self.expression_var.get()
        self.expression_var.set(current_expression[:-1])


if __name__ == "__main__":
    fenetre_principale = tk.Tk()
    calculatrice = CalculatriceGraphique(fenetre_principale)
    fenetre_principale.mainloop()
