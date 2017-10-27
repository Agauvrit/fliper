 #coding utf8
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
c11 = 'OGORYYRORGGBWBYBOGWOYWGWGOYGBBRROWROYBYGWWRRBBYRWWBOYG'
c12 = 'YRYWYWRGGROWGYYRROBGBWGGWOBRBOGRBGBBWRWGORWBOOYOYWYYOB'
c13 = 'WYBWYGGBBRRWOYYOWOWOGOGGROBOBGYRWWGGYRBYRYGBROBROWYBWR'
c14 = 'GYBRYGBWGYGRYGYROOWOORGYGOYBBBRRWGWYBYWROWBWWORGBWBOOR'


cube = Rubik(c4)


#-----------------------------------------------------------------------------------------------------------------------




def FLL(cube): 
	#si coin LDF en ULF
	if(cube.Dcube[6]==cube.Dcube['L'] and cube.Dcube[11]==cube.Dcube['D'] and cube.Dcube[12]== cube.Dcube['F']): 
		# LF en UF
		if (cube.Dcube[7]==cube.Dcube['L'] and cube.Dcube[13]==cube.Dcube['F']):
			cube.U()
			cube.F()
			cube.IU()
			cube.IF()
		# FL en UF 
		elif (cube.Dcube[7]==cube.Dcube['F'] and cube.Dcube[13]==cube.Dcube['L']):
			cube.L()
			cube.UU()
			cube.LL()
			cube.IU()
			cube.LL()
			cube.IU()
			cube.IL() 
		# LF en UR
		elif (cube.Dcube[5]==cube.Dcube['L'] and cube.Dcube[16]==cube.Dcube['F']):
			cube.IU()
			cube.F()
			cube.U()
			cube.IF()
			cube.UU()
			cube.F()
			cube.IU()
			cube.IF()
		# FL en UR
		elif (cube.Dcube[5]==cube.Dcube['F'] and cube.Dcube[16]==cube.Dcube['L']):
			cube.U()
			cube.IL()
			cube.IU()
			cube.L()
			cube.IU()
			cube.IL()
			cube.IU()
			cube.L()
		# LF en LF
		elif (cube.Dcube[22]==cube.Dcube['L'] and cube.Dcube[23]==cube.Dcube['F']):
			cube.IU()
			cube.F()
			cube.IU()
			cube.IF()
			cube.UU()
			cube.F()
			cube.IU()
			cube.IF()
		# FL en LF
		elif (cube.Dcube[22]==cube.Dcube['F'] and cube.Dcube[23]==cube.Dcube['L']):
			cube.UU()
			cube.F()
			cube.U()
			cube.IF()
			cube.L()
			cube.IF()
			cube.IL()
			cube.F()
		# LF en UB 
		elif (cube.Dcube[2]==cube.Dcube['L'] and cube.Dcube[19]==cube.Dcube['F']):
			cube.F()
			cube.U()
			cube.R()
			cube.UU()
			cube.IR()
			cube.U()
			cube.IF()
		# FL en UB
		elif (cube.Dcube[2]==cube.Dcube['F'] and cube.Dcube[19]==cube.Dcube['L']):
			cube.IL()
			cube.IU()
			cube.L()
		# LF en UL
		elif(cube.Dcube[4]==cube.Dcube['L'] and cube.Dcube[10]==cube.Dcube['F']):
			cube.IL()
			cube.U()
			cube.L()
			cube.UU()
			cube.F()
			cube.U()
			cube.IF()
		# FL en UL
		elif (cube.Dcube[4]==cube.Dcube['F'] and cube.Dcube[10]==cube.Dcube['L']):
			cube.U()
			cube.IL()
			cube.U()
			cube.L()
			cube.IU()
			cube.IL()
			cube.IU()
			cube.L()
	#si coin FLD en ULF
	elif(cube.Dcube[6]==cube.Dcube['F'] and cube.Dcube[11]==cube.Dcube['L'] and cube.Dcube[12]== cube.Dcube['D']):
		# LF en UF
		if(cube.Dcube[7]==cube.Dcube['L'] and cube.Dcube[13]==cube.Dcube['F']):
			cube.IU()
			cube.F()
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()
			cube.U()
			cube.IF()
		#FL en UF
		elif(cube.Dcube[7]==cube.Dcube['F'] and cube.Dcube[13]==cube.Dcube['L']):
			cube.F()
			cube.IU()
			cube.IF()
			cube.UU()
			cube.IL()
			cube.IU()
			cube.L()
		# LF en UL 
		elif(cube.Dcube[4]==cube.Dcube['L'] and cube.Dcube[10]==cube.Dcube['F']):
			cube.IF()
			cube.UU()
			cube.FF()
			cube.U()
			cube.FF()
			cube.U()
			cube.F()
		# FL en UL
		elif (cube.Dcube[4]==cube.Dcube['F'] and cube.Dcube[10]==cube.Dcube['L']):
			cube.IU()
			cube.IL()
			cube.U()
			cube.L()
		# FL en UR
		elif(cube.Dcube[5]==cube.Dcube['F'] and cube.Dcube[16]==cube.Dcube['L']):
			cube.IL()
			cube.IU()
			cube.IB()
			cube.UU()
			cube.B()
			cube.IU()
			cube.L()
		# LF en UR
		elif(cube.Dcube[5]==cube.Dcube['L'] and cube.Dcube[16]==cube.Dcube['F']):
			cube.F()
			cube.U()
			cube.IF()
		# LF en UB 
		elif(cube.Dcube[2]==cube.Dcube['L'] and cube.Dcube[19]==cube.Dcube['F']):
			cube.IU()
			cube.F()
			cube.U()
			cube.IF()
			cube.U()
			cube.F()
			cube.U()
			cube.IF()
		# FL en UB
		elif (cube.Dcube[2]==cube.Dcube['F'] and cube.Dcube[19]==cube.Dcube['L']):
			cube.U()
			cube.IL()
			cube.IU()
			cube.L()
			cube.UU()
			cube.IL()
			cube.U()
			cube.L()
		#LF en LF 
		elif(cube.Dcube[22]==cube.Dcube['L'] and cube.Dcube[23]==cube.Dcube['F']):
			cube.IU()
			cube.F()
			cube.UU()
			cube.IF()
			cube.U()
			cube.F()
			cube.U()
			cube.IF()
		# FL en FL
		elif(cube.Dcube[22]==cube.Dcube['F'] and cube.Dcube[23]==cube.Dcube['L']):
			cube.UU()
			cube.IL()
			cube.U()
			cube.L()
			cube.U()
			cube.F()
			cube.U()
			cube.IF()
	#si DFL en ULF
	elif(cube.Dcube[6]==cube.Dcube['D'] and cube.Dcube[11]==cube.Dcube['F'] and cube.Dcube[12]== cube.Dcube['L']):
		# LF en UF
		if(cube.Dcube[7]==cube.Dcube['L'] and cube.Dcube[13]==cube.Dcube['F']):
			cube.F()
			cube.UU()
			cube.IF()
			cube.IU()
			cube.F()
			cube.U()
			cube.IF()
		# FL en UF
		elif (cube.Dcube[7]==cube.Dcube['F'] and cube.Dcube[13]==cube.Dcube['L']):
			cube.IL()
			cube.IU()
			cube.L()
			cube.F()
			cube.IU()
			cube.IF()
			cube.IL()
			cube.IU()
			cube.L()
		# LF en UL
		elif(cube.Dcube[4]==cube.Dcube['L'] and cube.Dcube[10]==cube.Dcube['F']):
			cube.F()
			cube.U()
			cube.IF()
			cube.IL()
			cube.U()
			cube.L()
			cube.F()
			cube.U()
			cube.IF()
		# FL en UL
		elif (cube.Dcube[4]==cube.Dcube['F'] and cube.Dcube[10]==cube.Dcube['L']):
			cube.IL()
			cube.UU()
			cube.L()
			cube.U()
			cube.IL()
			cube.IU()
			cube.L()
		# FL en UR
		elif(cube.Dcube[5]==cube.Dcube['F'] and cube.Dcube[16]==cube.Dcube['L']):
			cube.IL()
			cube.IB()
			cube.UU()
			cube.B()
			cube.L()
		# LF en UR
		elif(cube.Dcube[5]==cube.Dcube['L'] and cube.Dcube[16]==cube.Dcube['F']):
			cube.U()
			cube.F()
			cube.UU()
			cube.IF()
			cube.U()
			cube.F()
			cube.IU()
			cube.IF()
		# LF en LF
		elif(cube.Dcube[22]==cube.Dcube['L'] and cube.Dcube[23]==cube.Dcube['F']):
			cube.FF()
			cube.U()
			cube.FF()
			cube.U()
			cube.FF()
			cube.UU()
			cube.FF()
		# FL en LF
		elif(cube.Dcube[22]==cube.Dcube['F'] and cube.Dcube[23]==cube.Dcube['L']):
			cube.F()
			cube.IU()
			cube.IF()
			cube.U()
			cube.IL()
			cube.U()
			cube.L()
		# LF en UB 
		elif(cube.Dcube[2]==cube.Dcube['L'] and cube.Dcube[19]==cube.Dcube['F']):
			cube.F()
			cube.R()
			cube.UU()
			cube.IR()
			cube.IF() 
		# FL en UB	
		elif(cube.Dcube[2]==cube.Dcube['F'] and cube.Dcube[19]==cube.Dcube['L']):
			cube.IU()
			cube.IL()
			cube.UU()
			cube.L()
			cube.IU()
			cube.IL()
			cube.U()
			cube.L()
	# si coin LFD en LFD
	elif(cube.Dcube[31]==cube.Dcube['L'] and cube.Dcube[32]==cube.Dcube['F'] and cube.Dcube[41]== cube.Dcube['D']):
		# si FL en LF
		if(cube.Dcube[22]==cube.Dcube['F'] and cube.Dcube[23]==cube.Dcube['L']):
			cube.F()
			cube.IU()
			cube.F()
			cube.UU()
			cube.L()
			cube.FF()
			cube.IL()
			cube.UU()
			cube.FF()
		# si LF en UF
		elif(cube.Dcube[7]==cube.Dcube['L'] and cube.Dcube[13]==cube.Dcube['F']):
			cube.IU()
			cube.IL()
			cube.U()
			cube.L()
			cube.IF()
			cube.L()
			cube.F()
			cube.IL()
		# FL en UL
		elif(cube.Dcube[4]==cube.Dcube['F'] and cube.Dcube[10]==cube.Dcube['L']):
			cube.U()
			cube.F()
			cube.IU()
			cube.IF()
			cube.L()
			cube.IF()
			cube.IL()
			cube.F()
	# si coin DLF en LFD 
	elif(cube.Dcube[31]==cube.Dcube['D'] and cube.Dcube[32]==cube.Dcube['L'] and cube.Dcube[41]== cube.Dcube['F']):
		# si LF en LF
		if(cube.Dcube[22]==cube.Dcube['L'] and cube.Dcube[23]==cube.Dcube['F']):
			cube.F()
			cube.UU()
			cube.F()
			cube.UU()
			cube.L()
			cube.F()
			cube.IL()
			cube.UU()
			cube.FF()
		# si LF en UF
		elif(cube.Dcube[7]==cube.Dcube['L'] and cube.Dcube[13]==cube.Dcube['F']):
			cube.F()
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()
			cube.IU()
			cube.IF()
		# si FL en UL 
		elif(cube.Dcube[4]==cube.Dcube['F'] and cube.Dcube[10]==cube.Dcube['L']):
			cube.IL()
			cube.IU()
			cube.L()
			cube.U()
			cube.IL()
			cube.IU()
			cube.L()
	# si coin FDL en LFD et LF en UF
	elif(cube.Dcube[31]==cube.Dcube['F'] and cube.Dcube[32]==cube.Dcube['D'] and cube.Dcube[41]== cube.Dcube['L']):
		#si LF en UF
		if cube.Dcube[7]==cube.Dcube['L'] and cube.Dcube[13]==cube.Dcube['F']: 
			cube.F()
			cube.U()
			cube.IF()
			cube.IU()
			cube.F()
			cube.U()
			cube.IF()
		# LF en LF
		elif cube.Dcube[22]==cube.Dcube['L'] and cube.Dcube[23]==cube.Dcube['F']:   
			cube.IL()
			cube.UU()
			cube.IL()
			cube.UU()
			cube.IF()
			cube.IL()
			cube.F()
			cube.UU()
			cube.LL()
		# FL en UL
		elif cube.Dcube[4]==cube.Dcube['F'] and cube.Dcube[10]==cube.Dcube['L']:
			cube.IL()
			cube.U()
			cube.L()
			cube.IU()
			cube.IL()
			cube.U()
			cube.L()

