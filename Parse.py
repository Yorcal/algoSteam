import sys
import os

    # Ouvrez le fichier en mode écriture
with open('NumberSteamwithComma.txt', 'w', encoding='utf-8') as f:
  # Ouvrez l'autre fichier en mode lecture
  with open('AnotherSteamGame.txt', 'r', encoding='utf-8') as input_file:
    # Itérez sur chaque ligne du fichier
    for line in input_file:
      # Divisez la ligne en une liste de mots
      words = line.split()
      print(line)
      # Récupérez le premier mot (le numéro de package) et enlevez les espaces inutiles autour de lui
      package_number = words[0].strip()
      # Écrivez le numéro de package dans le fichier
      f.write(package_number + ', ')