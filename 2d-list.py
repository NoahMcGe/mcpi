from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
v=246
def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    #mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc
'''
def matrixZ(mc,x,y,z):
    m = [[5,5,1,1,1,1,1,1,4,4],
        [5,5,7,7,7,7,7,7,4,4],
        [1,1,7,7,7,7,7,7,1,1],
        [1,1,1,1,7,7,1,1,1,1],
        [1,1,1,1,7,7,1,1,1,1],
        [1,1,1,1,7,7,1,1,1,1],
        [1,1,1,1,7,7,1,1,1,1],
        [1,1,7,7,7,7,5,5,1,1],
        [1,1,7,7,7,7,5,5,1,1],
        [1,1,1,1,1,1,1,1,1,1]]
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
'''








#Start
#Start
#Start
#Start
#Start
#Start








def matrixblank(mc,x,y,z):
    #    1 2 3 4 5 6 7 8 9 10
   m = [[0,0,0,0,0,0,0,0,0,0],#1
        [0,0,0,0,0,0,0,0,0,0],#2
        [0,0,0,0,0,0,0,0,0,0],#3
        [0,0,0,0,0,0,0,0,0,0],#4
        [0,0,0,0,0,0,0,0,0,0],#5
        [0,0,0,0,0,0,0,0,0,0],#6
        [0,0,0,0,0,0,0,0,0,0],#7
        [0,0,0,0,0,0,0,0,0,0],#8
        [0,0,0,0,0,0,0,0,0,0],#9
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












'''





def matrixY(mc,x,y,z):
    m = [[1,1,1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,1],
     [0,0,0,0,0,0,0,0,1,1],
     [1,1,1,1,1,1,1,0,0,1],
     [1,1,1,0,1,1,1,0,1,1],
     [1,1,1,0,1,1,1,0,0,1],
     [1,1,1,0,0,0,0,0,1,1],
     [1,1,1,1,1,1,1,0,0,1],
     [1,1,1,1,1,1,1,1,0,1],
     [1,1,1,1,1,1,1,1,1,1]]
    print(m)
    for h in range (0,10):
        for l  in range (0,10):
            print(m[h][l],end="")
            mc.setBlocks(x+h,y-5, z+l, x+h,y+20,z+l,m[h][l])

    print()
    mc.setBlocks(x-1,y-5, z-1, x+11,y-5,z+11,89)
    mc.setBlocks(x-1,y+10, z-1, x+11,y+10,z+11,89)
    mc.setBlocks(x-1,y+20, z-1, x+11,y+20,z+11,89)
'''
def yo():
    mc = init()
    x,y,z = mc.player.getPos()
    matrixrealY(mc,x+5,y,z+11)
    matrixO(mc,x+7,y,z+22)
    x = x -20

def amo():
    mc = init()
    x,y,z = mc.player.getPos()
    matrixA(mc,x+9,y,z+36)
    matrixM(mc,x+11,y,z+46)
    matrixO(mc,x+13,y,z+56)
    x = x -20

def main():
    yo()
    amo()
'''
matrixA
matrixB
matrixO
matrixrealY

'''



if __name__ == "__main__":
    main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
