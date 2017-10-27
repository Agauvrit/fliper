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

c12 = 'WWWWWWWWWGRBOBRBOGRGOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY'


# formules F2L pour résoudre les deux premières couronnes
def FLL(cube): 
	#si coin LDF en ULF
	if(cube.Dcube[6]==cube.Dcube['L'] and cube.Dcube[11]==cube.Dcube['D'] and cube.Dcube[12]== cube.Dcube['F']): 
		# LF en U
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

# formules OLL pour résoudre la face U
def OLL(cube): 
	#3
	if cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[10] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[16]:
		cube.R()
		cube.LL()
		cube.IB()
		cube.L()
		cube.IB()
		cube.IR()
		cube.UU()
		cube.R()
		cube.IB()
		cube.L()
		cube.IR() 
	#4 
	elif cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[10] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14]:
		cube.IL()
		cube.RR()
		cube.B()
		cube.IR()
		cube.B()
		cube.L()
		cube.UU()
		cube.IL()
		cube.B()
		cube.IR()
		cube.L()
	# 5
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[11] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IL()
		cube.BB()
		cube.R()
		cube.B()
		cube.IR()
		cube.B()
		cube.LL()
		cube.FF()
		cube.IR()
		cube.IF()
		cube.R()
		cube.IF()
		cube.IL()
	#6 
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.L()
		cube.F()
		cube.IR()
		cube.F()
		cube.R()
		cube.FF()
		cube.LL()
		cube.IB()
		cube.R()
		cube.IB()
		cube.IR()
		cube.BB()
		cube.L()
	#7 
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[10] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.R()
		cube.U()
		cube.IR()
		cube.U()
		cube.IR()
		cube.F()
		cube.R()
		cube.IF()
		cube.UU()
		cube.IR()
		cube.F()
		cube.R()
		cube.IF()
	#8
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IL()
		cube.R()
		cube.B()
		cube.R()
		cube.B()
		cube.IR()
		cube.IB()
		cube.LL()
		cube.RR()
		cube.F()
		cube.R()
		cube.IF()
		cube.IL()
	#9
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[10] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.R()
		cube.UU()
		cube.RR()
		cube.IU()
		cube.R()
		cube.IU()
		cube.IR()
		cube.UU()
		cube.F()
		cube.R()
		cube.IF()
	#10
	elif cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.F()
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.R()
		cube.IF()
		cube.L()
		cube.F()
		cube.IR()
		cube.IF()
		cube.IL()
	#11
	elif cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.B()
		cube.U()
		cube.L()
		cube.IU()
		cube.IL()
		cube.U()
		cube.L()
		cube.IU()
		cube.IL()
		cube.IB()
	#12
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IR()
		cube.IU()
		cube.R()
		cube.IU()
		cube.IR()
		cube.U()
		cube.IF()
		cube.U()
		cube.F()
		cube.R()
	#13
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14]:
		cube.L()
		cube.FF()
		cube.IR()
		cube.IF()
		cube.R()
		cube.F()
		cube.IR()
		cube.IF()
		cube.R()
		cube.IF()
		cube.IL()
	#14
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IR()
		cube.FF()
		cube.L()
		cube.F()
		cube.IL()
		cube.IF()
		cube.L()
		cube.F()
		cube.IL()
		cube.F()
		cube.R()
	#15
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[9]:
		cube.F()
		cube.IR()
		cube.FF()
		cube.L()
		cube.FF()
		cube.R()
		cube.FF()
		cube.IL()
		cube.F()
	#16
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IF()
		cube.L()
		cube.FF()
		cube.IR()
		cube.FF()
		cube.IL()
		cube.FF()
		cube.R()
		cube.IF()
	#17
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.F()
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.IF()
	#18
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IF()
		cube.IL()
		cube.IU()
		cube.L()
		cube.U()
		cube.IL()
		cube.IU()
		cube.L()
		cube.U()
		cube.F()
	#19
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14]:
		cube.L()
		cube.F()
		cube.IR()
		cube.F()
		cube.R()
		cube.FF()
		cube.IL()
	#20
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IR()
		cube.IF()
		cube.L()
		cube.IF()
		cube.IL()
		cube.FF()
		cube.R()
	#21
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.L()
		cube.RR()
		cube.IF()
		cube.R()
		cube.IF()
		cube.IR()
		cube.FF()
		cube.R()
		cube.IF()
		cube.R()
		cube.IL()
	#22
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.IR()
		cube.LL()
		cube.F()
		cube.IL()
		cube.F()
		cube.L()
		cube.FF()
		cube.IL()
		cube.F()
		cube.IL()
		cube.R()
	#23
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[9]:
		cube.IR()
		cube.IU()
		cube.R()
		cube.F()
		cube.IR()
		cube.IF()
		cube.U()
		cube.F()
		cube.R()
		cube.IF()	
	#24
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.L()
		cube.U()
		cube.IL()
		cube.IF()
		cube.L()
		cube.F()
		cube.IU()
		cube.IF()
		cube.IL()
		cube.F()
	#25
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.IR()
		cube.FF()
		cube.L()
		cube.F()
		cube.IL()
		cube.F()
		cube.R()
	#26
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.L()
		cube.FF()
		cube.IR()
		cube.IF()
		cube.R()
		cube.IF()
		cube.IL()
	#27
	elif cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14]:
		cube.F()
		cube.U()
		cube.R()
		cube.UU()
		cube.IR()
		cube.IU()
		cube.R()
		cube.U()
		cube.IR()
		cube.IF()
	#28
	elif cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[9]:
		cube.IF()
		cube.IU()
		cube.IL()
		cube.UU()
		cube.L()
		cube.U()
		cube.IL()
		cube.IU()
		cube.L()
		cube.F()
	#29
	elif cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.IL()
		cube.IB()
		cube.L()
		cube.IR()
		cube.IU()
		cube.R()
		cube.U()
		cube.IL()
		cube.B()
		cube.L()
	#30
	elif cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[9]:
		cube.R()
		cube.B()
		cube.IR()
		cube.L()
		cube.U()
		cube.IL()
		cube.IU()
		cube.R()
		cube.IB()
		cube.IR()
	#31
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[16]:
		cube.R()
		cube.U()
		cube.IR()
		cube.U()
		cube.R()
		cube.UU()
		cube.IR()
		cube.F()
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.IF()
	#32
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IL()
		cube.IU()
		cube.L()
		cube.IU()
		cube.IL()
		cube.UU()
		cube.L()
		cube.IF()
		cube.IL()
		cube.IU()
		cube.L()
		cube.U()
		cube.F()
	#33
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[12]:
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.R()
		cube.IU()
		cube.IR()
		cube.IF()
		cube.IU()
		cube.F()
		cube.R()
		cube.U()
		cube.IR()
	#34
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IL()
		cube.IU()
		cube.L()
		cube.U()
		cube.IL()
		cube.U()
		cube.L()
		cube.F()
		cube.U()
		cube.IF()
		cube.IL()
		cube.IU()
		cube.L()
	#35
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IR()
		cube.IU()
		cube.F()
		cube.U()
		cube.R()
		cube.IU()
		cube.IR()
		cube.IF()
		cube.R()
	#36
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14]:
		cube.L()
		cube.U()
		cube.IF()
		cube.IU()
		cube.IL()
		cube.U()
		cube.L()
		cube.F()
		cube.IL()	
	#37
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[13]:
		cube.F()
		cube.IR()
		cube.IF()
		cube.R()
		cube.U()
		cube.R()
		cube.IU()
		cube.IR()
	#38
	elif cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[11] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.B()
		cube.U()
		cube.L()
		cube.IU()
		cube.IL()
		cube.IB()
	#39
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[17]:
		cube.IB()
		cube.IU()
		cube.IR()
		cube.U()
		cube.R()
		cube.B()
	#40
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.R()
		cube.UU()
		cube.RR()
		cube.F()
		cube.R()
		cube.IF()
		cube.R()
		cube.UU()
		cube.IR()
	#41
	elif cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.F()
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.IF()
	#42
	elif cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[12]:
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.IR()
		cube.F()
		cube.R()
		cube.IF()
	#43
	elif cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[15]:
		cube.L()
		cube.IF()
		cube.IL()
		cube.IU()
		cube.L()
		cube.U()
		cube.F()
		cube.IU()
		cube.IL()
	#44
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.IR()
		cube.F()
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.IF()
		cube.U()
		cube.R()
	#45
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.F()
		cube.U()
		cube.IF()
		cube.IU()
		cube.IR()
		cube.IF()
		cube.L()
		cube.F()
		cube.IL()
		cube.R()
	#46
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IR()
		cube.IU()
		cube.IR()
		cube.F()
		cube.R()
		cube.IF()
		cube.U()
		cube.R()
	#47
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[13]:
		cube.R()
		cube.U()
		cube.IR()
		cube.U()
		cube.R()
		cube.IU()
		cube.IR()
		cube.IU()
		cube.IR()
		cube.F()
		cube.R()
		cube.IF()
	#48
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[11] and cube.Dcube['U'] == cube.Dcube[10]:
		cube.IL()
		cube.IU()
		cube.L()
		cube.IU()
		cube.IL()
		cube.U()
		cube.L()
		cube.U()
		cube.L()
		cube.IF()
		cube.IL()
		cube.F()
	#49
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[14]:
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
	#50
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[11]:
		cube.R()
		cube.UU()
		cube.RR()
		cube.IU()
		cube.RR()
		cube.IU()
		cube.RR()
		cube.UU()
		cube.R()
	#51
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[20]:
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
	#52
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[12] and cube.Dcube['U'] == cube.Dcube[20]:
		cube.L()
		cube.F()
		cube.IR()
		cube.IF()
		cube.IL()
		cube.F()
		cube.R()
		cube.IF()
	#53
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[12]:
		cube.F()
		cube.IR()
		cube.IF()
		cube.L()
		cube.F()
		cube.R()
		cube.IF()
		cube.IL()
	#54
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[12]:
		cube.IL()
		cube.IU()
		cube.L()
		cube.IU()
		cube.IL()
		cube.UU()
		cube.L()
	#55
	elif cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[7] and cube.Dcube['U'] == cube.Dcube[20] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[14]:
		cube.R()
		cube.U()
		cube.IR()
		cube.U()
		cube.R()
		cube.UU()
		cube.IR()
	#56
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[2] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[16]:
		cube.L()
		cube.F()
		cube.IR()
		cube.IF()
		cube.IL()
		cube.R()
		cube.U()
		cube.R()
		cube.IU()
		cube.IR()
	#57
	elif cube.Dcube['U'] == cube.Dcube[1] and cube.Dcube['U'] == cube.Dcube[3] and cube.Dcube['U'] == cube.Dcube[4] and cube.Dcube['U'] == cube.Dcube[5] and cube.Dcube['U'] == cube.Dcube[6] and cube.Dcube['U'] == cube.Dcube[8] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[19]:
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.IR()
		cube.L()
		cube.F()
		cube.R()
		cube.IF()
		cube.IL()
	#1 et 2
	else :
		#1 
		if cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[15] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[17] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[10] and cube.Dcube['U'] == cube.Dcube[11]:
			cube.R()
			cube.UU()
			cube.RR()
			cube.F()
			cube.R()
			cube.IF()
			cube.UU()
			cube.IR()
			cube.F()
			cube.R()
			cube.IF()
		#2
		elif cube.Dcube['U'] == cube.Dcube[19] and cube.Dcube['U'] == cube.Dcube[18] and cube.Dcube['U'] == cube.Dcube[16] and cube.Dcube['U'] == cube.Dcube[13] and cube.Dcube['U'] == cube.Dcube[14] and cube.Dcube['U'] == cube.Dcube[9] and cube.Dcube['U'] == cube.Dcube[10] and cube.Dcube['U'] == cube.Dcube[11]:
			cube.F()
			cube.R()
			cube.U()
			cube.IR()
			cube.IU()
			cube.IF()
			cube.B()
			cube.U()
			cube.L()
			cube.IU()
			cube.IL()
			cube.IB()

