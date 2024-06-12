# Projet réalisé par Choupe Stephane 
# Date de création : Mercredi 12 Juin 2024
# Code original par : Renaud Marchal 


import tkinter as tk
from tkinter import messagebox
import json
import random

# Lire les questions depuis le fichier
def lire_questions(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return json.load(f)

# Fonction pour montrer la question suivante
def afficher_question():
    global index_question, score, questions, var_reponse
    
    if index_question >= len(questions):
        messagebox.showinfo("Résultat", f"Votre score est de {score}/{len(questions)}")
        root.quit()
        return

    question = questions[index_question]
    label_question.config(text=question['texte'])
    
    for widget in frame_reponses.winfo_children():
        widget.destroy()

    if question['type'] == 'choix_multiple':
        var_reponse = [tk.IntVar() for _ in question['options']]
        for i, option in enumerate(question['options']):
            tk.Checkbutton(frame_reponses, text=option, variable=var_reponse[i]).pack(anchor='w')
    elif question['type'] == 'vrai_faux':
        var_reponse = tk.IntVar()
        tk.Radiobutton(frame_reponses, text="Oui", variable=var_reponse, value=1).pack(anchor='w')
        tk.Radiobutton(frame_reponses, text="Non", variable=var_reponse, value=2).pack(anchor='w')
    
    bouton_suivant.pack(pady=10)  # Afficher le bouton "Suivant"

# Vérifier la réponse
def verifier_reponse():
    global index_question, score
    
    question = questions[index_question]

    if question['type'] == 'choix_multiple':
        reponses_utilisateur = [question['options'][i] for i, var in enumerate(var_reponse) if var.get() == 1]
        if reponses_utilisateur and set(reponses_utilisateur) == set(question['reponse_correcte']):
            score += 1
    elif question['type'] == 'vrai_faux':
        reponse_utilisateur = var_reponse.get()
        if reponse_utilisateur in [1, 2] and reponse_utilisateur == question['reponse_correcte']:
            score += 1
    
    index_question += 1
    afficher_question()


# Fonction de lancement pour la simulation d'examen
def lancer_simulation():
    global questions, index_question, score, var_reponse
    
    questions = random.sample(questions_origine, 40)
    index_question = 0
    score = 0
    
    bouton_lancer.pack_forget()  # Cacher le bouton "Simulation d'examen"
    bouton_etude.pack_forget()   # Cacher le bouton "Hardcore mode"
    bouton_quitter.pack_forget() # Cacher le bouton "Quitter"
    afficher_question()

# Fonction de lancement pour le mode hardcore
def lancer_etude():
    global questions, index_question, score, var_reponse
    
    questions = questions_origine
    index_question = 0
    score = 0
    
    bouton_lancer.pack_forget()  # Cacher le bouton "Simulation d'examen"
    bouton_etude.pack_forget()   # Cacher le bouton "Hardcore mode"
    bouton_quitter.pack_forget() # Cacher le bouton "Quitter"
    afficher_question()

# Fonction pour quitter l'application
def quitter():
    root.quit()

# Fonction pour afficher l'ASCII art
def afficher_ascii_sc900():
    # Définir l'art ASCII
    ascii_art = """
   ___         _   _  __ _         _   _            ___  ___    ___  __   __  
  / __|___ _ _| |_(_)/ _(_)__ __ _| |_(_)___ _ _   / __|/ __|__/ _ \/  \ /  \ 
 | (__/ -_) '_|  _| |  _| / _/ _` |  _| / _ \ ' \  \__ \ (_|___\_, / () | () |
  \___\___|_|  \__|_|_| |_\__\__,_|\__|_\___/_||_| |___/\___|   /_/ \__/ \__/ 
                                               
                                   ___          ____
                               ,-""   `.      < HONK >
                             ,'  _   e )`-._ /  ----
                            /  ,' `-._<.===-'
                           /  /
                          /  ;
              _          /   ;
 (`._    _.-"" ""--..__,'    |
 <_  `-""                    \  
  <`-                          :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
                    `-'
"""
    # Créer un widget Label pour afficher l'art ASCII
    label_ascii = tk.Label(root, text=ascii_art, font=("Courier", 10), justify="left")
    label_ascii.pack(padx=10, pady=10)


# Lire les questions depuis le fichier
questions_origine = lire_questions("../SC-900-Questions.txt")

# Configurer la fenêtre principale
root = tk.Tk()
root.title("Simulation d'examen SC-900")

# Afficher l'ASCII art
label_ascii = tk.Label(root, text="", font=("Courier", 8), justify="center")
label_ascii.pack(pady=10)

# Appel de la fonction pour afficher l'ASCII art
afficher_ascii_sc900()

label_question = tk.Label(root, text="", wraplength=600, justify="left")
label_question.pack(pady=20)

frame_reponses = tk.Frame(root)
frame_reponses.pack(pady=10)

# Cadre pour le score
frame_score = tk.Frame(root)
frame_score.pack(pady=10)

index_question = 0
score = 0
questions = []

# Bouton pour passer à la question suivante
bouton_suivant = tk.Button(root, text="Suivant", command=verifier_reponse)

# Boutons pour lancer les différents modes
bouton_lancer = tk.Button(root, text="Simulation d'examen", command=lancer_simulation)
bouton_lancer.pack(pady=20)

bouton_etude = tk.Button(root, text="Hardcore mode", command=lancer_etude)
bouton_etude.pack(pady=20)

# Bouton pour quitter
bouton_quitter = tk.Button(root, text="Quitter", command=quitter)
bouton_quitter.pack(pady=20)

# Lancer la boucle principale
root.mainloop()
