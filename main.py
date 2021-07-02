from math import *
import os

def clear():
  os.system("cls")

# Partie Menu

def main():

  print("\nMath Basics")


# choix des fonctionnalités
  user = input("\n[1] Pythagore\n[2] Reciproque Pythagore\n[3] Calculer un volume\n[4] Calculer l'air\n\nChoisissez un chiffre : ")

  if user == "1":
    pythagore()
  elif user == "2":
    reciproque_pythagore()
  elif user == "3":
    volumes()
  elif user == "4":
    air()
  else:
    #en cas d'une erreur de saisi
   print("S'il vous plaît, choisissez un chiffre.")
   main()

#fin de la partie menu


#fonctionnalités

def pythagore():

  clear()

  valeur_ab = int(input("Entrez la valeur pour ab : "))
  valeur_bc = int(input("Entrez la valeur pour bc : "))

# Calcul
  resultat_pythagore = sqrt((valeur_ab**2 + valeur_bc**2))


# détail du calcul
  print(f"AC² = AB² + BC²\nAC² = {valeur_ab}² + {valeur_bc}²\nAC² = {valeur_ab**2} + {valeur_bc**2}\nAC² = {valeur_ab**2 + valeur_bc**2}\nAC = racine carré de({valeur_ab**2 + valeur_bc**2}) = {resultat_pythagore}")


#retour au menu
  main()



def reciproque_pythagore():

  # supprime les msg de la console
  clear()
  valeur_ab = float(input("Entrez la valeur pour ab : "))
  valeur_bc = float(input("Entrez la valeur pour bc : "))
  valeur_hypotenuse = float(input("Entrez la valeur pour l'hypotenuse : "))

# on separe les resultat pour l'hypo. et de ab et bc
  resultat_hypotenuse_reciproque = valeur_hypotenuse**2

  resultat_valeurs_reciproque = valeur_ab**2 + valeur_bc**2


# Verfication si hypo. = ab et bc
  if resultat_hypotenuse_reciproque == resultat_valeurs_reciproque:
    print(f"\n\nHypotenuse = {valeur_hypotenuse}² = {resultat_hypotenuse_reciproque}\n\nAB² + BC² = {valeur_ab}² + {valeur_bc}² = {resultat_valeurs_reciproque}\n\nDonc Hypotenuse² = AB² + BC²")
# Si hypo. != de ab et bc alors
  else:
    print(f"\n\nHypotenuse = {valeur_hypotenuse}² = {resultat_hypotenuse_reciproque}\n\nAB² + BC² = {valeur_ab}² + {valeur_bc}² = {resultat_valeurs_reciproque}\n\nDonc Hypotenuse² est different de AB² + BC²")



def volumes():
  #supprime les messages de la console
  clear()

  #menu pour choisir un solide pour calculer le volume
  choix_des_volumes = input("Quel solide voulez vous connaître le volume ?\n\n[1] Cube\n[2] Pavé droit\n[3] Cylindre droit\n[4] Prisme droit\n[5] Cône droit\n[6] Pyramide\n[7] Sphère\n\n")