# forumes PLL pour permuter les arêtes et les coins de la couronne
def PLL(cube): 
	# U et U'
	if cube.Dcube[12]==cube.Dcube[13]==cube.Dcube[14] and cube.Dcube[15]==cube.Dcube[17] and cube.Dcube[11]==cube.Dcube[9] and cube.Dcube[18]==cube.Dcube[20]:
		# cas U
		if cube.Dcube[19]==cube.Dcube[11]:
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
		elif cube.Dcube[19]==cube.Dcube[15]: 
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
	# cas A et A'
	elif cube.Dcube[10]==cube.Dcube[11] and cube.Dcube[12]==cube.Dcube[13]:
		#cas A 
		if cube.Dcube[14]==cube.Dcube[16]:
			cube.IR()
			cube.IR()
			cube.BB()
			cube.R()
			cube.F()
			cube.IR()
			cube.BB()
			cube.R()
			cube.IF()
			cube.R()
		#cas A'
		elif cube.Dcube[18]==cube.Dcube[16]:
			cube.IR()
			cube.F()
			cube.IR()
			cube.BB()
			cube.R()
			cube.IF()
			cube.IR()
			cube.BB()
			cube.RR()
	#cas Z et H
	elif cube.Dcube[12]==cube.Dcube[14] and cube.Dcube[15]==cube.Dcube[17] and cube.Dcube[18]==cube.Dcube[20] and cube.Dcube[9]==cube.Dcube[11]:
		# cas Z
		if cube.Dcube[16]==cube.Dcube[18] and cube.Dcube[13]==cube.Dcube[11]:
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
		#cas H 
		elif cube.Dcube[13]==cube.Dcube[18] and cube.Dcube[16]==cube.Dcube[11]:
			cube.LL()
			cube.RR()
			cube.D()
			cube.LL()
			cube.RR()
			cube.UU()
			cube.LL()
			cube.RR()
			cube.D()
			cube.RR()
			cube.LL()
	#cas J
	elif cube.Dcube[11]==cube.Dcube[10] and cube.Dcube[9]==cube.Dcube[10] and cube.Dcube[19]==cube.Dcube[20] and cube.Dcube[16]==cube.Dcube[12] and cube.Dcube[15]==cube.Dcube[19]:
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
		cube.RR()
		cube.IU()
		cube.IR()
		cube.IU()
	#cas Jsym
	elif cube.Dcube[15]==cube.Dcube[16] and cube.Dcube[16]==cube.Dcube[17] and cube.Dcube[18]==cube.Dcube[19] and cube.Dcube[11]==cube.Dcube[19] and cube.Dcube[10]==cube.Dcube[14]:
		cube.IL()
		cube.IU()
		cube.L()
		cube.F()
		cube.IL()
		cube.IU()
		cube.L()
		cube.U()
		cube.L()
		cube.IF()
		cube.LL()
		cube.U()
		cube.L()
		cube.U()
	#cas R
	elif cube.Dcube[10]==cube.Dcube[11] and cube.Dcube[12]==cube.Dcube[14] and cube.Dcube[16]==cube.Dcube[12] and cube.Dcube[18]==cube.Dcube[10]:
		cube.IR()
		cube.UU()
		cube.R()
		cube.UU()
		cube.IR()
		cube.F()
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.IR()
		cube.IF()
		cube.RR()
		cube.IU()
	#cas Rsym 
	elif cube.Dcube[12]==cube.Dcube[14] and cube.Dcube[15]==cube.Dcube[16] and cube.Dcube[10]==cube.Dcube[14] and cube.Dcube[20]==cube.Dcube[16]:
		cube.L()
		cube.UU()
		cube.IL()
		cube.UU()
		cube.L()
		cube.IF()
		cube.IL()
		cube.IU()
		cube.L()
		cube.U()
		cube.L()
		cube.F()
		cube.LL()
		cube.U()
	#cas T
	elif cube.Dcube[12]==cube.Dcube[13] and cube.Dcube[19]==cube.Dcube[20] and cube.Dcube[9]==cube.Dcube[11] and cube.Dcube[16]==cube.Dcube[11] and cube.Dcube[17]==cube.Dcube[13]:
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
	#cas F
	elif cube.Dcube[12]==cube.Dcube[13] and cube.Dcube[13]==cube.Dcube[14] and cube.Dcube[16]==cube.Dcube[11] and cube.Dcube[10]==cube.Dcube[15] and cube.Dcube[18]==cube.Dcube[11]:
		cube.IR()
		cube.U()
		cube.R()
		cube.IU()
		cube.RR()
		cube.IF()
		cube.IU()
		cube.F()
		cube.U()
		cube.R()
		cube.F()
		cube.IR()
		cube.IF()
		cube.RR()
		cube.IU()
	#cas V
	elif cube.Dcube[9]==cube.Dcube[10] and cube.Dcube[19]==cube.Dcube[20] and cube.Dcube[16]==cube.Dcube[18] and cube.Dcube[11]==cube.Dcube[13] and cube.Dcube[17]==cube.Dcube[10]:
		cube.IL()
		cube.U()
		cube.R()
		cube.IU()
		cube.L()
		cube.U()
		cube.IL()
		cube.U()
		cube.IR()
		cube.IU()
		cube.L()
		cube.UU()
		cube.R()
		cube.UU()
		cube.IR()
	#cas E
	elif cube.Dcube[17]==cube.Dcube[19] and cube.Dcube[9]==cube.Dcube[19] and cube.Dcube[15]==cube.Dcube[13] and cube.Dcube[11]==cube.Dcube[13]:
		cube.F()
		cube.IR()
		cube.IF()
		cube.L()
		cube.F()
		cube.R()
		cube.IF()
		cube.LL()
		cube.IB()
		cube.R()
		cube.B()
		cube.L()
		cube.IB()
		cube.IR()
		cube.B()
	#cas N
	elif cube.Dcube[12]==cube.Dcube[13] and cube.Dcube[18]==cube.Dcube[19] and cube.Dcube[16]==cube.Dcube[11] and cube.Dcube[10]==cube.Dcube[17] and cube.Dcube[20]==cube.Dcube[13]:
		cube.IR()
		cube.U()
		cube.IR()
		cube.F()
		cube.R()
		cube.IF()
		cube.R()
		cube.IU()
		cube.IR()
		cube.IF()
		cube.U()
		cube.F()
		cube.R()
		cube.U()
		cube.IR()
		cube.IU()
		cube.R()
	#cas Nsym
	elif cube.Dcube[13]==cube.Dcube[14] and cube.Dcube[19]==cube.Dcube[20] and cube.Dcube[16]==cube.Dcube[9] and cube.Dcube[10]==cube.Dcube[15] and cube.Dcube[18]==cube.Dcube[13]:
		cube.L()
		cube.IU()
		cube.L()
		cube.IF()
		cube.IL()
		cube.F()
		cube.IL()
		cube.U()
		cube.L()
		cube.F()
		cube.IU()
		cube.IF()
		cube.IL()
		cube.IU()
		cube.L()
		cube.U()
		cube.IL()
	#cas Y
	elif cube.Dcube[12]==cube.Dcube[13] and cube.Dcube[16]==cube.Dcube[17] and cube.Dcube[10]==cube.Dcube[18] and cube.Dcube[20]==cube.Dcube[13]:
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
	#cas G et G'
	elif cube.Dcube[12]==cube.Dcube[13]:
		#G
		if cube.Dcube[16]==cube.Dcube[11] and cube.Dcube[20]==cube.Dcube[13]:
			cube.LL()
			cube.ID()
			cube.B()
			cube.IU()
			cube.B()
			cube.U()
			cube.IB()
			cube.D()
			cube.LL()
			cube.F()
			cube.IU()
			cube.IF()
		#G' 
		elif cube.Dcube[19]==cube.Dcube[11] and cube.Dcube[17]==cube.Dcube[13]:
			cube.F()
			cube.U()
			cube.IF()
			cube.LL()
			cube.ID()
			cube.B()
			cube.IU()
			cube.IB()
			cube.U()
			cube.IB()
			cube.D()
			cube.LL()
	#Gsym et G'sym
	elif cube.Dcube[13]==cube.Dcube[14]:
		#Gsym
		if cube.Dcube[10]==cube.Dcube[15] and cube.Dcube[18]==cube.Dcube[13]:
			cube.RR()
			cube.D()
			cube.IB()
			cube.U()
			cube.IB()
			cube.IU()
			cube.B()
			cube.ID()
			cube.RR()
			cube.IF()
			cube.U()
			cube.F()
		#G'sym
		elif cube.Dcube[19]==cube.Dcube[15] and cube.Dcube[9]==cube.Dcube[13]:
			cube.IF()
			cube.IU()
			cube.F()
			cube.RR()
			cube.D()
			cube.IB()
			cube.U()
			cube.B()
			cube.IU()
			cube.B()
			cube.ID()
			cube.RR()

