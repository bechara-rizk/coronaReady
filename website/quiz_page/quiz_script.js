//on declare des variables qui contiennent les elements du code html par leur id
const start = document.getElementById("start");
const quiz = document.getElementById("quiz");
const question = document.getElementById("question");
const qImg = document.getElementById("qImg");
const choiceA = document.getElementById("A");
const choiceB = document.getElementById("B");
const choiceC = document.getElementById("C");
const counter = document.getElementById("counter");
const timeGauge = document.getElementById("timeGauge");
const progress = document.getElementById("progress");
const scoreDiv = document.getElementById("scoreContainer");

//on definit un tableau qui contient les questions du quiz, chaque question est un objet contenant la question, les reponses possibles et la bonne reponse avec une image
let questions = [
  {
    question : "How can you contract the COVID-19? ",
    imgSrc : "/Users/bechara/Desktop/github/coronaReady/python_program/images/corona_logo.png",
    choiceA : "Through animals",
    choiceB : "Through droplets of saliva or discharge from the nose",
    choiceC : "Through heated food",
    correct : "B"
  },
  {
    question : "Why is it important to wash your hands as much as you can?",
    imgSrc : "/Users/bechara/Desktop/github/coronaReady/python_program/images/corona_logo.png",
    choiceA : "To make them look nice and elegant",
    choiceB : "To waste water",
    choiceC : "To eliminate all the traces of viruses on your hands",
    correct : "C"
  },
  {
    question : "Why should you keep your hands away from your face?",
    imgSrc : "/Users/bechara/Desktop/github/coronaReady/python_program/images/corona_logo.png",
    choiceA : "To keep your face beautiful",
    choiceB : "Germs can take up residence in your mucous membranes",
    choiceC : "To avoid scratching your spots",
    correct : "B"
  },
  {
    question : "When should you wear a mask?",
    imgSrc : "/Users/bechara/Desktop/github/coronaReady/python_program/images/corona_logo.png",
    choiceA : "All the time",
    choiceB : "When at home",
    choiceC : "When close to people",
    correct : "C"
  },
  {
    question : "What are the most common symptoms caused by COVID-19? ",
    imgSrc : "/Users/bechara/Desktop/github/coronaReady/python_program/images/corona_logo.png",
    choiceA : "Cough, fever, tiredness",
    choiceB : "Loss of weight, pain in the back and vomiting",
    choiceC : "Loss of appetite and difficulty breathing",
    correct : "A"
  },
  {
    question : "Why is it important to practice confinement and self-isolation? ",
    imgSrc : "/Users/bechara/Desktop/github/coronaReady/python_program/images/corona_logo.png",
    choiceA : "Stay home to save others because the incubation period is 0 to 14 days",
    choiceB : "Stay home in order not to go to school",
    choiceC : "Stay home to watch TV",
    correct : "A"
  },
];

//on declare de nouvelles variables
const lastQuestion = questions.length - 1;  //on definit l'esmplacement (index) de la derniere question dans le tableau
let runningQuestion = 0;  //la question actuelle
let count = 0;  //le temps de chaque question commence a zero
const questionTime = 10;  //et se termine a 10 secondes
const gaugeWidth = 150;  //la largeur en pixels de la barre du temps
const gaugeUnit = gaugeWidth / questionTime;  //combie de la barre sera remplie a chaque seconde
let TIMER;
let score = 0;  //au debut le score est definit a zero

//on definit une fonction qui va ajouter et changer les questions dans le code html
function renderQuestion(){
    let q = questions[runningQuestion];  //on definit une variable qui va acceder a chaque question seule par rapport au numero de la question actuelle
    question.innerHTML = "<p>"+ q.question +"</p>";  //on ajoute le texte de la question
    qImg.innerHTML = "<img src="+ q.imgSrc +">";  //puis l'image
    choiceA.innerHTML = q.choiceA;  //et les 3 choix de reponse
    choiceB.innerHTML = q.choiceB;
    choiceC.innerHTML = q.choiceC;
}

start.addEventListener("click",startQuiz);  //quand l'element qui contient le bouton pour commencer le quiz est presse par l'utilisateur appeler la fonction qui va commencer le quiz et donc appeler toutes les autres fonctions

//on definit la fonction qui s'oocupe de commencer le quiz
function startQuiz(){
    start.style.display = "none";  //on cache l'element qui contenait le bouton pour commencer le quiz
    renderQuestion();  //on appele la fonction qui va montrer une question avec son image et les choix possibles
    quiz.style.display = "block";  //on montre l'element qui contient la question
    renderProgress();  //on appele la fonction qui va ajouter des cercles pour le nombre de questions
    renderCounter();  //on appele la fonction qui s'occupe du temps de chaque question
    TIMER = setInterval(renderCounter,1000); //chaque seconde on va appeler la fonction qui s'occupe du temps de chaque question
}

