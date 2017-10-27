from tkinter import * #Pour l'affichage graphique
from random import * #Pour le Scramble


class Rubik: 

	def __init__(self,cube=''):
		self.solve = [] #On initialise la liste des mouvements a faire pour résoudre le cube
		self.solution = ''
		self.orientation =''
		self.mvt = ['U','L','F','R','B','D']# la liste des mouvement possible. change selon l'orientation du cube 
		self.Dcube =  {}
		#La fonction prend en paramètre une chaîne de 54 caractère et retourne un dictionnaire qui modèlise le cube tel que vu en TP
		if self.estCube(cube):
			self.chaine=cube
			#On ajoute tout d'abord les pièces qui ne bougent pas (index U,L,F,R,B,D)
			self.Dcube["U"] = cube[4] 
			self.Dcube["L"] = cube[22]
			self.Dcube["F"] = cube[25]
			self.Dcube["R"] = cube[28]
			self.Dcube["B"] = cube[31]
			self.Dcube["D"] = cube[49]
			#On recompose la chaîne en supprimant les pièces que l'on vient d'ajouter
			cube = cube[0:4]+cube[5:22]+cube[23:25]+cube[26:28]+cube[29:31]+cube[32:49]+cube[50:]
			for i in range(0,48):
				self.Dcube[i+1] = cube[i] #On ajoute chaque autre pièce avec leurs index (Cf numerotation_cube.pdf @madoc.univ-nantes.fr)

		else :
			self.MAZ()

	def solChaine(self):
		for i in range (0,len(self.solve)):
			self.solution= self.solution+self.solve[i]


	def estCube(self,chaine): 
		#precaution supplémentaire pour s'assurer que notre input est bien valide
		if len(chaine) == 54: #Si la longueur est bonne
			for i in range(0,54): #Et que chaque caractère est valide
				if chaine[i] != 'O' and chaine[i] != 'R' and chaine[i] != 'W' and chaine[i] != 'Y' and chaine[i] != 'G' and chaine[i] != 'B' :
					print(chaine[i])
					return False
			return True #C'est bon
		else:
			return False #Sinon c'est pas bon

	def afficherRubik(self): 
		print("       ||"+self.Dcube[1]+"|"+self.Dcube[2]+"|"+self.Dcube[3]+"||")
		print("       ||"+self.Dcube[4]+"|"+self.Dcube['U']+"|"+self.Dcube[5]+"||")
		print("       ||"+self.Dcube[6]+"|"+self.Dcube[7]+"|"+self.Dcube[8]+"||")
		print("||"+self.Dcube[9]+"|"+self.Dcube[10]+"|"+self.Dcube[11]+"||"+self.Dcube[12]+"|"+self.Dcube[13]+"|"+self.Dcube[14]+"||"+self.Dcube[15]+"|"+self.Dcube[16]+"|"+self.Dcube[17]+"||"+self.Dcube[18]+"|"+self.Dcube[19]+"|"+self.Dcube[20]+"|")
		print("||"+self.Dcube[21]+"|"+self.Dcube['L']+"|"+self.Dcube[22]+"||"+self.Dcube[23]+"|"+self.Dcube['F']+"|"+self.Dcube[24]+"||"+self.Dcube[25]+"|"+self.Dcube['R']+"|"+self.Dcube[26]+"||"+self.Dcube[27]+"|"+self.Dcube['B']+"|"+self.Dcube[28]+"|")
		print("||"+self.Dcube[29]+"|"+self.Dcube[30]+"|"+self.Dcube[31]+"||"+self.Dcube[32]+"|"+self.Dcube[33]+"|"+self.Dcube[34]+"||"+self.Dcube[35]+"|"+self.Dcube[36]+"|"+self.Dcube[37]+"||"+self.Dcube[38]+"|"+self.Dcube[39]+"|"+self.Dcube[40]+"|")
		print("       ||"+self.Dcube[41]+"|"+self.Dcube[42]+"|"+self.Dcube[43]+"||")
		print("       ||"+self.Dcube[44]+"|"+self.Dcube['D']+"|"+self.Dcube[45]+"||")
		print("       ||"+self.Dcube[46]+"|"+self.Dcube[47]+"|"+self.Dcube[48]+"||")
		print("\n\n")



	#Les tests si dessous regardent si toutes les etiquettes d'une face sont de la meme couleur
	#---------------------------------------------------------------------------------------------------------------------------------------
	def TestFaceU(self):
		return self.Dcube[1]==self.Dcube[2]==self.Dcube[3]==self.Dcube[4]==self.Dcube["U"]==self.Dcube[5]==self.Dcube[6]==self.Dcube[7]==self.Dcube[8]

	def TestFaceL(self):
		return self.Dcube[9]==self.Dcube[10]==self.Dcube[11]==self.Dcube[21]==self.Dcube["L"]==self.Dcube[22]==self.Dcube[29]==self.Dcube[30]==self.Dcube[31]

	def TestFaceF(self):
		return self.Dcube[12]==self.Dcube[13]==self.Dcube[14]==self.Dcube[23]==self.Dcube["F"]==self.Dcube[24]==self.Dcube[32]==self.Dcube[33]==self.Dcube[34]

	def TestFaceR(self):
		return self.Dcube[15]==self.Dcube[16]==self.Dcube[17]==self.Dcube[25]==self.Dcube["R"]==self.Dcube[26]==self.Dcube[35]==self.Dcube[36]==self.Dcube[37]

	def TestFaceB(self):
		return self.Dcube[18]==self.Dcube[19]==self.Dcube[20]==self.Dcube[27]==self.Dcube["B"]==self.Dcube[28]==self.Dcube[38]==self.Dcube[39]==self.Dcube[40]

	def TestFaceD(self):
		return self.Dcube[41]==self.Dcube[42]==self.Dcube[43]==self.Dcube[44]==self.Dcube["D"]==self.Dcube[45]==self.Dcube[46]==self.Dcube[47]==self.Dcube[48]

	def TestCubeResolu(self):
		return self.TestFaceU() and self.TestFaceL() and self.TestFaceF() and self.TestFaceR()
	#-----------------------------------------------------------------------------------------------------------------------------------------



	# permutation gauche
	def L(self): 
		#permutation aretes
		self.Dcube[10],self.Dcube[22],self.Dcube[30],self.Dcube[21] = self.Dcube[21],self.Dcube[10],self.Dcube[22],self.Dcube[30]
		self.Dcube[4],self.Dcube[23],self.Dcube[44],self.Dcube[28] = self.Dcube[28],self.Dcube[4],self.Dcube[23],self.Dcube[44]
		# permrutation coin
		self.Dcube[11],self.Dcube[31],self.Dcube[29],self.Dcube[9] = self.Dcube[9],self.Dcube[11],self.Dcube[31],self.Dcube[29]
		self.Dcube[6],self.Dcube[32],self.Dcube[46],self.Dcube[20] = self.Dcube[20],self.Dcube[6],self.Dcube[32],self.Dcube[46]
		self.Dcube[1],self.Dcube[12],self.Dcube[41],self.Dcube[40] = self.Dcube[40],self.Dcube[1],self.Dcube[12],self.Dcube[41]
		self.ajoutermvt("L")
	def LL(self): 
		#permutation aretes
		self.Dcube[10],self.Dcube[22],self.Dcube[30],self.Dcube[21] = self.Dcube[30],self.Dcube[21],self.Dcube[10],self.Dcube[22]
		self.Dcube[4],self.Dcube[23],self.Dcube[44],self.Dcube[28] = self.Dcube[44],self.Dcube[28],self.Dcube[4],self.Dcube[23]
		# permrutation coin
		self.Dcube[11],self.Dcube[31],self.Dcube[29],self.Dcube[9] = self.Dcube[29],self.Dcube[9],self.Dcube[11],self.Dcube[31]
		self.Dcube[6],self.Dcube[32],self.Dcube[46],self.Dcube[20] = self.Dcube[46],self.Dcube[20],self.Dcube[6],self.Dcube[32]
		self.Dcube[1],self.Dcube[12],self.Dcube[41],self.Dcube[40] = self.Dcube[41],self.Dcube[40],self.Dcube[1],self.Dcube[12]
		self.ajoutermvt("L2")
	def IL(self): 
		#permutation aretes
		self.Dcube[10],self.Dcube[22],self.Dcube[30],self.Dcube[21] = self.Dcube[22],self.Dcube[30],self.Dcube[21],self.Dcube[10]
		self.Dcube[4],self.Dcube[23],self.Dcube[44],self.Dcube[28] = self.Dcube[23],self.Dcube[44],self.Dcube[28],self.Dcube[4]
		# permrutation coin
		self.Dcube[11],self.Dcube[31],self.Dcube[29],self.Dcube[9] = self.Dcube[31],self.Dcube[29],self.Dcube[9],self.Dcube[11]
		self.Dcube[6],self.Dcube[32],self.Dcube[46],self.Dcube[20] = self.Dcube[32],self.Dcube[46],self.Dcube[20],self.Dcube[6]
		self.Dcube[1],self.Dcube[12],self.Dcube[41],self.Dcube[40] = self.Dcube[12],self.Dcube[41],self.Dcube[40],self.Dcube[1]
		self.ajoutermvt("L'")

	# Permutation DOWN du cube
	def D(self):
                #permutation aretes
		self.Dcube[42],self.Dcube[45],self.Dcube[47],self.Dcube[44] = self.Dcube[44],self.Dcube[42],self.Dcube[45],self.Dcube[47]
		self.Dcube[33],self.Dcube[36],self.Dcube[39],self.Dcube[30] = self.Dcube[30],self.Dcube[33],self.Dcube[36],self.Dcube[39]
		# permrutation coin
		self.Dcube[43],self.Dcube[48],self.Dcube[46],self.Dcube[41] = self.Dcube[41],self.Dcube[43],self.Dcube[48],self.Dcube[46]
		self.Dcube[34],self.Dcube[37],self.Dcube[40],self.Dcube[31] = self.Dcube[31],self.Dcube[34],self.Dcube[37],self.Dcube[40]
		self.Dcube[32],self.Dcube[35],self.Dcube[38],self.Dcube[29] = self.Dcube[29],self.Dcube[32],self.Dcube[35],self.Dcube[38]
		self.ajoutermvt("D")
	def DD(self):
                #permutation aretes
		self.Dcube[42],self.Dcube[45],self.Dcube[47],self.Dcube[44] = self.Dcube[47],self.Dcube[44],self.Dcube[42],self.Dcube[45]
		self.Dcube[33],self.Dcube[36],self.Dcube[39],self.Dcube[30] = self.Dcube[39],self.Dcube[30],self.Dcube[33],self.Dcube[36]
		# permrutation coin
		self.Dcube[43],self.Dcube[48],self.Dcube[46],self.Dcube[41] = self.Dcube[46],self.Dcube[41],self.Dcube[43],self.Dcube[48]
		self.Dcube[34],self.Dcube[37],self.Dcube[40],self.Dcube[31] = self.Dcube[40],self.Dcube[31],self.Dcube[34],self.Dcube[37]
		self.Dcube[32],self.Dcube[35],self.Dcube[38],self.Dcube[29] = self.Dcube[38],self.Dcube[29],self.Dcube[32],self.Dcube[35]
		self.ajoutermvt("D2")

	def ID(self):
                #permutation aretes
		self.Dcube[42],self.Dcube[45],self.Dcube[47],self.Dcube[44] = self.Dcube[45],self.Dcube[47],self.Dcube[44],self.Dcube[42]
		self.Dcube[33],self.Dcube[36],self.Dcube[39],self.Dcube[30] = self.Dcube[36],self.Dcube[39],self.Dcube[30],self.Dcube[33]
		# permrutation coin
		self.Dcube[43],self.Dcube[48],self.Dcube[46],self.Dcube[41] = self.Dcube[48],self.Dcube[46],self.Dcube[41],self.Dcube[43]
		self.Dcube[34],self.Dcube[37],self.Dcube[40],self.Dcube[31] = self.Dcube[37],self.Dcube[40],self.Dcube[31],self.Dcube[34]
		self.Dcube[32],self.Dcube[35],self.Dcube[38],self.Dcube[29] = self.Dcube[35],self.Dcube[38],self.Dcube[29],self.Dcube[32]
		self.ajoutermvt("D'")

		
	#---Permutations de la face UP---
	#Quart de tour sens horaire
	def U(self):
		#Permutations arêtes
		self.Dcube[2],self.Dcube[5],self.Dcube[7],self.Dcube[4] = self.Dcube[4],self.Dcube[2],self.Dcube[5],self.Dcube[7]
		self.Dcube[1],self.Dcube[3],self.Dcube[8],self.Dcube[6] = self.Dcube[6],self.Dcube[1],self.Dcube[3],self.Dcube[8]
		#Permutations coins
		self.Dcube[9],self.Dcube[12],self.Dcube[15],self.Dcube[18] = self.Dcube[12],self.Dcube[15],self.Dcube[18],self.Dcube[9]
		self.Dcube[10],self.Dcube[13],self.Dcube[16],self.Dcube[19] = self.Dcube[13],self.Dcube[16],self.Dcube[19],self.Dcube[10]
		self.Dcube[11],self.Dcube[14],self.Dcube[17],self.Dcube[20] = self.Dcube[14],self.Dcube[17],self.Dcube[20],self.Dcube[11]
		self.ajoutermvt("U")

	#Demi-tour
	def UU(self):
		#Permutations arêtes
		self.Dcube[2],self.Dcube[5],self.Dcube[7],self.Dcube[4] = self.Dcube[7],self.Dcube[4],self.Dcube[2],self.Dcube[5]
		self.Dcube[1],self.Dcube[3],self.Dcube[8],self.Dcube[6] = self.Dcube[8],self.Dcube[6],self.Dcube[1],self.Dcube[3]
		#Permutations coins
		self.Dcube[9],self.Dcube[12],self.Dcube[15],self.Dcube[18] = self.Dcube[15],self.Dcube[18],self.Dcube[9],self.Dcube[12]
		self.Dcube[10],self.Dcube[13],self.Dcube[16],self.Dcube[19] = self.Dcube[16],self.Dcube[19],self.Dcube[10],self.Dcube[13]
		self.Dcube[11],self.Dcube[14],self.Dcube[17],self.Dcube[20] = self.Dcube[17],self.Dcube[20],self.Dcube[11],self.Dcube[14]
		self.ajoutermvt("U2")

	#Quart de tour sens anti-horaire
	def IU(self):
		#Permutations arêtes
		self.Dcube[2],self.Dcube[5],self.Dcube[7],self.Dcube[4] = self.Dcube[5],self.Dcube[7],self.Dcube[4],self.Dcube[2]
		self.Dcube[1],self.Dcube[3],self.Dcube[8],self.Dcube[6] = self.Dcube[3],self.Dcube[8],self.Dcube[6],self.Dcube[1]
		#Permutations coins
		self.Dcube[9],self.Dcube[12],self.Dcube[15],self.Dcube[18] = self.Dcube[18],self.Dcube[9],self.Dcube[12],self.Dcube[15]
		self.Dcube[10],self.Dcube[13],self.Dcube[16],self.Dcube[19] = self.Dcube[19],self.Dcube[10],self.Dcube[13],self.Dcube[16]
		self.Dcube[11],self.Dcube[14],self.Dcube[17],self.Dcube[20] = self.Dcube[20],self.Dcube[11],self.Dcube[14],self.Dcube[17]
		self.ajoutermvt("U'")

	#Permutation Right

	def R(self):


		self.Dcube[15],self.Dcube[35],self.Dcube[37],self.Dcube[17]=self.Dcube[35],self.Dcube[37],self.Dcube[17],self.Dcube[15]
		self.Dcube[16],self.Dcube[25],self.Dcube[36],self.Dcube[26]=self.Dcube[25],self.Dcube[36],self.Dcube[26],self.Dcube[16]
		self.Dcube[14],self.Dcube[43],self.Dcube[38],self.Dcube[3]=self.Dcube[43],self.Dcube[38],self.Dcube[3],self.Dcube[14]
		self.Dcube[24],self.Dcube[5],self.Dcube[27],self.Dcube[45]=self.Dcube[45],self.Dcube[24],self.Dcube[5],self.Dcube[27]
		self.Dcube[34],self.Dcube[8],self.Dcube[18],self.Dcube[48]=self.Dcube[48],self.Dcube[34],self.Dcube[8],self.Dcube[18]
		self.ajoutermvt("R")

	def IR(self):

		self.Dcube[35],self.Dcube[37],self.Dcube[17],self.Dcube[15]=self.Dcube[15],self.Dcube[35],self.Dcube[37],self.Dcube[17]
		self.Dcube[25],self.Dcube[36],self.Dcube[26],self.Dcube[16]=self.Dcube[16],self.Dcube[25],self.Dcube[36],self.Dcube[26]
		self.Dcube[43],self.Dcube[38],self.Dcube[3],self.Dcube[14]=self.Dcube[14],self.Dcube[43],self.Dcube[38],self.Dcube[3]
		self.Dcube[45],self.Dcube[24],self.Dcube[5],self.Dcube[27]=self.Dcube[24],self.Dcube[5],self.Dcube[27],self.Dcube[45]
		self.Dcube[48],self.Dcube[34],self.Dcube[8],self.Dcube[18]=self.Dcube[34],self.Dcube[8],self.Dcube[18],self.Dcube[48]
		self.ajoutermvt("R'")

	def RR(self):

		self.Dcube[15],self.Dcube[17],self.Dcube[37],self.Dcube[35]=self.Dcube[37],self.Dcube[35],self.Dcube[15],self.Dcube[17]
		self.Dcube[16],self.Dcube[36],self.Dcube[25],self.Dcube[26]=self.Dcube[36],self.Dcube[16],self.Dcube[26],self.Dcube[25]
		self.Dcube[43],self.Dcube[38],self.Dcube[3],self.Dcube[14]=self.Dcube[3],self.Dcube[14],self.Dcube[43],self.Dcube[38]
		self.Dcube[45],self.Dcube[24],self.Dcube[5],self.Dcube[27]=self.Dcube[5],self.Dcube[27],self.Dcube[45],self.Dcube[24]
		self.Dcube[48],self.Dcube[34],self.Dcube[8],self.Dcube[18]=self.Dcube[8],self.Dcube[18],self.Dcube[48],self.Dcube[34]
		self.ajoutermvt("R2")


	# Permutation Back
	def B(self): 
		
		self.Dcube[19],self.Dcube[28],self.Dcube[39],self.Dcube[27] = self.Dcube[27],self.Dcube[19],self.Dcube[28],self.Dcube[39]
		self.Dcube[2],self.Dcube[21],self.Dcube[47],self.Dcube[26] = self.Dcube[26],self.Dcube[2],self.Dcube[21],self.Dcube[47]
		self.Dcube[20],self.Dcube[40],self.Dcube[38],self.Dcube[18] = self.Dcube[18],self.Dcube[20],self.Dcube[40],self.Dcube[38]
		self.Dcube[1],self.Dcube[29],self.Dcube[48],self.Dcube[17] = self.Dcube[17],self.Dcube[1],self.Dcube[29],self.Dcube[48]
		self.Dcube[3],self.Dcube[9],self.Dcube[46],self.Dcube[37] = self.Dcube[37],self.Dcube[3],self.Dcube[9],self.Dcube[46]
		self.ajoutermvt("B")

	def BB(self): 
		
		self.Dcube[19],self.Dcube[28],self.Dcube[39],self.Dcube[27] = self.Dcube[39],self.Dcube[27],self.Dcube[19],self.Dcube[28]
		self.Dcube[2],self.Dcube[21],self.Dcube[47],self.Dcube[26] = self.Dcube[47],self.Dcube[26],self.Dcube[2],self.Dcube[21]
		self.Dcube[20],self.Dcube[40],self.Dcube[38],self.Dcube[18] = self.Dcube[38],self.Dcube[18],self.Dcube[20],self.Dcube[40]
		self.Dcube[1],self.Dcube[29],self.Dcube[48],self.Dcube[17] = self.Dcube[48],self.Dcube[17],self.Dcube[1],self.Dcube[29]
		self.Dcube[3],self.Dcube[9],self.Dcube[46],self.Dcube[37] = self.Dcube[46],self.Dcube[37],self.Dcube[3],self.Dcube[9]
		self.ajoutermvt("B2")

	def IB(self): 
		
		self.Dcube[19],self.Dcube[28],self.Dcube[39],self.Dcube[27] = self.Dcube[28],self.Dcube[39],self.Dcube[27],self.Dcube[19]
		self.Dcube[2],self.Dcube[21],self.Dcube[47],self.Dcube[26] = self.Dcube[21],self.Dcube[47],self.Dcube[26],self.Dcube[2]
		self.Dcube[20],self.Dcube[40],self.Dcube[38],self.Dcube[18] = self.Dcube[40],self.Dcube[38],self.Dcube[18],self.Dcube[20]
		self.Dcube[1],self.Dcube[29],self.Dcube[48],self.Dcube[17] = self.Dcube[29],self.Dcube[48],self.Dcube[17],self.Dcube[1]
		self.Dcube[3],self.Dcube[9],self.Dcube[46],self.Dcube[37] = self.Dcube[9],self.Dcube[46],self.Dcube[37],self.Dcube[3]
		self.ajoutermvt("B'")


	#permutation F,FF,IF
	def F(self):
		self.Dcube[6],self.Dcube[15],self.Dcube[43],self.Dcube[31]=self.Dcube[31],self.Dcube[6],self.Dcube[15],self.Dcube[43]
		self.Dcube[7],self.Dcube[25],self.Dcube[42],self.Dcube[22]=self.Dcube[22],self.Dcube[7],self.Dcube[25],self.Dcube[42]
		self.Dcube[8],self.Dcube[35],self.Dcube[41],self.Dcube[11]=self.Dcube[11],self.Dcube[8],self.Dcube[35],self.Dcube[41]
		self.Dcube[12],self.Dcube[14],self.Dcube[34],self.Dcube[32]=self.Dcube[32],self.Dcube[12],self.Dcube[14],self.Dcube[34]
		self.Dcube[13],self.Dcube[24],self.Dcube[33],self.Dcube[23]=self.Dcube[23],self.Dcube[13],self.Dcube[24],self.Dcube[33]
		self.ajoutermvt('F')
                
	def FF(self):
		self.Dcube[6],self.Dcube[15],self.Dcube[43],self.Dcube[31]=self.Dcube[43],self.Dcube[31],self.Dcube[6],self.Dcube[15]
		self.Dcube[7],self.Dcube[22],self.Dcube[42],self.Dcube[25]=self.Dcube[42],self.Dcube[25],self.Dcube[7],self.Dcube[22]
		self.Dcube[8],self.Dcube[35],self.Dcube[41],self.Dcube[11]=self.Dcube[41],self.Dcube[11],self.Dcube[8],self.Dcube[35]
		self.Dcube[12],self.Dcube[14],self.Dcube[34],self.Dcube[32]=self.Dcube[34],self.Dcube[32],self.Dcube[12],self.Dcube[14]
		self.Dcube[13],self.Dcube[24],self.Dcube[33],self.Dcube[23]=self.Dcube[33],self.Dcube[23],self.Dcube[13],self.Dcube[24]
		self.ajoutermvt('F2')

	def IF(self):
		self.Dcube[6],self.Dcube[15],self.Dcube[43],self.Dcube[31]=self.Dcube[15],self.Dcube[43],self.Dcube[31],self.Dcube[6]
		self.Dcube[7],self.Dcube[25],self.Dcube[42],self.Dcube[22]=self.Dcube[25],self.Dcube[42],self.Dcube[22],self.Dcube[7]
		self.Dcube[8],self.Dcube[35],self.Dcube[41],self.Dcube[11]=self.Dcube[35],self.Dcube[41],self.Dcube[11],self.Dcube[8]
		self.Dcube[12],self.Dcube[14],self.Dcube[34],self.Dcube[32]=self.Dcube[14],self.Dcube[34],self.Dcube[32],self.Dcube[12]
		self.Dcube[13],self.Dcube[24],self.Dcube[33],self.Dcube[23]=self.Dcube[24],self.Dcube[33],self.Dcube[23],self.Dcube[13]
		self.ajoutermvt('F\'')


	def UtoR(self):

		self.Dcube[6],self.Dcube[15],self.Dcube[43],self.Dcube[31]=self.Dcube[31],self.Dcube[6],self.Dcube[15],self.Dcube[43]
		self.Dcube[7],self.Dcube[25],self.Dcube[42],self.Dcube[22]=self.Dcube[22],self.Dcube[7],self.Dcube[25],self.Dcube[42]
		self.Dcube[8],self.Dcube[35],self.Dcube[41],self.Dcube[11]=self.Dcube[11],self.Dcube[8],self.Dcube[35],self.Dcube[41]
		self.Dcube[12],self.Dcube[14],self.Dcube[34],self.Dcube[32]=self.Dcube[32],self.Dcube[12],self.Dcube[14],self.Dcube[34]
		self.Dcube[13],self.Dcube[24],self.Dcube[33],self.Dcube[23]=self.Dcube[23],self.Dcube[13],self.Dcube[24],self.Dcube[33]
		

		self.Dcube[19],self.Dcube[28],self.Dcube[39],self.Dcube[27] = self.Dcube[28],self.Dcube[39],self.Dcube[27],self.Dcube[19]
		self.Dcube[2],self.Dcube[21],self.Dcube[47],self.Dcube[26] = self.Dcube[21],self.Dcube[47],self.Dcube[26],self.Dcube[2]
		self.Dcube[20],self.Dcube[40],self.Dcube[38],self.Dcube[18] = self.Dcube[40],self.Dcube[38],self.Dcube[18],self.Dcube[20]
		self.Dcube[1],self.Dcube[29],self.Dcube[48],self.Dcube[17] = self.Dcube[29],self.Dcube[48],self.Dcube[17],self.Dcube[1]
		self.Dcube[3],self.Dcube[9],self.Dcube[46],self.Dcube[37] = self.Dcube[9],self.Dcube[46],self.Dcube[37],self.Dcube[3]

		self.Dcube[4],self.Dcube[16],self.Dcube[45],self.Dcube[30]=self.Dcube[30],self.Dcube[4],self.Dcube[16],self.Dcube[45]
		self.Dcube[5],self.Dcube[36],self.Dcube[44],self.Dcube[10]=self.Dcube[10],self.Dcube[5],self.Dcube[36],self.Dcube[44]
		self.Dcube['U'],self.Dcube['R'],self.Dcube['D'],self.Dcube['L']=self.Dcube['L'],self.Dcube['U'],self.Dcube['R'],self.Dcube['D']

		self.orientation = self.orientation+'r'

		


	def UtoF(self):

		self.Dcube[10],self.Dcube[22],self.Dcube[30],self.Dcube[21] = self.Dcube[21],self.Dcube[10],self.Dcube[22],self.Dcube[30]
		self.Dcube[4],self.Dcube[23],self.Dcube[44],self.Dcube[28] = self.Dcube[28],self.Dcube[4],self.Dcube[23],self.Dcube[44]
		self.Dcube[11],self.Dcube[31],self.Dcube[29],self.Dcube[9] = self.Dcube[9],self.Dcube[11],self.Dcube[31],self.Dcube[29]
		self.Dcube[6],self.Dcube[32],self.Dcube[46],self.Dcube[20] = self.Dcube[20],self.Dcube[6],self.Dcube[32],self.Dcube[46]
		self.Dcube[1],self.Dcube[12],self.Dcube[41],self.Dcube[40] = self.Dcube[40],self.Dcube[1],self.Dcube[12],self.Dcube[41]
		

		self.Dcube[35],self.Dcube[37],self.Dcube[17],self.Dcube[15]=self.Dcube[15],self.Dcube[35],self.Dcube[37],self.Dcube[17]
		self.Dcube[25],self.Dcube[36],self.Dcube[26],self.Dcube[16]=self.Dcube[16],self.Dcube[25],self.Dcube[36],self.Dcube[26]
		self.Dcube[43],self.Dcube[38],self.Dcube[3],self.Dcube[14]=self.Dcube[14],self.Dcube[43],self.Dcube[38],self.Dcube[3]
		self.Dcube[45],self.Dcube[24],self.Dcube[5],self.Dcube[27]=self.Dcube[24],self.Dcube[5],self.Dcube[27],self.Dcube[45]
		self.Dcube[48],self.Dcube[34],self.Dcube[8],self.Dcube[18]=self.Dcube[34],self.Dcube[8],self.Dcube[18],self.Dcube[48]
		

		self.Dcube[2],self.Dcube[13],self.Dcube[42],self.Dcube[39]=self.Dcube[39],self.Dcube[2],self.Dcube[13],self.Dcube[42]
		self.Dcube[7],self.Dcube[33],self.Dcube[47],self.Dcube[19]=self.Dcube[19],self.Dcube[7],self.Dcube[33],self.Dcube[47]
		self.Dcube['U'],self.Dcube['F'],self.Dcube['D'],self.Dcube['B']=self.Dcube['B'],self.Dcube['U'],self.Dcube['F'],self.Dcube['D']
		self.orientation = self.orientation+'f'

	def FtoR(self):
		self.UtoF()
		self.UtoR()
		self.UtoF()
		self.UtoR()
		self.UtoR()



	def mouvt(self):# permet de changer la liste de mouvement selon l'orientation


		self.mvt = ['U','L','F','R','B','D']# on peut optimiser 
		for i in range (1,len(self.orientation)+1):
			for j in range (0,6):

				if self.orientation[-i] == "r" :
					if self.mvt[j] == 'U':
						self.mvt[j] = 'L'

					elif self.mvt[j] == 'L':
						self.mvt[j] = 'D'

					elif self.mvt[j] == 'F':
						self.mvt[j] = 'F'

					elif self.mvt[j] == 'R':
						self.mvt[j] = 'U'

					elif self.mvt[j] == 'B':
						self.mvt[j] = 'B'

					elif self.mvt[j] == 'D':
						self.mvt[j] = 'R'

				elif self.orientation[-i] == "f" :

					if self.mvt[j] == 'U':
						self.mvt[j] = 'B'

					elif self.mvt[j] == 'L':
						self.mvt[j] = 'L'

					elif self.mvt[j] == 'F':
						self.mvt[j] = 'U'

					elif self.mvt[j] == 'R':
						self.mvt[j] = 'R'

					elif self.mvt[j] == 'B':
						self.mvt[j] = 'D'

					elif self.mvt[j] == 'D':
						self.mvt[j] = 'F'

	def ajoutermvt(self,mouvement):# permet d'ajouter le bon mouvement selon l'orientation

		self.mouvt()
		if mouvement[0] == 'U':
			self.solve.append(self.mvt[0]+mouvement[1:])

		elif mouvement[0] == 'L':
			self.solve.append(self.mvt[1]+mouvement[1:])

		elif mouvement[0] == 'F':
			self.solve.append(self.mvt[2]+mouvement[1:])

		elif mouvement[0] == 'R':
			self.solve.append(self.mvt[3]+mouvement[1:])

		elif mouvement[0] == 'B':
			self.solve.append(self.mvt[4]+mouvement[1:])

		elif mouvement[0] == 'D':
			self.solve.append(self.mvt[5]+mouvement[1:])




	def reduction(self):
		tmp = []
		i = 0
		table1 = ['U','L','F','R','B','D']
		table2 = ['U2','L2','F2','R2','B2','D2']
		table3 = ['U\'','L\'','F\'','R\'','B\'','D\'']
		
		while i < len(self.solve):
			j = i+1

			if j+1 < len(self.solve) and self.solve[i] == self.solve[j] == self.solve[j+1] and self.solve[i] in table1:#si il y a trosi fois le mouvement de base
				tmp.append(self.solve[i][0]+'\'')
				i = i+3

			elif j+1 < len(self.solve) and self.solve[i] == self.solve[j] == self.solve[j+1] and self.solve[i] in table3:#si il y a trois fois le mouvement anti horaire
				tmp.append(self.solve[i][0])
				i = i+3

			elif j < len(self.solve) and self.solve[i] == self.solve[j] and self.solve[i] in (table1+table3):#si il y a deux fois le même mouvement 
				tmp.append(self.solve[i][0]+'2')
				i = i+2

			elif j < len(self.solve) and self.solve[i][0] == self.solve[j][0] and ((self.solve[i] in table1 and self.solve[j] in table3) or (self.solve[i] in table1 and self.solve[j] in table3)):#si les 2 mvt s'annule 
				i = i+2

			elif j < len(self.solve) and self.solve[i][0] == self.solve[j][0] and ((self.solve[i] in table1 and self.solve[j] in table2) or (self.solve[j] in table1 and self.solve[i] in table2)):#mvt 2 et un basique
				tmp.append(self.solve[i][0]+'\'')
				i = i+2

			elif j < len(self.solve) and self.solve[i][0] == self.solve[j][0] and ((self.solve[i] in table1 and self.solve[j] in table3) or(self.solve[j] in table1 and self.solve[i] in table3)) :# mvt et un anti horaire
				i = i+2

			elif j < len(self.solve) and self.solve[i] == self.solve[j] and self.solve[i] in table2:# deux fois 2 reviens a rien 
				i = i+2
			
			else :# sinon on ajoute le mvt 
				tmp.append(self.solve[i])
				i = i+1

		self.solve = tmp
	

	def Simplifier(self):
		#On parcours trois fois la chaine de solution pour retirer toutes les erreurs
		self.reduction()
		self.reduction()
		self.reduction()

	def afficher2D(self, numero = True, theme = 'base'):
		#Cette fonction sert à afficher graphiquement notre cube en 2D
		affichage = Tk()
		if theme == 'base':
			couleur ={'W':'white','G':'green','R':'#F00000','B':'#0A64FE','O':'#FB8E00','Y':'#FEE500','N':'#CCCCCC'} #On définit les couleurs de nos etiquettes
		canvas = Canvas(affichage, width=810, height=610)
		
		#La position de notre cube initial
		posX = 220
		posY = 20

		#La liste des etiquettes
		liste =[1,2,3,4,'U',5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,'L',22,23,'F',24,25,'R',26,27,'B',28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,'D',45,46,47,48]

		#On définit ensuite le indices auxquels on doit faire des sauts particulier dans la position
		RemiseX220=[2,5,32,47,50,44]
		SautY=[20,2,5,32,47,50]
		SautY2=[8,44]
		SautX=[11,14,17,23,26,29,35,38,41]
		RemiseX20=[8,20,32]

		for i in range(0,len(liste)):
			canvas.create_rectangle(posX,posY,posX+50,posY+50,fill=couleur[self.Dcube[liste[i]]],activedash=(1,10)) #Chaque etiquette conrrespond à un rectangle

			if numero: #On peux choisir en paramètre d'afficher ou non le numéro dans l'étiquette
				canvas.create_text(posX+25, posY+25,text = liste[i])
			posX +=60


			if i in RemiseX220:
				posX = 220
			if i in SautY:
				posY +=60
			if i in SautX:
				posX += 20
			if i in SautY2:
				posY += 80
			if i in RemiseX20:
				posX = 20
		canvas.pack()
		affichage.mainloop()

	def MAZ(self): #Mise A Zero
		#Cette fonction prend un cube et met toute ses étiquettes à 'N' (pour Null) et reinitialise les attributs
		#Cette fonction est utile dans le cas d'un input invalide ou pour mélanger un cube
		liste =[1,2,3,4,'U',5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,'L',22,23,'F',24,25,'R',26,27,'B',28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,'D',45,46,47,48]
		for i in range(0,len(liste)):
			self.Dcube[liste[i]] = 'N'

		#On reinitialise ensuite tous les attributs
		self.chaine =''
		self.solve = []
		self.orientation =''
		self.solution = ''
		self.mvt = ['U','L','F','R','B','D']

	def Scramble(self,nombreMelange=25):
		#Cette fonction prend un cube resolu, lui applique 25 mouvements aléatoire (paramétrable) et rentre la configuration dans notre cube
		self.MAZ()
		cubeResolu = 'WWWWWWWWWOOOYYYBBBGGGOOOYYYBBBGGGOOOYYYBBBGGGRRRRRRRRR'
		cube = Rubik(cubeResolu)
		a = 0
		for i in range(0,nombreMelange):
			a = randint(0,17)
			if a == 0:
				cube.U()
			elif a == 1:
				cube.UU()
			elif a == 2:
				cube.IU()
			elif a == 3:
				cube.L()
			elif a == 4:
				cube.LL()
			elif a == 5:
				cube.IL()
			elif a == 6:
				cube.F()
			elif a == 7:
				cube.FF()
			elif a == 8:
				cube.IF()
			elif a == 9:
				cube.R()
			elif a == 10:
				cube.RR()
			elif a == 11:
				cube.IR()
			elif a == 12:
				cube.B()
			elif a == 13:
				cube.BB()
			elif a == 14:
				cube.IB()
			elif a == 15:
				cube.D()
			elif a == 16:
				cube.DD()
			elif a == 17:
				cube.ID()
		self.Dcube = cube.Dcube
		self.solve = []
#--------------------------------------------------------------------------------------------------

#ZONE DE TEST /!\

cubeResolu = 'WWWWWWWWWOOOYYYBBBGGGOOOYYYBBBGGGOOOYYYBBBGGGRRRRRRRRR'
cube = Rubik(cubeResolu)
cube.afficher2D()