def maximum(liste): #Renvoie l'indice du maximum d'une liste
	maximum = 0
	indice = 1 #Par defaut on est a 1 car on a pas a modifier le cube si aucun coin ne vaut mieux qu'un autre
	for i in range(0,len(liste)):
		if liste[i] > maximum:
			maximum = liste[i]
			indice = i

	return indice

# resolution du cube 2x2x2
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
	"LD est placée"
	cube.UtoR()
	cube.UtoF()

	PlaceEdge(cube)
	"LB est placée"
	cube.UtoR()
	cube.UtoF()
	PlaceEdge(cube)
	cube.UtoF()

#
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

# etape qui résoude le cube en 3x2x2
def step2(cube): 
	cpt = 0
	#regarde si l'etape 2 a deja ete realise
	while(cube.Dcube['F']!=cube.Dcube[23] or cube.Dcube['F']!=cube.Dcube[32] or cube.Dcube['F']!=cube.Dcube[33] or cube.Dcube['L']!=cube.Dcube[22] or cube.Dcube['L']!=cube.Dcube[21] or cube.Dcube['L']!=cube.Dcube[29] or cube.Dcube['L']!=cube.Dcube[30] or cube.Dcube['L']!=cube.Dcube[31] or cube.Dcube['D']!=cube.Dcube[41] or cube.Dcube['D']!=cube.Dcube[42] or cube.Dcube['D']!=cube.Dcube[44] or cube.Dcube['D']!=cube.Dcube[46] or cube.Dcube['D']!=cube.Dcube[47] or cube.Dcube['B']!=cube.Dcube[28] or cube.Dcube['B']!=cube.Dcube[39] or cube.Dcube['B']!=cube.Dcube[40]) and cpt < 20:
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
		# Recherche arrête UB et UL 
		elif ((cube.Dcube[10]==cube.Dcube['F'] and cube.Dcube[4]==cube.Dcube['D']) or (cube.Dcube[19]== cube.Dcube['F'] and cube.Dcube[2]== cube.Dcube['D'])):
			if cube.Dcube[10]==cube.Dcube['F'] and cube.Dcube[4]==cube.Dcube['D'] : 
				cube.IU()
			elif cube.Dcube[19]==cube.Dcube['F'] and cube.Dcube[2]==cube.Dcube['D'] : 
				cube.UU()
			cube.FF()
		#Recherche arrête RD et RB
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

		#Recherche du Coin LFD que l'on positionne en ULF
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
		#si cion ULB
		elif((cube.Dcube[20]==cube.Dcube['D'] and cube.Dcube[9]==cube.Dcube['F'] and cube.Dcube[1]==cube.Dcube['L']) or (cube.Dcube[20]== cube.Dcube['L'] and cube.Dcube[9]== cube.Dcube['D'] and cube.Dcube[1]==cube.Dcube['F']) or (cube.Dcube[20]== cube.Dcube['F'] and cube.Dcube[9]== cube.Dcube['L'] and cube.Dcube[1]== cube.Dcube['D'])):
			cube.IU()
		#Si coin LFD - Positionner l'arrete LF 
		elif (cube.Dcube[31]==cube.Dcube['L'] and cube.Dcube[32]==cube.Dcube['F'] and cube.Dcube[41]==cube.Dcube['D']) or (cube.Dcube[31]== cube.Dcube['F'] and cube.Dcube[32]== cube.Dcube['D'] and cube.Dcube[41]==cube.Dcube['L']) or (cube.Dcube[31]== cube.Dcube['D'] and cube.Dcube[32]== cube.Dcube['L'] and cube.Dcube[41]== cube.Dcube['F']):
			#LF en FR 
			if (cube.Dcube[24]==cube.Dcube['F'] and cube.Dcube[25]==cube.Dcube['L']) or (cube.Dcube[25]==cube.Dcube['F'] and cube.Dcube[24]==cube.Dcube['L']):
				cube.IF()
				cube.U()
				cube.F()
				if cube.Dcube[10] == cube.Dcube['F']:
					cube.IU()
			# LF en RD 
			elif (cube.Dcube[36]==cube.Dcube['F'] and cube.Dcube[45]==cube.Dcube['L']) or (cube.Dcube[45]==cube.Dcube['F'] and cube.Dcube[36]==cube.Dcube['L']):
				cube.RR()
				if cube.Dcube[16] == cube.Dcube['F']:
					cube.U()
				else :
					cube.UU()
			# LF en RB
			elif (cube.Dcube[26]==cube.Dcube['F'] and cube.Dcube[27]==cube.Dcube['L']) or (cube.Dcube[27]==cube.Dcube['F'] and cube.Dcube[26]==cube.Dcube['L']):
				cube.IR()
				if cube.Dcube[16] == cube.Dcube['F']:
					cube.U()
				else :
					cube.UU()
			# LF en UR
			elif (cube.Dcube[5] == cube.Dcube['F'] and cube.Dcube[16] == cube.Dcube['L']) or (cube.Dcube[16] == cube.Dcube['F'] and cube.Dcube[5] == cube.Dcube['L']):
				if cube.Dcube[16] == cube.Dcube['F']:
					cube.U()
				else:
					cube.UU()
			# LF en UB
			elif (cube.Dcube[2] == cube.Dcube['F'] and cube.Dcube[19] == cube.Dcube['L']) or (cube.Dcube[19] == cube.Dcube['F'] and cube.Dcube[2] == cube.Dcube['L']):
				if cube.Dcube[19] == cube.Dcube['F']:
					cube.UU()
				else:
					cube.IU()
			# LF en UL mal positionne 
			elif (cube.Dcube[4] == cube.Dcube['F'] and cube.Dcube[10] == cube.Dcube['L']) or (cube.Dcube[10] == cube.Dcube['F'] and cube.Dcube[4] == cube.Dcube['L']):
				if cube.Dcube[10] == cube.Dcube['F']:
					cube.IU()
			# LF en UF mal positionne 
			elif (cube.Dcube[7] == cube.Dcube['F'] and cube.Dcube[13] == cube.Dcube['L']) or (cube.Dcube[13] == cube.Dcube['F'] and cube.Dcube[7] == cube.Dcube['L']):
				if cube.Dcube[13] == cube.Dcube['L']:
					cube.U()
			# LF en LF mal oriente
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

		cpt += 1

	if cpt == 20 : 
		return False
	else : 
		return True
		
