import requests
import webbrowser
import pyautogui
import time
import re

# Importez la bibliothèque re pour utiliser les expressions régulières
webbrowser.open('http://localhost:1242/commands')
time.sleep(2)

print(time.strftime("%H:%M:%S", time.localtime()))

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



# Ouvrez le fichier en mode lecture
with open('NumberSteamWithCommaErased.txt', 'r') as f:
  
  # Itérez sur chaque ligne du fichier
    for line in f:
      # Divisez la ligne en une liste de mots
      words = line.split(", ")
      # Itérez sur chaque mot de la liste
      
      for word in words:
        # Vérifiez si le mot est un numéro en utilisant l'expression régulière \d+
        if re.match(r'\d+', word):
          # Convertissez le numéro en entier et ajoutez-le à la liste temporaire
          temp_list.append(int(word))
          # Vérifiez si la liste temporaire atteint 30 éléments
          if len(temp_list) == 31:
            # Ajoutez la liste temporaire à la liste de groupes et réinitialisez la liste temporaire
            groups.append(temp_list)
            pyautogui.typewrite('play Yorcal ')
            for i in range(0, 31):
                pyautogui.typewrite(str(temp_list[i]))
                pyautogui.typewrite(', ')
            pyautogui.press('enter')
            time.sleep(600)
            pyautogui.typewrite('reset Yorcal')
            time.sleep(1)   
            pyautogui.press('enter')
            temp_list = []
            print(time.strftime("%H:%M:%S", time.localtime()) + " dernier groupe")
            with open('NumberGroupPassed.txt', 'w') as f5:
              groupAlreadyLaunched = groupAlreadyLaunched + 1
              f5.write(str(groupAlreadyLaunched))

# Ajoutez la dernière liste temporaire à la liste de groupes
groups.append(temp_list)