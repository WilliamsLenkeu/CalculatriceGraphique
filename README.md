# Calculatrice Graphique en Tkinter

Ce script Python utilise la bibliothèque Tkinter pour créer une interface graphique simple pour une calculatrice. La calculatrice prend en charge les opérations mathématiques de base et utilise la bibliothèque SymPy pour évaluer les expressions.

## Fonctionnalités

1. **Affichage de l'expression en cours :**
   - Un champ d'affichage en haut de la calculatrice affiche l'expression mathématique en cours.

2. **Boutons pour les chiffres :**
   - Les chiffres de 0 à 9 sont disposés en trois lignes sur la gauche de la calculatrice. En cliquant sur ces boutons, les chiffres correspondants sont ajoutés à l'expression en cours.

3. **Boutons pour les opérations mathématiques :**
   - Les opérations d'addition, soustraction, multiplication et division sont disposées sur la droite de la calculatrice. En cliquant sur ces boutons, les opérations correspondantes sont ajoutées à l'expression en cours.

4. **Bouton égal (=) :**
   - En appuyant sur ce bouton, l'expression en cours est évaluée à l'aide de la bibliothèque SymPy, et le résultat est affiché à la fois dans le champ d'affichage et le champ de résultat en bas de la calculatrice.

5. **Bouton Clear (C) :**
   - En appuyant sur ce bouton, l'expression en cours ainsi que le champ de résultat sont effacés.

6. **Bouton Backspace (←) :**
   - En appuyant sur ce bouton, le dernier caractère de l'expression en cours est supprimé.

## Utilisation

1. **Ajout de chiffres et opérations :**
   - Cliquez sur les boutons correspondants pour ajouter des chiffres et des opérations à l'expression en cours.

2. **Évaluation de l'expression :**
   - Cliquez sur le bouton "=" pour évaluer l'expression et afficher le résultat.

3. **Effacement :**
   - Utilisez le bouton "C" pour effacer l'expression en cours et le résultat.

4. **Suppression du dernier caractère :**
   - Cliquez sur le bouton "←" pour supprimer le dernier caractère de l'expression en cours.

## Dépendances

- Python 3.x
- Tkinter
- SymPy

## Exemple d'utilisation

```python
# Importation des bibliothèques nécessaires
import tkinter as tk
from sympy import sympify

# Classe de la Calculatrice Graphique
class CalculatriceGraphique:
    # ... (voir le code ci-dessus)

if __name__ == "__main__":
    # Création de la fenêtre principale Tkinter et de la calculatrice
    fenetre_principale = tk.Tk()
    calculatrice = CalculatriceGraphique(fenetre_principale)
    fenetre_principale.mainloop()
```

Ce script crée une interface utilisateur simple pour effectuer des opérations mathématiques de base à l'aide de la bibliothèque Tkinter et SymPy.