#etape2 resolution du cube 2x2x3
def step2(cube): 
	w=0
	#regarde si l'etape 2 a deja ete realise
	while(cube.Dcube['F']!=cube.Dcube[23] or cube.Dcube['F']!=cube.Dcube[32] or cube.Dcube['F']!=cube.Dcube[33] or cube.Dcube['L']!=cube.Dcube[22] or cube.Dcube['L']!=cube.Dcube[21] or cube.Dcube['L']!=cube.Dcube[29] or cube.Dcube['L']!=cube.Dcube[30] or cube.Dcube['L']!=cube.Dcube[31] or cube.Dcube['D']!=cube.Dcube[41] or cube.Dcube['D']!=cube.Dcube[42] or cube.Dcube['D']!=cube.Dcube[44] or cube.Dcube['D']!=cube.Dcube[46] or cube.Dcube['D']!=cube.Dcube[47] or cube.Dcube['B']!=cube.Dcube[28] or cube.Dcube['B']!=cube.Dcube[39] or cube.Dcube['B']!=cube.Dcube[40]):
		w+=1
		if w>=100:
			break
		#placement de l'arrete FD
		#Recherche Face U
		if((cube.Dcube[2]==cube.Dcube['F'] and cube.Dcube[19]==cube.Dcube['D']) or (cube.Dcube[5]== cube.Dcube['F'] and cube.Dcube[16]== cube.Dcube['D']) or (cube.Dcube[7]== cube.Dcube['F'] and cube.Dcube[13]== cube.Dcube['D']) or (cube.Dcube[4]== cube.Dcube['F'] and cube.Dcube[10]== cube.Dcube['D'])): 
			if cube.Dcube[2]==cube.Dcube['F'] and cube.Dcube[19]==cube.Dcube['D'] : 
				cube.U()
			elif cube.Dcube[4]==cube.Dcube['F'] and cube.Dcube[10]==cube.Dcube['D'] : 
				cube.UU()
			elif cube.Dcube[7]==cube.Dcube['F'] and cube.Dcube[13]==cube.Dcube['D'] : 
				cube.IU()
			cube.IR()
			cube.F()
		#Recherche Face R
		elif ((cube.Dcube[16]==cube.Dcube['F'] and cube.Dcube[5]==cube.Dcube['D']) or (cube.Dcube[26]== cube.Dcube['F'] and cube.Dcube[27]== cube.Dcube['D']) or (cube.Dcube[36]== cube.Dcube['F'] and cube.Dcube[45]== cube.Dcube['D']) or (cube.Dcube[25]== cube.Dcube['F'] and cube.Dcube[24]== cube.Dcube['D'])): 
			if cube.Dcube[25]==cube.Dcube['F'] and cube.Dcube[24]==cube.Dcube['D'] : 
				cube.R()
			elif cube.Dcube[36]==cube.Dcube['F'] and cube.Dcube[45]==cube.Dcube['D'] : 
				cube.RR()
			elif cube.Dcube[26]==cube.Dcube['F'] and cube.Dcube[27]==cube.Dcube['D'] : 
				cube.IR()
			cube.U()
			cube.FF()
			#Recherche Face F
		elif ((cube.Dcube[13]==cube.Dcube['F'] and cube.Dcube[7]==cube.Dcube['D']) or (cube.Dcube[24]== cube.Dcube['F'] and cube.Dcube[25]== cube.Dcube['D']) or (cube.Dcube[33]== cube.Dcube['F'] and cube.Dcube[42]== cube.Dcube['D']) or (cube.Dcube[23]== cube.Dcube['F'] and cube.Dcube[22]== cube.Dcube['D'])): 
			if cube.Dcube[24]==cube.Dcube['F'] and cube.Dcube[25]==cube.Dcube['D'] : 
				cube.F()
			elif cube.Dcube[13]==cube.Dcube['F'] and cube.Dcube[7]==cube.Dcube['D'] : 
				cube.FF()
			elif cube.Dcube[23]==cube.Dcube['F'] and cube.Dcube[22]==cube.Dcube['D'] : 
				cube.IF()
		# Recherche arrete UB et UL 
		elif ((cube.Dcube[10]==cube.Dcube['F'] and cube.Dcube[4]==cube.Dcube['D']) or (cube.Dcube[19]== cube.Dcube['F'] and cube.Dcube[2]== cube.Dcube['D'])):
			if cube.Dcube[10]==cube.Dcube['F'] and cube.Dcube[4]==cube.Dcube['D'] : 
				cube.IU()
			elif cube.Dcube[19]==cube.Dcube['F'] and cube.Dcube[2]==cube.Dcube['D'] : 
				cube.UU()
			cube.FF()
		#Recherche arrete RD et RB
		elif ((cube.Dcube[45]==cube.Dcube['F'] and cube.Dcube[36]==cube.Dcube['D']) or (cube.Dcube[27]== cube.Dcube['F'] and cube.Dcube[26]== cube.Dcube['D'])):
			if cube.Dcube[45]==cube.Dcube['F'] and cube.Dcube[36]==cube.Dcube['D'] : 
				cube.IR()
			elif cube.Dcube[27]==cube.Dcube['F'] and cube.Dcube[26]==cube.Dcube['D'] : 
				cube.RR()
			cube.F()	
		#Recherche FD et FL 
		elif ((cube.Dcube[22]==cube.Dcube['F'] and cube.Dcube[23]==cube.Dcube['D']) or (cube.Dcube[42]== cube.Dcube['F'] and cube.Dcube[33]== cube.Dcube['D'])):
			if cube.Dcube[22]==cube.Dcube['F'] and cube.Dcube[23]==cube.Dcube['D'] : 
				cube.F()
			elif cube.Dcube[42]==cube.Dcube['F'] and cube.Dcube[33]==cube.Dcube['D'] : 
				cube.FF()
			cube.IU()
			cube.IR()
			cube.F()	

		#Recherche du Coin LFD
		#si coin FRD
		if((cube.Dcube[43]==cube.Dcube['D'] and cube.Dcube[35]==cube.Dcube['F'] and cube.Dcube[34]==cube.Dcube['L']) or (cube.Dcube[43]== cube.Dcube['L'] and cube.Dcube[35]== cube.Dcube['D'] and cube.Dcube[34]==cube.Dcube['F']) or (cube.Dcube[43]== cube.Dcube['F'] and cube.Dcube[35]== cube.Dcube['L'] and cube.Dcube[34]== cube.Dcube['D'])):
			cube.R()
			cube.U()
		#si coin RBD
		elif((cube.Dcube[38]==cube.Dcube['D'] and cube.Dcube[37]==cube.Dcube['F'] and cube.Dcube[48]==cube.Dcube['L']) or (cube.Dcube[38]== cube.Dcube['L'] and cube.Dcube[37]== cube.Dcube['D'] and cube.Dcube[48]==cube.Dcube['F']) or (cube.Dcube[38]== cube.Dcube['F'] and cube.Dcube[37]== cube.Dcube['L'] and cube.Dcube[48]== cube.Dcube['D'])):
			cube.IR()
			cube.UU()
		#si coin FUR
		elif((cube.Dcube[14]==cube.Dcube['D'] and cube.Dcube[15]==cube.Dcube['F'] and cube.Dcube[8]==cube.Dcube['L']) or (cube.Dcube[14]== cube.Dcube['L'] and cube.Dcube[15]== cube.Dcube['D'] and cube.Dcube[8]==cube.Dcube['F']) or (cube.Dcube[14]== cube.Dcube['F'] and cube.Dcube[15]== cube.Dcube['L'] and cube.Dcube[8]== cube.Dcube['D'])):
			cube.U()
		#si coin URB
		elif((cube.Dcube[17]==cube.Dcube['D'] and cube.Dcube[18]==cube.Dcube['F'] and cube.Dcube[3]==cube.Dcube['L']) or (cube.Dcube[17]== cube.Dcube['L'] and cube.Dcube[18]== cube.Dcube['D'] and cube.Dcube[3]==cube.Dcube['F']) or (cube.Dcube[17]== cube.Dcube['F'] and cube.Dcube[18]== cube.Dcube['L'] and cube.Dcube[3]== cube.Dcube['D'])):
			cube.UU()
		#si coin ULB
		elif((cube.Dcube[20]==cube.Dcube['D'] and cube.Dcube[9]==cube.Dcube['F'] and cube.Dcube[1]==cube.Dcube['L']) or (cube.Dcube[20]== cube.Dcube['L'] and cube.Dcube[9]== cube.Dcube['D'] and cube.Dcube[1]==cube.Dcube['F']) or (cube.Dcube[20]== cube.Dcube['F'] and cube.Dcube[9]== cube.Dcube['L'] and cube.Dcube[1]== cube.Dcube['D'])):
			cube.IU()
		# si coin FLD
		elif (cube.Dcube[31]==cube.Dcube['L'] and cube.Dcube[32]==cube.Dcube['F'] and cube.Dcube[41]==cube.Dcube['D']) or (cube.Dcube[31]== cube.Dcube['F'] and cube.Dcube[32]== cube.Dcube['D'] and cube.Dcube[41]==cube.Dcube['L']) or (cube.Dcube[31]== cube.Dcube['D'] and cube.Dcube[32]== cube.Dcube['L'] and cube.Dcube[41]== cube.Dcube['F']):
			#si LF en FR 
			if (cube.Dcube[24]==cube.Dcube['F'] and cube.Dcube[25]==cube.Dcube['L']) or (cube.Dcube[25]==cube.Dcube['F'] and cube.Dcube[24]==cube.Dcube['L']):
				cube.IF()
				cube.U()
				cube.F()
				if cube.Dcube[10] == cube.Dcube['F']:
					cube.IU()
			#si LF en RD
			elif (cube.Dcube[36]==cube.Dcube['F'] and cube.Dcube[45]==cube.Dcube['L']) or (cube.Dcube[45]==cube.Dcube['F'] and cube.Dcube[36]==cube.Dcube['L']):
				cube.RR()
				if cube.Dcube[16] == cube.Dcube['F']:
					cube.U()
				else :
					cube.UU()
			#Si LF en RB
			elif (cube.Dcube[26]==cube.Dcube['F'] and cube.Dcube[27]==cube.Dcube['L']) or (cube.Dcube[27]==cube.Dcube['F'] and cube.Dcube[26]==cube.Dcube['L']):
				cube.IR()
				if cube.Dcube[16] == cube.Dcube['F']:
					cube.U()
				else :
					cube.UU()
			#si LF en UR
			elif (cube.Dcube[5] == cube.Dcube['F'] and cube.Dcube[16] == cube.Dcube['L']) or (cube.Dcube[16] == cube.Dcube['F'] and cube.Dcube[5] == cube.Dcube['L']):
				if cube.Dcube[16] == cube.Dcube['F']:
					cube.U()
				else:
					cube.UU()
			#Si LF en UB
			elif (cube.Dcube[2] == cube.Dcube['F'] and cube.Dcube[19] == cube.Dcube['L']) or (cube.Dcube[19] == cube.Dcube['F'] and cube.Dcube[2] == cube.Dcube['L']):
				if cube.Dcube[19] == cube.Dcube['F']:
					cube.UU()
				else:
					cube.IU()
			#si LF en UL mal positionne
			elif (cube.Dcube[4] == cube.Dcube['F'] and cube.Dcube[10] == cube.Dcube['L']) or (cube.Dcube[10] == cube.Dcube['F'] and cube.Dcube[4] == cube.Dcube['L']):
				if cube.Dcube[10] == cube.Dcube['F']:
					cube.IU()
			#si LF en UF mal positionne
			elif (cube.Dcube[7] == cube.Dcube['F'] and cube.Dcube[13] == cube.Dcube['L']) or (cube.Dcube[13] == cube.Dcube['F'] and cube.Dcube[7] == cube.Dcube['L']):
				if cube.Dcube[13] == cube.Dcube['L']:
					cube.U()
			#si LF en LF mal oriente
			elif (cube.Dcube[22] == cube.Dcube['F'] and cube.Dcube[23] == cube.Dcube['L']):
				cube.F()
				cube.U()
				cube.IF()
				cube.IU()

		#Recherche arrete LF sur la face R
		if (cube.Dcube[24]==cube.Dcube['L'] and cube.Dcube[25]==cube.Dcube['F']) or (cube.Dcube[24]==cube.Dcube['F'] and cube.Dcube[25]==cube.Dcube['L']): 
			cube.R()
		elif (cube.Dcube[36]==cube.Dcube['L'] and cube.Dcube[45]==cube.Dcube['F']) or (cube.Dcube[36]==cube.Dcube['F'] and cube.Dcube[45]==cube.Dcube['L']):
			cube.RR()
		elif (cube.Dcube[26]==cube.Dcube['L'] and cube.Dcube[27]==cube.Dcube['F']) or (cube.Dcube[26]==cube.Dcube['F'] and cube.Dcube[27]==cube.Dcube['L']):
			cube.IR()

		#appel de FLL
		FLL(cube)


