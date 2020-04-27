#!/usr/bin/env python3  #on dit au terminal d'interpreter ce code en utilisant le langage python3 directement

from python_program.updating.update_graphs import Graph  #du fichier update_graphs localise dans le dossier python_program/updating on va importer la methode Graph
from python_program.updating.update_numbers import NewNumbers  #du fichier update_graphs localise dans le dossier python_program/updating on va importer la methode NewNumbers


number=NewNumbers()  #On appele la methode NewNumbers qui va renouveler les valeurs du site internet avec les valeurs que nous allons entrer
number.title("Update coronaReady")  #puis on definit le titre de la fenetre qui sera ouverte
number.configure(bg="#cfcfcf")  #et on fixe la couleur du fond au gris
number.mainloop()  #c'est une boucle infinie (tant que la fenetre nest pas fermee), elle va attendre qu'un evenement se produise et le traitera si besoin
lebanon=Graph("Lebanon")  #On appele la methode Graph qui va renouveler les graphiques des cas specifiquement pour le Liban
iran=Graph("Iran")  #On appele la methode Graph qui va renouveler les graphiques des cas specifiquement pour l'Iran
japan=Graph("Japan")  #On appele la methode Graph qui va renouveler les graphiques des cas specifiquement pour le Japon
