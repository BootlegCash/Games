from time import sleep
import random
''' 
s = smarts
g = game
l = life
d = difficulty
'''

s = 1
g = 1
m = 10
ma = 20
d = 1
sc = 1
gc = 1
class stu():
    def __init__(self, s, g,d):
        self.s = s
        self.g = g
        self.d = d
        
        
gay = stu(1,1,1)
#Skill needed to seduce the teacher
tsc = random.randint(10, 20)
while (gc + sc != tsc):

    sc = random.randint(5, 15)
    gc = random.randint(5, 15)
    
    

        

def gh():
    print("\nDo you want to study or practice?")
    b = input().lower()
    if "s" in b:
        q = random.randint(1, 3)
        gay.s = gay.s +q
        print(gay.s)
        print("\nYou gained ", int(q), "smartness")
        sleep(2)
        st()
    elif "s" in b:
        q = random.randint(1, 3)
        gay.g = gay.g +q
        print(gay.g)
        print("\nYou gained ", int(q), "levels of game")
        sleep(2)
        st()
    else:
        gh()
def st():
    if gay.s>= sc:
        print("\nDo you want to try and seduce the teacher?, y/n")
        y = input().lower()
        if "y" in y:
            if gay.g< gc:
                print("You failed and are expelled from school")

            else:
                print("You seduced the teacher")
        elif "n" in y:
            day()
    
    else:
        day()
        
        
def day():
    print("Gc: ", int(gc))
    print("Sc: ",int(sc))

    print("\nYou have just woken up time to go to school")
    print("\nTime to answer the question")
    x = input(" \nWhat do you want to do answer, cheat, or guess randomly or check your stats ")
    if "s" in x:
        print("These are your stat")
        print("Smarts:", gay.s)
        print("Game: ", gay.g)
        input("Press enter to continue")
        day()
    elif "ch" in x:
        if g >= d:
            print("You passed today, you may leave")
            gay.d = gay.d +1
            gh()
        else:
            print("You failed, You are expelled")
    elif "an" in x:
        if s >= d:
            print("You passed today, you may leave")
            gay.d = gay.d +1
            gh()
        else:
            print("The teacher caught you cheating, You are expelled")
    elif "ra" in x:
        if random.randint(1, 20) == 1:
            print("You passed today, you may leave")
            gay.d = gay.d +1
            gh()
        else:
            print("You failed, You are expelled")
    else:
        day()
    
    
        


input("Are you ready to play, press enter")


print("\nSo you are in a math class and your goal is to seduce the teacher")
sleep(2)
print("\nTo seduce the teacher you will have to be smart enough to catch her attention and have enough game to seduce her")
sleep(3)
print("\nTo increase your stats you will have to study or either increase your game, you will be able to do one after school, then go to school the next day, and answer a math question to finish school")
sleep(4)
print("\nTo answer the math questions you will have to do a skill check, or randomly guess it")
sleep (1)
day()


    