//on definit une fonction qui va ajouter les cercles en bas a droite du conteneur pour montrer a l'utilisateur ou il en est
function renderProgress(){
    for(let qIndex = 0; qIndex <= lastQuestion; qIndex++){  //on definit une boucle qui va ajouter une cercle pour chaque question
        progress.innerHTML += "<div class='prog' id="+ qIndex +"></div>";  //pour chaque question on va acceder le code html et ajouter un cercle
    }
}

//on definit une fonction qui va s'occuper du temps de chaque question
function renderCounter(){
    if(count <= questionTime){  //si le temps utilise est plus petit ou egal au temps maximal
        counter.innerHTML = count;  //changer le nombre du temps dans le code html
        timeGauge.style.width = count * gaugeUnit + "px";  //et la portion utilisee de la barre
        count++  //et ajouter 1 (ou une seconde) au temps utilise
    }else{  //si la condition precedente n'est pas satisfaite et donc l'utilisateur n'a pas repondu a temps
        count = 0;  //on remet le temps utilise a zero
        answerIsWrong();  //la reponse sera considere comme fausse et le cercle correspondant sera colore en rouge
        if(runningQuestion < lastQuestion){  //si la question actuelle n'est pas la derniere
            runningQuestion++;  //ajouter 1 a la question actuelle
            renderQuestion();  //on appele la fonction qui va montrer une question avec son image et les choix possibles
        }else{  //si la condition precedente n'est pas satisfaite alors c'est la derniere question
            clearInterval(TIMER);  //on va arreter le temps contenu dans cette variable
            scoreRender();  //on appele la fonction qui va montrer le score final
        }
    }
}

//on definit une fonction qui va voir quelle reponse nous avons choisi et prend comme argument la lettre de la reponse choisie
function checkAnswer(answer){
    if( answer == questions[runningQuestion].correct){  //si la reponse choisie correspond a la bonne reponse de la question
        score++; //on ajoute un point au score
        answerIsCorrect();  //on appele la fonction qui va changer la couleur du cercle correspondant a la question au vert
    }else{  //si la condition n'est pas satisfaite et donc la reponse donnee est fausse
        answerIsWrong();  //on appele la fonction qui va changer la couleur du cercle correspondant a la question au rouge
    }
    count = 0;  //apres chaque question on remet le temps utilise a zero
    if(runningQuestion < lastQuestion){  //si la question actuelle n'est pas la derniere
        runningQuestion++;  //ajouter 1 a la question actuelle
        renderQuestion();  //on appele la fonction qui va montrer une question avec son image et les choix possibles
    }else{  //si la condition precedente n'est pas satisfaite alors c'est la derniere question
        clearInterval(TIMER);  //on va arreter le temps contenu dans cette variable
        scoreRender();  //on appele la fonction qui va montrer le score final
    }
}

//on definit une fonction qui va changer la couleur du cercle correspondant a la question au vert
function answerIsCorrect(){
    document.getElementById(runningQuestion).style.backgroundColor = "#00ff00";  //on change la couleur du font du cercle dans le code html au vert
}

//on definit une fonction qui va changer la couleur du cercle correspondant a la question au rouge
function answerIsWrong(){
    document.getElementById(runningQuestion).style.backgroundColor = "#f00f00";  //on change la couleur du font du cercle dans le code html au rouge
}

//on definit une fonction qui va montrer le score final
function scoreRender(){
    scoreDiv.style.display = "block";  //on montre le conteneur du score
    const scorePerCent = Math.round(100 * score/questions.length);  //on definit une variable qui contiendra le pourcentage de reponse justes arrondie a l'entier
    //on definit une variable qui par rapport au pourcentage obtenu va montrer une image differente a la fin du quiz
    let img = (scorePerCent >= 80) ? "/Users/bechara/Desktop/github/coronaReady/python_program/images/result_img_5.png" :
              (scorePerCent >= 60) ? "/Users/bechara/Desktop/github/coronaReady/python_program/images/result_img_4.png" :
              (scorePerCent >= 40) ? "/Users/bechara/Desktop/github/coronaReady/python_program/images/result_img_3.png" :
              (scorePerCent >= 20) ? "/Users/bechara/Desktop/github/coronaReady/python_program/images/result_img_2.png" :
              "/Users/bechara/Desktop/github/coronaReady/python_program/images/result_img_1.png";
    scoreDiv.innerHTML = "<img src="+ img +">";  //on accede au code html pour ajouter l'image correspondante au score
    scoreDiv.innerHTML += "<p>"+ scorePerCent +"%</p>";  //et on ajoute le pourcentage en dessous de l'image
}
