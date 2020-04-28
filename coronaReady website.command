#!/usr/bin/env python3   #on dit au terminal d'interpreter ce code en utilisant le langage python3 directement

from webbrowser import open  #de la librairie webbrowser on va importer uniquement la methode open qui peut ouvrir une fenetre dans moteur de recherche
new = 2  #cette variable va ouvrir si possible une nouvelle fenetre du moteur de recherche
url = "file:///Users/bechara/Desktop/github/coronaReady/website/home_page/index.html"  #cette variable definie le lien qui va etre ouvert par la fonction, il peut etre un lien externe (de l'internet) ou local comme ici
open(url,new=new)  #avec la fonction importee et les variables definies on va ouvrir le fichier qui contient le code de notre site internet dans une nouvelle fenetre du moteur de recherche si possible
