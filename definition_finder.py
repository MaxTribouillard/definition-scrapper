from bs4 import BeautifulSoup
import requests
import os
from colorama import Fore

mot = input(Fore.LIGHTBLUE_EX + "Saisissez le mot dont vous souhaitez la défintion : ")
url = "https://www.larousse.fr/dictionnaires/francais/" + mot
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
definition = soup.find('ul', class_="Definitions")
print("Voici la définition de " + mot + ":" + str(definition.text))
stock = input("Souhaitez-vous enregistrer les définitions trouvées dans un fichier texte ? (Oui/Non) : ")
if stock == "Oui":
    name_stock = input("Entrez un nom pour votre fichier texte : ")
    file = open(name_stock+".txt", "w+")
    file.write(f"Définition de {mot} : \n {definition.text}")
    file.close()
else:
    exit()