def etape3(cube):               # Réalisation de la troisième étape de la méthode de Petrus

        # Orientation du cube permettant d'avoir le cube 2*2*3 derrière en bas pour pouvoir faire directement les mouvements
	cube.UtoR()
	cube.UtoR()
	cube.UtoR()
	cube.UtoF()
	cube.UtoR()

        # Caclul du nombre d'arêtes mal orientées sur le cube afin de lancer les tests qui correspondent
	tmp = compterAretesMalOrientees(cube)


        # Dans le cas ou il y a deux arêtes mals orientées
	if tmp == 2:
		

		# Les 2 arêtes sur F
		if (cube.Dcube[7] == cube.Dcube["F"] or cube.Dcube[13] == cube.Dcube["U"]) and \
			 (cube.Dcube[22] == cube.Dcube["F"] or cube.Dcube[23] == cube.Dcube["U"]) :
				cube.UU()
				cube.IL()
				cube.IU()
				cube.L()
		elif (cube.Dcube[7] == cube.Dcube["F"] or cube.Dcube[13] == cube.Dcube["U"]) and \
			 (cube.Dcube[25] == cube.Dcube["F"] or cube.Dcube[24] == cube.Dcube["U"]) :
				 cube.U()
				 RecoMotif3(cube)	  
		elif (cube.Dcube[22] == cube.Dcube["F"] or cube.Dcube[23] == cube.Dcube["U"]) and \
			 (cube.Dcube[42] == cube.Dcube["F"] or cube.Dcube[33] == cube.Dcube["U"]) :
				 cube.F()
				 cube.U()
				 cube.U()
				 cube.IL()
				 cube.IU()
				 cube.L()   
		elif (cube.Dcube[42] == cube.Dcube["F"] or cube.Dcube[33] == cube.Dcube["U"]) and \
			 (cube.Dcube[25] == cube.Dcube["F"] or cube.Dcube[24] == cube.Dcube["U"]) :
				 cube.IF()
				 cube.U()
				 RecoMotif3(cube)	
		elif (cube.Dcube[7] == cube.Dcube["F"] or cube.Dcube[13] == cube.Dcube["U"]) and \
			 (cube.Dcube[42] == cube.Dcube["F"] or cube.Dcube[33] == cube.Dcube["U"]) :
				 cube.UU()
				 cube.IF()
				 cube.R()
				 cube.U()
				 cube.IR()
		elif (cube.Dcube[22] == cube.Dcube["F"] or cube.Dcube[23] == cube.Dcube["U"]) and \
			 (cube.Dcube[25] == cube.Dcube["F"] or cube.Dcube[24] == cube.Dcube["U"]) :
				 cube.F()
				 cube.UU()
				 cube.IF()
				 cube.R()
				 cube.U()
				 cube.IR()


		# Les deux arêtes sur U 
		elif (cube.Dcube[4] == cube.Dcube["F"] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[5] == cube.Dcube["F"] or cube.Dcube[16]==cube.Dcube['U']) :
				cube.U()
				RecoMotif4(cube)
		elif (cube.Dcube[2] == cube.Dcube["F"] or cube.Dcube[19]==cube.Dcube['U']) and (cube.Dcube[7] == cube.Dcube["F"] or cube.Dcube[13] == cube.Dcube["U"]) :
				RecoMotif4(cube)
		elif (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[7]==cube.Dcube['F'] or cube.Dcube[13]==cube.Dcube['U']):
				RecoMotif2(cube)
		elif (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[2]==cube.Dcube['F'] or cube.Dcube[19]==cube.Dcube['U']):
				cube.IU()
				RecoMotif2(cube)
		elif (cube.Dcube[2]==cube.Dcube['F'] or cube.Dcube[19]==cube.Dcube['U']) and (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']):
				cube.UU()
				RecoMotif2(cube)
		elif (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[7]==cube.Dcube['F'] or cube.Dcube[13]==cube.Dcube['U']):
				cube.U()
				RecoMotif2(cube)


		# 1 arête sur U et 1 sur F
		elif (cube.Dcube[2] == cube.Dcube['F'] or cube.Dcube[19] == cube.Dcube['U']) and (cube.Dcube[25] == cube.Dcube['F'] or cube.Dcube[24] == cube.Dcube['U']) :
				cube.FF()
				RecoMotif1(cube)

		elif (cube.Dcube[2] == cube.Dcube["F"] or cube.Dcube[19] == cube.Dcube["U"]) and \
			 (cube.Dcube[22] == cube.Dcube["F"] or cube.Dcube[23] == cube.Dcube["U"]) :
				RecoMotif1(cube)
				
		elif (cube.Dcube[2] == cube.Dcube["F"] or cube.Dcube[19] == cube.Dcube["U"]) and \
			 (cube.Dcube[42] == cube.Dcube["F"] or cube.Dcube[33] == cube.Dcube["U"]) :
				cube.IF()
				cube.R()
				cube.U()
				cube.IR()

		elif (cube.Dcube[4] == cube.Dcube["F"] or cube.Dcube[10] == cube.Dcube["U"]) and \
			 (cube.Dcube[25] == cube.Dcube["F"] or cube.Dcube[24] == cube.Dcube["U"]) :
				RecoMotif3(cube)
						   
		elif (cube.Dcube[4] == cube.Dcube["F"] or cube.Dcube[10] == cube.Dcube["U"]) and \
			 (cube.Dcube[22] == cube.Dcube["F"] or cube.Dcube[23] == cube.Dcube["U"]) :
				cube.U()
				RecoMotif1(cube)

		elif (cube.Dcube[4] == cube.Dcube["F"] or cube.Dcube[10] == cube.Dcube["U"]) and \
			 (cube.Dcube[42] == cube.Dcube["F"] or cube.Dcube[33] == cube.Dcube["U"]) :
				cube.IF()
				RecoMotif3(cube)

		elif (cube.Dcube[5] == cube.Dcube["F"] or cube.Dcube[16] == cube.Dcube["U"]) and \
			 (cube.Dcube[25] == cube.Dcube["F"] or cube.Dcube[24] == cube.Dcube["U"]) :
				cube.UU()
				RecoMotif3(cube)

		elif (cube.Dcube[5] == cube.Dcube["F"] or cube.Dcube[16] == cube.Dcube["U"]) and \
			 (cube.Dcube[22] == cube.Dcube["F"] or cube.Dcube[23] == cube.Dcube["U"]) :
				cube.IU()
				RecoMotif1(cube)

		elif (cube.Dcube[5] == cube.Dcube["F"] or cube.Dcube[16] == cube.Dcube["U"]) and \
			 (cube.Dcube[42] == cube.Dcube["F"] or cube.Dcube[33] == cube.Dcube["U"]) :
				cube.IU()
				cube.F()
				RecoMotif1(cube)

        
        # ************************************************************************************************************


        # Dans le cas ou il y a 4 arêtes mals orientés
	elif tmp == 4:

		# 4 arêtes sur U :
		if (cube.Dcube[2] == cube.Dcube["F"] or cube.Dcube[19] == cube.Dcube["U"]) and \
		   (cube.Dcube[4] == cube.Dcube["F"] or cube.Dcube[10] == cube.Dcube["U"]) and \
		   (cube.Dcube[5] == cube.Dcube["F"] or cube.Dcube[16] == cube.Dcube["U"]) and \
		   (cube.Dcube[7] == cube.Dcube["F"] or cube.Dcube[13] == cube.Dcube["U"]) :
				cube.FF()
				cube.UU()
				cube.L()
				cube.IR()
				cube.F()
				cube.IL()
				cube.R()

		# 4 arêtes sur F :
		elif (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) :
				cube.U()
				cube.IF()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()
				

		# 3 arêtes sur F et 1 sur U
		elif (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) :
				cube.F()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()
				
		elif (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) :
				cube.IU()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.FF()
				cube.IL()

		elif (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) :
				cube.R()
				cube.IU()
				cube.RR()
				cube.FF()
				cube.R()
				



		elif (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) :
				cube.IF()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()

		elif (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) :
				cube.IU()
				cube.IF()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()

		elif (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) :
				cube.UU()
				cube.IF()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()
				

		elif (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) :
				cube.FF()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()

		elif (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) :
				cube.IF()
				cube.IU()
				cube.IF()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()
				
		elif (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) :
				cube.IF()
				cube.UU()
				cube.IF()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()
				

		elif (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) :
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()

		elif (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) :
				cube.F()
				cube.IU()
				cube.IF()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()

		elif (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) :
				cube.F()
				cube.UU()
				cube.IF()
				cube.L()
				cube.IF()
				cube.IL()
				cube.R()
				cube.IU()
				cube.IR()


		# 3 arêtes sur U 1 sur F
		elif (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) and \
			(cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) and \
			(cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) :
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()

		elif (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) and \
		   (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) :
				cube.F()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()

		elif (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) :
				cube.FF()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()
				

		elif (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) :
				cube.UU()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()

		elif (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) and \
		   (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) :
				cube.UU()
				cube.F()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()

		elif (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) :
				cube.UU()
				cube.FF()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()


		elif (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) :
				cube.U()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()

		elif (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) :
				cube.U()
				cube.F()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()

		elif (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) and \
		   (cube.Dcube[10] == cube.Dcube["U"] or cube.Dcube[4] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) :
				cube.U()
				cube.FF()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()



		elif (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) and \
		   (cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
		   (cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) and \
		   (cube.Dcube[23] == cube.Dcube["U"] or cube.Dcube[22] == cube.Dcube["F"]) :
				cube.IU()
				cube.IL()
				cube.UU()
				cube.LL()
				cube.IF()
				cube.IL()
				
		elif (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) and \
			(cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
			(cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) and \
			(cube.Dcube[33] == cube.Dcube["U"] or cube.Dcube[42] == cube.Dcube["F"]) :
			cube.IU()
			cube.F()
			cube.IL()
			cube.UU()
			cube.LL()
			cube.IF()
			cube.IL()
				
		elif (cube.Dcube[19] == cube.Dcube["U"] or cube.Dcube[2] == cube.Dcube["F"]) and \
			(cube.Dcube[13] == cube.Dcube["U"] or cube.Dcube[7] == cube.Dcube["F"]) and \
			(cube.Dcube[16] == cube.Dcube["U"] or cube.Dcube[5] == cube.Dcube["F"]) and \
			(cube.Dcube[24] == cube.Dcube["U"] or cube.Dcube[25] == cube.Dcube["F"]) :
			cube.IU()
			cube.FF()
			cube.IL()
			cube.UU()
			cube.LL()
			cube.IF()
			cube.IL()



		#cas ou on 2 arêtes mal orientées sur chaque face :
		#cas ou on a 2 arêtes mal orientées en 2/4
		elif (cube.Dcube[2]==cube.Dcube['F'] or cube.Dcube[19]==cube.Dcube['U']) and (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			Motif1(cube)
		elif (cube.Dcube[2]==cube.Dcube['F'] or cube.Dcube[19]==cube.Dcube['U']) and (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']):
			Motif2(cube)
		elif (cube.Dcube[2]==cube.Dcube['F'] or cube.Dcube[19]==cube.Dcube['U']) and (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			cube.F()
			Motif1(cube)

		#cas ou a 2 arêtes en 2/5
		elif (cube.Dcube[2]==cube.Dcube['F'] or cube.Dcube[19]==cube.Dcube['U']) and (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			cube.IU()
			Motif1(cube)
		elif (cube.Dcube[2]==cube.Dcube['F'] or cube.Dcube[19]==cube.Dcube['U']) and (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']):
			cube.IU()
			Motif2(cube)
		elif (cube.Dcube[2]==cube.Dcube['F'] or cube.Dcube[19]==cube.Dcube['U']) and (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			Motif3(cube)

		#cas ou 2 arêtes en 4/7
		elif (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[7]==cube.Dcube['F'] or cube.Dcube[13]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			cube.U()
			Motif1(cube)
		elif (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[7]==cube.Dcube['F'] or cube.Dcube[13]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']):
			cube.U()
			Motif2(cube)
		elif (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[7]==cube.Dcube['F'] or cube.Dcube[13]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			cube.U()
			Motif3(cube)

		#cas ou 2 arêtes en 5/7
		elif (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[7]==cube.Dcube['F'] or cube.Dcube[13]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			cube.UU()
			Motif1(cube)
		elif (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[7]==cube.Dcube['F'] or cube.Dcube[13]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']):
			cube.UU()
			Motif2(cube)
		elif (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[7]==cube.Dcube['F'] or cube.Dcube[13]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			cube.UU()
			Motif3(cube)

		#cas ou 2 arêtes en 4/5
		elif (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			cube.F()
			cube.L()
			cube.IF()
			cube.LL()
			cube.UU()
			cube.L()
		elif (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[22]==cube.Dcube['F'] or cube.Dcube[23]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']):
			cube.IL()
			cube.UU()
			cube.LL()
			cube.FF()
			cube.IL()
		elif (cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['U']) and (cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['U']) and (cube.Dcube[24]==cube.Dcube['U'] or cube.Dcube[25]==cube.Dcube['F']) and (cube.Dcube[33]==cube.Dcube['U'] or cube.Dcube[42]==cube.Dcube['F']):
			cube.UtoF()
			cube.UtoR()
			cube.UtoR()
			Motif2(cube)

        # ************************************************************************************************************
	

        # dans le cas ou 6 arêtes sont mals orientées
	elif tmp == 6:
		# 6 arêtes mal orientés
		# On récupère le nombre d'arêtes mal placées, si c'est 6 on exécute ce qui suit

		if cube.Dcube[22]==cube.Dcube['U'] or cube.Dcube[23]==cube.Dcube['F']:
			Edges6(cube)
		elif cube.Dcube[7]==cube.Dcube['U'] or cube.Dcube[13]==cube.Dcube['F']:
			cube.IF()
			Edges6(cube)
		elif cube.Dcube[24]==cube.Dcube['F'] or cube.Dcube[25]==cube.Dcube['U']:
			cube.FF()
			Edges6(cube)
		elif cube.Dcube[33]==cube.Dcube['F'] or cube.Dcube[42]==cube.Dcube['U']:
			cube.F()
			Edges6(cube)
		elif cube.Dcube[4]==cube.Dcube['U'] or cube.Dcube[10]==cube.Dcube['F']:
			cube.UtoF()
			cube.UtoR()
			cube.UtoR()
			cube.FF()
			Edges6(cube)
		elif cube.Dcube[2]==cube.Dcube['U'] or cube.Dcube[19]==cube.Dcube['F']:
			cube.UU()
			cube.IF()
			Edges6(cube)
		elif cube.Dcube[5]==cube.Dcube['U'] or cube.Dcube[16]==cube.Dcube['F']:
			cube.UtoF()
			cube.UtoR()
			cube.UtoR()
			Edges6(cube)

		
# Boite a outil étape 3
def Edges6(cube):

	cube.L()
	cube.IR()
	cube.F()
	cube.IL()
	cube.RR()
	cube.U()
	cube.IR()		

# L F' L'
def RecoMotif1(cube):

	cube.IL()
	cube.IU()
	cube.L()

# L' U' L
def RecoMotif2(cube):

	cube.L()
	cube.IF()
	cube.IL()

# R 2U R'
def RecoMotif3(cube):

	cube.R()
	cube.UU()
	cube.IR()

# F R U R'
def RecoMotif4(cube):

	cube.F()
	cube.R()
	cube.U()
	cube.IR()


#Motif Adjacent/Adjacent ex 2/4 23/33
def Motif1(cube):

	cube.IL()
	cube.IU()
	cube.LL()
	cube.F()
	cube.IL()

#Motif Adjacent/Opposé ex 2/4 23/24
def Motif2(cube):

	cube.IL()
	cube.IU()
	cube.LL()
	cube.FF()
	cube.IL()

#Motif Adjacent/Adjacent ex 2/5 24/33
def Motif3(cube):

	cube.R()
	cube.U()
	cube.RR()
	cube.IF()
	cube.R()


def CoinsFaceD(cube):

	#Cette fonction reconnait dans quel configuration le cube se trouve et le résoud de manière optimale suivant la configuration
	FinDeLetape = False
	k = 0
	while not FinDeLetape:
		if k == 40:
			break
			#On utilise un break au bout de 40 tour de boucle soit si le cube est insolvable dans cette configuration


			#Chaque configuration conrrespond à un cas différent
		#Cas O 
		if cube.TestFaceU():

			#Si les coins sont dejà bien placé, on ne fait rien
			if cube.Dcube[9] == cube.Dcube['L'] and cube.Dcube[12] == cube.Dcube['F'] and cube.Dcube[15] == cube.Dcube['R'] and cube.Dcube[18] == cube.Dcube['B']:
				return None


			#Cas O.1
			if cube.Dcube[14] != cube.Dcube['F'] and cube.Dcube[15] != cube.Dcube['R'] and cube.Dcube[17] != cube.Dcube['R'] and cube.Dcube[18] != cube.Dcube['B']:
				cube.R()
				cube.U()
				cube.IR()
				cube.IU()
				cube.IR()
				cube.F()
				cube.RR()
				cube.IU()
				cube.IR()
				cube.IU()
				cube.R()
				cube.U()
				cube.IR()
				cube.IF()

			if cube.Dcube[17] != cube.Dcube['R'] and cube.Dcube[18] != cube.Dcube['B'] and cube.Dcube[20] != cube.Dcube['B'] and cube.Dcube[9] != cube.Dcube['L']:
				cube.B()
				cube.U()
				cube.IB()
				cube.IU()
				cube.IB()
				cube.R()
				cube.BB()
				cube.IU()
				cube.IB()
				cube.IU()
				cube.B()
				cube.U()
				cube.IB()
				cube.IR()

			if cube.Dcube[11] != cube.Dcube['L'] and cube.Dcube[12] != cube.Dcube['F'] and cube.Dcube[20] != cube.Dcube['B'] and cube.Dcube[9] != cube.Dcube['L']:
				cube.L()
				cube.U()
				cube.IL()
				cube.IU()
				cube.IL()
				cube.B()
				cube.LL()
				cube.IU()
				cube.IL()
				cube.IU()
				cube.L()
				cube.U()
				cube.IL()
				cube.IB()

			if cube.Dcube[11] != cube.Dcube['L'] and cube.Dcube[12] != cube.Dcube['F'] and cube.Dcube[14] != cube.Dcube['F'] and cube.Dcube[15] != cube.Dcube['R']:
				cube.F()
				cube.U()
				cube.IF()
				cube.IU()
				cube.IF()
				cube.L()
				cube.FF()
				cube.IU()
				cube.IF()
				cube.IU()
				cube.F()
				cube.U()
				cube.IF()
				cube.IL()


			#Cas O.2
			if cube.Dcube[14] != cube.Dcube['F'] and cube.Dcube[15] != cube.Dcube['R'] and cube.Dcube[9] != cube.Dcube['L'] and cube.Dcube[20] != cube.Dcube['B']:
				cube.F()
				cube.R()
				cube.IU()
				cube.IR()
				cube.IU()
				cube.R()
				cube.U()
				cube.IR()
				cube.IF()
				cube.R()
				cube.U()
				cube.IR()
				cube.IU()
				cube.IR()
				cube.F()
				cube.R()
				cube.IF()

			if cube.Dcube[12] != cube.Dcube['F'] and cube.Dcube[17] != cube.Dcube['R'] and cube.Dcube[11] != cube.Dcube['L'] and cube.Dcube[18] != cube.Dcube['B']:
				cube.R()
				cube.B()
				cube.IU()
				cube.IB()
				cube.IU()
				cube.B()
				cube.U()
				cube.IB()
				cube.IR()
				cube.B()
				cube.U()
				cube.IB()
				cube.IU()
				cube.IB()
				cube.R()
				cube.B()
				cube.IR()

		#Cas H ou Pi
		elif cube.Dcube[1] != cube.Dcube['U'] and cube.Dcube[3] != cube.Dcube['U'] and cube.Dcube[6] != cube.Dcube['U'] and cube.Dcube[8] != cube.Dcube['U']:

			#Cas H
			if (cube.Dcube[12] == cube.Dcube[14] == cube.Dcube['U'] == cube.Dcube[18] == cube.Dcube[20]) or (cube.Dcube[15] == cube.Dcube[17] == cube.Dcube['U'] == cube.Dcube[9] == cube.Dcube[11]):
				#2 cas possibles, pour se simplifier la vie on se met forcement dans le premier cas via un FintoR
				if (cube.Dcube[15] == cube.Dcube['U'] and cube.Dcube[17] == cube.Dcube['U']):
					cube.FtoR()

				#Cas H.1
				if cube.Dcube[1] == cube.Dcube['L'] and cube.Dcube[6] == cube.Dcube['L'] and cube.Dcube[3] == cube.Dcube['R'] and cube.Dcube[8] == cube.Dcube['R']:
					cube.R()
					cube.UU()
					cube.IR()
					cube.IU()
					cube.R()
					cube.U()
					cube.IR()
					cube.IU()
					cube.R()
					cube.IU()
					cube.IR()

				#cas H.2
				if cube.Dcube[1] == cube.Dcube['R']  == cube.Dcube[3]:
					cube.U()
					cube.IR()
					cube.IU()
					cube.R()
					cube.IU()
					cube.IR()
					cube.IU()
					cube.L()
					cube.IU()
					cube.R()
					cube.U()
					cube.IL()


				if cube.Dcube[6] == cube.Dcube['L'] == cube.Dcube[8]:
					cube.U()
					cube.IL()
					cube.IU()
					cube.L()
					cube.IU()
					cube.IL()
					cube.IU()
					cube.R()
					cube.IU()
					cube.L()
					cube.U()
					cube.IR()




					
				#Cas H.3
				if cube.Dcube[3] == cube.Dcube['B'] == cube.Dcube[8]:
					cube.U()
					cube.F()
					cube.R()
					cube.IU()
					cube.IR()
					cube.U()
					cube.R()
					cube.UU()
					cube.IR()
					cube.IU()
					cube.R()
					cube.U()
					cube.IR()
					cube.IU()
					cube.IF()

				if cube.Dcube[1] == cube.Dcube['F'] == cube.Dcube[6]:
					cube.U()
					cube.B()
					cube.L()
					cube.IU()
					cube.IL()
					cube.U()
					cube.L()
					cube.UU()
					cube.IL()
					cube.IU()
					cube.L()
					cube.U()
					cube.IL()
					cube.IU()
					cube.IB()

				#Cas H.4
				if cube.Dcube[6] == cube.Dcube['F'] == cube.Dcube[8] and cube.Dcube[1] == cube.Dcube['B'] == cube.Dcube[3]:
					cube.F()
					for i in range(0,3):
						cube.R()
						cube.U()
						cube.IR()
						cube.IU()
					cube.IF()

				#Cas H.5
				if cube.Dcube[6] == cube.Dcube['B'] == cube.Dcube[8] and cube.Dcube[1] == cube.Dcube['F'] == cube.Dcube[3]:
					cube.R()
					cube.U()
					cube.IR()
					cube.U()
					cube.IF()
					cube.U()
					cube.F()
					cube.IU()
					cube.FF()
					cube.L()
					cube.F()
					cube.IL()
					cube.F()

			#Cas Pi		
			else:

				#On se place dans une configuration facile
				if cube.Dcube[12] == cube.Dcube['U'] == cube.Dcube[14]:
					for i in range(0,3):
						cube.FtoR()
				elif cube.Dcube[15] == cube.Dcube['U'] == cube.Dcube[17]:
					for i in range(0,2):
						cube.FtoR()
				elif cube.Dcube[18] == cube.Dcube['U'] == cube.Dcube[20]:
					cube.FtoR()

				#Cas Pi.1 ou Pi.4
				if cube.Dcube[3] == cube.Dcube[8] == cube.Dcube['L']:

					#Cas Pi.4
					if cube.Dcube[1] == cube.Dcube[6] == cube.Dcube['R'] and cube.Dcube[15]== cube.Dcube['B'] and cube.Dcube[17] == cube.Dcube['F']:
						cube.UU()
						cube.IL()
						cube.U()
						cube.R()
						cube.IU()
						cube.L()
						cube.IU()
						cube.IR()
						cube.IU()
						cube.R()
						cube.IU()
						cube.IR()

					#Cas Pi.1
					elif cube.Dcube[1] == cube.Dcube['F'] and cube.Dcube['B'] == cube.Dcube[6] and cube.Dcube[15]== cube.Dcube['B'] and cube.Dcube[17] == cube.Dcube['F']:
						cube.R()
						cube.UU()
						cube.RR()
						cube.IU()
						cube.RR()
						cube.IU()
						cube.RR()
						cube.UU()
						cube.R()

				#Cas Pi.2
				elif cube.Dcube[1] == cube.Dcube[8] == cube.Dcube['F'] and cube.Dcube[15] == cube.Dcube['L'] and cube.Dcube[17] == cube.Dcube['B']:
					cube.U()
					cube.R()
					cube.UU()
					cube.IR()
					cube.IU()
					cube.R()
					cube.IU()
					cube.RR()
					cube.U()
					cube.L()
					cube.IU()
					cube.R()
					cube.U()
					cube.IL()

				#Cas Pi.3
				elif cube.Dcube[3] == cube.Dcube[6] == cube.Dcube['B'] and cube.Dcube[15] == cube.Dcube['F'] and cube.Dcube[17] == cube.Dcube['L']:
					cube.IU()
					cube.IR()
					cube.UU()
					cube.R()
					cube.U()
					cube.IR()
					cube.U()
					cube.RR()
					cube.IU()
					cube.IL()
					cube.U()
					cube.IR()
					cube.IU()
					cube.L()

				#Cas Pi.5
				elif cube.Dcube[1] == cube.Dcube[8] == cube.Dcube['B'] and cube.Dcube[15]== cube.Dcube[17] == cube.Dcube['R']:
					cube.IU()
					cube.IR()
					cube.IU()
					cube.F()
					cube.IU()
					cube.RR()
					cube.U()
					cube.RR()
					cube.U()
					cube.IF()
					cube.RR()
					cube.UU()
					cube.IR()

				#Cas Pi.6
				elif cube.Dcube[1] == cube.Dcube[6] == cube.Dcube['R'] and cube.Dcube[15]== cube.Dcube[17] == cube.Dcube['L']:
					cube.F()
					cube.RR()
					cube.IU()
					cube.R()
					cube.IU()
					cube.R()
					cube.IU()
					cube.IR()
					cube.UU()
					cube.IR()
					cube.U()
					cube.RR()
					cube.IF()

		#Cas T ou U
		elif (cube.Dcube[1] != cube.Dcube['U'] and cube.Dcube[6] != cube.Dcube['U'] and cube.Dcube[3] == cube.Dcube[8] == cube.Dcube['U']) or (cube.Dcube[8] != cube.Dcube['U'] and cube.Dcube[6] != cube.Dcube['U'] and cube.Dcube[3] == cube.Dcube[1] == cube.Dcube['U']) or (cube.Dcube[3] != cube.Dcube['U'] and cube.Dcube[8] != cube.Dcube['U'] and cube.Dcube[1] == cube.Dcube[6] == cube.Dcube['U']) or (cube.Dcube[1] != cube.Dcube['U'] and cube.Dcube[3] != cube.Dcube['U'] and cube.Dcube[6] == cube.Dcube[8] == cube.Dcube['U']):
			#Cas U
			#On se place dans la situation ou il suffit de vérifier 1 et 6
			if cube.Dcube[9] == cube.Dcube[11] == cube.Dcube['U'] or cube.Dcube[12] == cube.Dcube[14] == cube.Dcube['U'] or cube.Dcube[15] == cube.Dcube[17] == cube.Dcube['U'] or cube.Dcube[18] == cube.Dcube[20] == cube.Dcube['U']:
				if cube.Dcube[12] == cube.Dcube['U'] == cube.Dcube[14]:
					for i in range(0,3):
						cube.FtoR()
				elif cube.Dcube[15] == cube.Dcube['U'] == cube.Dcube[17]:
					for i in range(0,2):
						cube.FtoR()
				elif cube.Dcube[18] == cube.Dcube['U'] == cube.Dcube[20]:
					cube.FtoR()


				#Cas U.1
				if cube.Dcube[1] == cube.Dcube['L'] and cube.Dcube[6] == cube.Dcube['R'] and cube.Dcube[15] == cube.Dcube[17] == cube.Dcube['B']:
					cube.IU()
					cube.IL()
					cube.IU()
					cube.L()
					cube.IU()
					cube.IL()
					cube.UU()
					cube.LL()
					cube.U()
					cube.IL()
					cube.U()
					cube.L()
					cube.UU()
					cube.IL()

				#Cas U.2
				elif cube.Dcube[1] == cube.Dcube['R'] and cube.Dcube[6] == cube.Dcube['F'] and cube.Dcube[15] == cube.Dcube['R'] and cube.Dcube[17] == cube.Dcube['B']:
					cube.IU()
					cube.RR()
					cube.D()
					cube.IR()
					cube.UU()
					cube.R()
					cube.ID()
					cube.IR()
					cube.UU()
					cube.IR()

				#Cas U.3
				elif cube.Dcube[1] == cube.Dcube['B'] and cube.Dcube[6] == cube.Dcube['R'] and cube.Dcube[15] == cube.Dcube['F'] and cube.Dcube[17] == cube.Dcube['R']:
					cube.U()
					cube.RR()
					cube.ID()
					cube.R()
					cube.UU()
					cube.IR()
					cube.D()
					cube.R()
					cube.UU()
					cube.R()

				#Cas U.5
				elif cube.Dcube[1] == cube.Dcube['F'] and cube.Dcube[6] == cube.Dcube['B'] and cube.Dcube[15] == cube.Dcube['F'] and cube.Dcube[17] == cube.Dcube['B']:
					cube.U()
					cube.IR()
					cube.UU()
					cube.R()
					cube.IF()
					cube.IR()
					cube.F()
					cube.UU()
					cube.IF()
					cube.R()
					cube.F()

				#Cas U.4 ou U.6
				elif cube.Dcube[1] == cube.Dcube[6] == cube.Dcube['L']:

					#Cas U.4
					if cube.Dcube[15] == cube.Dcube[17] == cube.Dcube['R'] and cube.Dcube[14]== cube.Dcube['F'] and cube.Dcube[18] == cube.Dcube['B']:
						cube.IR()
						cube.IU()
						cube.R()
						cube.F()
						cube.RR()
						cube.ID()
						cube.R()
						cube.U()
						cube.IR()
						cube.D()
						cube.RR()
						cube.IU()
						cube.IF()

					#Cas U.6
					elif cube.Dcube[15] == cube.Dcube['B'] and cube.Dcube[17] == cube.Dcube['F'] and cube.Dcube[14] == cube.Dcube['R'] == cube.Dcube[18]:
						cube.U()
						cube.IR()
						cube.UU()
						cube.R()
						cube.F()
						cube.IU()
						cube.IR()
						cube.IU()
						cube.R()
						cube.U()
						cube.IF()


			#Cas T
			else:
				if cube.Dcube[11] == cube.Dcube['U'] == cube.Dcube[15]:
					for i in range(0,3):
						cube.FtoR()
				elif cube.Dcube[14] == cube.Dcube['U'] == cube.Dcube[18]:
					for i in range(0,2):
						cube.FtoR()
				elif cube.Dcube[17] == cube.Dcube['U'] == cube.Dcube[9]:
					cube.FtoR()

				#Cas T.2
				if cube.Dcube[1] == cube.Dcube['B'] and cube.Dcube[6] == cube.Dcube['L'] and cube.Dcube[15] == cube.Dcube['R'] and cube.Dcube[17] == cube.Dcube['B']:
					cube.IU()
					cube.R()
					cube.B()
					cube.IR()
					cube.F()
					cube.R()
					cube.IB()
					cube.IR()
					cube.IF()

				#Cas T.3
				elif cube.Dcube[1] == cube.Dcube['L'] and cube.Dcube[6] == cube.Dcube['F'] and cube.Dcube[15] == cube.Dcube['F'] and cube.Dcube['R'] == cube.Dcube[17]:
					cube.U()
					cube.IR()
					cube.IF()
					cube.R()
					cube.IB()
					cube.IR()
					cube.F()
					cube.R()
					cube.B()

				#Cas T.4
				elif cube.Dcube[1] == cube.Dcube['R'] and cube.Dcube[6] == cube.Dcube['L'] and cube.Dcube[15] == cube.Dcube[17] == cube.Dcube['B']:
					cube.U()
					cube.IR()
					cube.U()
					cube.R()
					cube.UU()
					cube.IL()
					cube.IR()
					cube.U()
					cube.R()
					cube.IU()
					cube.L()

				#Cas T.6
				elif cube.Dcube[1] == cube.Dcube['L'] and cube.Dcube[6] == cube.Dcube['R'] and cube.Dcube[15]== cube.Dcube['R'] and cube.Dcube[17] == cube.Dcube['L']:
					cube.U()
					cube.IR()
					cube.U()
					cube.RR()
					cube.D()
					cube.IL()
					cube.BB()
					cube.L()
					cube.ID()
					cube.RR()
					cube.IU()
					cube.R()

				#Cas T.1 ou T.5
				elif cube.Dcube[1] == cube.Dcube[6] == cube.Dcube['B']:

					#Cas T.5
					if cube.Dcube[15] == cube.Dcube['R'] and cube.Dcube[14] == cube.Dcube['F'] and cube.Dcube[17] == cube.Dcube['L'] and cube.Dcube[18] == cube.Dcube['F']:
						cube.IU()
						cube.F()
						cube.R()
						cube.U()
						cube.IR()
						cube.IU()
						cube.R()
						cube.IU()
						cube.IR()
						cube.IU()
						cube.R()
						cube.U()
						cube.IR()
						cube.IF()

					#Cas T.1
					elif cube.Dcube[14] == cube.Dcube['L'] and cube.Dcube[15] == cube.Dcube['F'] == cube.Dcube[17] and cube.Dcube[18] == cube.Dcube['R']:
						cube.U()
						cube.R()
						cube.UU()
						cube.IR()
						cube.IU()
						cube.R()
						cube.IU()
						cube.RR()
						cube.UU()
						cube.R()
						cube.U()
						cube.IR()
						cube.U()
						cube.R()


		#Cas L
		elif (cube.Dcube[1] == cube.Dcube[8] == cube.Dcube['U'] and cube.Dcube[3] != cube.Dcube['U'] and cube.Dcube[6] !=cube.Dcube['U']) or (cube.Dcube[6] == cube.Dcube[3] == cube.Dcube['U'] and cube.Dcube[1] != cube.Dcube['U'] and cube.Dcube[8] != cube.Dcube['U']):

			if (cube.Dcube[6] == cube.Dcube[3] == cube.Dcube['U'] and cube.Dcube[1] != cube.Dcube['U'] and cube.Dcube[8] != cube.Dcube['U']):
				cube.FtoR()

			if k%5 == 0:
				cube.FtoR()
				cube.FtoR()
			#Cas L.1
			if cube.Dcube[3] == cube.Dcube['B'] and cube.Dcube[6] == cube.Dcube['L'] and cube.Dcube[14] == cube.Dcube['F'] and cube.Dcube[15] == cube.Dcube['R']:
				cube.UU()
				cube.R()
				cube.UU()
				cube.IR()
				cube.IU()
				cube.R()
				cube.U()
				cube.IR()
				cube.IU()
				cube.R()
				cube.U()
				cube.IR()
				cube.IU()
				cube.R()
				cube.IU()
				cube.IR()

			#Cas L.2
			if cube.Dcube[3] == cube.Dcube[6] == cube.Dcube['F'] and cube.Dcube[14] == cube.Dcube['R'] and cube.Dcube[15] == cube.Dcube['B']:
				cube.R()
				cube.UU()
				cube.R()
				cube.D()
				cube.IR()
				cube.UU()
				cube.R()
				cube.ID()
				cube.RR()

			#Cas L.3
			if cube.Dcube[3] == cube.Dcube['L'] and cube.Dcube[6] == cube.Dcube['R'] and cube.Dcube[14] == cube.Dcube['F'] and cube.Dcube[15] == cube.Dcube['R']:
				cube.IR()
				cube.F()
				cube.R()
				cube.IB()
				cube.IR()
				cube.IF()
				cube.R()
				cube.B()

			#Cas L.4
			if cube.Dcube[3] == cube.Dcube[6] == cube.Dcube['B'] and cube.Dcube[14] == cube.Dcube['F'] and cube.Dcube[15] == cube.Dcube['R']:
				cube.IU()
				cube.IR()
				cube.UU()
				cube.IR()
				cube.ID()
				cube.R()
				cube.UU()
				cube.IR()
				cube.D()
				cube.RR()

			#Cas L.5
			if cube.Dcube[3] == cube.Dcube['R'] and cube.Dcube[6] == cube.Dcube['L'] and cube.Dcube[14] == cube.Dcube['R'] and cube.Dcube[15] == cube.Dcube['B']:
				cube.IU()
				cube.R()
				cube.IB()
				cube.IR()
				cube.F()
				cube.R()
				cube.B()
				cube.IR()
				cube.IF()

			#Cas L.6
			if cube.Dcube[3] == cube.Dcube['R'] and cube.Dcube[6] == cube.Dcube['B'] and cube.Dcube[14] == cube.Dcube['R'] and cube.Dcube[15] == cube.Dcube['B']:
				cube.R()
				cube.UU()
				cube.IL()
				cube.IR()
				cube.U()
				cube.R()
				cube.IU()
				cube.L()
				cube.UU()
				cube.IR()


		#Cas S ou S'
		else:
			#Cas S 
			if cube.Dcube[11] == cube.Dcube['U'] or cube.Dcube[14] == cube.Dcube['U'] or cube.Dcube[17] == cube.Dcube['U'] or cube.Dcube[20] == cube.Dcube['U']:
				if cube.Dcube[14] != cube.Dcube['U']:
					for i in range(0,3):
						cube.FtoR()
				elif cube.Dcube[17] != cube.Dcube['U']:
					for i in range(0,2):
						cube.FtoR()
				elif cube.Dcube[20] != cube.Dcube['U']:
					cube.FtoR()


				#Cas S.1
				if cube.Dcube[1] == cube.Dcube['R'] and cube.Dcube[3] == cube.Dcube['F'] and cube.Dcube[8] == cube.Dcube['L'] and cube.Dcube[12] == cube.Dcube['B'] == cube.Dcube[15]:
					cube.R()
					cube.U()
					cube.IR()
					cube.U()
					cube.R()
					cube.UU()
					cube.IR()

				#Cas S.2
				if cube.Dcube[1] == cube.Dcube['L'] and cube.Dcube[3] == cube.Dcube['F'] and cube.Dcube[8] == cube.Dcube['B'] and cube.Dcube[12] == cube.Dcube['R'] == cube.Dcube[15]:
					cube.UU()
					cube.R()
					cube.U()
					cube.IR()
					cube.U()
					cube.RR()
					cube.D()
					cube.IR()
					cube.UU()
					cube.R()
					cube.ID()
					cube.RR()

				#Cas S.3
				if cube.Dcube[1] == cube.Dcube['L'] and cube.Dcube[3] == cube.Dcube['B'] and cube.Dcube[8] == cube.Dcube['F'] and cube.Dcube[12] == cube.Dcube['R'] and cube.Dcube[15] == cube.Dcube['L']:
					cube.IU()
					cube.F()
					cube.IR()
					cube.UU()
					cube.R()
					cube.IF()
					cube.IR()
					cube.F()
					cube.UU()
					cube.IF()
					cube.R()

				#Cas S.4
				if cube.Dcube[1] == cube.Dcube['B'] and cube.Dcube[3] == cube.Dcube['F'] and cube.Dcube[8] == cube.Dcube['L'] and cube.Dcube[12] == cube.Dcube['R'] and cube.Dcube[15]== cube.Dcube['B']:
					cube.R()
					cube.IU()
					cube.IL()
					cube.U()
					cube.IR()
					cube.IU()
					cube.L()

				#Cas S.5
				if cube.Dcube[1] == cube.Dcube['F'] and cube.Dcube[3] == cube.Dcube['B'] and cube.Dcube[8] == cube.Dcube['L'] and cube.Dcube[12] == cube.Dcube['R'] and cube.Dcube[15]== cube.Dcube['B']:
					cube.R()
					cube.IL()
					cube.U()
					cube.IR()
					cube.IU()
					cube.L()
					cube.UU()
					cube.R()
					cube.UU()
					cube.IR()

				#Cas S.6
				if cube.Dcube[1] == cube.Dcube['F'] and cube.Dcube[3] == cube.Dcube['R'] and cube.Dcube[8] == cube.Dcube['B'] and cube.Dcube[12] == cube.Dcube['L'] and cube.Dcube[15] == cube.Dcube['R']:
					cube.UU()
					cube.R()
					cube.U()
					cube.IR()
					cube.U()
					cube.IL()
					cube.U()
					cube.R()
					cube.IU()
					cube.L()
					cube.UU()
					cube.IR()

			#Cas S'
			else:
				if cube.Dcube[9] != cube.Dcube['U']:
					for i in range(0,3):
						cube.FtoR()
				elif cube.Dcube[12] != cube.Dcube['U']:
					for i in range(0,2):
						cube.FtoR()
				elif cube.Dcube[15] != cube.Dcube['U']:
					cube.FtoR()


				#Cas S'.1
				if cube.Dcube[1] == cube.Dcube['F'] and cube.Dcube[6] == cube.Dcube['R'] and cube.Dcube[8] == cube.Dcube['B'] and cube.Dcube[14] == cube.Dcube[17] == cube.Dcube['L']:
					cube.R()
					cube.UU()
					cube.IR()
					cube.IU()
					cube.R()
					cube.IU()
					cube.IR()

				#Cas S'.2
				if cube.Dcube[1] == cube.Dcube['B'] and cube.Dcube[6] == cube.Dcube['F'] and cube.Dcube[8] == cube.Dcube['R'] and cube.Dcube[14]== cube.Dcube['B'] and cube.Dcube[17]==cube.Dcube['L']:
					cube.U()
					cube.IL()
					cube.U()
					cube.R()
					cube.IU()
					cube.L()
					cube.U()
					cube.IR()

				#Cas S'.3
				if cube.Dcube[1] == cube.Dcube['F'] and cube.Dcube[6] == cube.Dcube['B'] and cube.Dcube[8] == cube.Dcube['R'] and cube.Dcube[14]== cube.Dcube['B'] and cube.Dcube[17] == cube.Dcube['L']:
					cube.IU()
					cube.LL()
					cube.D()
					cube.IL()
					cube.UU()
					cube.L()
					cube.ID()
					cube.LL()
					cube.IU()
					cube.L()
					cube.IU()
					cube.IL()

				#Cas S'.4
				if cube.Dcube[1] == cube.Dcube['R'] and cube.Dcube[6] == cube.Dcube['F'] and cube.Dcube[8] == cube.Dcube['B'] and cube.Dcube[14]== cube.Dcube[17] == cube.Dcube['L']:
					cube.U()
					cube.R()
					cube.UU()
					cube.IR()
					cube.UU()
					cube.IL()
					cube.U()
					cube.R()
					cube.IU()
					cube.L()
					cube.IR()

				#Cas S'.5
				if cube.Dcube[1] == cube.Dcube['B'] and cube.Dcube[6] == cube.Dcube['L'] and cube.Dcube[8] == cube.Dcube['R'] and cube.Dcube[14] == cube.Dcube['B'] and cube.Dcube[17] == cube.Dcube['F']:
					cube.U()
					cube.IR()
					cube.F()
					cube.UU()
					cube.IF()
					cube.R()
					cube.F()
					cube.IR()
					cube.UU()
					cube.R()
					cube.IF()


				#Cas S'.6
				if cube.Dcube[1] == cube.Dcube['F'] and cube.Dcube[6] == cube.Dcube['L'] and cube.Dcube[8] == cube.Dcube['B'] and cube.Dcube[14]== cube.Dcube['L'] and cube.Dcube[17] == cube.Dcube['R']:
					cube.IU()
					cube.R()
					cube.UU()
					cube.IL()
					cube.U()
					cube.IR()
					cube.IU()
					cube.L()
					cube.IU()
					cube.R()
					cube.IU()
					cube.IR()

		if cube.Dcube[1] == cube.Dcube[3] == cube.Dcube[6] == cube.Dcube[8] == cube.Dcube['U'] and cube.Dcube['L'] == cube.Dcube[9] == cube.Dcube[11] and cube.Dcube['F'] == cube.Dcube[12] == cube.Dcube[14] and cube.Dcube['R'] == cube.Dcube[15] == cube.Dcube[17] and cube.Dcube['B'] == cube.Dcube[18] == cube.Dcube[20]:
			FinDeLetape = True
		else:
			cube.U()
			#Si le cas ne correspond à aucune configuration connue, on applique un U afin de tester d'autres orientations
		k +=1

def OrienterArreteFaceD(cube):

	i = 0
	cube.UtoF()
	cube.UtoR()
	cube.UtoF()
	cube.UtoF()
	cube.UtoF()
	while not cube.TestCubeResolu() and i <40: 
		
		if cube.Dcube[16]== cube.Dcube['B']:
			
			cube.RR()
			cube.IU()
			cube.IR()
			cube.IU()
			cube.R()
			cube.U()
			cube.R()
			cube.U()
			cube.R()
			cube.IU()
			cube.R()

		elif cube.Dcube[16]== cube.Dcube['L'] and cube.Dcube[19]== cube.Dcube['R']:
			
			cube.IR()
			cube.U()
			cube.IR()
			cube.IU()
			cube.IR()
			cube.IU()
			cube.IR()
			cube.U()
			cube.R()
			cube.U()
			cube.RR()

		elif cube.Dcube[16]== cube.Dcube['F'] and cube.Dcube[13]== cube.Dcube['R']:
			
			cube.U()
			cube.IR()
			cube.IU()
			cube.R()
			cube.IU()
			cube.R()
			cube.U()
			cube.R()
			cube.IU()
			cube.IR()
			cube.U()
			cube.R()
			cube.U()
			cube.RR()
			cube.IU()
			cube.IR()
			cube.U()


		elif cube.Dcube[16] == cube.Dcube['L'] and cube.Dcube[13] == cube.Dcube['B']:
			
			cube.LL()
			cube.RR()
			cube.D()
			cube.LL()
			cube.RR()
			cube.UU()
			cube.LL()
			cube.RR()
			cube.D()
			cube.LL()
			cube.RR()

		else : 
			cube.UtoF()
			cube.UtoR()
			cube.UtoF()
			cube.UtoF()
			cube.UtoF()
		i = i +1


def maximum(liste): #Renvoie l'indice du maximum d'une liste
	maximum = 0
	indice = 1 #Par defaut on est a 1 car on a pas a modifier le cube si aucun coin ne vaut mieux qu'un autre
	for i in range(0,len(liste)):
		if liste[i] > maximum:
			maximum = liste[i]
			indice = i

	return indice

def Cube222(cube):

	#On commence par orienter le cube de manière à ce que le coin le plus simple à résoudre soit en DBL
	#On défini chaque coin
	faceCoin1 = [cube.Dcube[1], cube.Dcube[46], cube.Dcube[3], cube.Dcube[48], cube.Dcube[6], cube.Dcube[41], cube.Dcube[8], cube.Dcube[43]]
	faceCoin2 = [cube.Dcube[20], cube.Dcube[40], cube.Dcube[18], cube.Dcube[38], cube.Dcube[12], cube.Dcube[32], cube.Dcube[14], cube.Dcube[34]]
	faceCoin3 = [cube.Dcube[9], cube.Dcube[29], cube.Dcube[17], cube.Dcube[37],cube.Dcube[11], cube.Dcube[31], cube.Dcube[15], cube.Dcube[35]]
	checkCoin = [['U','L','B'],['D','L','B'],['U','R','B'],['D','R','B'],['U','L','F'],['D','L','F'],['U','R','F'],['D','R','F']]
	
	#On défini les arrêtes
	faceArrete11 = [cube.Dcube[10], cube.Dcube[5], cube.Dcube[36], cube.Dcube[44]]
	faceArrete12 = [cube.Dcube[4], cube.Dcube[16], cube.Dcube[45], cube.Dcube[30]]
	checkArrete1 = [['L','U'],['U','R'],['R','D'],['D','L']]

	faceArrete21 = [cube.Dcube[21], cube.Dcube[23], cube.Dcube[25], cube.Dcube[27]]
	faceArrete22 = [cube.Dcube[28], cube.Dcube[22], cube.Dcube[24], cube.Dcube[26]]
	checkArrete2 = [['L','B'],['F','L'],['R','F'],['B','R']]

	faceArrete31 = [cube.Dcube[2], cube.Dcube[13], cube.Dcube[42], cube.Dcube[39]]
	faceArrete32 = [cube.Dcube[19], cube.Dcube[7], cube.Dcube[33], cube.Dcube[47]]
	checkArrete3 = [['U','B'],['F','U'],['D','F'],['B','D']]

	#On initialise le compte qui choisi quel est le meilleur coin pour commencer
	#L'indice nous donne le coin (équivalent à la liste CheckCoin)
	#Plus la valeur est élevé, plus il est intéressant de commencer par ce coin
	compte =[]

	#On vérifie les coins bien placé. Ils valent 1.5
	for i in range(0,len(faceCoin1)):
		compte.append(0)
		if faceCoin1[i] == cube.Dcube[checkCoin[i][0]] and faceCoin2[i] == cube.Dcube[checkCoin[i][2]] and faceCoin3[i] == cube.Dcube[checkCoin[i][1]]:
			compte[i] += 1.5

	for i in range(0,4):
		if faceArrete11[i] == cube.Dcube[checkArrete1[i][0]] and faceArrete12[i] == cube.Dcube[checkArrete1[i][1]]:
			if i == 0:
				compte[0] +=1
				compte[4] +=1
			if i == 1:
				compte[2] +=1
				compte[6] +=1
			if i == 2:
				compte[3] +=1
				compte[7] +=1
			if i == 3:
				compte[1] +=1
				compte[5] +=1

	for i in range(0,4):
		if faceArrete21[i] == cube.Dcube[checkArrete2[i][0]] and faceArrete22[i] == cube.Dcube[checkArrete2[i][1]]:
			if i == 0:
				compte[0] +=1
				compte[1] +=1
			if i == 1:
				compte[4] +=1
				compte[5] +=1
			if i == 2:
				compte[6] +=1
				compte[7] +=1
			if i == 3:
				compte[2] +=1
				compte[3] +=1

	for i in range(0,4):
		if faceArrete31[i] == cube.Dcube[checkArrete3[i][0]] and faceArrete32[i] == cube.Dcube[checkArrete3[i][1]]:
			if i == 0:
				compte[0] +=1
				compte[2] +=1
			if i == 1:
				compte[4] +=1
				compte[6] +=1
			if i == 2:
				compte[5] +=1
				compte[7] +=1
			if i == 3:
				compte[1] +=1
				compte[3] +=1

	indiceCoinMaximum = maximum(compte)

	if indiceCoinMaximum == 0:
		for i in range(0,3):
			cube.UtoR()
	elif indiceCoinMaximum == 2:
		for i in range(0,2):
			cube.UtoR()
	elif indiceCoinMaximum == 3:
		cube.UtoR()
	elif indiceCoinMaximum == 4:
		pass
		cube.UtoR()
		cube.FtoR()
		cube.UtoR()
		cube.FtoR()
	elif indiceCoinMaximum == 5:
		for i in range(0,3):
			cube.FtoR()
	elif indiceCoinMaximum == 6:
		cube.UtoR()
		cube.FtoR()
		cube.FtoR()
	elif indiceCoinMaximum == 7:
		cube.FtoR()
		cube.FtoR()



	#on commencera toujours avec le coin LBD pour l'instant pour des soucis de complexité
	#les pièces importantes sont : 28,B,21,L,39,40,29,30,44,D,46,47
	#on commence par vérifier si le cube 222 est déjà formé
	if TestCube222(cube):
		# print("Cube222 ok en BLD")
		pass
	#il faut vérifier s'il y a des paires coin milieu déjà formées
	#on crée un dictionnaire avec les pièces intéressantes
	#les pièces sont stockées avec les vignettes du plus haut vers le plus bas, rotation horaire ex: UBL : 1 20 9
	cpiece={}
	#liste des coins :UBL,URB,ULF,UFR
	cpiece['ULB']=[cube.Dcube[1],cube.Dcube[9],cube.Dcube[20]]
	cpiece['UBR']=[cube.Dcube[3],cube.Dcube[18],cube.Dcube[17]]
	cpiece['UFL']=[cube.Dcube[6],cube.Dcube[12],cube.Dcube[11]]
	cpiece['URF']=[cube.Dcube[8],cube.Dcube[15],cube.Dcube[14]]
	#liste des coins BLD,RBD,LFD,RFD
	cpiece['LBD']=[cube.Dcube[29],cube.Dcube[40],cube.Dcube[46]]
	cpiece['BRD']=[cube.Dcube[38],cube.Dcube[37],cube.Dcube[48]]
	cpiece['FLD']=[cube.Dcube[32],cube.Dcube[31],cube.Dcube[41]]
	cpiece['RFD']=[cube.Dcube[35],cube.Dcube[34],cube.Dcube[43]]
	#arêtes dans l'ordre de haut en bas rotation horaire
	cpiece['UL']=[cube.Dcube[4],cube.Dcube[10]]
	cpiece['UB']=[cube.Dcube[2],cube.Dcube[19]]
	cpiece['UR']=[cube.Dcube[5],cube.Dcube[16]]
	cpiece['UF']=[cube.Dcube[7],cube.Dcube[13]]
	
	cpiece['LB']=[cube.Dcube[21],cube.Dcube[28]]		
	cpiece['BR']=[cube.Dcube[27],cube.Dcube[26]]
	cpiece['RF']=[cube.Dcube[25],cube.Dcube[24]]
	cpiece['FL']=[cube.Dcube[23],cube.Dcube[22]]
	
	cpiece['LD']=[cube.Dcube[30],cube.Dcube[44]]
	cpiece['BD']=[cube.Dcube[39],cube.Dcube[47]]
	cpiece['RD']=[cube.Dcube[36],cube.Dcube[45]]
	cpiece['FD']=[cube.Dcube[33],cube.Dcube[42]]

	listearetes=[cpiece['UL'],cpiece['LB'],cpiece['UB'],cpiece['BR'],cpiece['UR'],cpiece['RF'],cpiece['UF'],cpiece['FL'],cpiece['UL'],cpiece['FD'],cpiece['FL'],cpiece['LD'],cpiece['LB'],cpiece['BD'],cpiece['BR'],cpiece['RD'],cpiece['RF'],cpiece['FD']]
	listecoins=[cpiece['ULB'],cpiece['UBR'],cpiece['URF'],cpiece['UFL'],cpiece['FLD'],cpiece['LBD'],cpiece['BRD'],cpiece['RFD']]


	


	#Cette partie permet de déterminer dans un premier temps si un coin est déjà bien placé, afin de l'utiliser comme base
	couleursULB = [cube.Dcube['U'],cube.Dcube['L'],cube.Dcube['B']]
	couleursUBR = [cube.Dcube['U'],cube.Dcube['B'],cube.Dcube['R']]
	couleursURF = [cube.Dcube['U'],cube.Dcube['R'],cube.Dcube['F']]
	couleursUFL = [cube.Dcube['U'],cube.Dcube['F'],cube.Dcube['L']]
	couleursLBD = [cube.Dcube['L'],cube.Dcube['B'],cube.Dcube['D']]
	couleursBDR = [cube.Dcube['B'],cube.Dcube['D'],cube.Dcube['R']]
	couleursFRD = [cube.Dcube['F'],cube.Dcube['R'],cube.Dcube['D']]
	couleursFLD = [cube.Dcube['F'],cube.Dcube['L'],cube.Dcube['D']]

	#Coin ULB
	if cube.Dcube[9] in couleursULB and cube.Dcube[1] in couleursULB and cube.Dcube[20] in couleursULB:
		cube.UtoF()
		cube.UtoF()
		cube.UtoF()
	#Coin UBR
	elif cube.Dcube[3] in couleursUBR and cube.Dcube[17] in couleursUBR and cube.Dcube[18] in couleursUBR:
		cube.UtoR()
		cube.UtoR()
	#Coin URF
	elif cube.Dcube[8] in couleursURF and cube.Dcube[14] in couleursURF and cube.Dcube[15] in couleursURF:
		cube.UtoR()
		cube.UtoR()
		cube.UtoF()
	#Coin UFL
	elif cube.Dcube[6] in couleursUFL and cube.Dcube[11] in couleursUFL and cube.Dcube[12] in couleursUFL:
		cube.UtoF()
		cube.UtoF()

	#Coins de la face DOWN
	#Coin LBD (bien placé)
	elif cube.Dcube[29] in couleursLBD and cube.Dcube[40] in couleursLBD and cube.Dcube[46] in couleursLBD:
		pass
	#Coin BDR
	elif cube.Dcube[48] in couleursBDR and cube.Dcube[37] in couleursBDR and cube.Dcube[38] in couleursBDR:
		cube.UtoR()
	#Coin FRD
	elif cube.Dcube[43] in couleursFRD and cube.Dcube[34] in couleursFRD and cube.Dcube[35] in couleursFRD:
		cube.UtoR()
		cube.UtoF()
	#Coin FLD
	elif cube.Dcube[31] in couleursFLD and cube.Dcube[32] in couleursFLD and cube.Dcube[41] in couleursFLD:
		cube.UtoF()
	#Si aucun coin n'est bien positionné, dans ce cas on doit chercher le coin à positionner en LBD parmis les 8 possibles 
	else:
		#Cette partie permet de mettre en place le bon coin LBD dans la bonne orientation, si aucun coin n'est placé au bon endroit
		#On déclare un tableau contenant les couleurs des faces L,B et D par souci de simplification de vérification
		couleursLBD = [cube.Dcube['L'],cube.Dcube['B'],cube.Dcube['D']]

		#Il y a 8 coins sur le cube
		#On teste chaque coin pour repérer celui qui correspond à la face LBD grace à une série de if
		#On le place simplement dans un premier temps (peu importe l'orientation)


		#Coins de la face UP
		#Coin ULB
		if cube.Dcube[9] in couleursLBD and cube.Dcube[1] in couleursLBD and cube.Dcube[20] in couleursLBD:
			cube.B()
		#Coin UBR
		elif cube.Dcube[3] in couleursLBD and cube.Dcube[17] in couleursLBD and cube.Dcube[18] in couleursLBD:
			cube.BB()
		#Coin URF
		elif cube.Dcube[8] in couleursLBD and cube.Dcube[14] in couleursLBD and cube.Dcube[15] in couleursLBD:
			cube.UU()
			cube.B()
		#Coin UFL
		elif cube.Dcube[6] in couleursLBD and cube.Dcube[11] in couleursLBD and cube.Dcube[12] in couleursLBD:
			cube.U()
			cube.B()

		#Coins de la face DOWN (moins le coin LBD, qui on sait n'est pas le bon)
		#Coin BDR
		elif cube.Dcube[48] in couleursLBD and cube.Dcube[37] in couleursLBD and cube.Dcube[38] in couleursLBD:
			cube.D()
		#Coin FRD
		elif cube.Dcube[43] in couleursLBD and cube.Dcube[34] in couleursLBD and cube.Dcube[35] in couleursLBD:
			cube.DD()
		#Coin FLD
		elif cube.Dcube[31] in couleursLBD and cube.Dcube[32] in couleursLBD and cube.Dcube[41] in couleursLBD:
			cube.ID()

	#On oriente le cube grâce à la fonction OrienterLBD()
	OrienterLBD(cube)

	#A ce niveau là le coin LBD est en place"
	#On cherche à positionner les pièces LD et BD"
	#Faisons LD en premier, on veut se mettre dans une configuration dans laquelle l'endroit où on veut placer l'arête soit sur la deuxième courrone face F"
	
	#A ce niveau là le coin LBD est en place"
	#On cherche à positionner les pièces LD , LB et BD"
	# "Faisons LD en premier, on veut se mettre dans une configuration dans laquelle l'endroit où on veut placer l'arête soit sur la deuxième courrone face F"
	cube.UtoF()
	cube.UtoF()
	cube.UtoF()
	PlaceEdge(cube)
	#"LD est placée"
	cube.UtoR()
	cube.UtoF()
	PlaceEdge(cube)
	#"LB est placée"
	cube.UtoR()
	cube.UtoF()
	PlaceEdge(cube)
	cube.UtoF()

	
def PlaceEdge(cube):
		
	if cube.Dcube[22]==cube.Dcube['F'] and cube.Dcube[23]==cube.Dcube['L']:
		# "A sa place mais mal orienté"
		cube.DD()
		cube.F()
		cube.U()
		cube.L()
		cube.DD()
		return
	areteU=[cube.Dcube[2],cube.Dcube[19],cube.Dcube[5],cube.Dcube[16],cube.Dcube[7],cube.Dcube[13],cube.Dcube[4],cube.Dcube[10]]
	areteB=[cube.Dcube[28],cube.Dcube[21],cube.Dcube[27],cube.Dcube[26],cube.Dcube[39],cube.Dcube[47]]
	areteR=[cube.Dcube[24],cube.Dcube[25],cube.Dcube[36],cube.Dcube[45]]
	couleursFL=[cube.Dcube['F'],cube.Dcube['L']]
	for i in (0,2,4,6):
		if (areteU[i]==cube.Dcube['L'] and areteU[i+1]==cube.Dcube['F']) or (areteU[i+1]==cube.Dcube['L'] and areteU[i]==cube.Dcube['F']):
			if EdgeOnU(cube,i):
				return
	for i in (0,2,4):
		if (areteB[i]==cube.Dcube['L'] and areteB[i+1]==cube.Dcube['F']) or (areteB[i+1]==cube.Dcube['L'] and areteB[i]==cube.Dcube['F']):

			if i==0:
				if cube.Dcube[21]==cube.Dcube['L']:
					cube.D()
					cube.LL()
					cube.ID()
					return
				else:
					cube.IB()
					if EdgeOnU(cube,0):
						return
			elif i==2:
				if cube.Dcube[27]==cube.Dcube['F']:
					cube.RR()
					cube.ID()
					cube.FF()
					cube.D()
					return
				else:
					cube.B()
					if EdgeOnU(cube,0):
						return
			elif i==4:
				if cube.Dcube[39]==cube.Dcube['F']:
					cube.IB()
					cube.D()
					cube.LL()
					cube.ID()
					return
				else:
					cube.BB()
					if EdgeOnU(cube,0):
						return

	for i in (0,2):
		if (areteR[i]==cube.Dcube['L'] and areteR[i+1]==cube.Dcube['F']) or (areteR[i+1]==cube.Dcube['L'] and areteR[i]==cube.Dcube['F']):

			if i==0:
				if cube.Dcube[24]==cube.Dcube['F']:
					cube.ID()
					cube.FF()
					cube.D()
					return
				if cube.Dcube[24]==cube.Dcube['L']:
					cube.R()
					if EdgeOnU(cube,2):
						return

				
			if i==2:
				if cube.Dcube[45]==cube.Dcube['F']:
					cube.R()
					cube.ID()
					cube.FF()
					cube.D()
					return
				else:
					cube.RR()
					if EdgeOnU(cube,2):
						return
	if cube.Dcube[33] in couleursFL and cube.Dcube[42] in couleursFL:
		cube.L()
		cube.FF()
		cube.IL()
		if EdgeOnU(cube,4):
			return
	elif cube.Dcube[30] in couleursFL and cube.Dcube[44] in couleursFL:
		cube.IF()
		cube.LL()
		cube.F()
		if EdgeOnU(cube,6):
			return
	return






def EdgeOnU(cube,i):
	"Place l'arete en FL a partir de la face U"
	if i==6 and cube.Dcube[10]==cube.Dcube['L']:
		LBelge(cube)
		return True
	elif i==6 and cube.Dcube[10]==cube.Dcube['F']: 
		cube.IU()
		FBelge(cube)
		return True
	elif i==0 and cube.Dcube[19]==cube.Dcube['L']:
		cube.IU()
		LBelge(cube)
		return True
	elif i==0 and cube.Dcube[19]==cube.Dcube['F']:
		cube.UU()
		FBelge(cube)
		return True
	elif i==2 and cube.Dcube[16]==cube.Dcube['L']:
		cube.UU()
		LBelge(cube)
		return True
	elif i==2 and cube.Dcube[16]==cube.Dcube['F']:
		cube.U()
		FBelge(cube)
		return True
	elif i==4 and cube.Dcube[13]==cube.Dcube['L']:
		cube.U()
		LBelge(cube)
		return True
	elif i==4 and cube.Dcube[13]==cube.Dcube['F']:
		FBelge(cube)
		return True
	else : 
		return False

def LBelge(cube):
	cube.DD()
	cube.L()
	cube.DD()
def FBelge(cube):
	cube.DD()
	cube.IF()
	cube.DD()

def OrienterLBD(cube):
	if cube.Dcube[29]!=cube.Dcube['L']: 

		# "le cube n'est pas bien orienté"
		if cube.Dcube[29]==cube.Dcube['B']:
			cube.LL()
			cube.IF()
			cube.L()
		elif cube.Dcube[29]==cube.Dcube['D']:
			cube.IB()
			cube.L()
			cube.IF()
			cube.L()

def TestCube222(cube):
	if cube.Dcube[21]==cube.Dcube[29]==cube.Dcube[30]==cube.Dcube['L'] and cube.Dcube[28]==cube.Dcube[39]==cube.Dcube[40]==cube.Dcube['B'] and cube.Dcube[44]==cube.Dcube[46]==cube.Dcube[47]==cube.Dcube['D']:
		return True
	else:
		return False

def compterAretesMalOrientees(cube):
	#Cette fonction renvoie le nombre d'arêtes bien placées mais mal orientées sur le cube
	nbAretesNonOK = 0

	#FU
	if cube.Dcube[7] == cube.Dcube['F']:
		nbAretesNonOK += 1
	elif cube.Dcube[13] == cube.Dcube['U']:
		nbAretesNonOK += 1
	#UB
	if cube.Dcube[2] == cube.Dcube['F']:
		nbAretesNonOK += 1
	elif cube.Dcube[19] == cube.Dcube['U']:
		nbAretesNonOK += 1
	#UL
	if cube.Dcube[4] == cube.Dcube['F']:
		nbAretesNonOK += 1
	elif cube.Dcube[10] == cube.Dcube['U']:
		nbAretesNonOK += 1
	#UR
	if cube.Dcube[5] == cube.Dcube['F']:
		nbAretesNonOK += 1
	elif cube.Dcube[16] == cube.Dcube['U']:
		nbAretesNonOK += 1
	#FD
	if cube.Dcube[42] == cube.Dcube['F']:
		nbAretesNonOK += 1
	elif cube.Dcube[33] == cube.Dcube['U']:
		nbAretesNonOK += 1
	#FR
	if cube.Dcube[25] == cube.Dcube['F']:
		nbAretesNonOK += 1
	elif cube.Dcube[24] == cube.Dcube['U']:
		nbAretesNonOK += 1
	#FL
	if cube.Dcube[22] == cube.Dcube['F']:
		nbAretesNonOK += 1
	elif cube.Dcube[23] == cube.Dcube['U']:
		nbAretesNonOK += 1

	return nbAretesNonOK


#Fonction qui fait l'étape 4 de Petrus
#Elle va compléter les 2 couronnes du bas
def etape4(cube):
		#Etape 4.1 --> Cette sous étape va faire un cube 2*2*1 sur une face qui n'a pas été résolu
		
		#On positionne notre cube
		cube.UtoR()
		cube.UtoF()
		cube.UtoR()
		cube.UtoR()
		cube.UtoR()
		
		#On va positionner l'arête R-D correctement et on n'y retouche pas par la suite
		if cube.Dcube[16] == cube.Dcube['R'] and cube.Dcube[5] == cube.Dcube['D']:
				cube.IR()
		elif cube.Dcube[26] == cube.Dcube['R'] and cube.Dcube[27] == cube.Dcube['D']:
				cube.RR()
		elif cube.Dcube[36] == cube.Dcube['R'] and cube.Dcube[45] == cube.Dcube['D']:
				cube.R()
		elif cube.Dcube[19] == cube.Dcube['R'] and cube.Dcube[2] == cube.Dcube['D']:
				cube.U()
				cube.IR()
		elif cube.Dcube[13] == cube.Dcube['R'] and cube.Dcube[7] == cube.Dcube['D']:
				cube.IU()
				cube.IR()
		elif cube.Dcube[10] == cube.Dcube['R'] and cube.Dcube[4] == cube.Dcube['D']:
				cube.UU()
				cube.IR()
				
		#On va positionner l'arête R-F correctement et on n'y retouche pas par la suite
		if cube.Dcube[10] == cube.Dcube['R'] and cube.Dcube[4] == cube.Dcube['F']:
				cube.UU()
		elif cube.Dcube[13] == cube.Dcube['R'] and cube.Dcube[7] == cube.Dcube['F']:
				cube.IU()
		elif cube.Dcube[19] == cube.Dcube['R'] and cube.Dcube[2] == cube.Dcube['F']:
				cube.U()
		elif cube.Dcube[26] == cube.Dcube['R'] and cube.Dcube[27] == cube.Dcube['F']:
				cube.IR()
				cube.U()
				cube.R()
				cube.IU()
		elif cube.Dcube[36] == cube.Dcube['R'] and cube.Dcube[45] == cube.Dcube['F']:
				cube.RR()
				cube.U()
				cube.RR()
				cube.IU()
		cube.IR()

		coin, arete = emplacementCoinArete(cube)
		if(len(coin) != 0 and len(arete) != 0):
		#On effectue un des cas PF2L
			PF2L(cube)
		#Etape 4.2 --> Après avoir obtenue le cube 2*2*1, on va compléter les deux couronnes du bas
		#Pour cela on va positionner le cube
		cube.UtoF()
		cube.UtoR()
		cube.UtoF()
		cube.UtoF()
		cube.UtoF()
		coin, arete = emplacementCoinArete(cube)
		if(len(coin) != 0 and len(arete) != 0):
		#et appliquer une nouvelle fois un des cas PF2L
			PF2L(cube)


#Fonction qui regroupe la liste des F2L mais en utilisant que deux types de rotation --> PF2L
def PF2L(cube):
		#On recupere le coin et l'arête qu'on veux positionner
	coin, arete = emplacementCoinArete(cube)
	#Selon où est le coin, on va le placer dans une position qui va correspondre à un des cas PF2L
	#(si le coin est en F-R-D on le laisse, sinon on le met en F-R-U)
	if (coin[0] == 18 or coin[0] ==  9  or coin[0] == 12 or coin[0] == 34 or coin[0] == 37):
		if coin[0] == 18 or (coin[0] == 34 and arete[0] == 5):
			cube.U()
		elif coin[0] ==  9 or (coin[0] == 34 and arete[0] == 2):
			cube.UU()
		elif coin[0] ==  12 or (coin[0] == 34 and arete[0] == 4):
			cube.IU()
		elif coin[0] == 12 and arete[0] == 45:
			cube.R()
			cube.IU()
		elif coin[0] == 37:
			cube.IR()
			cube.UU()
			cube.R()
			cube.IU()
	#On recupère encore une fois les positions car le cube a pu être bouger
	coin, arete = emplacementCoinArete(cube)
		#La liste des cas en PF2L
	
		#Le coin est en F-R-D et l'arête est en F-R
	#Ensuite on regarde l'orientation du coin
	if(coin[0] == 34) and (arete[0] == 24):
		if cube.Dcube[34]==cube.Dcube['R']:
			cube.IF()
			cube.IF()
			cube.UU()
			cube.F()
			cube.U()
			cube.IF()
			cube.U()
			cube.F()
			cube.IU()
			cube.IU()
			cube.F()
		elif cube.Dcube[34]==cube.Dcube['D']:
			cube.IF()
			cube.UU()
			cube.IF()
			cube.IU()
			cube.F()
			cube.IU()
			cube.IF()
			cube.UU()
			cube.FF()
			
	#Le coin est en F-R-D et l'arête est en F-U
	#Ensuite on regarde l'orientation du coin
	elif(coin[0] == 34) and (arete[0] == 13):
		if cube.Dcube[34]==cube.Dcube['R']:
			cube.IF()
			cube.U()
			cube.F()
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()
		elif cube.Dcube[34]==cube.Dcube['D']:
			cube.IF()
			cube.IU()
			cube.F()
			cube.U()
			cube.IF()
			cube.IU()
			cube.F()
		elif cube.Dcube[34]==cube.Dcube['F']:
			cube.IF()
			cube.U()
			cube.F()
			cube.U()
			cube.IF()
			cube.U()
			cube.F()
			cube.IU()
			cube.IF()
			cube.IU()
			cube.F()
	#Le coin est en F-R-U et l'arête est en F-R
	#Ensuite on regarde l'orientation du coin
	elif(coin[0] == 14) and (arete[0] == 24):
		if cube.Dcube[14]==cube.Dcube['R']:
			cube.U()
			cube.IF()
			cube.U()
			cube.F()
			cube.IU()
			cube.IF()
			cube.UU()
			cube.F()
			cube.U()
			cube.IF()
			cube.IU()
			cube.F()
		elif cube.Dcube[14]==cube.Dcube['D']:
			cube.U()
			cube.IF()
			cube.UU()
			cube.F()
			cube.IU()
			cube.IF()
			cube.IU()
			cube.F()
		elif cube.Dcube[14]==cube.Dcube['F']:
			cube.U()
			cube.IF()
			cube.U()
			cube.F()
			cube.IU()
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()

	#Le coin est en F-R-U et l'arête est en F-U
	#Ensuite on regarde l'orientation du coin
	elif(coin[0] == 14) and (arete[0] == 13):
		if cube.Dcube[14]==cube.Dcube['R']:
			cube.IF()
			cube.UU()
			cube.F()
			cube.U()
			cube.IF()
			cube.IU()
			cube.F()
		elif cube.Dcube[14]==cube.Dcube['D']:
			cube.U()
			cube.IF()
			cube.U()
			cube.F()
			cube.IU()
			cube.IF()
			cube.IU()
			cube.F()
		elif cube.Dcube[14]==cube.Dcube['F']:
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()

	#Le coin est en F-R-U et l'arête est en L-U
	#Ensuite on regarde l'orientation du coin
	elif(coin[0] == 14) and (arete[0] == 4):
		if cube.Dcube[14]==cube.Dcube['R']:
			cube.IU()
			cube.IF()
			cube.UU()
			cube.F()
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()
		elif cube.Dcube[14]==cube.Dcube['D']:
			cube.IF()
			cube.IU()
			cube.F()
		elif cube.Dcube[14]==cube.Dcube['F']:
			cube.U()
			cube.IF()
			cube.IU()
			cube.F()
			cube.IU()
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()
			
	#Le coin est en F-R-U et l'arête est en B-U
	#Ensuite on regarde l'orientation du coin
	elif(coin[0] == 14) and (arete[0] == 2):
		if cube.Dcube[14]==cube.Dcube['R']:
			cube.UU()
			cube.IF()
			cube.IU()
			cube.F()
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()
		elif cube.Dcube[14]==cube.Dcube['D']:
			cube.U()
			cube.IF()
			cube.IU()
			cube.F()
			cube.IU()
			cube.IF()
			cube.IU()
			cube.F()
		elif cube.Dcube[14]==cube.Dcube['F']:
			cube.U()
			cube.IF()
			cube.UU()
			cube.F()
			cube.IU()
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()
			
	#Le coin est en F-R-U et l'arête est en R-U
	#Ensuite on regarde l'orientation du coin
	elif(coin[0] == 14) and (arete[0] == 5):
		if cube.Dcube[14]==cube.Dcube['R']:
			cube.UU()
			cube.IF()
			cube.IF()
			cube.UU()
			cube.F()
			cube.U()
			cube.IF()
			cube.U()
			cube.FF()
		elif cube.Dcube[14]==cube.Dcube['D']:
			cube.F()
			cube.IU()
			cube.IU()
			cube.FF()
			cube.IU()
			cube.FF()
			cube.IU()
			cube.IF()
		elif cube.Dcube[14]==cube.Dcube['F']:
			cube.IF()
			cube.UU()
			cube.F()
			cube.IU()
			cube.IF()
			cube.IU()
			cube.F()
			cube.IU()
			cube.IF()
			cube.U()
			cube.F()
		

#Fonction qui permet de savoir les positions du coin et de l'arête qu'on veux possitionner correctement
def emplacementCoinArete(cube):
		#On regarde où est le coin
	posCoin = []
	if((cube.Dcube[34]==cube.Dcube['F'] or cube.Dcube[34]==cube.Dcube['R'] or cube.Dcube[34]==cube.Dcube['D']) and (cube.Dcube[35]==cube.Dcube['F'] or cube.Dcube[35]==cube.Dcube['R'] or cube.Dcube[35]==cube.Dcube['D']) and (cube.Dcube[43]==cube.Dcube['F'] or cube.Dcube[43]==cube.Dcube['R'] or cube.Dcube[43]==cube.Dcube['D'])):
			posCoin = [34,35,43]
	elif((cube.Dcube[14]==cube.Dcube['F'] or cube.Dcube[14]==cube.Dcube['R'] or cube.Dcube[14]==cube.Dcube['D']) and (cube.Dcube[15]==cube.Dcube['F'] or cube.Dcube[15]==cube.Dcube['R'] or cube.Dcube[15]==cube.Dcube['D']) and (cube.Dcube[8]==cube.Dcube['F'] or cube.Dcube[8]==cube.Dcube['R'] or cube.Dcube[8]==cube.Dcube['D'])):
			posCoin = [14,15,8]
	elif((cube.Dcube[12]==cube.Dcube['F'] or cube.Dcube[12]==cube.Dcube['R'] or cube.Dcube[12]==cube.Dcube['D']) and (cube.Dcube[11]==cube.Dcube['F'] or cube.Dcube[11]==cube.Dcube['R'] or cube.Dcube[11]==cube.Dcube['D']) and (cube.Dcube[6]==cube.Dcube['F'] or cube.Dcube[6]==cube.Dcube['R'] or cube.Dcube[6]==cube.Dcube['D'])):
			posCoin = [12,11,6]
	elif((cube.Dcube[9]==cube.Dcube['F'] or cube.Dcube[9]==cube.Dcube['R'] or cube.Dcube[9]==cube.Dcube['D']) and (cube.Dcube[20]==cube.Dcube['F'] or cube.Dcube[20]==cube.Dcube['R'] or cube.Dcube[20]==cube.Dcube['D']) and (cube.Dcube[1]==cube.Dcube['F'] or cube.Dcube[1]==cube.Dcube['R'] or cube.Dcube[1]==cube.Dcube['D'])):
			posCoin = [9,20,1]
	elif((cube.Dcube[18]==cube.Dcube['F'] or cube.Dcube[18]==cube.Dcube['R'] or cube.Dcube[18]==cube.Dcube['D']) and (cube.Dcube[17]==cube.Dcube['F'] or cube.Dcube[17]==cube.Dcube['R'] or cube.Dcube[17]==cube.Dcube['D']) and (cube.Dcube[3]==cube.Dcube['F'] or cube.Dcube[3]==cube.Dcube['R'] or cube.Dcube[3]==cube.Dcube['D'])):
			posCoin = [18,17,3]
	elif((cube.Dcube[37]==cube.Dcube['F'] or cube.Dcube[37]==cube.Dcube['R'] or cube.Dcube[37]==cube.Dcube['D']) and (cube.Dcube[38]==cube.Dcube['F'] or cube.Dcube[38]==cube.Dcube['R'] or cube.Dcube[38]==cube.Dcube['D']) and (cube.Dcube[48]==cube.Dcube['F'] or cube.Dcube[48]==cube.Dcube['R'] or cube.Dcube[48]==cube.Dcube['D'])):
			posCoin = [37,38,48]
	#On regarde où est l'arête
	posArete = []
	if((cube.Dcube[24]==cube.Dcube['F'] or cube.Dcube[24]==cube.Dcube['R']) and (cube.Dcube[25]==cube.Dcube['F'] or cube.Dcube[25]==cube.Dcube['R'])):
			posArete = [24,25]
	elif((cube.Dcube[13]==cube.Dcube['F'] or cube.Dcube[13]==cube.Dcube['R']) and (cube.Dcube[7]==cube.Dcube['F'] or cube.Dcube[7]==cube.Dcube['R'])):
			posArete = [13,7]
	elif((cube.Dcube[4]==cube.Dcube['F'] or cube.Dcube[4]==cube.Dcube['R']) and (cube.Dcube[10]==cube.Dcube['F'] or cube.Dcube[10]==cube.Dcube['R'])):
			posArete = [4,10]
	elif((cube.Dcube[2]==cube.Dcube['F'] or cube.Dcube[2]==cube.Dcube['R']) and (cube.Dcube[19]==cube.Dcube['F'] or cube.Dcube[19]==cube.Dcube['R'])):
			posArete = [2,19]
	elif((cube.Dcube[5]==cube.Dcube['F'] or cube.Dcube[5]==cube.Dcube['R']) and (cube.Dcube[16]==cube.Dcube['F'] or cube.Dcube[16]==cube.Dcube['R'])):
			posArete = [5,16]
	elif((cube.Dcube[45]==cube.Dcube['F'] or cube.Dcube[45]==cube.Dcube['R']) and (cube.Dcube[36]==cube.Dcube['F'] or cube.Dcube[36]==cube.Dcube['R'])):
			posArete = [45,36]
	elif((cube.Dcube[26]==cube.Dcube['F'] or cube.Dcube[26]==cube.Dcube['R']) and (cube.Dcube[27]==cube.Dcube['F'] or cube.Dcube[27]==cube.Dcube['R'])):
			posArete = [26,27]
		#On retourne les positions
	return posCoin, posArete

# def EdgeCornerOrientation(num_coin,num_arete,face):
# 	# num_coin correspond à la place du coin dans la liste listecoins
# 	#num_arete correspond à la place de l'arete dans la liste listearete. Elle peut être bien oritentée ou mal orientée par rapport au coin. Elle est aussi senséé être à côté du coin
# 	if face=='U':
# 		if listearetes[num_arete][]





#--------------------------------------------------------------------------------------

def ResoudrePetrusE(cube): #Ne pas modifier
	#Cette fonction résoud le cube en affichant chaque etape
	#Sert notamment au debuggage
	print("etat initial")
	cube.afficher2D()
	Cube222(cube)
	print("etape 1")
	cube.afficher2D()
	step2(cube)
	print("etape 2")
	cube.afficher2D()
	etape3(cube)
	print("etape 3")
	cube.afficher2D()
	etape4(cube)
	print("etape 4")
	cube.afficher2D()
	CoinsFaceD(cube)
	print("etape 5")
	cube.afficher2D()
	OrienterArreteFaceD(cube)
	print("etape 6")
	cube.afficher2D()


def ResoudrePetrus(cube): #Ne pas Modifier
	#Fonction principale de resolution de cube
	if type(cube) == str:
		cube = Rubik(cube)
	Cube222(cube)
	step2(cube)
	etape3(cube)
	etape4(cube)
	CoinsFaceD(cube)
	OrienterArreteFaceD(cube)
	cube.Simplifier()
	cube.solChaine()
	# if cube.TestCubeResolu():
	# 	print("cube resolu en "+str(len(cube.solve))+" mouvements")
	return cube.solve


def StockageErreurs(n=1000): 
	#Cette fonction tente de résoudre N cubes mélangés aléatoirement. A chaque erreur rencontrées, on stocke le du cube en question dans un fichier txt
	minimum = 1000
	maximum = 0
	moyenne = 0
	cube=Rubik()
	cube.Scramble()
	Fichier = open("CubePetrus.txt",'a')
	tmp = ''
	Erreur =0
	for i in range(0,n):
		cube.Scramble()
		tmp = str(cube.Dcube)
		ResoudrePetrus(cube)
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




def ChoixPetrus(cube):#cette fonction choisi l'orientation du cube qui est optimale pour la résolution
	i = 0 
	eInit = cube.chaine# on recupere la chaine pour créer un cube de test
	listeO = ['','r','f','rr','rf','fr','ff','rrr','rrf','rfr','rff','frr','ffr','fff','rrrf','rrfr','rrff','rfrr','rfff','frrr','fffr','frrrf','frfrr','frfff']
	longueur=[]
	mini = 1000
	
	while i < 24 :
		cubeTest = Rubik(eInit)#creation du cube de test 

		for j in range (0,len(listeO[i])):# on parcours la liste des orientation possible
			if listeO[i][j]== 'r' :# on appplique l'orientation qui nous interesse 
				cubeTest.UtoR()
			elif listeO[i][j] == 'f':
				cubeTest. UtoF()
		
		ResoudrePetrus(cubeTest)# on resoud le cube de test 
		longueur.append(len(cubeTest.solve))# on recupere le nombre de mouvement servant a resoudre le cube de test
		i = i+1

	
	for j in range (0,len(longueur)):#on choisi l'orientation qui est la plus optimise
		if mini> longueur[j]:
			mini = longueur[j]
			court = j

	for k in range (0,len(listeO[court])):# on met le vrai cube dans la bone orientation 
		if listeO[court][k] == 'r':
			cube.UtoR()
		elif listeO[court][k] == 'f':
			cube.UtoF()
	ResoudrePetrus(cube)
	return cube.solution

def ResoudrePetrusN(n=10000):
	cube = Rubik()
	for i in range(0,n):
		cube.Scramble()
		ResoudrePetrus(cube)
		if not cube.TestCubeResolu():
			print ("non")
		else:
			print("oui")
		cube.solve = []
		cube.orientation = ''
		cube.solution = ''
	#print(len(cube.solve))# on resoud le cube
	return cube.solution
ResoudrePetrusE(cube)