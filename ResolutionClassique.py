from Rubik import *
from time import time
#On peux se servir des cubes suivants pour les tests, ce sont des mélanges officiels

Superflip = 'WOWGWBWRWGWGRWRBWBOWOOGRGRBRBOBOGGYGRYRBYBOYOYRYGYBYOY'
c1 = 'BOWOYGGWYRWWOBRGWBOGWYGYBOWRBRGRRBRRGOBYGGYYYWBRBWYOOO'
c2 = 'WGOWYGOWYGBYGOBRWBYOOBGBOOGYBYRRRWRRYRBWOBRYGGGOWWYRBW'
c3 = 'GWBRYYYGROWGOYWGOOWOWBGYBOGOBRBROBGWBBGRYBOGRRWYWWRYRY'
c4 = 'BYBRWWGOGYGOYBWOBYOGRRBOWOYOGRWRYRGWOGRWBRYBWBWBOYYGRG'
c5 = 'GYOWWGRRGWRYBYYRYYGORWORBGGWRGRBBWOWGOOYYBROBOWBGYBOBW'
c6 = 'OGBBWOWWRGRBORYBYYOWYWOYRGOBRYBBBRGWGGRGGRYOBORWYYOWWG'
c7 = 'ROYBYRRWWYYWGRRBBGOWGBGGOORGBYGRWRYOBGWGBYBRYWWOOWOBYO'
c8 = 'YYRYYOWWOGGBOGBYYYBBRRGWROGRBOGRBRWWBBYOOGOYWRWGOWBGRW'
c9 = 'GGWGYOOYWRYYGOBOBRBRYGGYROGWBWOROBBOWRWRROYBRGBGYWWYWB'
c10 = 'BBGBYYORGOWWBYOYGWORYWGWROGWBGRROWOGWBGROYRORRYYYWBBGB'
c11 = 'ROOYYBRGGBGBWOYRRWBYYOBRGRWGGWROBYBWGOOGRGWBOOWYWWYBYR'


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def CoinPlace(cube):#cette fonction sert a combien de coin de la première face sont bien placée

	nb = 0
	liste = [1,3,6,8]
	liste1 = [9,18,12,15]
	liste2 =[20,17,11,14]
	couleur1 = [cube.Dcube['L'],cube.Dcube['B'],cube.Dcube['F'],cube.Dcube['R']]
	couleur2 = [cube.Dcube['B'],cube.Dcube['R'],cube.Dcube['L'],cube.Dcube['F']]
	for i in range(4):
		if (cube.Dcube[liste[i]] == cube.Dcube['U']) and (cube.Dcube[liste2[i]] == couleur2[i]) and (cube.Dcube[liste1[i]] == couleur1[i]):
			nb = nb+1

	

	return nb


def coinMalP(cube):
	if cube.Dcube[1] != cube.Dcube['U'] or (cube.Dcube[1] == cube.Dcube['U'] and cube.Dcube[9] != cube.Dcube['L'] and cube.Dcube[20] != cube.Dcube['B']):
		return 1
	elif cube.Dcube[3] != cube.Dcube['U'] or (cube.Dcube[3] == cube.Dcube['U'] and cube.Dcube[17] != cube.Dcube['R'] and cube.Dcube[18] != cube.Dcube['B']):
		return 2
	elif cube.Dcube[6] != cube.Dcube['U'] or (cube.Dcube[6] == cube.Dcube['U'] and cube.Dcube[11] != cube.Dcube['L'] and cube.Dcube[12] != cube.Dcube['F']):
		return 3
	elif cube.Dcube[8] != cube.Dcube['U'] or (cube.Dcube[8] == cube.Dcube['U'] and cube.Dcube[14] != cube.Dcube['F'] and cube.Dcube[15] != cube.Dcube['R']):
		return 4


def comparaison(cube,case,couleur):
	if  cube.Dcube[case] == cube.Dcube[couleur] :
		return True 



def CheckCroix(cube):
	#Cette fonction compte et retourne le nombre d'arrete bien placée sur la face du haut (Piece Placee)
	#Ainsi que le nombre d'arrete dont l'etiquette du haut correspond au centre de la face supérieur mais dont l'autre étiquette de la pièce ne correspond pas (Piece Presque Placee).
	AutreFaceDeLaPiece = 10
	IndiceListeDisposition = 0
	PiecePlacee = 0
	PiecePresquePlacee = 0
	ListeDisposition = [cube.Dcube['L'],cube.Dcube['F'],cube.Dcube['R'],cube.Dcube['B']]
	for i in [4,7,5,2]: #On parcours toute les arretes de la face supérieur et on compte les pièces de manières décrites plus haut
		if cube.Dcube[i] == cube.Dcube['U']:
			if cube.Dcube[AutreFaceDeLaPiece] == ListeDisposition[IndiceListeDisposition]:
				PiecePlacee +=1
			else:
				PiecePresquePlacee +=1
		IndiceListeDisposition +=1
		AutreFaceDeLaPiece +=3
	return PiecePlacee, PiecePresquePlacee #On retourne les deux valeurs qui nous interesse

