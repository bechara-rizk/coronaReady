from tkinter import *  #de la librairie tkinter on va importer toutes les methodes
from sys import path  #de la librairie sys on va importer uniquement laa methode path


class Application(Tk):  #on definit le nom de la methode qu'on veut creer et elle a comme methode parent la methode Frame
    def __init__(self, *args, **kwargs):  #la premiere fonction __init__ va etre tout le temps appelee avec la methode (initialisation)
        super(Application, self).__init__()  #on va heriter de la methode parent sa fonction d'initialisation
        self.img_path=path[0]+"/images/"  #on definit une variable qui contiendra le chemin des images
        self.img_path.replace("\\", "/")  #au cas ou il y a des \ dans le chemin les remplacer par des /
        self.corona_banner=self.img_path+"corona_banner_720.png"  #on definit une variable qui aura le chemin d'une image
        self.corona_banner_img=PhotoImage(file=self.corona_banner)  #on dit a l'interprete que c'est une image
        Label(image=self.corona_banner_img).grid(row=0, column=0, ipadx=5)  #on place l'image dans la fenetre
        self.home_bttn_img=self.img_path+"home_bttn.png"  #on definit une variable qui aura le chemin d'une image
        self.home_bttn_img1=PhotoImage(file=self.home_bttn_img)  #on dit a l'interprete que c'est une image
        self.info_bttn_img=self.img_path+"info_bttn.png"  #on definit une variable qui aura le chemin d'une image
        self.info_bttn_img1=PhotoImage(file=self.info_bttn_img)  #on dit a l'interprete que c'est une image
        self.articles_bttn_img=self.img_path+"articles_bttn.png"  #on definit une variable qui aura le chemin d'une image
        self.articles_bttn_img1=PhotoImage(file=self.articles_bttn_img)  #on dit a l'interprete que c'est une image
        self.stats_bttn_img=self.img_path+"stats_bttn.png"  #on definit une variable qui aura le chemin d'une image
        self.stats_bttn_img1=PhotoImage(file=self.stats_bttn_img)  #on dit a l'interprete que c'est une image
        self.tips_bttn_img=self.img_path+"tips_bttn.png"  #on definit une variable qui aura le chemin d'une image
        self.tips_bttn_img1=PhotoImage(file=self.tips_bttn_img)  #on dit a l'interprete que c'est une image
        self.sum_bttn_img=self.img_path+"sum_bttn.png"  #on definit une variable qui aura le chemin d'une image
        self.sum_bttn_img1=PhotoImage(file=self.sum_bttn_img)  #on dit a l'interprete que c'est une image
        self.quiz_bttn_img=self.img_path+"quiz_bttn.png"  #on definit une variable qui aura le chemin d'une image
        self.quiz_bttn_img1=PhotoImage(file=self.quiz_bttn_img)  #on dit a l'interprete que c'est une image
        self.home_bttn=Button(text="Home", image=self.home_bttn_img1, highlightbackground="#ffffff", width=97, height=75, command=self.home_page)  #on definit un bouton qui va montrer une image
        self.info_bttn=Button(text="Info", image=self.info_bttn_img1, highlightbackground="#ffffff", width=97, height=75, command=self.info_page)  #on definit un bouton qui va montrer une image
        self.articles_bttn=Button(text="Articles", image=self.articles_bttn_img1, highlightbackground="#ffffff", width=97, height=75, command=self.articles_page)  #on definit un bouton qui va montrer une image
        self.stats_bttn=Button(text="Statistics", image=self.stats_bttn_img1, highlightbackground="#ffffff", width=97, height=75, command=self.stats_page)  #on definit un bouton qui va montrer une image
        self.tips_bttn=Button(text="Tips", image=self.tips_bttn_img1, highlightbackground="#ffffff", width=97, height=75, command=self.tips_page)  #on definit un bouton qui va montrer une image
        self.sum_bttn=Button(text="Daily Summary", image=self.sum_bttn_img1, highlightbackground="#ffffff", width=97, height=75, command=self.summary_page)  #on definit un bouton qui va montrer une image
        self.quiz_bttn=Button(text="coronaQuiz", image=self.quiz_bttn_img1, highlightbackground="#ffffff", width=97, height=75, command=self.quiz_page)  #on definit un bouton qui va montrer une image
        self.home_bttn.grid(row=0, column=1)  #on place le bouton dans la fenetre
        self.info_bttn.grid(row=0, column=2)  #on place le bouton dans la fenetre
        self.articles_bttn.grid(row=0, column=3)  #on place le bouton dans la fenetre
        self.stats_bttn.grid(row=0, column=4)  #on place le bouton dans la fenetre
        self.tips_bttn.grid(row=0, column=5)  #on place le bouton dans la fenetre
        self.sum_bttn.grid(row=0, column=6)  #on place le bouton dans la fenetre
        self.quiz_bttn.grid(row=0, column=7)  #on place le bouton dans la fenetre

        self.main_frame = Frame(bg="#0000ff")  #on definit un cadre qui aura la couleur bleue
        self.main_frame.grid(row = 1, column=0, columnspan = 8, sticky = "news")  #on place le cadre
        Grid.rowconfigure(self, 1, weight = 1)  #on modifie les parametres de l'emplacement du cadre

        self.page_title = Label(self.main_frame, text="Home", font = 90)  #on definit une etiquette qui va montrer du texte
        self.page_title.place(anchor="center", relx = 0.5, rely = 0.05)  #on place l'etiquette dans la fenetre

    def home_page(self):  #on definit une fonction qui pourrat etre appele apres
        self.page_title["text"]="Home"  #quand la fonction sera appelee le texte de l'etiquete va changer

    def info_page(self):  #on definit une fonction qui pourrat etre appele apres
        self.page_title["text"]="Info"  #quand la fonction sera appelee le texte de l'etiquete va changer

    def articles_page(self):  #on definit une fonction qui pourrat etre appele apres
        self.page_title["text"]="Articles"  #quand la fonction sera appelee le texte de l'etiquete va changer

    def stats_page(self):  #on definit une fonction qui pourrat etre appele apres
        self.page_title["text"]="Statistics"  #quand la fonction sera appelee le texte de l'etiquete va changer

    def tips_page(self):  #on definit une fonction qui pourrat etre appele apres
        self.page_title["text"]="Tips"  #quand la fonction sera appelee le texte de l'etiquete va changer

    def summary_page(self):  #on definit une fonction qui pourrat etre appele apres
        self.page_title["text"]="Summary"  #quand la fonction sera appelee le texte de l'etiquete va changer

    def quiz_page(self):  #on definit une fonction qui pourrat etre appele apres
        self.page_title["text"]="Quiz"  #quand la fonction sera appelee le texte de l'etiquete va changer


root=Application()  #on appele la methode qu'on a cree
root.title("coronaReady")  #le nom de la fenetre est definit a coronaReady
root.geometry("1440x860")  #les dimensions de la fenetre seront 1440 pixels en large par 860 pixels en long
root.configure(bg="#ffffff")  #le font de la fenetre sera blanc
root.mainloop()  #c'est une boucle infinie (tant que la fenetre nest pas fermee), elle va attendre qu'un evenement se produise et le traitera si besoin
