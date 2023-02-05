import requests
import webbrowser
import pyautogui
import time
import re



# Importez la bibliothèque re pour utiliser les expressions régulières

# Initialisez la liste de groupes et la liste temporaire
groups = []
temp_list = []

with open("NumberGroupPassed.txt", "r") as f:
    groupAlreadyLaunched = int(f.read())

with open('NumberSteamwithComma.txt', 'r') as f:
  with open('NumberSteamWithCommaErased.txt','w') as f2:
    for line in f:
      words = line.split(", ")
      for word in words:
        #obtenir index de word dans la liste
        index = words.index(word)
        if(index >= groupAlreadyLaunched*31):
          f2.write(word + ', ')