def PlacerCroixFaceU(cube):
	#La fonction prend en paramètre un objet Rubik et résoud la face U

	#On fait une croix sur la face supérieur du cube
	#Les problemes d'optimisations sont dans l'ordre des étapes notamment
	#On va gagner en optimisation en changeant de methode (Petrus)
	#Tout est optimisable ça fonctionne
	k=0
	while cube.Dcube[2] != cube.Dcube['U'] or cube.Dcube[4] != cube.Dcube['U'] or cube.Dcube[5] != cube.Dcube['U'] or cube.Dcube[7] != cube.Dcube['U']:
		k+=1
		if k ==20:
			break
		#ETAPE 1:
		#On verifie l'orientation des pièces du dessus et on en met un maximum dans la bonne position
		PiecePlacee, PiecePresquePlacee = CheckCroix(cube)
		ListeDisposition = [cube.Dcube['L'],cube.Dcube['F'],cube.Dcube['R'],cube.Dcube['B']]
		while PiecePlacee == 0 and PiecePresquePlacee>0:
			cube.U() #Pas de panique, on utilise ensuite une fonction pour condenser les U
			PiecePlacee, PiecePresquePlacee = CheckCroix(cube)

		#Si une pièce est mal placé, on la tourne d'un quart de tour pour la resoudre a l'étape suivante
		i=0		
		Listeparcours = [4,7,5,2]
		AutreFace = 10
		p = 0
		while PiecePresquePlacee > 0:
			if p == 40:
				break
			p = p+1
			if i == 4:
				i =0
			if cube.Dcube[Listeparcours[i]] == cube.Dcube['U'] and cube.Dcube[AutreFace] != ListeDisposition[i]:
				if i == 0:
					cube.L()
				if i == 1:
					cube.F()
				if i == 2:
					cube.R()
				if i == 3:
					cube.B()
			else:
				i +=1
				AutreFace +=3
			PiecePlacee, PiecePresquePlacee = CheckCroix(cube)


		#ETAPE 2 :
		#On place toutes les pièces qui nous interessent de la couronne centrale au bon endroit
		#On verifie la couleur et la position de chaque pièce pour résoudre le mieux possible
		ListeDisposition1 = [cube.Dcube['L'],cube.Dcube['F'],cube.Dcube['R'],cube.Dcube['B']]
		ListeDisposition2 = [cube.Dcube['B'],cube.Dcube['L'],cube.Dcube['F'],cube.Dcube['R']]
		ListeDisposition3 = [cube.Dcube['F'],cube.Dcube['R'],cube.Dcube['B'],cube.Dcube['L']]
		ListeDisposition4 = [cube.Dcube['R'],cube.Dcube['B'],cube.Dcube['L'],cube.Dcube['F']]
		Listeface1 =[28,22,24,26]
		Listeface2 =[21,23,25,27]
		i = 0
		p = 0
		stop = 0
		while(cube.Dcube[21] == cube.Dcube['U'] or cube.Dcube[23] == cube.Dcube['U'] or cube.Dcube[25] == cube.Dcube['U'] or cube.Dcube[27] == cube.Dcube['U'] or cube.Dcube[22] == cube.Dcube['U'] or cube.Dcube[24] == cube.Dcube['U'] or cube.Dcube[26] == cube.Dcube['U'] or cube.Dcube[28] == cube.Dcube['U']):
			p+=1
			if p == 60:
				break
			if i == 4:
				i=0
			stop +=1

			if cube.Dcube[Listeface1[i]] == cube.Dcube['U']:
				if cube.Dcube[Listeface2[i]] == ListeDisposition1[i]:
					if i == 0 :
						cube.L()
					if i == 1 :
						cube.F()
					if i == 2 :
						cube.R()
					if i == 3:
						cube.B()
				else:
					if cube.Dcube[Listeface2[i]] == ListeDisposition2[i]:
						if i == 0:
							cube.IU()
							cube.L()
							cube.U()
						if i == 1:
							cube.IU()
							cube.F()
							cube.U()
						if i ==2:
							cube.IU()
							cube.R()
							cube.U()
						if i ==3:
							cube.IU()
							cube.B()
							cube.U()
					else:
						if cube.Dcube[Listeface2[i]] == ListeDisposition3[i]:
							if i == 0:
								cube.U()
								cube.L()
								cube.IU()
							if i == 1:
								cube.U()
								cube.F()
								cube.IU()
							if i == 2:
								cube.U()
								cube.R()
								cube.IU()
							if i == 3:
								cube.U()
								cube.B()
								cube.IU()
						else :
							if cube.Dcube[Listeface2[i]] == ListeDisposition4[i]:
								if i == 0:
									cube.UU()
									cube.L()
									cube.UU()
								if i == 1:
									cube.UU()
									cube.F()
									cube.UU()
								if i == 2:
									cube.UU()
									cube.R()
									cube.UU()
								if i == 3:
									cube.UU()
									cube.B()
									cube.UU()



			else:

				if cube.Dcube[Listeface2[i]] == cube.Dcube['U']:
					if cube.Dcube[Listeface1[i]] == ListeDisposition2[i]:
						if i == 0:
							cube.IB()
						if i == 1:
							cube.IL()
						if i ==2:
							cube.IF()
						if i ==3:
							cube.IR()
					else:
						if cube.Dcube[Listeface1[i]] == ListeDisposition1[i]:
							if i == 0 :
								cube.U()
								cube.IB()
								cube.IU()
							if i == 1 :
								cube.U()
								cube.IL()
								cube.IU()
							if i == 2 :
								cube.U()
								cube.IF()
								cube.IU()
							if i == 3:
								cube.U()
								cube.IR()
								cube.IU()
						else:
							if cube.Dcube[Listeface1[i]] == ListeDisposition4[i]:
								if i == 0:
									cube.IU()
									cube.IB()
									cube.U()
								if i == 1:
									cube.IU()
									cube.IL()
									cube.U()
								if i == 2:
									cube.IU()
									cube.IF()
									cube.U()
								if i == 3:
									cube.IU()
									cube.IR()
									cube.U()
							else:
								if cube.Dcube[Listeface1[i]] == ListeDisposition3[i]:
									if i ==0:
										cube.UU()
										cube.IB()
										cube.UU()
									if i == 1:
										cube.UU()
										cube.IL()
										cube.UU()
									if i == 2:
										cube.UU()
										cube.IF()
										cube.UU()
									if i == 3:
										cube.UU()
										cube.IR()
										cube.UU()


				else:
					i+=1
					stop = 0


		#ETAPE 3:
		#On place les pièces qui sont sur la face opposé
		#Il suffit d'un simple demi-tour
		IndiceFace2 = 30
		listeparcours = [44,42,45,47]
		i = 0
		k=0
		while (cube.Dcube[44] == cube.Dcube['U'] or cube.Dcube[42] == cube.Dcube['U'] or cube.Dcube[45] == cube.Dcube['U'] or cube.Dcube[47] == cube.Dcube['U']):
			k+=1
			if k ==20:
				break
			if i ==4:
				i = 0
				IndiceFace2 = 30

			if cube.Dcube[listeparcours[i]] == cube.Dcube['U']:
				if cube.Dcube[IndiceFace2] == ListeDisposition[i]:
					if i == 0:
						cube.LL()
					if i == 1:
						cube.FF()
					if i == 2:
						cube.RR()
					if i == 3:
						cube.BB()
					i +=1
					IndiceFace2 +=3
				else:
					#Si le demi-tour défait une pièce en meme temps qu'elle en place une, on applique un quart de tour en bas afin d'éviter de boucler
					cube.D()
			else:
				i +=1
				IndiceFace2 +=3

		
		#ETAPE 4:
		#On met les pièces qui sont sur la couronne du haut mais mal placé sur la couronne du bas pour les placer à l'étape suivante
		Indiceparcours = 10
		Listeface2 = [4,7,5,2]
		i = 0
		sortie = 0
		k=0
		while (cube.Dcube[10] == cube.Dcube['U'] or cube.Dcube[13] == cube.Dcube['U'] or cube.Dcube[16] == cube.Dcube['U'] or cube.Dcube[19] == cube.Dcube['U']):
			k+=1
			if k ==20:
				break
			sortie +=1
			if i == 4:
				i=0
				Indiceparcours = 10
			if cube.Dcube[Indiceparcours] == cube.Dcube['U']:
				if i == 0 :
					cube.LL()
				if i == 1 :
					cube.FF()
				if i == 2:
					cube.RR()
				if i == 3:
					cube.BB()
				if sortie == 2:
					cube.D()
					sortie = 0
			else:
				i+=1
				sortie = 0
				Indiceparcours +=3

		#ETAPE 5
		#On place la couronne du bas
		Listeface2 = [44,42,45,47]
		i = 0
		Indiceparcours = 30
		k=0
		while (cube.Dcube[30] == cube.Dcube['U'] or cube.Dcube[33] == cube.Dcube['U'] or cube.Dcube[36] == cube.Dcube['U'] or cube.Dcube[39] == cube.Dcube['U']):
			if i == 4:
				i=0
				Indiceparcours =30
			if k ==20:
				break

			if cube.Dcube[Indiceparcours] == cube.Dcube['U']:
				if cube.Dcube[Listeface2[i]] == ListeDisposition[i]:
					if i == 0:
						cube.D()
						cube.F()
						cube.IL()
						cube.IF()
					if i == 1:
						cube.D()
						cube.R()
						cube.IF()
						cube.IR()
					if i == 2:
						cube.D()
						cube.B()
						cube.IR()
						cube.IB()
					if i == 3:
						cube.D()
						cube.L()
						cube.IB()
						cube.IL()
				else :
					#On applique un quart de tour en bas pour placer les arretes en vis à vis de leurs couleur avant d'appliquer la méthode de résolution
					cube.D()
			else:
				i+=1
				Indiceparcours+=3

		PiecePlacee, PiecePresquePlacee = CheckCroix(cube)
		if PiecePlacee == 4:
			return True









