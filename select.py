from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random
global mc
v=246


def tnt(mc,x,y,z):
	for each in range(10):
		for other in range(1):
			mc.setBlock(x,y,z,46)
			sleep(0.1)
			mc.setBlock(x,y,z,11)
			sleep(0.1)
		if mc.getBlock(x,y-1,z)==0:
			mc.setBlock(x,y,z,0)
			y=y-1
	sphere(mc,x,y,z)

def sphere(mc,x,y,z):
	radius=2
	for x1 in range(radius*-2,radius+10):#eye
		for y1 in range(radius*-2,radius+10):
			for z1 in range(radius*-2,radius+10):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+10)**2:
					mc.setBlock(x+x1+5,y+y1,z+z1+5,56)
					
	for x1 in range(radius*-1,radius+5):#Nose center
		for y1 in range(radius*-1,radius+5):
			for z1 in range(radius*-1,radius+5):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+6)**2:
					mc.setBlock(x+x1,y+y1,z+z1,3)
					
	for x1 in range(radius*-2,radius+10):#eye
		for y1 in range(radius*-2,radius+10):
			for z1 in range(radius*-2,radius+10):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+10)**2:
					mc.setBlock(x+x1+5,y+y1,z+z1-5,56)
					
	for x1 in range(radius*-2,radius+5):#smile start
		for y1 in range(radius*-2,radius+7):
			for z1 in range(radius*-2,radius+7):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
					mc.setBlock(x+x1-7,y+y1,z+z1,56)
					
	for x1 in range(radius*-2,radius+5):#smile
		for y1 in range(radius*-2,radius+7):
			for z1 in range(radius*-2,radius+7):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
					mc.setBlock(x+x1-7,y+y1,z+z1+3,56)
					
	for x1 in range(radius*-2,radius+5):#smile
		for y1 in range(radius*-2,radius+10):
			for z1 in range(radius*-2,radius+10):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
					mc.setBlock(x+x1-7,y+y1,z+z1-3,56)
					
	for x1 in range(radius*-2,radius+5):#smile
		for y1 in range(radius*-2,radius+10):
			for z1 in range(radius*-2,radius+10):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
					mc.setBlock(x+x1-5,y+y1,z+z1-6,56)
					
	for x1 in range(radius*-2,radius+5):#smile end
		for y1 in range(radius*-2,radius+10):
			for z1 in range(radius*-2,radius+10):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+7)**2:
					mc.setBlock(x+x1-5,y+y1,z+z1+6,56)
					
	for x1 in range(radius*-2,radius+10):#right tear
		for y1 in range(radius*-2,radius+10):
			for z1 in range(radius*-2,radius+10):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+5)**2:
					mc.setBlock(x+x1+1,y+y1,z+z1+7,9)
					
	for x1 in range(radius*-2,radius+10):#left tear
		for y1 in range(radius*-2,radius+10):
			for z1 in range(radius*-2,radius+10):
				if (x1**6)+(y1**6)+(z1**6)<=(radius+5)**2:
					mc.setBlock(x+x1+1,y+y1,z+z1-7,9)
					
	for x1 in range(radius*-2,radius+3):#Eye brow
		for y1 in range(radius*-2,radius+1):
			for z1 in range(radius*-2,radius+2):
				if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
					mc.setBlock(x+x1+11,y+y1,z+z1,3)
					
	for x1 in range(radius*-2,radius+3):#Eye brow
		for y1 in range(radius*-2,radius+1):
			for z1 in range(radius*-2,radius+2):
				if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
					mc.setBlock(x+x1+11,y+y1,z+z1+3,3)
					
	for x1 in range(radius*-2,radius+3):#Eye brow
		for y1 in range(radius*-2,radius+1):
			for z1 in range(radius*-2,radius+2):
				if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
					mc.setBlock(x+x1+11,y+y1,z+z1-3,3)
					
	for x1 in range(radius*-2,radius+3):#Eye brow
		for y1 in range(radius*-2,radius+1):
			for z1 in range(radius*-2,radius+2):
				if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
					mc.setBlock(x+x1+11,y+y1,z+z1-6,3)
					
	for x1 in range(radius*-2,radius+3):#Eye brow
		for y1 in range(radius*-2,radius+1):
			for z1 in range(radius*-2,radius+2):
				if (x1**6)+(y1**2)+(z1**6)<=(radius+6)**2:
					mc.setBlock(x+x1+11,y+y1,z+z1+6,3)