#Fonction qui met le carre 2*2 (bas à gauche) de la face R
def step3(cube):
        #On place le cube de façon que la face R devienne F
        cube.UtoR()
        cube.UtoR()
        cube.UtoR()
        cube.UtoF()
        cube.UtoR()

        #On commence par placer l'arête F-D
        #Fonction qui verifie si l'arête n'est pas déjà à sa place
        if (cube.Dcube[33]==cube.Dcube['F'] and cube.Dcube[42]==cube.Dcube['D']) or (cube.Dcube[42]==cube.Dcube['F'] and cube.Dcube[33]==cube.Dcube['D']):
                if cube.Dcube[33] == cube.Dcube['D']:
                        cube.FF()
                        cube.U()
                        cube.L()
                        cube.IF()
                        cube.IL()
        #Sinon on checke toutes les positions possible de l'arête F-D et on effectue un/des mouvement/s pour placer l'arête correctement
        #On fait des mouvements different selon l'orientation de l'arête
        #(On sait déjà que l'arete n'est pas sur le cube 2*2*3 donc on n'est pas obligé de checker les arêtes de cette partie du cube)
        elif (cube.Dcube[23] == cube.Dcube['F'] and cube.Dcube[22] == cube.Dcube['D']) or (cube.Dcube[22] == cube.Dcube['F'] and cube.Dcube[23] == cube.Dcube['D']):
                if cube.Dcube[23] == cube.Dcube['F']:
                        cube.IF()
                else:
                        cube.F()
                        cube.U()
                        cube.L()
                        cube.IF()
                        cube.IL()
  		# FD en UF     
        elif (cube.Dcube[13] == cube.Dcube['F'] and cube.Dcube[7] == cube.Dcube['D']) or (cube.Dcube[7] == cube.Dcube['F'] and cube.Dcube[13] == cube.Dcube['D']):
                if cube.Dcube[13] == cube.Dcube['F']:
                        cube.FF()
                else:
                        cube.U()
                        cube.L()
                        cube.IF()
                        cube.IL()
        # FD en FR
        elif (cube.Dcube[24] == cube.Dcube['F'] and cube.Dcube[25] == cube.Dcube['D']) or (cube.Dcube[25] == cube.Dcube['F'] and cube.Dcube[24] == cube.Dcube['D']):
                if cube.Dcube[24] == cube.Dcube['F']:
                        cube.F()
                else:
                        cube.IF()
                        cube.U()
                        cube.L()
                        cube.IF()
                        cube.IL()
        # FD en UR
        elif (cube.Dcube[5] == cube.Dcube['F'] and cube.Dcube[16] == cube.Dcube['D']) or (cube.Dcube[16] == cube.Dcube['F'] and cube.Dcube[5] == cube.Dcube['D']):
                if cube.Dcube[16] == cube.Dcube['F']:
                        cube.U()
                        cube.FF()
                else:
                        cube.IR()
                        cube.F()
                        cube.R()
        # FD en UB
        elif (cube.Dcube[2] == cube.Dcube['F'] and cube.Dcube[19] == cube.Dcube['D']) or (cube.Dcube[19] == cube.Dcube['F'] and cube.Dcube[2] == cube.Dcube['D']):
                if cube.Dcube[19] == cube.Dcube['F']:
                        cube.UU()
                        cube.FF()
                else:
                        cube.U()
                        cube.IR()
                        cube.F()
                        cube.R()
        # FD en UL
        elif (cube.Dcube[4] == cube.Dcube['F'] and cube.Dcube[10] == cube.Dcube['D']) or (cube.Dcube[10] == cube.Dcube['F'] and cube.Dcube[4] == cube.Dcube['D']):
                if cube.Dcube[10] == cube.Dcube['F']:
                        cube.IU()
                        cube.FF()
                else:
                        cube.L()
                        cube.IF()
                        cube.IL()
        # FD en FD mal orienté 
        elif (cube.Dcube[33]==cube.Dcube['D'] and cube.Dcube[42]==cube.Dcube['F']):
        	cube.FF()
        	cube.R()
        	cube.IU()
        	cube.IR()

        #Ensuite on place le coin F-D-L
        #Il peut être placé à deux endroits, soit en 32-31-41 (bas à gauche de F) soit en 11-12-6 (haut à gauche de F)
        #On regarde si le coin n'est pas déjà dans une des deux positions valide
        if not verifCoinF_L_U(cube):
                #Sinon on checke toutes les positions possible du coin F_L_D et on effectue un/des mouvement/s pour placer le coin en 11-12-6 mais sans bouger de place l'arête F-D
                #(Comme pour l'arête, on peut ne pas checker les coins du cube 2*2*3)
                if (cube.Dcube[35]==cube.Dcube['F'] and cube.Dcube[34]==cube.Dcube['L'] and cube.Dcube[43]==cube.Dcube['D']) or (cube.Dcube[34]==cube.Dcube['F'] and cube.Dcube[43]==cube.Dcube['L'] and cube.Dcube[35]==cube.Dcube['D']) or (cube.Dcube[43]==cube.Dcube['F'] and cube.Dcube[35]==cube.Dcube['L'] and cube.Dcube[34]==cube.Dcube['D']):
                        cube.IF()
                        cube.IU()
                        cube.F()
                        cube.UU()
                # FLD en UFR
                elif (cube.Dcube[14]==cube.Dcube['D'] and cube.Dcube[15]==cube.Dcube['F'] and cube.Dcube[8]==cube.Dcube['L']) or (cube.Dcube[14]== cube.Dcube['L'] and cube.Dcube[15]== cube.Dcube['D'] and cube.Dcube[8]==cube.Dcube['F']) or (cube.Dcube[14]== cube.Dcube['F'] and cube.Dcube[15]== cube.Dcube['L'] and cube.Dcube[8]== cube.Dcube['D']):
                        cube.U()
                # FLD en URB
                elif (cube.Dcube[17]==cube.Dcube['D'] and cube.Dcube[18]==cube.Dcube['F'] and cube.Dcube[3]==cube.Dcube['L']) or (cube.Dcube[17]== cube.Dcube['L'] and cube.Dcube[18]== cube.Dcube['D'] and cube.Dcube[3]==cube.Dcube['F']) or (cube.Dcube[17]== cube.Dcube['F'] and cube.Dcube[18]== cube.Dcube['L'] and cube.Dcube[3]== cube.Dcube['D']):
                        cube.UU()
                # FLD en UBL
                elif (cube.Dcube[20]==cube.Dcube['D'] and cube.Dcube[9]==cube.Dcube['F'] and cube.Dcube[1]==cube.Dcube['L']) or (cube.Dcube[20]== cube.Dcube['L'] and cube.Dcube[9]== cube.Dcube['D'] and cube.Dcube[1]==cube.Dcube['F']) or (cube.Dcube[20]== cube.Dcube['F'] and cube.Dcube[9]== cube.Dcube['L'] and cube.Dcube[1]== cube.Dcube['D']):
                        cube.IU()
                # FLD en LFD
                elif (cube.Dcube[31]==cube.Dcube['L'] and cube.Dcube[32]==cube.Dcube['F'] and cube.Dcube[41]==cube.Dcube['D']) or (cube.Dcube[31]== cube.Dcube['F'] and cube.Dcube[32]== cube.Dcube['D'] and cube.Dcube[41]==cube.Dcube['L']) or (cube.Dcube[31]== cube.Dcube['D'] and cube.Dcube[32]== cube.Dcube['L'] and cube.Dcube[41]== cube.Dcube['F']):
                        # si LF en FR
                        if (cube.Dcube[24]==cube.Dcube['F'] and cube.Dcube[25]==cube.Dcube['L']) or (cube.Dcube[25]==cube.Dcube['F'] and cube.Dcube[24]==cube.Dcube['L']):
                                cube.IF()
                                cube.U()
                                cube.F()
                                if cube.Dcube[10] == cube.Dcube['F']:
                                        cube.IU()
                        # si LF en UR
                        elif (cube.Dcube[5] == cube.Dcube['F'] and cube.Dcube[16] == cube.Dcube['L']) or (cube.Dcube[16] == cube.Dcube['F'] and cube.Dcube[5] == cube.Dcube['L']):
                                if cube.Dcube[16] == cube.Dcube['F']:
                                        cube.U()
                                else :
                                        cube.UU()
                        # si LF en UB
                        elif (cube.Dcube[2] == cube.Dcube['F'] and cube.Dcube[19] == cube.Dcube['L']) or (cube.Dcube[19] == cube.Dcube['F'] and cube.Dcube[2] == cube.Dcube['L']):
                                if cube.Dcube[19] == cube.Dcube['F']:
                                        cube.UU()
                                else:
                                        cube.IU()
                        # si LF en UL mal positionne 
                        elif (cube.Dcube[4] == cube.Dcube['F'] and cube.Dcube[10] == cube.Dcube['L']) or (cube.Dcube[10] == cube.Dcube['F'] and cube.Dcube[4] == cube.Dcube['L']):
                                if cube.Dcube[10] == cube.Dcube['F']:
                                        cube.IU()
                        # si LF en UF mal positionne
                        elif (cube.Dcube[7] == cube.Dcube['F'] and cube.Dcube[13] == cube.Dcube['L']) or (cube.Dcube[13] == cube.Dcube['F'] and cube.Dcube[7] == cube.Dcube['L']):
                                if cube.Dcube[13] == cube.Dcube['L']:
                                        cube.U()
                        # si LF en LF mal oriente
                        elif (cube.Dcube[22] == cube.Dcube['F'] and cube.Dcube[23] == cube.Dcube['L']):
                            cube.F()
                            cube.U()
                            cube.IF()
                            cube.IU()
        # Si arrête LF en FR
        if (cube.Dcube[24] == cube.Dcube['L'] and cube.Dcube[25] == cube.Dcube['F']) or (cube.Dcube[25] == cube.Dcube['L'] and cube.Dcube[24] == cube.Dcube['F']) :
                cube.U()
                cube.R()
                cube.IU()
                cube.IR()

        #enfin on utilise la méthode FFL qui va orienter correctement le coin ou/et l'arête 
        FLL(cube)

        # Réorientation
        cube.UtoR()
        cube.UtoR()
        cube.UtoR()
        cube.UtoF()
        cube.UtoR()

        #Recherche du coin FLD 
        # Si FLD en UFR
        if((cube.Dcube[14]==cube.Dcube['D'] and cube.Dcube[15]==cube.Dcube['F'] and cube.Dcube[8]==cube.Dcube['L']) or (cube.Dcube[14]== cube.Dcube['L'] and cube.Dcube[15]== cube.Dcube['D'] and cube.Dcube[8]==cube.Dcube['F']) or (cube.Dcube[14]== cube.Dcube['F'] and cube.Dcube[15]== cube.Dcube['L'] and cube.Dcube[8]== cube.Dcube['D'])):
            cube.U()
        # si FLD en URB
        elif (cube.Dcube[17]==cube.Dcube['D'] and cube.Dcube[18]==cube.Dcube['F'] and cube.Dcube[3]==cube.Dcube['L']) or (cube.Dcube[17]== cube.Dcube['L'] and cube.Dcube[18]== cube.Dcube['D'] and cube.Dcube[3]==cube.Dcube['F']) or (cube.Dcube[17]== cube.Dcube['F'] and cube.Dcube[18]== cube.Dcube['L'] and cube.Dcube[3]== cube.Dcube['D']):
            cube.UU()
        # si FLD en UBL
        elif((cube.Dcube[20]==cube.Dcube['D'] and cube.Dcube[9]==cube.Dcube['F'] and cube.Dcube[1]==cube.Dcube['L']) or (cube.Dcube[20]== cube.Dcube['L'] and cube.Dcube[9]== cube.Dcube['D'] and cube.Dcube[1]==cube.Dcube['F']) or (cube.Dcube[20]== cube.Dcube['F'] and cube.Dcube[9]== cube.Dcube['L'] and cube.Dcube[1]== cube.Dcube['D'])):
            cube.IU()
        # si FLD en FLD 
        elif (cube.Dcube[31]==cube.Dcube['L'] and cube.Dcube[32]==cube.Dcube['F'] and cube.Dcube[41]==cube.Dcube['D']) or (cube.Dcube[31]== cube.Dcube['F'] and cube.Dcube[32]== cube.Dcube['D'] and cube.Dcube[41]==cube.Dcube['L']) or (cube.Dcube[31]== cube.Dcube['D'] and cube.Dcube[32]== cube.Dcube['L'] and cube.Dcube[41]== cube.Dcube['F']):
            # si LF en UR 
            if (cube.Dcube[5] == cube.Dcube['F'] and cube.Dcube[16] == cube.Dcube['L']) or (cube.Dcube[16] == cube.Dcube['F'] and cube.Dcube[5] == cube.Dcube['L']):
                if cube.Dcube[16] == cube.Dcube['F']:
                    cube.U()
                else:
                    cube.UU()
            # si LF en UB
            elif (cube.Dcube[2] == cube.Dcube['F'] and cube.Dcube[19] == cube.Dcube['L']) or (cube.Dcube[19] == cube.Dcube['F'] and cube.Dcube[2] == cube.Dcube['L']):
                if cube.Dcube[19] == cube.Dcube['F']:
                    cube.UU()
                else:
                    cube.IU()
            # Si LF en UL mal positionne
            elif (cube.Dcube[4] == cube.Dcube['F'] and cube.Dcube[10] == cube.Dcube['L']) or (cube.Dcube[10] == cube.Dcube['F'] and cube.Dcube[4] == cube.Dcube['L']):
                if cube.Dcube[10] == cube.Dcube['F']:
                    cube.IU()
			# si LF en UF mal positionne            
            elif (cube.Dcube[7] == cube.Dcube['F'] and cube.Dcube[13] == cube.Dcube['L']) or (cube.Dcube[13] == cube.Dcube['F'] and cube.Dcube[7] == cube.Dcube['L']):
                if cube.Dcube[13] == cube.Dcube['L']:
                    cube.U()
            # Si LF en LF mal oriente
            elif (cube.Dcube[22] == cube.Dcube['F'] and cube.Dcube[23] == cube.Dcube['L']):
                cube.F()
                cube.U()
                cube.IF()
                cube.IU()

        #enfin on utilise la méthode FFL qui va orienter correctement le coin ou/et l'arête 
        FLL(cube)