def PlacerCoinFaceU(cube): 

		k=0# condition d'arret de la boucle
		while CoinPlace(cube)<4 :
			k+=1
			if k==10:# arret de la boucle 
				break

			# on s'interresse a chaque coin de la dernière ligne du cube 
			# il a 4 coin chaque coin peu etre dans 3 configuration differente
			# donc pour chaque essaie 12 cas qui nous interesse 
			#chaque cas peut être dans 4 coins différents donc 48 cas possible au final !


			if  comparaison(cube,32,'U') and comparaison(cube,31,'F') and comparaison(cube,41,'R'):
				cube.D()
				cube.IR()
				cube.ID()
				cube.R() 
				
			elif comparaison(cube,32,'R') and comparaison(cube,31,'U') and comparaison(cube,41,'F'):
				cube.IR()
				cube.D()
				cube.R()
				
			elif comparaison(cube,32,'F') and comparaison(cube,31,'R') and comparaison(cube,41,'U'):
				cube.D()
				cube.IR()
				cube.DD()
				cube.R()
				cube.D()
				cube.IR()
				cube.ID()
				cube.R()
				
			elif comparaison(cube,32,'F') and comparaison(cube,31,'U') and comparaison(cube,41,'L'):
				cube.L()
				cube.D()
				cube.IL()


			elif comparaison(cube,32,'L') and comparaison(cube,31,'F') and comparaison(cube,41,'U'):
				cube.IF()
				cube.DD()
				cube.F()
				cube.D()
				cube.IF()
				cube.ID()
				cube.F()

			elif comparaison(cube,32,'U') and comparaison(cube,31,'L') and comparaison(cube,41,'F'):
				cube.IF()
				cube.ID()
				cube.F()

			elif comparaison(cube,32,'U') and comparaison(cube,31,'B') and comparaison(cube,41,'L'):
				cube.ID()
				cube.IL()
				cube.ID()
				cube.L()

			elif comparaison(cube,32,'L') and comparaison(cube,31,'U') and comparaison(cube,41,'B'):
				cube.DD()
				cube.IL()
				cube.D()
				cube.L()

			elif comparaison(cube,32,'B') and comparaison(cube,31,'L') and comparaison(cube,41,'U'):
				cube.ID()
				cube.IL()
				cube.DD()
				cube.L()
				cube.D()
				cube.IL()
				cube.ID()
				cube.L()

			elif comparaison(cube,32,'U') and comparaison(cube,31,'R') and comparaison(cube,41,'B'):
				cube.DD()
				cube.IB()
				cube.ID()
				cube.B()

			elif comparaison(cube,32,'B') and comparaison(cube,31,'U') and comparaison(cube,41,'R'):
				cube.D()
				cube.IB()
				cube.D()
				cube.B()

			elif comparaison(cube,32,'R') and comparaison(cube,31,'B') and comparaison(cube,41,'U'):
				cube.DD()
				cube.IB()
				cube.DD()
				cube.B()
				cube.D()
				cube.IB()
				cube.ID()
				cube.B()

			else :
				if  comparaison(cube,35,'U') and comparaison(cube,34,'F') and comparaison(cube,43,'R'): 
					cube.IR()
					cube.ID()
					cube.R()

				elif comparaison(cube,35,'R') and comparaison(cube,34,'U') and comparaison(cube,43,'F'):
					cube.ID()
					cube.IR()
					cube.D()
					cube.R()

				elif comparaison(cube,35,'F') and comparaison(cube,34,'R') and comparaison(cube,43,'U'):
					cube.IR()
					cube.DD()
					cube.R()
					cube.D()
					cube.IR()
					cube.ID()
					cube.R()

				elif comparaison(cube,35,'F') and comparaison(cube,34,'U') and comparaison(cube,43,'L'):#tromper de combinaison a refaire R est F
					cube.ID()
					cube.L()
					cube.D()
					cube.IL()

				elif comparaison(cube,35,'L') and comparaison(cube,34,'F') and comparaison(cube,43,'U'):
					cube.ID()
					cube.IF()
					cube.DD()
					cube.F()
					cube.D()
					cube.IF()
					cube.ID()
					cube.F()

				elif comparaison(cube,35,'U') and comparaison(cube,34,'L') and comparaison(cube,43,'F'):
					cube.L()
					cube.D()
					cube.IL()


				elif comparaison(cube,35,'U') and comparaison(cube,34,'B') and comparaison(cube,43,'L'):
					cube.B()
					cube.DD()
					cube.IB()

				elif comparaison(cube,35,'L') and comparaison(cube,34,'U') and comparaison(cube,43,'B'):
					cube.IL()
					cube.DD()
					cube.L()

				elif comparaison(cube,35,'B') and comparaison(cube,34,'L') and comparaison(cube,43,'U'):
					cube.DD()
					cube.IL()
					cube.DD()
					cube.L()
					cube.D()
					cube.IL()
					cube.ID()
					cube.L()

				elif comparaison(cube,35,'U') and comparaison(cube,34,'R') and comparaison(cube,43,'B'):
					cube.D()
					cube.IB()
					cube.ID()
					cube.B()

				elif comparaison(cube,35,'B') and comparaison(cube,34,'U') and comparaison(cube,43,'R'):
					cube.IB()
					cube.D()
					cube.B()

				elif comparaison(cube,35,'R') and comparaison(cube,34,'B') and comparaison(cube,43,'U'):
					cube.D()
					cube.IB()
					cube.DD()
					cube.B()
					cube.D()
					cube.IB()
					cube.ID()
					cube.B()

				else : 
					if  comparaison(cube,38,'U') and comparaison(cube,37,'F') and comparaison(cube,48,'R'):
						cube.F()
						cube.ID()
						cube.IF()


					elif comparaison(cube,38,'R') and comparaison(cube,37,'U') and comparaison(cube,48,'F'):
						cube.DD()
						cube.IR()
						cube.D()
						cube.R()

					elif comparaison(cube,38,'F') and comparaison(cube,37,'R') and comparaison(cube,48,'U'):
						cube.ID()
						cube.IR()
						cube.DD()
						cube.R()
						cube.D()
						cube.IR()
						cube.ID()
						cube.R()

					elif comparaison(cube,38,'F') and comparaison(cube,37,'U') and comparaison(cube,48,'L'):
						cube.DD()
						cube.L()
						cube.D()
						cube.IL()

					elif comparaison(cube,38,'L') and comparaison(cube,37,'F') and comparaison(cube,48,'U'):
						cube.DD()
						cube.IF()
						cube.DD()
						cube.F()
						cube.D()
						cube.IF()
						cube.ID()
						cube.F()

					elif comparaison(cube,38,'U') and comparaison(cube,37,'L') and comparaison(cube,48,'F'):
						cube.L()
						cube.DD()
						cube.IL()

					elif comparaison(cube,38,'U') and comparaison(cube,37,'B') and comparaison(cube,48,'L'):
						cube.DD()
						cube.B()
						cube.ID()
						cube.IB()

					elif comparaison(cube,38,'L') and comparaison(cube,37,'U') and comparaison(cube,48,'B'):
						cube.IL()
						cube.D()
						cube.L()

					elif comparaison(cube,38,'B') and comparaison(cube,37,'L') and comparaison(cube,48,'U'):
						cube.D()
						cube.IL()
						cube.DD()
						cube.L()
						cube.D()
						cube.IL()
						cube.ID()
						cube.L()

					elif comparaison(cube,38,'U') and comparaison(cube,37,'R') and comparaison(cube,48,'B'):
						cube.IB()
						cube.ID()
						cube.B()

					elif comparaison(cube,38,'B') and comparaison(cube,37,'U') and comparaison(cube,48,'R'):
						cube.ID()
						cube.IB()
						cube.D()
						cube.B()

					elif comparaison(cube,38,'R') and comparaison(cube,37,'B') and comparaison(cube,48,'U'):
						cube.IB()
						cube.DD()
						cube.B()
						cube.D()
						cube.IB()
						cube.ID()
						cube.B()

					else:
						if 	comparaison(cube,29,'U') and comparaison(cube,40,'F') and comparaison(cube,46,'R'): 
							cube.F()
							cube.DD()
							cube.IF()

						elif comparaison(cube,29,'R') and comparaison(cube,40,'U') and comparaison(cube,46,'F'):
							cube.IR()
							cube.DD()
							cube.R()

						elif comparaison(cube,29,'F') and comparaison(cube,40,'R') and comparaison(cube,46,'U'):
							cube.DD()
							cube.IR()
							cube.DD()
							cube.R()
							cube.D()
							cube.IR()
							cube.ID()
							cube.R()

						elif comparaison(cube,29,'F') and comparaison(cube,40,'U') and comparaison(cube,46,'L'):#tromper de combinaison a refaire R est F
							cube.F()
							cube.D()
							cube.IF()

						elif comparaison(cube,29,'L') and comparaison(cube,40,'F') and comparaison(cube,46,'U'):
							cube.D()
							cube.IF()
							cube.DD()
							cube.F()
							cube.D()
							cube.IF()
							cube.ID()
							cube.F()

						elif comparaison(cube,29,'U') and comparaison(cube,40,'L') and comparaison(cube,46,'F'):
							cube.D()
							cube.IF()
							cube.ID()
							cube.F()

						elif comparaison(cube,29,'U') and comparaison(cube,40,'B') and comparaison(cube,46,'L'):
							cube.IL()
							cube.ID()
							cube.L()

						elif comparaison(cube,29,'L') and comparaison(cube,40,'U') and comparaison(cube,46,'B'):
							cube.ID()
							cube.IL()
							cube.D()# correction mettre D a la place de B 
							cube.L()

						elif comparaison(cube,29,'B') and comparaison(cube,40,'L') and comparaison(cube,46,'U'):
							cube.IL()
							cube.DD()
							cube.L()
							cube.D()
							cube.IL()
							cube.ID()
							cube.L()

						elif comparaison(cube,29,'U') and comparaison(cube,40,'R') and comparaison(cube,46,'B'):
							cube.R()
							cube.ID()
							cube.IR()

						elif comparaison(cube,29,'B') and comparaison(cube,40,'U') and comparaison(cube,46,'R'):
							cube.ID()
							cube.R()
							cube.D()
							cube.IR()

						elif comparaison(cube,29,'R') and comparaison(cube,40,'B') and comparaison(cube,46,'U'):
							cube.ID()
							cube.IB()
							cube.DD()
							cube.B()
							cube.D()
							cube.IB()
							cube.ID()
							cube.B()

						else :# dans le cas ou il n'y a aucune des possibilité ci dessus, c'est a dire que tout les coins sont sur la première couronne
							if coinMalP(cube) == 1:#on regarde quel coin est mal placé
								cube.IL()# et on le met sur la dernière couronne 
								cube.ID()
								cube.L()
							elif coinMalP(cube) == 2:
								cube.R()
								cube.D()
								cube.IR()
							elif coinMalP(cube) == 3:
								cube.L()
								cube.D()
								cube.IL()

							elif coinMalP(cube) == 4:
								cube.IR()
								cube.ID()
								cube.R()


