# poqb.py
# -*- coding: utf-8 -*-
from Rubik import *
from ResolutionPetrus import *
from ResolutionClassique import *
from ResolutionFridrich import *

cube = 'BYOROBWWOYWRBGWBWBYGROWRGBOWYBRGBGYYOYGRORGOWGRYBRGOYW'

#Ce fichier renvoie la meilleur chaîne de mouvements solution parmis 3 méthodes de résolution
def solve(cube_c54):

	longueur = []
	court = 0
	mini = 1000
	cube=Rubik(cube_c54)
	for i in (0,1,2):
		cubeTest = Rubik(cube_c54)

		if i == 0:
			ChoixPetrus(cubeTest)
			longueur.append(len(cubeTest.solve))
			

		elif i == 1:
			ChoixClassique(cubeTest)
			longueur.append(len(cubeTest.solve))

		elif i == 2:
	 		ChoixFridrich(cubeTest)
		 	longueur.append(len(cubeTest.solve))

	for j in range (0,len(longueur)):#on choisi l'orientation qui est la plus optimise
		if mini> longueur[j]:
			mini = longueur[j]
			court = j

	if court == 0:
		return ChoixPetrus(cube)
		#return cube.solution

	elif court == 1:
		 return ChoixClassique(cube)
		#return cube.solution

	elif court == 2:
		return ChoixFridrich(cube)

print(solve(cube))

# ######### dans le programme initial
# if __name__=="__main__":
# 	cube = 'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'
# 	print ("Pour la resolution de {}\nExecuter la manoeuvre {}".format(cube, solve(cube)))









    
