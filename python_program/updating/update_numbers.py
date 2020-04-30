from tkinter import Label, Tk, Entry, Button  #de la librairie tkinter on va importer les methodes Label, Tk, Entry et Button
from webbrowser import open as webopen  #de la librairie webbrowser on va importer la methode open et la nommer webopen
from datetime import date, timedelta  #de la librairie datetime on va importer les methodes date et timedelta
from sys import stdout  #de la librairie sys on va importer la mthode stdout


class NewNumbers(Tk):  #on definit le nom de la methode qu'on veut creer et elle a comme methode parent la methode Tk
    def __init__(self):  #la premiere fonction __init__ va etre tout le temps appelee avec la methode (initialisation)
        super(NewNumbers, self).__init__()  #on va heriter de la methode parent sa fonction d'initialisation
        webopen("https://www.worldometers.info/coronavirus/")  #on ouvre une fenetre dans un moteur de recherche qui va nous montrer la page du lien
        self.title_label=Label(text="Enter The Numbers To Update The\nStatistics Page", font=("Arial, Helvetica, sans-serif", 20), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.title_label.grid(row=0, column=0, columnspan=2)  #on place l'etiquette qu'on vient de definir dans une fentre

        self.world_total_label=Label(text="World Total Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.world_total_label.grid(row=1, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.world_total_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.world_total_entry.grid(row=1, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.world_deaths_label=Label(text="World Death Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.world_deaths_label.grid(row=2, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.world_deaths_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.world_deaths_entry.grid(row=2, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.world_reco_label=Label(text="World Recovered Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.world_reco_label.grid(row=3, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.world_reco_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.world_reco_entry.grid(row=3, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.world_active_label=Label(text="World Active Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.world_active_label.grid(row=4, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.world_active_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.world_active_entry.grid(row=4, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre

        self.white_space=Label(text="", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui sera vide pour creer un espace vide
        self.white_space.grid(row=5)  #on place l'etiquette qu'on vient de definir dans la fentre

        self.lebanon_total_label=Label(text="Lebanon Total Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.lebanon_total_label.grid(row=6, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.lebanon_total_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.lebanon_total_entry.grid(row=6, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.lebanon_deaths_label=Label(text="Lebanon Deaths Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.lebanon_deaths_label.grid(row=7, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.lebanon_deaths_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.lebanon_deaths_entry.grid(row=7, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.lebanon_reco_label=Label(text="Lebanon Recovered Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.lebanon_reco_label.grid(row=8, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.lebanon_reco_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.lebanon_reco_entry.grid(row=8, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.lebanon_active_label=Label(text="Lebanon Active Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.lebanon_active_label.grid(row=9, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.lebanon_active_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.lebanon_active_entry.grid(row=9, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre

        self.white_space=Label(text="", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui sera vide pour creer un espace vide
        self.white_space.grid(row=10)  #on place l'etiquette qu'on vient de definir dans la fentre

        self.iran_total_label=Label(text="Iran Total Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.iran_total_label.grid(row=11, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.iran_total_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.iran_total_entry.grid(row=11, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.iran_deaths_label=Label(text="Iran Deaths Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.iran_deaths_label.grid(row=12, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.iran_deaths_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.iran_deaths_entry.grid(row=12, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.iran_reco_label=Label(text="Iran Recovered Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.iran_reco_label.grid(row=13, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.iran_reco_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.iran_reco_entry.grid(row=13, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.iran_active_label=Label(text="Iran Active Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.iran_active_label.grid(row=14, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.iran_active_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.iran_active_entry.grid(row=14, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre

        self.white_space=Label(text="", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui sera vide pour creer un espace vide
        self.white_space.grid(row=15)  #on place l'etiquette qu'on vient de definir dans la fentre

        self.japan_total_label=Label(text="Japan Total Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.japan_total_label.grid(row=16, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.japan_total_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.japan_total_entry.grid(row=16, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.japan_deaths_label=Label(text="Japan Deaths Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.japan_deaths_label.grid(row=17, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.japan_deaths_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.japan_deaths_entry.grid(row=17, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.japan_reco_label=Label(text="Japan Recovered Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.japan_reco_label.grid(row=18, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.japan_reco_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.japan_reco_entry.grid(row=18, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre
        self.japan_active_label=Label(text="Japan Active Cases: ", font=("Arial, Helvetica, sans-serif", 15), fg="#000000", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui va montrer du texte
        self.japan_active_label.grid(row=19, column=0, sticky="w")  #on place l'etiquette qu'on vient de definir dans la fentre
        self.japan_active_entry=Entry()  #on definit un champ de texte ou l'utilisateur peut ajouter des valeurs
        self.japan_active_entry.grid(row=19, column=1, sticky="e")  #on place le champ de texte qu'on vient de definir dans la fenetre

        self.white_space=Label(text="", bg="#cfcfcf")  #on defini un champ de texte (ou etiquette) qui sera vide pour creer un espace vide
        self.white_space.grid(row=20)  #on place l'etiquette qu'on vient de definir dans la fentre

        self.update_bttn=Button(text="Update Numbers", command=self.update_values)  #on definit un bouton qui montre du texte et quand il sera presse il appelera la fonction update_values
        self.update_bttn.grid(row=21, column=1, sticky="e")  #on place le bouton qu'on vient de definir dans la fentre

    def update_values(self):  #on definit une nouvelle fonction qui ne prendre effet que quand elle sera appelee
        self.world_total=self.world_total_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.world_deaths=self.world_deaths_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.world_reco=self.world_reco_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.world_active=self.world_active_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.lebanon_total=self.lebanon_total_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.lebanon_deaths=self.lebanon_deaths_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.lebanon_reco=self.lebanon_reco_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.lebanon_active=self.lebanon_active_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.iran_total=self.iran_total_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.iran_deaths=self.iran_deaths_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.iran_reco=self.iran_reco_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.iran_active=self.iran_active_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.japan_total=self.japan_total_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.japan_deaths=self.japan_deaths_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.japan_reco=self.japan_reco_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.japan_active=self.japan_active_entry.get()  #on prend les valeurs que l'utilisateur a entre dans le champ de texte
        self.update_date=date.today()  #on defnit une variable qui contient la date d'aujourdhui
        self.update_date-=timedelta(days=1)  #on enleve un jour a la date d'aujourdhui pour avoir la date d'hier
        self.update_date=self.update_date.strftime("%d/%m/%Y")  #on definit le format avec le quel cette date sera vue
        self.update_text="Values and Graphs Succesfully \nUpdated as of "+self.update_date  #on definit une variable qui contiendra le texte avec la date
        self.title_label["text"]=self.update_text  #on modifie le texte de l'etiquette
        self.title_label["bg"]="#ff0000"  #on modifie le font du texte qu'on va ajouter pour qu'il soit rouge

        #on definit une variable qui contient le code HTML avec les nouvelles valeurs entrees par l'utilisateur
        self.html_stat_code=f"""
<!DOCTYPE html>

<html lang="en" dir="ltr">
  <head>
    <title>coronaReady - Statistics</title>
    <meta name="keywords" content="coronaReady, coronavirus, corona, COVID19, COVID-19">
    <meta name="description" content="A page about the coronavirus">
    <meta name="author" content="coronaReady">
    <meta charset="utf-8">
    <link rel="stylesheet" href="website/universal_css.css">
    <link rel="stylesheet" href="website/stats_page/stats_page.css">
    <link rel="icon" href="https://raw.githubusercontent.com/bechara-rizk/coronaReady/master/python_program/images/corona_logo.png">
  </head>
  <body>
    <div class="header">
      <img src="https://raw.githubusercontent.com/bechara-rizk/coronaReady/master/python_program/images/corona_banner_720.png", alt="coronaReady logo">
      <a href="index.html"><button class="head_buttons", title="Go to Home page"><img src="python_program/images/home_bttn.png", alt="Home button"></button></a>
      <a href="info_page.html"><button class="head_buttons", title="Go to Informations page"><img src="python_program/images/info_bttn.png", alt="Info button"></button></a>
      <a href="articles_page.html"><button class="head_buttons", title="Go to Articles page"><img src="python_program/images/articles_bttn.png", alt="Articles button"></button></a>
      <a href="stats_page.html"><button class="head_buttons head_buttons_active", title="Go to Statistics page"><img src="python_program/images/stats_bttn.png", alt="Statistics button"></button></a>
      <a href="tips_page.html"><button class="head_buttons", title="Go to Tips page"><img src="python_program/images/tips_bttn.png", alt="Tips button"></button></a>
      <a href="sum_page.html"><button class="head_buttons", title="Go to Daily Summary page"><img src="python_program/images/sum_bttn.png", alt="Dailt Summary button"></button></a>
      <a href="quiz_page.html"><button class="head_buttons", title="Go to Quiz page"><img src="python_program/images/quiz_bttn.png", alt="Quiz button"></button></a>
    </div>
    <h1 class="page_title">COVID-19 Statistics</h1>
    <a href="https://www.worldometers.info/coronavirus/", target="_blank">
      <div class="cases source">
        <h1>World-wide cases</h1>
        <p>Total: {self.world_total}</p>
        <p>Active: {self.world_active}</p>
        <p>Recovered: {self.world_reco}</p>
        <p>Deaths: {self.world_deaths}</p>
      </div>
    </a>
    <div class="cases">
      <h1>Lebanese cases</h1>
      <p>Total: {self.lebanon_total}</p>
      <p>Active: {self.lebanon_active}</p>
      <p>Recovered: {self.lebanon_reco}</p>
      <p>Deaths: {self.lebanon_deaths}</p>
      <img src="python_program/images/data_corona_plot_Lebanon.png", alt="line plot">
    </div>
    <div class="cases">
      <h1>Iranian cases</h1>
      <p>Total: {self.iran_total}</p>
      <p>Active: {self.iran_active}</p>
      <p>Recovered: {self.iran_reco}</p>
      <p>Deaths: {self.iran_deaths}</p>
      <img src="python_program/images/data_corona_plot_Iran.png", alt="line plot">
    </div>
    <div class="cases">
      <h1>Japanese cases</h1>
      <p>Total: {self.japan_total}</p>
      <p>Active: {self.japan_active}</p>
      <p>Recovered: {self.japan_reco}</p>
      <p>Deaths: {self.japan_deaths}</p>
      <img src="python_program/images/data_corona_plot_Japan.png", alt="line plot">
    </div>
    <div class="updt">
      <p>Last update: {self.update_date}</p>
    </div>
  </body>
</html>
"""
        #on definit une variable qui contient le code HTML avec les nouvelles valeurs entrees par l'utilisateur
        self.html_home_code=f"""
<!DOCTYPE html>

<html lang="en" dir="ltr">
  <head>
    <title>coronaReady - Home</title>
    <meta name="keywords" content="coronaReady, coronavirus, corona, COVID19, COVID-19">
    <meta name="description" content="A page about the coronavirus">
    <meta name="author" content="coronaReady">
    <meta charset="utf-8">
    <link rel="stylesheet" href="website/universal_css.css">
    <link rel="stylesheet" href="website/home_page/home_page.css">
    <link rel="icon" href="https://raw.githubusercontent.com/bechara-rizk/coronaReady/master/python_program/images/corona_logo.png">
  </head>
  <body>
    <div class="header">
      <img src="https://raw.githubusercontent.com/bechara-rizk/coronaReady/master/python_program/images/corona_banner_720.png", alt="coronaReady logo">
      <a href="index.html"><button class="head_buttons head_buttons_active", title="Go to Home page"><img src="python_program/images/home_bttn.png", alt="Home button"></button></a>
      <a href="info_page.html"><button class="head_buttons", title="Go to Informations page"><img src="python_program/images/info_bttn.png", alt="Info button"></button></a>
      <a href="articles_page.html"><button class="head_buttons", title="Go to Articles page"><img src="python_program/images/articles_bttn.png", alt="Articles button"></button></a>
      <a href="stats_page.html"><button class="head_buttons", title="Go to Statistics page"><img src="python_program/images/stats_bttn.png", alt="Statistics button"></button></a>
      <a href="tips_page.html"><button class="head_buttons", title="Go to Tips page"><img src="python_program/images/tips_bttn.png", alt="Tips button"></button></a>
      <a href="sum_page.html"><button class="head_buttons", title="Go to Daily Summary page"><img src="python_program/images/sum_bttn.png", alt="Dailt Summary button"></button></a>
      <a href="quiz_page.html"><button class="head_buttons", title="Go to Quiz page"><img src="python_program/images/quiz_bttn.png", alt="Quiz button"></button></a>
    </div>
    <h1 class="page_title">Home</h1>
    <a href="info_page.html">
      <div class="info_preview">
        <h1 class="info_title">Virus Information</h1>
        <p class="info_text">
          People may experience
          <ul class="info_list">
            <li>Cough</li>
            <li>Fever</li>
            <li>Tiredness</li>
            <li>Difficulty breathing (severe cases)</li>
            <li>Very occasionally, loss of appetite</li>
          </ul>
        </p>
      </div>
    </a>
    <a href="stats_page.html">
      <div class="info_preview">
        <h1 class="info_title">Statistics</h1>
        <div class="stats_div">
          <h3 class="stats_title">World-wide cases</h1>
          <p class="stats_numbers">Total: {self.world_total}</p>
          <p class="stats_numbers">Active: {self.world_active}</p>
          <p class="stats_numbers">Recovered: {self.world_reco}</p>
          <p class="stats_numbers">Deaths: {self.world_deaths}</p>
        </div>
        <div class="stats_div">
          <h3 class="stats_title">Lebanese cases</h1>
          <p class="stats_numbers">Total: {self.lebanon_total}</p>
          <p class="stats_numbers">Active: {self.lebanon_active}</p>
          <p class="stats_numbers">Recovered: {self.lebanon_reco}</p>
          <p class="stats_numbers">Deaths: {self.lebanon_deaths}</p>
        </div>
      </div>
    </a>
    <a href="articles_page.html">
      <div class="info_preview">
        <h1 class="info_title">Articles</h1>
        <article class="article_quote">
          <img src="python_program/images/web_seek_pic.jpeg", alt="article picture", class="article_pic">
          <h1 class="article_title">Speakup Covid</h1>
          <p class="article_text">"With reference to the ethical code of psychologists, this professional and experienced team will be offering psychological support to the frontline Health Caregivers dealing with the outbreak of Novel Coronavirus (COVID-19)."</p>
        </article>
        <article class="article_quote">
          <img src="python_program/images/web_thae-pic.jpg", alt="article picture", class="article_pic">
          <h1 class="article_title">How The Pandemic Will End ~ The Atlantic</h1>
          <p class="article_text">"Three months ago, no one knew that SARS-CoV-2 existed. Now the virus has spread to almost every country, infecting at least 446,000 people whom we know about, and many more whom we do not."</p>
        </article>
      </div>
    </a>
    <a href="tips_page.html">
      <div class="info_preview">
        <h1 class="info_title">Tips</h1>
        <p class="info_text"><ul class="info_list">
          <li>Stay Home</li>
          <li>Wash Your Hands</li>
          <li>Practice Social Distancing</li>
          <li>Rest</li>
          <li>Keep Warm</li>
        </ul></p>
      </div>
    </a>
  </body>
</html>

        """

        #on ouvre le fichier HTML, on ecrit le nouveau code avec les nouvelles valeurs et puis on le ferme
        self.stat_code=open("/Users/bechara/Desktop/github/coronaReady/stats_page.html", "w")
        self.stat_code.write(self.html_stat_code)
        self.stat_code.close()
        #on ouvre le fichier HTML, on ecrit le nouveau code avec les nouvelles valeurs et puis on le ferme
        self.home_code=open("/Users/bechara/Desktop/github/coronaReady/index.html","w")
        self.home_code.write(self.html_home_code)
        self.home_code.close()
        self.after(4000, self.destroy)  #apres 4 secondes que toutes les actions soient finies la fenetre va se fermer automatiquement

if __name__=="__main__":  #si ce code est execute directement (s'il n'est pas importe en tant que librairie)
    number=NewNumbers()  #On appele la methode NewNumbers qui va renouveler les valeurs du site internet avec les valeurs que nous allons entrer
    number.title("Update coronaReady")  #puis on definit le titre de la fenetre qui sera ouverte
    number.configure(bg="#cfcfcf")  #et on fixe la couleur du fond au gris
    number.mainloop()  #c'est une boucle infinie (tant que la fenetre nest pas fermee), elle va attendre qu'un evenement se produise et le traitera si besoin