def PlaceFL(cube):
	couleurs=[cube.Dcube['F'],cube.Dcube['L']]
	#si la pièce est bien placée on s'en fiche
	if cube.Dcube[22]==cube.Dcube['L'] and cube.Dcube[23]==cube.Dcube['F']:
		return
	else:
		#si la pièce est bien placée mal orientée
		if (cube.Dcube[22]==cube.Dcube['F'] and cube.Dcube[23]==cube.Dcube['L']) or (cube.Dcube[22]!=cube.Dcube['D'] and cube.Dcube[23]!=cube.Dcube['D']):
			GBelgeL(cube)
		elif cube.Dcube[33] in couleurs and cube.Dcube[42] in couleurs:
			if cube.Dcube[33]==cube.Dcube['F']:
				DBelgeF(cube)
			else:
				cube.ID()
				GBelgeL(cube)
		elif cube.Dcube[36] in couleurs and cube.Dcube[45] in couleurs:
			if cube.Dcube[36]==cube.Dcube['F']:
				cube.ID()
				DBelgeF(cube)
			else:
				cube.DD()
				GBelgeL(cube)
		elif cube.Dcube[39] in couleurs and cube.Dcube[47] in couleurs:
			if cube.Dcube[39]==cube.Dcube['F']:
				cube.DD()
				DBelgeF(cube)
			else:
				cube.D()
				GBelgeL(cube)
		elif cube.Dcube[30] in couleurs and cube.Dcube[44] in couleurs:
			if cube.Dcube[30]==cube.Dcube['F']:
				cube.D()
				DBelgeF(cube)
			else:
				GBelgeL(cube)
		return 

