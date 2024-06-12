import sys
import json
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QCheckBox, QRadioButton, QPushButton, QMessageBox, QButtonGroup, QHBoxLayout, QScrollArea
from PyQt6.QtCore import Qt

class Application(QMainWindow):
    def __init__(self, fichier_questions):
        super().__init__()
        self.setWindowTitle("Simulation d'examen SC-900")

        self.questions_origine = self.lire_questions(fichier_questions)
        self.questions = []
        self.index_question = 0
        self.score = 0

        self.init_ui()

    def lire_questions(self, fichier):
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            QMessageBox.critical(self, "Erreur", f"Erreur de chargement des questions : {e}")
            sys.exit(1)

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        # ASCII Art
        self.label_ascii = QLabel(self.central_widget)
        self.label_ascii.setText("""
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
""")
        self.label_ascii.setStyleSheet("font-family: Courier; text-align: center;")
        self.layout.addWidget(self.label_ascii)

        # Question
        self.label_question = QLabel(self.central_widget)
        self.label_question.setWordWrap(True)
        self.layout.addWidget(self.label_question)
        
        # Scroll area for responses
        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setWidgetResizable(True)
        self.frame_reponses = QWidget()
        self.frame_reponses_layout = QVBoxLayout(self.frame_reponses)
        self.scroll_area.setWidget(self.frame_reponses)
        self.layout.addWidget(self.scroll_area)

        # Buttons
        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)
        
        self.bouton_suivant = QPushButton("Suivant", self.central_widget)
        self.bouton_suivant.clicked.connect(self.verifier_reponse)
        self.button_layout.addWidget(self.bouton_suivant)
        self.bouton_suivant.hide()  # Hide "Suivant" by default
        
        self.bouton_lancer = QPushButton("Simulation d'examen", self.central_widget)
        self.bouton_lancer.clicked.connect(self.lancer_simulation)
        self.layout.addWidget(self.bouton_lancer)
        
        self.bouton_etude = QPushButton("Hardcore mode", self.central_widget)
        self.bouton_etude.clicked.connect(self.lancer_etude)
        self.layout.addWidget(self.bouton_etude)
        
        self.bouton_quitter = QPushButton("Quitter", self.central_widget)
        self.bouton_quitter.clicked.connect(self.quitter)
        self.layout.addWidget(self.bouton_quitter)

    def afficher_question(self):
        if self.index_question >= len(self.questions):
            QMessageBox.information(self, "Résultat", f"Votre score est de {self.score}/{len(self.questions)}")
            self.quitter()
            return
        
        question = self.questions[self.index_question]
        self.label_question.setText(question['texte'])
        
        for i in reversed(range(self.frame_reponses_layout.count())): 
            widget = self.frame_reponses_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        if question['type'] == 'choix_multiple':
            self.var_reponse = []
            for option in question['options']:
                checkbox = QCheckBox(option, self.frame_reponses)
                self.var_reponse.append(checkbox)
                self.frame_reponses_layout.addWidget(checkbox)
        elif question['type'] == 'vrai_faux':
            self.var_reponse = QButtonGroup(self.frame_reponses)
            rb_oui = QRadioButton("Oui", self.frame_reponses)
            rb_non = QRadioButton("Non", self.frame_reponses)
            self.var_reponse.addButton(rb_oui, 1)
            self.var_reponse.addButton(rb_non, 2)
            self.frame_reponses_layout.addWidget(rb_oui)
            self.frame_reponses_layout.addWidget(rb_non)

    def verifier_reponse(self):
        question = self.questions[self.index_question]
        reponse_donnee = False

        if question['type'] == 'choix_multiple':
            reponses_utilisateur = [option.text() for option in self.var_reponse if option.isChecked()]
            reponse_donnee = bool(reponses_utilisateur)  # Check if any checkbox is selected
            correct = set(reponses_utilisateur) == set(question['reponse_correcte'])
        elif question['type'] == 'vrai_faux':
            reponse_utilisateur = self.var_reponse.checkedId()
            reponse_donnee = reponse_utilisateur != -1  # Check if a radio button is selected
            correct = reponse_utilisateur == question['reponse_correcte']

        if not reponse_donnee:
            QMessageBox.warning(self, "Avertissement", "Veuillez sélectionner une réponse avant de continuer.")
            return
        
        if correct:
            self.score += 1

        self.index_question += 1
        self.afficher_question()

    def lancer_simulation(self):
        self.questions = random.sample(self.questions_origine, min(40, len(self.questions_origine)))
        self.index_question = 0
        self.score = 0

        self.bouton_lancer.hide()
        self.bouton_etude.hide()
        self.bouton_quitter.hide()
        self.bouton_suivant.show()
        self.afficher_question()

    def lancer_etude(self):
        self.questions = self.questions_origine
        self.index_question = 0
        self.score = 0

        self.bouton_lancer.hide()
        self.bouton_etude.hide()
        self.bouton_quitter.hide()
        self.bouton_suivant.show()
        self.afficher_question()

    def quitter(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application("../SC-900-Questions.txt")
    window.show()
    sys.exit(app.exec())
