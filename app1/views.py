from django.shortcuts import render
from .extraire_texte import extraction
from .models import Professeur, Etudiant, Quizz, Cours
from rest_framework import viewsets
from .serializers import Cours_Serializers
from .serializers import Quizz_Serializers
from .serializers import Etudiant_Serializers
from .serializers import Professeur_Serializers


# UTILISATION DES DONNEES CONVERTIT EN JSONS ( c'est ça un endpoint)

class Cours_ViewSest(viewsets.ModelViewSet):
    queryset=Cours.objects.all() #recup tout les donnes enrengistre et qui sont  associeé a cette table
    serializer_class=Cours_Serializers

class Etudiant_ViewSest(viewsets.ModelViewSet):
    queryset=Etudiant.objects.all() #recup tout les donnes enrengistre et qui sont  associeé a cette table
    serializer_class=Etudiant_Serializers

class Quizz_ViewSest(viewsets.ModelViewSet):
    queryset=Quizz.objects.all() #recup tout les donnes enrengistre et qui sont  associeé a cette table
    serializer_class=Quizz_Serializers

class Professeur_ViewSest(viewsets.ModelViewSet):
    queryset=Professeur.objects.all() #recup tout les donnes enrengistre et qui sont  associeé a cette table
    serializer_class=Professeur_Serializers
# Create your views here.

def index(request): #La fonction qui va traiter les requetes https qu'elle va recevoir
    fichier=request.FILES.get("fichier")# recup le contenue texte du fichier
    if fichier is None:
        return render(request, "index.html",{ "erreur":"pas de fichier"})
    texte=extraction(fichier);
    return render(request, "index.html", texte) #transoforme le code(html?) en qq chose de visible à l'ecran 
    """context={
        "professeur": professeur,
        "etudiant": etudiant,
        "cours": cours,
        "quizz": quizz,
    }"""