# si user choisi un chiffre corespondant à un solide, alors on execute le programme prévu à cet effet
  if choix_des_volumes == "1":
    cote_cube = float(input("\n\nCôte du cube : "))

    resultat_volume_cube = float(cote_cube**3)

    print(f"V = c * c *c = {cote_cube} * {cote_cube} * {cote_cube} = {resultat_volume_cube}")

  elif choix_des_volumes == "2":
    longueur_pavé = float(input("\n\nLongueur du pavé : "))
    largeur_pavé = float(input("\nLargeur du pavé : "))
    hauteur_pavé = float(input("\nHauteur du pavé : "))

    resultat_volume_pave = float(longueur_pavé * largeur_pavé * hauteur_pavé)

    print(f"V = L * l * h = {longueur_pavé} * {largeur_pavé} * {hauteur_pavé} = {resultat_volume_pave}")

  elif choix_des_volumes == "3":
    base_cylindre = float(input("\n\nBase du cylindre : "))
    hauteur_cylindre = float(input("\nHauteur du cylindre : "))

    resultat_cylindre = float(base_cylindre * hauteur_cylindre)

    print(f"V = B * h = {base_cylindre} * {hauteur_cylindre} = {resultat_cylindre}")

  elif choix_des_volumes == "4":
    base_prisme = float(input("\n\nBase du prisme : "))
    hauteur_prisme = float(input("\nHauteur du prisme : "))

    resultat_prisme = float(base_prisme * hauteur_prisme)

    print(f"V = B * h = {base_prisme} * {hauteur_prisme} = {resultat_prisme}")

  elif choix_des_volumes == "5":
    base_cone = float(input("\n\nBase du cône : "))
    hauteur_cone = float(input("\nHauteur du cône : "))

    resultat_cone = float(1/3 * base_cone * hauteur_cone)

    print(f"V = 1/3* B * h = 1/3 * {base_cone} * {hauteur_cone} = {resultat_cone}")

  elif choix_des_volumes == "6":
    base_pyramide = float(input("\n\nBase de la pyramide : "))
    hauteur_pyramide = float(input("\nHauteur de la pyramide : "))

    resultat_pyramide = float(1/3 * base_pyramide * hauteur_pyramide)

    print(f"V = 1/3* B * h = 1/3 * {base_pyramide} * {hauteur_pyramide} = {resultat_pyramide}")

  elif choix_des_volumes == "7":
    rayon_sphere = float(input("Rayon de la sphère : "))

    resultat_sphere = float(4/3 * pi * rayon_sphere**3)

    print(f"V = 4/3 * pi * r**3 = 4/3 * pi * {rayon_sphere} = {resultat_sphere}")

#retour au menu
  main()


def air():
  #supprime les msg de la console
  clear()


#menu des fonctionalités
  choix_des_solides = input("Quel solide voulez vous connaître l'air ?\n\n[1] Carré\n[2] Rectangle\n[3] Triangle rectangle\n[4] Triangle\n[5] Disque\n[6] Demi-disque\n\n")



  # si user choisi un chiffre corespondant à un solide, alors on execute le programme prévu à cet effet

  if choix_des_solides == "1":

    cote_cube = float(input("Longueur du carré : "))

    resultat_cube = float(cote_cube**2)

    print(f"A = c * c = {cote_cube} * {cote_cube} = {resultat_cube}")

  elif choix_des_solides == "2":

    longueur_rectangle = float(input("Longueur du rectangle : "))
    largeur_rectangle = float(input("Largeur du rectangle : "))

    resultat_rectangle = float(longueur_rectangle * largeur_rectangle)

    print(f"A = L * l = {longueur_rectangle} * {largeur_rectangle} = {resultat_rectangle}")

  elif choix_des_solides == "3":

    longueur_hypotenuse = float(input("Longeur de l'hypotenuse : "))
    longueur_cote_oppose = float(input("Longueur du côté opposé à l'angle : "))

    resulat_triangle_rectangle = float((longueur_hypotenuse * longueur_cote_oppose)/2)

    print(f"A = Hyptenuse * côté opposé : 2 = A = {longueur_hypotenuse} * {longueur_cote_oppose} : 2 = {resulat_triangle_rectangle}")

  elif choix_des_solides == "4":

    base_triangle = float(input("Base du triangle : "))
    hauteur_triangle = float(input("Hauteur du triangle : "))

    resultat_triangle = float((base_triangle * hauteur_triangle)/2)

    print(f"A = base * hauteur : 2 = {base_triangle} * {hauteur_triangle} : 2 = {resultat_triangle}")

  elif choix_des_solides == "5":

    rayon_disque = float(input("Rayon du disque : "))

    resultat_disque = float(pi * rayon_disque * rayon_disque)

    print(f"A = pi * r * r = pi * {rayon_disque} * {rayon_disque} = {resultat_disque}")

  elif choix_des_solides == "6":

    rayon_disque = float(input("Rayon du demi-disque : "))

    resultat_disque = float((pi * rayon_disque * rayon_disque)/é)

    print(f"A = (pi * r * r) : 2 = (pi * {rayon_disque} * {rayon_disque}) : 2 = {resultat_disque}")

#retour au menu
  main()

# fin fonctionnalités

if __name__ == "__main__":
  main()