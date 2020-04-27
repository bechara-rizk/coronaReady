Comme l'explication des fichiers HTML et CSS allait etre trop repetitive (ils sont des langages de codage et pas de programmation comme python et javascript) on
  va expliquer les notions a comprendre dans ce fichier tout en expliquant lea lien des autres fichiers entre eux.

Le fichier README.txt contient ces explications.

Tout d'abord il y a les fichiers dans le dossier principal avec une extension .command, faire attention en ouvrant ceux la car ils sont cense executer le code python a
  l'interrieur directement donc en les ouvrant choisi de les ouvrir avec un editeur de texte.

Dans le dossier layouts:
    Il y a les plans initiaux du design qu'on voulait faire pour notre page.

Dans le dossier python_program:
    Les dossiers __pycache__ contiennent le meme code que nous avons ecrit sauf qu'il est deja compile en bytecode pour faciliter la tache a l'ordinateur de les importer
      dans d'autres fichiers python.
    Le dossier data contient des fichier avec une extension .csv, ils sont creer et interpreter par notre code pour creer les graphiques.
    Le dossier images contient les image utilisee dans notre projet.
    Le dossier updating contient les codes qui sont importes pour renouveller les statistiques (et un dossier __pycache__ deja expliquer).
    Les fichiers main.py et main_tests.py sont des anciens fichiers avant qu'on choisissent de faire le site internet uniquement en HTML, CSS et javascript avec python
      qui va renouveller les statistiques mais on les a conserver pour montrer des anciennes versions de notre projet. On a aussi ajoute des capture d'ecran montrant ou
      nous sommes arrive dans ces fichiers avant de changer notre projet (main_screenshot.png et main_tests_screenshot.png). Meme si ces code ne seront pas compte dans
      notre projet actuel ils contiennent des explications.

Dans le dossier website:
    Chaque dossier contient un  fichier .html et un fichier .css pour chaque page. Or la page du quiz contenue dans le dossier quiz_page a besoin de javascript (qui est
      un langage de programmation tout comme python) pour pouvoir jouer au quiz, il contient ses propres explications.
    Pour les fichier HTML:
        Chaque fichier commence avec <!DOCTYPE html> pour dire au moteur de recherche que c'est un fichier ecrit en html
        Le langage est compose de "tags", chaqu'un commence comme <tag> et se termine avec </tag> et peuvent contenir entre le tag d'ouverture et le tag de fermeture du
          texte ou aussi d'autre tags. Quelques tags qui ne contiennent rien entre l'ouverture et la fermeture peuvent juste etre composes de l'ouverture sans la
          fermeture comme pour le tag des images <img>.
        Chaque tag peut avoir des attributs places apres le nom du tag dans l'ouverture, par exemple dans <html lang="en" dir="ltr"> les attributs du tag html sont
          lang et dir, ils definissent le langage de la page et la direction de lecture de la page.
        Le tag <head> contient quelques informations en plus sur la page pour le moteur de recherche.
        Le tag <title> definit le titre de la page.
        Le tag <meta> utilise les attributs name et content pour aussi aider le moteur de recherche.
        Le tag <link> utilise les attributs rel et href pour importer les styles de la page d'un fichier .css externe.
        Le tag <body> contient le corps de la page.
        Le tag <div> designe un "conteneur" pour aider a la mise en page de notre website
        Les tags <h1>, <h3>, et <hx> (avec x allant de 1 a 6) designe du texte par defaut interpreter comme titre (header).
        Le tag <p> designe du texte par defaut interpreter comme un paragraphe.
        Le tag <a> designe un lien qui peut prendre a une autre page et utilise l'attribut href.
        Le tag <img> designe des images et utilise les attributs src pour choisir l'image et alt pour mettre du texte au cas ou l'image ne peut etre vue.
        Le tag <button> design un bouton pressable et utilise l'attribut title pour montrer le nom du bouton quand on laisse le curseur au dessus.
        Le tag <ul> definit un liste sans ordre (des points et pas des numeros) et chaque tag <li> definit une ligne de la liste.
        Le tag <script> definit le chemin du fichier javascript qui devra etre importer pour le bon fonctionnement de la page et utilise l'attribut src.
        Quelques tag utilisent un attribut onclick qui refere a une action dans le code javascript.
        Finalement, chaque tag utilise les attributs class et id qui referent aux codes css et javascript exterieurs qui peuvent acceder le code html
          pour changer le style par exemple.
    Pour les fichiers CSS:
        Les tag en html utilisent des attributs class et id, or on peut definir le style des tags utilisant chaque class et id dans css, si un tag
          a une class "explication" on peut changer sont style dans le code css en utilisant .explication{} avec entre les accolades le style.
          Si on utilisait une id a la place de la class on aurai ecrit la meme chose mais a la place du point au debut on aurait mit une disese,
          par exemple #explication{}.
        Apres chaque option de style on doit terminer la ligne par un point virgule ;.
        Les difinitions de chaque option sont plutot explicites (elles ne necessites pas toutes trop d'explications comme color et background-color).
        L'option float est utilisee pour la position des objets
        Les options font-size, font-famili, et font-weight definisse la mise en page l'ecriture et la police.
        L'option transition-duration definit le temps qu'un transition doit prendre
        Quand on ajoute :hover et :visited definit le style des objet au cas ou l'utilisateur poisitionne sont curseur au dessus de l'objet ou s'il a
          deja visite une page (si c'est un lien).
        On peut aussi definir le style par defaut d'un tag directement en ecrivant tag{}.


Finalement quelques petites explications seront aussi dites dans la video.





Merci.