def checkBlock(mc):
	blockEvent=mc.events.pollBlockHits()
	for each in blockEvent:
		x=each.pos.x
		y=each.pos.y
		z=each.pos.z
		if mc.getBlock(x,y,z)==46:
			tnt(mc,x,y,z)


def yo():
    x,y,z = mc.player.getPos()
    matrixrealY(mc,x+5,y,z+11)
    matrixO(mc,x+7,y,z+22)
    x = x -20

def amo():
    x,y,z = mc.player.getPos()
    matrixA(mc,x+9,y,z+36)
    matrixM(mc,x+11,y,z+46)
    matrixO(mc,x+13,y,z+56)
    x = x -20

def matrixA(mc,x,y,z):
    #    1 2 3 4 5 6 7 8 9 10
   m = [[0,0,0,0,0,0,0,0,0,0],#1
        [0,0,0,0,v,0,0,0,0,0],#2
        [0,0,0,v,v,v,0,0,0,0],#3
        [0,0,v,v,0,v,v,0,0,0],#4
        [0,v,v,0,0,0,v,v,0,0],#5
        [v,v,0,0,0,0,0,v,v,0],#6
        [v,0,0,0,0,0,0,0,v,0],#7
        [v,v,v,v,v,v,v,v,v,0],#8
        [v,0,0,0,0,0,0,0,v,0],#9
        [v,0,0,0,0,0,0,0,v,0]]#10
   print(m)
   for k in range (0,10):
        for l  in range (0,10):
            print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 7):
                theBlock = 79;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,9+y-k,z+l,theBlock)
   print()

def matrixB(mc,x,y,z):
    #    1 2 3 4 5 6 7 8 9 10
   m = [[0,0,0,0,0,0,0,0,0,0],#1
        [0,v,v,v,v,v,0,0,0,0],#2
        [0,v,0,0,0,0,v,0,0,0],#3
        [0,v,0,0,0,0,0,v,0,0],#4
        [0,v,0,0,0,0,v,0,0,0],#5
        [0,v,0,0,v,v,v,v,0,0],#6
        [0,v,0,0,0,0,0,v,0,0],#7
        [0,v,0,0,0,0,0,v,0,0],#8
        [0,v,v,v,v,v,v,0,0,0],#9
        [0,0,0,0,0,0,0,0,0,0]]#10
   print(m)
   for k in range (0,10):
        for l  in range (0,10):
            print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 7):
                theBlock = 79;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,9+y-k,z+l,theBlock)
   print()



def matrixO(mc,x,y,z):
    #    1 2 3 4 5 6 7 8 9 10
   m = [[0,0,0,0,0,0,0,0,0,0],#1
        [0,v,v,v,v,v,v,v,v,0],#2
        [0,v,0,0,0,0,0,0,v,0],#3
        [0,v,0,0,0,0,0,0,v,0],#4
        [0,v,0,0,0,0,0,0,v,0],#5
        [0,v,0,0,0,0,0,0,v,0],#6
        [0,v,0,0,0,0,0,0,v,0],#7
        [0,v,0,0,0,0,0,0,v,0],#8
        [0,v,v,v,v,v,v,v,v,0],#9
        [0,0,0,0,0,0,0,0,0,0]]#10
   print(m)
   for k in range (0,10):
        for l  in range (0,10):
            print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 7):
                theBlock = 79;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,9+y-k,z+l,theBlock)
   print()