#Fonction qui vérifie si le coin F-L-D n'est pas placé en 11-12-6 (haut à gauche de F)
def verifCoinF_L_U(cube):
        return (cube.Dcube[12]==cube.Dcube['F'] or cube.Dcube[12]==cube.Dcube['L'] or cube.Dcube[12]==cube.Dcube['D']) and (cube.Dcube[11]==cube.Dcube['F'] or cube.Dcube[11]==cube.Dcube['L'] or cube.Dcube[11]==cube.Dcube['D']) and (cube.Dcube[6]==cube.Dcube['F'] or cube.Dcube[6]==cube.Dcube['L'] or cube.Dcube[6]==cube.Dcube['D'])

# etape qui verifie si l'etape resout bien la face U 
def step4(cube):
	cpt = 0
	# tant que la face U n est pas resolu
	while not cube.TestFaceU() and cpt < 10 : 
		# appel de PLL 
		OLL(cube)
		cube.FtoR() # rotation du cube afin de tester le cube dans toutes ses configurations
		cpt += 1
	if cpt == 10:
		return False
	else : 
		return True

# etape qui verifie si le cube est bien resolu
def step5(cube):
	cpt = 0
	# tant que la dernière couronne n est pas resolu 
	while  (not (cube.Dcube[12]==cube.Dcube[13]==cube.Dcube[14]) or not (cube.Dcube[15]==cube.Dcube[16]==cube.Dcube[17]) or not (cube.Dcube[18]==cube.Dcube[19]==cube.Dcube[20]) or  not (cube.Dcube[9]==cube.Dcube[10]==cube.Dcube[11])) and cpt < 10: 
		# appel de PLL 
		PLL(cube)
		cube.FtoR() # rotation du cube afin de tester le cube dans toutes ses configurations
		cpt += 1

	if(cube.Dcube[10]==cube.Dcube['F']):
		cube.IU()
	elif(cube.Dcube[19]==cube.Dcube['F']):
		cube.UU()
	elif(cube.Dcube[16]==cube.Dcube['F']):
		cube.U()

	if cpt == 10:
		return False
	else : 
		return True


#------------------------------------------------------------------------------------------------
def ResoudreFridrich(cube): 
	#Fonction princiaple de resolution de cube avec la methode de Friedrich
	resolu = True
	Cube222(cube)
	resolu = step2(cube)
	if resolu : 
		step3(cube)
	if resolu : 
		resolu = step4(cube)
	if resolu :
		resolu = step5(cube)

	if cube.TestCubeResolu():
		#print("cube resolu en "+str(len(cube.solve))+" mouvements")
		cube.solChaine()
		pass
	#print(cube.solve)

def ChoixFridrich(cube):#cette fonction choisi l'orientation du cube qui est optimale pour la résolution
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
		
		ResoudreFridrich(cubeTest)# on resoud le cube de test 
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
	ResoudreFridrich(cube)
	return cube.solution

def StockageErreurs(n=1000): #Ne pas éxéctuer sans l'avis d'un professionnel
	moyenne = 0
	minimum = 1000
	maximum = 0
	cube=Rubik()
	cube.Scramble()
	Fichier = open("CubeFriedrich.txt",'a')
	tmp = ''
	Erreur =0
	for i in range(0,n):
		cube=Rubik()
		cube.Scramble()
		tmp = str(cube.Dcube)
		ChoixFridrich(cube)
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