def PlaceLB(cube):
	couleurs=[cube.Dcube['B'],cube.Dcube['L']]
	#si la pièce est bien placée on s'en fiche
	if cube.Dcube[21]==cube.Dcube['L'] and cube.Dcube[28]==cube.Dcube['B']:
		return
	else:
		#si la pièce est bien placée mal orientée
		if (cube.Dcube[21]==cube.Dcube['B'] and cube.Dcube[28]==cube.Dcube['L']) or (cube.Dcube[21]!=cube.Dcube['D'] and cube.Dcube[28]!=cube.Dcube['D']):
			GBelgeB(cube)
		elif cube.Dcube[33]in couleurs and cube.Dcube[42] in couleurs:
			if cube.Dcube[33]==cube.Dcube['L']:
				cube.ID()
				DBelgeL(cube)
			else:
				cube.DD()
				GBelgeB(cube)
		elif cube.Dcube[36] in couleurs and cube.Dcube[45] in couleurs:
			if cube.Dcube[36]==cube.Dcube['L']:
				cube.DD()
				DBelgeL(cube)
			else:
				cube.D()
				GBelgeB(cube)
		elif cube.Dcube[39] in couleurs and cube.Dcube[47] in couleurs:
			if cube.Dcube[39]==cube.Dcube['L']:
				cube.D()
				DBelgeL(cube)
			else:
				GBelgeB(cube)
		elif cube.Dcube[30] in couleurs and cube.Dcube[44] in couleurs:
			if cube.Dcube[30]==cube.Dcube['L']:
				DBelgeL(cube)
			else:
				cube.ID()
				GBelgeB(cube)
		return 

def PlaceBR(cube):
	couleurs=[cube.Dcube['B'],cube.Dcube['R']]
	#si la pièce est bien placée on s'en fiche
	if cube.Dcube[26]==cube.Dcube['R'] and cube.Dcube[27]==cube.Dcube['B']:
		return
	else:
		#si la pièce est bien placée mal orientée
		if (cube.Dcube[26]==cube.Dcube['B'] and cube.Dcube[27]==cube.Dcube['R']) or (cube.Dcube[26]!=cube.Dcube['D'] and cube.Dcube[27]!=cube.Dcube['D']):
			GBelgeR(cube)
		elif cube.Dcube[33] in couleurs and cube.Dcube[42] in couleurs:
			if cube.Dcube[33]==cube.Dcube['B']:
				cube.DD()
				DBelgeB(cube)
			else:
				cube.D()
				GBelgeR(cube)
		elif cube.Dcube[36] in couleurs and cube.Dcube[45] in couleurs:
			if cube.Dcube[36]==cube.Dcube['B']:
				cube.D()
				DBelgeB(cube)
			else:
				GBelgeR(cube)
		elif cube.Dcube[39] in couleurs and cube.Dcube[47] in couleurs:
			if cube.Dcube[39]==cube.Dcube['B']:
				DBelgeB(cube)
			else:
				cube.ID()
				GBelgeR(cube)
		elif cube.Dcube[30] in couleurs and cube.Dcube[44] in couleurs:
			if cube.Dcube[30]==cube.Dcube['B']:
				cube.ID()
				DBelgeB(cube)
			else:
				cube.DD()
				GBelgeR(cube)
		return 

def PlaceRF(cube):
	couleurs=[cube.Dcube['R'],cube.Dcube['F']]
	#si la pièce est bien placée on s'en fiche
	if cube.Dcube[25]==cube.Dcube['R'] and cube.Dcube[24]==cube.Dcube['F']:
		return
	else:
		#si la pièce est bien placée mal orientée
		if (cube.Dcube[25]==cube.Dcube['F'] and cube.Dcube[24]==cube.Dcube['R']) or (cube.Dcube[25]!=cube.Dcube['D'] and cube.Dcube[24]!=cube.Dcube['D']):
			GBelgeF(cube)
		elif cube.Dcube[33] in couleurs and cube.Dcube[42] in couleurs:
			if cube.Dcube[33]==cube.Dcube['R']:
				cube.D()
				DBelgeL(cube)
			else:
				GBelgeF(cube)
		elif cube.Dcube[36] in couleurs and cube.Dcube[45] in couleurs:
			if cube.Dcube[36]==cube.Dcube['R']:
				DBelgeR(cube)
			else:
				cube.ID()
				GBelgeF(cube)
		elif cube.Dcube[39] in couleurs and cube.Dcube[47] in couleurs:
			if cube.Dcube[39]==cube.Dcube['R']:
				cube.ID()
				DBelgeR(cube)
			else:
				cube.DD()
				GBelgeF(cube)
		elif cube.Dcube[30] in couleurs and cube.Dcube[44] in couleurs:
			if cube.Dcube[30]==cube.Dcube['L']:
				cube.DD()
				DBelgeR(cube)
			else:
				cube.D()
				GBelgeF(cube)
		return 

