from pandas import read_csv, melt  #import uniquement de deux methodes specifiques de la librairie pandas
import matplotlib  #import de la librairie matplotlib
matplotlib.use("TkAgg")  #on definit le "backend" de la librairie qu'on veut que notre code utilise
from matplotlib import pyplot as plt #import uniquement d'une methode specifique de la librairie matplotlib et la nommer plt

class Graph():  #on definit le nom de la methode qu'on veut creer
    def __init__(self, country):  #la premiere fonction __init__ va etre tout le temps appelee avec la methode (initialisation), et on definit un argument que l'utilisateur va entrer en appelant la methode
        self.in_file=read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")  #on definit une variable qui va contenir un fichier csv importe directement de l'internet
        self.country_file=self.in_file.loc[self.in_file["Country/Region"]==country,:]  #on defnit une variable qui va contenir uniquement le nombre de cas du pays que l'utilisateur a entre
        self.country_file=self.country_file.drop(columns=["Lat", "Long", "Province/State"])  #on efface les cases non voulues dans les nombres restants
        self.country_file=melt(self.country_file, id_vars=["Country/Region"])  #on echange le format des donnee de large en long
        self.country_file=self.country_file.value.values  #on garde uniquement les cases dans la colone value et on efface tout le reste
        self.file=open(f"/Users/bechara/Desktop/github/coronaReady/python_program/data/data_corona_{country}.csv", "w")  #on ouvre un fichier specifique au pays entre par l'utilisateur en mode ecriture, si le fichier n'existeait pas il sera creer et s'il existait les donnees qu'il contenait seront ecrasees
        self.file.write(str(self.country_file))  #on ecrit le contenu de la variable dans le fichier ouvert
        self.file.close()  #on sauvegarde le fichier et on le ferme
        self.file=open(f"/Users/bechara/Desktop/github/coronaReady/python_program/data/data_corona_{country}.csv", "r")  #on reouvre le meme fichier mais cette fois en mode lecture
        self.data=[]  #on defnit le nom d'un tableau
        self.data=self.file.read()  #et on met le contenu du fichier qu'on vient d'ouvrir dans le tableau qu'on a definit
        self.file.close()  #on ferme le fichier apres en avoir finit
        self.data=self.data.split()  #le tableau contient les donnees en 1 seul objet alors on va le diviser entre chaque espace en plusieurs objets
        self.data_len=len(self.data)  #on definit une variable qui va contenir le nombre d'objets dans le tableau
        for self.a in range(self.data_len):  #on va modifier chaque objet du tableau seul
            try:  #on va essayer d'executer la commande suivante, si une erreur survient on executera les commandes dans le except
                self.data[a]=int(self.data[self.a])  #on essaye de rendre chaque objet de str a int
            except:  #on va executer ces commandes uniquement si une erreur survient dans la commande du try
                if self.data[self.a]=="[":  #si l'objet est un "[" debut des donnees
                    self.data[self.a]=0  #changer cet objet a un 0
                elif self.data[self.a].endswith("]")==True:  #si l'ojbet finit par un "]"
                    self.data[self.a]=int(self.data[self.a][:-1])  #effacer le "]" et puis changer le type de l'objet de str a int
        plt.plot(self.data, color="#ff0000")  #on cree un graphique avec la couleur de la ligne en rouge
        plt.xlabel("days since 22/01/2020")  #on definit le nom de l'axe des abscisses
        plt.ylabel("Total cases")  #on definit le nom de l'axe des ordonnees
        plt.savefig(f"/Users/bechara/Desktop/github/coronaReady/python_program/images/data_corona_plot_{country}.png", bbox_inches="tight")  #on sauvegarde le graphique creer en image avec un nom specifique pour chaque pays et on enleve les bordures du tableau
        plt.clf()  #on remet le graphique a zero (vide)

if __name__=="__main__":  #si ce code est execute directement (s'il n'est pas importe en tant que librairie)
    lebanon=Graph("Lebanon")  #on appele la methode qu'on a cree et donc elle renouvelle le graphique du Liban
    iran=Graph("Iran")  #on appele la methode qu'on a cree et donc elle renouvelle le graphique de l'Iran
    japan=Graph("Japan")  #on appele la methode qu'on a cree et donc elle renouvelle le graphique du Japon