def matrixM(mc,x,y,z):
    #    1 2 3 4 5 6 7 8 9 10
   m = [[v,v,0,0,0,0,0,0,v,v],#1
        [v,v,v,0,0,0,0,v,v,v],#2
        [v,0,v,v,0,0,v,v,0,v],#3
        [v,0,0,v,v,v,v,0,0,v],#4
        [v,0,0,0,v,v,0,0,0,v],#5
        [v,0,0,0,0,0,0,0,0,v],#6
        [v,0,0,0,0,0,0,0,0,v],#7
        [v,0,0,0,0,0,0,0,0,v],#8
        [v,0,0,0,0,0,0,0,0,v],#9
        [v,0,0,0,0,0,0,0,0,v]]#10
   print(m)
   for k in range (0,10):
        for l  in range (0,10):
            print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 7):
                theBlock = 79;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,9+y-k,z+l,theBlock)
   print()



def matrixrealY(mc,x,y,z):
    #    1 2 3 4 5 6 7 8 9 10
   m = [[v,v,0,0,0,0,0,0,v,v],#1
        [0,v,v,0,0,0,0,v,v,0],#2
        [0,0,v,v,0,0,v,v,0,0],#3
        [0,0,0,v,v,v,v,0,0,0],#4
        [0,0,0,0,v,v,0,0,0,0],#5
        [0,0,0,0,v,v,0,0,0,0],#6
        [0,0,0,0,v,v,0,0,0,0],#7
        [0,0,0,0,v,v,0,0,0,0],#8
        [0,0,0,0,v,v,0,0,0,0],#9
        [0,0,0,0,v,v,0,0,0,0]]#10
   print(m)
   for k in range (0,10):
        for l  in range (0,10):
            print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 7):
                theBlock = 79;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,9+y-k,z+l,theBlock)
   print()



def checkBlock(mc):
	blockEvent=mc.events.pollBlockHits()
	for each in blockEvent:
		x=each.pos.x
		y=each.pos.y
		z=each.pos.z
		if mc.getBlock(x,y,z)==46:
			tnt(mc,x,y,z)

def realtnt():
	while True:
		checkBlock(mc)
		select()



def boomerstatus(mc):
    for i in range (0,1000):
        mc.postToChat("Do you know da wae?")
        sleep(0.1)

def typestuff(mc):
	for i in range (0,20):
		switcher = {
			1:  "Crimson",
			2:  "Logan!!",
			3:  "lblblb!",
			4:  "Bluebur",
			5:  "BenJet1",
			6:  "NoahMcGe",
			7:  "hehexd!",
			8:  "TiToniC",
			9:  "kriptic",
			10: "icebowl",
			11: "whithat",
			12: "redhat!"
		}
		#print ("joined the game")
		mc.postToChat("%s joined the game" % str(switcher.get(random.randint(1, 12))))
		sleep(0.2)













#
#
#
#
#
#MAIN
#MAIN
#MAIN
#MAIN
#MAIN
#
#
#
#
#



def init():
	global mc
	global ipcon
	global b
	b = input("Last num of ip : ")
	mc = Minecraft.create("192.168.7."+b, 4711)
	return mc


def select():
	c = input("\n1.) Post to chat \n2.) Yo Amo \n3.) Noah's tnt \n4.) Fake people join \n5.) Empty \n6.) Empty\nSelect an option : ")
	if (c == "1"):
		print("Type 'Exit' to exit chat")
		chat()
	elif(c == "2"):
		yo()
		amo()
		select()
	elif(c == "3"):
		realtnt()
		select()
	elif(c == "4"):
		typestuff(mc)
		select()
	else:
		print("---------------------------------------------")
		print("Please Select one of the options")
		select()

def chat():
	a = input("Chat : ")
	mc.postToChat(a)
	if (a == "Exit" or a == "exit"):
		main()
	chat()

def main():
	init()
	select()
if __name__ == "__main__":
    main()