def ResoudreCourronne(cube):

	w=0
	while not checkEtape2(cube):
		w+=1
		PlaceFL(cube)
		PlaceLB(cube)
		PlaceBR(cube)
		PlaceRF(cube)
		if w>=100:
			return print("Rate")
	while cube.Dcube[13]!=cube.Dcube['F']:
			cube.U()

def checkEtape2(cube):
	courronne=[21,'L',22,23,'F',24,25,'R',26,27,'B',28]
	a=0
	for i in (0,3,6,9):
		if cube.Dcube[courronne[i]]==cube.Dcube['D']:
			return False
		elif cube.Dcube[courronne[i]]==cube.Dcube[courronne[i+1]]==cube.Dcube[courronne[i+2]]:
			a+=1
	if a!=4:
		return False
	return True

def GBelgeF(cube):
	cube.ID()
	cube.IR()
	cube.D()
	cube.R()
	cube.D()
	cube.F()
	cube.ID()
	cube.IF()


def GBelgeL(cube):
	cube.ID()
	cube.IF()
	cube.D()
	cube.F()
	cube.D()
	cube.L()
	cube.ID()
	cube.IL()
def GBelgeR(cube):
	cube.ID()
	cube.IB()
	cube.D()
	cube.B()
	cube.D()
	cube.R()
	cube.ID()
	cube.IR()
def GBelgeB(cube):
	cube.ID()
	cube.IL()
	cube.D()
	cube.L()
	cube.D()
	cube.B()
	cube.ID()
	cube.IB()

def DBelgeF(cube):
	cube.D()
	cube.L()
	cube.ID()
	cube.IL()
	cube.ID()
	cube.IF()
	cube.D()
	cube.F()
def DBelgeL(cube):
	cube.D()
	cube.B()
	cube.ID()
	cube.IB()
	cube.ID()
	cube.IL()
	cube.D()
	cube.L()

def DBelgeR(cube):
	cube.D()
	cube.F()
	cube.ID()
	cube.IF()
	cube.ID()
	cube.IR()
	cube.D()
	cube.R()

def DBelgeB(cube):
	cube.D()
	cube.R()
	cube.ID()
	cube.IR()
	cube.ID()
	cube.IB()
	cube.D()
	cube.B()
	
#Cette méthode résoud la mise en place de la croix sur la face Down
def PlacerCroixFaceD(cube):
	croix_faite = False
	k = 0
	while not croix_faite :
		k+=1
		if k ==20:
			break
		#configuration cherchée : la croix est déjà placée
		if cube.Dcube['D'] == cube.Dcube[45] and cube.Dcube['D'] == cube.Dcube[44] and cube.Dcube['D'] == cube.Dcube[47] and cube.Dcube['D'] == cube.Dcube[42] :
			croix_faite = True
		#Première configuration possible : L bien placé
		elif cube.Dcube['D'] == cube.Dcube[44] and cube.Dcube['D'] == cube.Dcube[42]:
			mouvementCroix(cube)
			croix_faite = True
		#Deuxième configuration possible : L mal placé à une rotation anti-horaire
		elif cube.Dcube['D'] == cube.Dcube[42] and cube.Dcube['D'] == cube.Dcube[45]:
			cube.ID()
			mouvementCroix(cube)
			croix_faite = True
		#Troisième configuration possible : L mal placé à 2 rotations
		elif cube.Dcube['D'] == cube.Dcube[45] and cube.Dcube['D'] == cube.Dcube[47]:
			cube.DD()
			mouvementCroix(cube)
			croix_faite = True
		#Quatrième configuration possible : L mal placé à une rotation horaire
		elif cube.Dcube['D'] == cube.Dcube[47] and cube.Dcube['D'] == cube.Dcube[44]:
			cube.D()
			mouvementCroix(cube)
			croix_faite = True
		#Cinquième configuration : positionnement par rapport à une ligne horizontale
		elif cube.Dcube['D'] == cube.Dcube[45] and cube.Dcube['D'] == cube.Dcube[44]:
			mouvementCroix(cube)
		#Sixième configuration : positionnement par rapport à une ligne verticale
		elif cube.Dcube['D'] == cube.Dcube[45] and cube.Dcube['D'] == cube.Dcube[44]:
			cube.D()
			mouvementCroix(cube)
		#Pas de L ni de ligne sur la face du dessous, on cherche à en créer un
		else:
			mouvementCroix(cube)

#Cette méthode effectue le mouvement générique pour placer la croix sur la face du dessous
#Elle est utilisée dans la fonction PlacerCroixFaceD
def mouvementCroix(cube):
	cube.IR()
	cube.ID()
	cube.IB()
	cube.D()
	cube.B()
	cube.R()

#Cette méthode place correctement le cube pour effectuer les mouvements pour placer les coins de la face du dessous
def PlacerCoinFaceD(cube):
	#On effectue les mouvements tant qu'on n'obtient pas la face du dessous complete
	k=0
	while not cube.TestFaceD():
		k+=1
		if k == 20:
			break
		nbC = nombreCoins(cube)
		#si il existe un coin on prend en priorité la face du dessous
		if nbC == 1:
			#le coin sur la face du dessous est bien placé, on peut effectuer directement la liste de mouvement
			if cube.Dcube['D'] == cube.Dcube[43]:
				mouvementCoins(cube)
			#le coin sur la face du dessous est à gauche en haut, on effectue une rotation horaire du bas
			elif cube.Dcube['D'] == cube.Dcube[48]:
				cube.D()
				mouvementCoins(cube)
			#le coin sur la face du dessous est à gauche en bas, on effectue deux rotation horaire du bas
			elif cube.Dcube['D'] == cube.Dcube[46]:
				cube.DD()
				mouvementCoins(cube)
			#le coin sur la face est à droite en bas, on effectue une rotation anti-horaire du bas
			elif cube.Dcube['D'] == cube.Dcube[41]:
				cube.ID()
				mouvementCoins(cube)
		#si il existe 0, 2 ou 3 coins, on ne prend pas la face du dessous en priorité
		else:
			#le coin où il y a une partie de la couleur de la face du dessous est bien placé, on effectue la liste de mouvement
			if cube.Dcube['D'] == cube.Dcube[34] or cube.Dcube['D'] == cube.Dcube[35]:
				mouvementCoins(cube) 
			elif cube.Dcube['D'] == cube.Dcube[37] or cube.Dcube['D'] == cube.Dcube[38]:
				cube.ID()
				mouvementCoins(cube)
			elif cube.Dcube['D'] == cube.Dcube[40] or cube.Dcube['D'] == cube.Dcube[29]:
				cube.DD()
				mouvementCoins(cube)
			elif cube.Dcube['D'] == cube.Dcube[43] or cube.Dcube['D'] == cube.Dcube[32]:
				cube.D()
				mouvementCoins(cube)

#Cette méthode effectue la liste des mouvements pour placer les coins de la face du dessous
def mouvementCoins(cube):
	cube.L()
	cube.D()
	cube.IL()
	cube.D()
	cube.L()
	cube.D()
	cube.D()
	cube.IL()

#Cette méthode permet de savoir le nombre de coin qui est placé sur la face du dessous
def nombreCoins(cube):
	nbC = 0
	if cube.Dcube['D'] == cube.Dcube[41]:
		nbC += 1
	if cube.Dcube['D'] == cube.Dcube[43]:
		nbC += 1
	if cube.Dcube['D'] == cube.Dcube[46]:
		nbC += 1
	if cube.Dcube['D'] == cube.Dcube[48]:
		nbC += 1
	return nbC

# derniere etape de resolution 
def OrienterArreteFaceD(cube):
	k=0
	while not cube.TestCubeResolu():
		k+=1
		if k ==20:
			break
		if cube.Dcube[39] == cube.Dcube['B']: 
			if cube.Dcube[36] == cube.Dcube['L']: 
				cube.FF()
				cube.D()
				cube.R()
				cube.IL()
				cube.FF()
				cube.IR()
				cube.L()
				cube.D()
				cube.FF()
			else : 
				cube.FF()
				cube.ID()
				cube.R()
				cube.IL()
				cube.FF()
				cube.IR()
				cube.L()
				cube.ID()
				cube.FF()
		elif cube.Dcube[30] == cube.Dcube['L']:
			if cube.Dcube[39] == cube.Dcube['F']: 
				cube.RR()
				cube.D()
				cube.B()
				cube.IF()
				cube.RR()
				cube.IB()
				cube.F()
				cube.D()
				cube.RR()
			else :  
				cube.RR()
				cube.ID()
				cube.B()
				cube.IF()
				cube.RR()
				cube.IB()
				cube.F()
				cube.ID()
				cube.RR()
		elif cube.Dcube[36] == cube.Dcube['R']: 
			if cube.Dcube[33] == cube.Dcube['B']:
				cube.LL()
				cube.D()
				cube.F()
				cube.IB()
				cube.LL()
				cube.IF()
				cube.B()
				cube.D()
				cube.LL() 
			else : 
				cube.LL()
				cube.ID()
				cube.F()
				cube.IB()
				cube.LL()
				cube.IF()
				cube.B()
				cube.ID()
				cube.LL()
		else : 
			if cube.Dcube[30] == cube.Dcube['R']:
				cube.BB()
				cube.D()
				cube.L()
				cube.IR()
				cube.BB()
				cube.IL()
				cube.R()
				cube.D()
				cube.BB()
			else : 
				cube.BB()
				cube.ID()
				cube.L()
				cube.IR()
				cube.BB()
				cube.IL()
				cube.R()
				cube.ID()
				cube.BB()
	

def OrienterCoinFaceD(cube):# Résolution etape 5

    verifF = False      # Variable permettant la résolution de l'étape 5
    verifS = False
    cpt = 0
    cpt2 = 0

    
    if not ((cube.Dcube[38] == cube.Dcube[40]) and (cube.Dcube[38] == cube.Dcube['B']) and ((cube.Dcube[35] == cube.Dcube[37]) and (cube.Dcube[35] == cube.Dcube['R'])) \
          and ((cube.Dcube[32] == cube.Dcube[34]) and (cube.Dcube[32] == cube.Dcube['F'])) and \
          ((cube.Dcube[29] == cube.Dcube[31]) and (cube.Dcube[31] == cube.Dcube['L']))):  # Vérification que le cube n'est pas dans la forme finale de l'étape
        
        # Vérification si il y a 2 bons coin de placés sur une même face
        while( (not verifF) and (cpt < 4)):   # On tourne le down pour voir si il y en a un de bien placé
            if ( (cube.Dcube[29] == cube.Dcube[31] and cube.Dcube[29] == cube.Dcube['L']) or (cube.Dcube[32] == cube.Dcube[34] and cube.Dcube[32] == cube.Dcube['F']) \
                 or (cube.Dcube[35] == cube.Dcube[37] and cube.Dcube[35] == cube.Dcube['R']) or (cube.Dcube[38] == cube.Dcube[40] and cube.Dcube[38] == cube.Dcube['B'])):
                verifF = True
            else:
                cpt += 1        # Compteur du nombre de tour de recherche des coins biens placés
                cube.D()
               

        # Dans le cas ou il y a eu des rotations du down ou rectifie ce qu'il y aura dans la chaine finale
        # if cpt == 2 :
        #     taille = len(cube.solve)
        #     cube.solve[taille-2:]
        #     cube.solve.append("D2")
        # if cpt == 3:
        #     # taille = len(cube.solve)
        #     # cube.solve[taille-3:]
        #     # cube.solve.append("D'")
            
        if cpt == 4:                    # Il s'agit ici de deux coins qui sont en diagonales donc la séquence permettra de les remettre sur une même face
            # taille = len(cube.solve)
            # cube.solve = cube.solve[taille-4:]
            cube.IL()                                                                     
            cube.F()                    
            cube.IL()
            cube.BB()
            cube.L()
            cube.IF()                  
            cube.IL()                   
            cube.BB()
            cube.LL()
            cube.ID()

        if not((cube.Dcube[38] == cube.Dcube[40]) and (cube.Dcube[38] == cube.Dcube['B']) and ((cube.Dcube[35] == cube.Dcube[37]) and (cube.Dcube[35] == cube.Dcube['R'])) \
          and ((cube.Dcube[32] == cube.Dcube[34]) and (cube.Dcube[32] == cube.Dcube['F'])) and \
          ((cube.Dcube[29] == cube.Dcube[31]) and (cube.Dcube[31] == cube.Dcube['L']))):
                while not verifS and (cpt2<20):
                    if ( (cube.Dcube[29] == cube.Dcube[31] and cube.Dcube[29] == cube.Dcube['L']) or (cube.Dcube[32] == cube.Dcube[34] and cube.Dcube[32] == cube.Dcube['F']) \
                         or (cube.Dcube[35] == cube.Dcube[37] and cube.Dcube[35] == cube.Dcube['R']) or (cube.Dcube[38] == cube.Dcube[40] and cube.Dcube[38] == cube.Dcube['B'])):
                        verifS = True
                    else:
                        cpt2 += 1  # Placer les coins sur la bonne face
                        cube.D()

                # De la même manière rectification de la chaine 
                # if cpt2 == 2:
                #     taille = len(cube.solve)
                #     cube.solve[taille-2:]
                #     cube.solve.append("D2")
                # if cpt2 == 3:
                #     taille = len(cube.solve)
                #     cube.solve[taille-3:]
                #     cube.solve.append("D'")
                # if cpt2 == 4:
                #     taille = len(cube.solve)
                #     cube.solve = cube.solve[taille-4:]
                    

                # En fonction d'ou sont placés les coins on applique la méthode de résolution qui convient
                if cube.Dcube[29] == cube.Dcube[31] and cube.Dcube[29] == cube.Dcube['L']:
                    cube.IF()
                    cube.R()
                    cube.IF()
                    cube.LL()
                    cube.F()
                    cube.IR()
                    cube.IF()
                    cube.LL()
                    cube.FF()
                    cube.ID()

                elif cube.Dcube[32] == cube.Dcube[34] and cube.Dcube[32] == cube.Dcube['F']:
                    cube.IR()
                    cube.B()
                    cube.IR()
                    cube.FF()
                    cube.R()
                    cube.IB()
                    cube.IR()
                    cube.FF()
                    cube.RR()
                    cube.ID()

                elif cube.Dcube[35] == cube.Dcube[37] and cube.Dcube[35] == cube.Dcube['R']:
                    cube.IB()
                    cube.L()
                    cube.IB()
                    cube.RR()
                    cube.B()
                    cube.IL()
                    cube.IB()
                    cube.RR()
                    cube.BB()
                    cube.ID()
                   
                    
                elif cube.Dcube[38] == cube.Dcube[40] and cube.Dcube[38] == cube.Dcube['B']:
                    cube.IL()
                    cube.F()
                    cube.IL()
                    cube.BB()
                    cube.L()
                    cube.IF()
                    cube.IL()
                    cube.BB()
                    cube.LL()
                    cube.ID()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#cette fonction résoud le cube en affichant l'etat du cube etape par etape. Sert au debeugage
def ResoudreClassiqueE(cube):
	print("etat initial")
	cube.afficher2D()
	PlacerCroixFaceU(cube)
	print(cube.solve)
	print("etape 1")
	cube.afficher2D()
	PlacerCoinFaceU(cube)
	print(cube.solve)
	print("etape 2")
	cube.afficher2D()
	ResoudreCourronne(cube)
	print(cube.solve)
	print("etape 3")
	cube.afficher2D()
	PlacerCroixFaceD(cube)
	print(cube.solve)
	print("etape 4")
	cube.afficher2D()
	PlacerCoinFaceD(cube)
	print(cube.solve)
	print("etape 5")
	cube.afficher2D()
	OrienterCoinFaceD(cube)
	print(cube.solve)
	print("etape 6")
	cube.afficher2D()
	OrienterArreteFaceD(cube)
	print(cube.solve)
	print("etape 7")
	cube.afficher2D()

def ResoudreClassiqueTemps(cube):# resolution classique du cube avec affichage du temps et du nombre de mouvement
	t0 = time()
	if type(cube) == str:
		cube = Rubik(cube)
	PlacerCroixFaceU(cube)
	PlacerCoinFaceU(cube)
	ResoudreCourronne(cube)
	PlacerCroixFaceD(cube)
	PlacerCoinFaceD(cube)
	OrienterCoinFaceD(cube)
	OrienterArreteFaceD(cube)
	cube.Simplifier()
	cube.solChaine()
	if cube.TestCubeResolu():
		print("Cube resolu en "+str(len(cube.solve))+" mouvements et "+ str(round(time()-t0,5))+" secondes !")
	return cube.solution


def ResoudreClassique(cube):# resolution classique du cube
	if type(cube) == str:
		cube = Rubik(cube)
	PlacerCroixFaceU(cube)
	PlacerCoinFaceU(cube)
	ResoudreCourronne(cube)
	PlacerCroixFaceD(cube)
	PlacerCoinFaceD(cube)
	OrienterCoinFaceD(cube)
	OrienterArreteFaceD(cube)
	cube.Simplifier()
	cube.solChaine()
	return cube.solution





def StockageErreurs(n=1000):
	moyenne = 0
	maximum =0
	minimum =1000
	cube =Rubik()
	cube.Scramble()
	Fichier = open("CubeClassique.txt",'a')
	tmp = ''
	Erreur =0
	for i in range(0,n):
		cube.Scramble()
		tmp = str(cube.Dcube)
		ResoudreClassique(cube)
		if not cube.TestCubeResolu():
			Fichier.write(str(tmp))
			Fichier.write("\n")
			Erreur +=1
		else :
			moyenne += len(cube.solve)
			if len(cube.solve) > maximum: 
				maximum = len(cube.solve)
			if len(cube.solve) < minimum : 
				minimum = len(cube.solve)
	Fichier.close()
	print("Termine avec "+str(Erreur)+" erreurs sur "+str(n)+" cubes testes")
	print("moyenne : " + str(moyenne/n))
	print("max :" + str(maximum) + "/ min :" + str(minimum))


def ChoixClassique(cube):#cette fonction choisi l'orientation du cube qui est optimale pour la résolution
	i = 0 
	eInit = cube.chaine# on récupère la chaine pour créer un cube de test
	listeO = ['','r','f','rr','rf','fr','ff','rrr','rrf','rfr','rff','frr','ffr','fff','rrrf','rrfr','rrff','rfrr','rfff','frrr','fffr','frrrf','frfrr','frfff']
	longueur=[]
	mini = 1000
	
	while i < 24 :
		cubeTest = Rubik(eInit)#création du cube de test 

		for j in range (0,len(listeO[i])):# on parcours la liste des orientation possible
			if listeO[i][j]== 'r' :# on appplique l'orientation qui nous interesse 
				cubeTest.UtoR()
			elif listeO[i][j] == 'f':
				cubeTest. UtoF()
		
		ResoudreClassique(cubeTest)# on résoud le cube de test 
		longueur.append(len(cubeTest.solve))# on recupere le nombre de mouvement servant a resoudre le cube de test
		i = i+1

	
	for j in range (0,len(longueur)):#on choisi l'orientation qui est la plus optimisé
		if mini> longueur[j]:
			mini = longueur[j]
			court = j

	for k in range (0,len(listeO[court])):# on met le vrai cube dans la bone orientation 
		if listeO[court][k] == 'r':
			cube.UtoR()
		elif listeO[court][k] == 'f':
			cube.UtoF()
	ResoudreClassique(cube)
	return cube.solution


