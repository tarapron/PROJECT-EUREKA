"""Names: FLORES, PETER JOHN (2018-09423)
          PATIO, PAUL ALLEN TRISTAN(2018-11844)
          SUPANGA, BEA ROSARI (2018-10282)"""


import pygame
import datetime
import pickle

pygame.init()
HP = 100
DEF = 5
ATK = 10
gold = 100
gold1 = 0
width = 1800
height = 900
Edamage = 5
ally = 0
info = 0
ability = 0
parts = ""
gameDisplay = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption('PROJECT:EUREKA')


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (34,177,76)
lightgreen = (0, 255, 0)
blue = (255,239,213)
lightblue = (238,213,183)

smallfont = pygame.font.SysFont("unispacebold", 15)
medfont = pygame.font.SysFont("unispacebold", 50)
largefont = pygame.font.SysFont("unispacebold", 85)
clock = pygame.time.Clock()

print(pygame.font.get_fonts())
def loadimage(image, pos_x, pos_y):
    gameDisplay.blit(image, (pos_x, pos_y))

def getgold():
    return gold1

def getgold2():
    return gold

def getATK():
    return ATK

def getDEF():
    return DEF

def getHP():
    return HP

def getALLY():
    return ally

def getINFO():
    return info

def getABI():
    return ability
def getPART():
    return parts
def getDATE():
    """"gets date and time"""
    now = datetime.datetime.now()
    ey = now.strftime("%Y-%m-%d %H:%M")
    return ey

def textbutton(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    """"places text inside the buttons and centers it"""
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, color,size = "small"):
    """"Size of text"""
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def button(text, x, y, width, height, inactive_color, active_color,action = None,part = 27):
    """"function for creating buttons and allowin actions on mouseclick"""
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1:
            if action == "start":
                starting()
            elif action == "next":
                screen1()
            elif action =="next1":
                screen2()
            elif action =="next2":
                screen3()
            elif action =="next3":
                screen4()
            elif action =="next4":
                screen5()
            elif action =="next5":
                screen6()
            elif action =="next6":
                screen7()
            elif action =="next7":
                screen8()
            elif action =="next8":
                screen9()
            elif action =="next9":
                screen10()
            elif action =="next10":
                screen11()
            elif action =="next11":
                screen12()
            elif action =="next12":
                battle1()
            elif action =="next13":
                screen14()
            elif action =="next14":
                screen15()
            elif action =="next15":
                screen16()
            elif action =="next16":
                screen17()
            elif action =="next17":
                screen18()
            elif action =="next18":
                screen19()
            elif action =="next19":
                screen20()
            elif action =="next20":
                screen21()
            elif action =="next21":
                screen22()
            elif action =="next22":
                screen23()
            elif action =="next23":
                screen24()
            elif action =="next24":
                screen25()
            elif action =="next25":
                screen26()
            elif action =="next26":
                screen27()
            elif action =="next27":
                screen28()
            elif action =="next28":
                screen29()
            elif action =="next29":
                screen30()
            elif action =="next30":
                screen31()
            elif action =="next31":
                screen32()
            elif action =="next32":
                screen33()
            elif action =="next33":
                screen34()
            elif action =="next341":
                screen35()
            elif action =="next342":
                global ally
                ally = 1
                screen35()
            elif action =="next35":
                screen36()
            elif action =="next36":
                screen37()
            elif action =="next37":
                screen38()
            elif action =="next38":
                screen39()
            elif action =="next39":
                screen40()
            elif action =="next40":
                screen41()
            elif action =="next41":
                screen42()
            elif action =="next42":
                screen43()
            elif action =="next43":
                screen44()
            elif action =="next44":
                screen45()
            elif action =="next45":
                screen46()
            elif action =="next46":
                screen47()
            elif action =="next47":
                screen48()
            elif action =="next48":
                screen49()
            elif action =="next49":
                screen50()
            elif action =="next50":
                screen51()
            elif action =="next51":
                screen52()
            elif action =="next52":
                screen53()
            elif action =="next53":
                screen54()
            elif action =="next54":
                screen55()
            elif action =="next55":
                screen56()
            elif action =="next56":
                screen57()
            elif action =="next57":
                screen58()
            elif action =="next58":
                screen59()
            elif action =="next59":
                screen60()
            elif action =="next60":
                screen61()
            elif action =="next61":
                screen62()
            elif action =="next62":
                screen63()
            elif action =="next63":
                screen64()
            elif action =="next64":
                screen65()
            elif action =="next65":
                screen66()
            elif action =="next66":
                screen67()

            elif action =="next167":
                screen167()
            elif action =="next1681":
                global info
                info = 1
                screen169()
            elif action =="next1682":
                global gold
                gold = getgold2() + 200
                screen169()
            elif action =="next169":
                screen170()
            elif action =="next170":
                screen171()
            elif action =="next171":
                screen172()
            elif action =="next172":
                screen173()
            elif action =="next173":
                screen174()
            elif action =="next174":
                screen175()
            elif action =="next175":
                screen176()
            elif action =="next176":
                screen177()
            elif action =="next177":
                screen178()
            elif action =="next178":
                screen179()
            elif action =="next179":
                screen180()
            elif action =="next180":
                screen181()
            elif action =="next181":
                screen182()
            elif action =="next182":
                screen183()
            elif action =="next183":
                screen184()
            elif action =="next184":
                screen185()
            elif action =="next185":
                screen186()
            elif action =="next1861":
                global ability
                ability = 1
                screen187()
            elif action == "next1862":
                screen187()
            elif action =="next187":
                screen188()
            elif action =="next188":
                screen189()
            elif action =="next189":
                screen190()
            elif action =="next190":
                screen191()
            elif action =="next191":
                screen192()

            elif action =="next266":
                screen267()
            elif action =="next267":
                screen268()
            elif action =="next268":
                screen269()
            elif action =="next269":
                screen270()
            elif action =="next270":
                screen271()
            elif action =="next271":
                screen272()
            elif action =="next272":
                screen273()
            elif action =="next273":
                screen274()
            elif action =="next274":
                screen275()
            elif action =="next273":
                screen274()
            elif action =="next274":
                screen275()
            elif action =="next275":
                screen276()
            elif action =="next276":
                screen277()
            elif action =="next277":
                screen278()
            elif action =="next278":
                screen279()
            elif action =="next279":
                screen280()
            elif action =="next280":
                screen281()
            elif action =="next281":
                screen282()
            elif action =="next282":
                screen283()
            elif action =="next283":
                screen284()
            elif action =="next284":
                screen285()
            elif action =="next285":
                screen286()
            elif action =="next286":
                screen287()

            elif action =="shop":
                screen27(part-1)
            elif action =="ATK1":
                damage = getATK()
                return damage
            elif action =="DEF1":
                defd = getDEF()*2
                return defd
            elif action =="PAS1":
                damage = getATK()
                return damage

            elif action =="ATK":
                lvl2()
            elif action =="DEF":
                lvl3()
            elif action =="HP":
                lvl1()

            elif action =="mommy":
                mommy()

            elif action =="ATK2":
                lvl22()
            elif action =="DEF2":
                lvl33()
            elif action =="HP2":
                lvl11()

            elif action =="ATK+":
                return 1
            elif action =="DEF+":
                return 1
            elif action =="HP+":
                return 2

            elif action =="choice1":
                choice1()
            elif action =="choice2":
                choice2()
            elif action =="choice3":
                choice3()

            elif action =="battle2":
                battle2()
            elif action =="battle3":
                rescue()
            elif action =="train":
                train()
            elif action =="pay":
                pay1()

            elif action =="battle4":
                battle4()
            elif action =="battle5":
                rescue1()
            elif action =="train1":
                train1()
            elif action =="pay1":
                pay11()

            elif action =="battlebad1":
                battlebad1()
            elif action =="battlebad2":
                battlebad2()
            elif action =="battlebad3":
                battlebad3()
            elif action == "battlebad4":
                battlebad4()
            elif action =="rescue2":
                rescue2()
            elif action =="train2":
                train2()
            elif action =="pay2":
                pay12()
            elif action =="battle6":
                battle6()

            elif action =="yes":
                return "yes"
            elif action =="no":
                return "no"

            elif action =="battlegood1":
                battlegood1()
            elif action =="battlegood2":
                battlegood2()
            elif action =="battlegood3":
                battlegood3()
            elif action =="battlegood4":
                battlegood4()
            elif action =="battlegood5":
                battlegood5()
            elif action =="battlegood6":
                battlegood6()
            elif action =="battlegood7":
                battlegood7()

            elif action == "screenbad":
                screenbad()
            elif action == "screenbadd":
                screenbadd()
            elif action == "screenbaddd":
                screenbaddd()
            elif action == "screenbadd2":
                screenbadd2()
            elif action == "screenbaddd2":
                screenbaddd2()

            elif action == "gooda1":
                gooda1()
            elif action == "gooda2":
                gooda2()
            elif action == "gooda3":
                gooda3()
            elif action == "gooda4":
                gooda4()
            elif action == "gooda5":
                gooda5()

            elif action == "credits":
                credits()
            elif action == "credits2":
                credits2()
            elif action == "intro":
                intro()
            elif action == "save":
                save(part)
            elif action == "load":
                load(part)
            elif action == "savescreen":
                savescreen(part)
            elif action == "loadscreen":
                loadscreen()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
    textbutton(text,black,x,y,width,height)

def messagescreen(msg, color, y_displace=0, size="small"):
    """"Places messages on screen"""
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(1800 / 2), int(900 / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)

def loadscreen():
    """"Load screen function"""
    intro = True
    gameDisplay.fill(black)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        messagescreen("LOAD SCREEN", white, -300, "large")
        button(loadate(1), 100, 300, 700, 50, blue, lightblue, "load", 1)
        button(loadate(2), 100, 400, 700, 50, blue, lightblue, "load", 2)
        button(loadate(3), 100, 500, 700, 50, blue, lightblue, "load", 3)
        button(loadate(4), 100, 600, 700, 50, blue, lightblue, "load", 4)
        button(loadate(5), 100, 700, 700, 50, blue, lightblue, "load", 5)
        button(loadate(6), 1000, 300, 700, 50, blue, lightblue, "load", 6)
        button(loadate(7), 1000, 400, 700, 50, blue, lightblue, "load", 7)
        button(loadate(8), 1000, 500, 700, 50, blue, lightblue, "load", 8)
        button(loadate(9), 1000, 600, 700, 50, blue, lightblue, "load", 9)
        button(loadate(10), 1000, 700, 700, 50, blue, lightblue, "load", 10)
        pygame.display.update()

def savescreen(part):
    """"savescreen function"""
    intro = True
    gameDisplay.fill(black)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        messagescreen("SAVE SCREEN", white, -300, "large")
        button(loadate(1), 100, 300, 700, 50, blue, lightblue, "save",1)
        button(loadate(2), 100, 400, 700, 50, blue, lightblue, "save",2)
        button(loadate(3), 100, 500, 700, 50, blue, lightblue, "save",3)
        button(loadate(4), 100, 600, 700, 50, blue, lightblue, "save",4)
        button(loadate(5), 100, 700, 700, 50, blue, lightblue, "save",5)
        button(loadate(6), 1000, 300, 700, 50, blue, lightblue, "save",6)
        button(loadate(7), 1000, 400, 700, 50, blue, lightblue, "save",7)
        button(loadate(8), 1000, 500, 700, 50, blue, lightblue, "save",8)
        button(loadate(9), 1000, 600, 700, 50, blue, lightblue, "save",9)
        button(loadate(10), 1000, 700, 700, 50, blue, lightblue, "save",10)
        button("Go Back", 1600, 800, 100, 50, blue, lightblue,"next"+str(part-1))
        pygame.display.update()

def save(part):
    """"saves to a file"""
    save = [getPART(),getHP(),getATK(),getDEF,getALLY(),getINFO(),getABI(),getgold(),getgold2(),getDATE()]
    pickle_out = open("save"+str(part)+".pickle","wb")
    pickle.dump(save,pickle_out)
    pickle_out.close()

def loadate(part):
    """"loads the date and time from the saved file"""
    pickle_in = open("save"+str(part)+".pickle","rb")
    data = pickle.load(pickle_in)
    DATE = data[9]
    return DATE

def load(part):
    """"loads the file"""
    global parts,HP,ATK,DEF,ALLY,ability,gold1,gold
    pickle_in = open("save"+str(part)+".pickle","rb")
    data = pickle.load(pickle_in)
    parts = data[0]
    HP = data[1]
    ATK = data[2]
    DEF = data[3]
    ALLY = data[4]
    info = data[5]
    ability = data[6]
    gold1 = data[7]
    gold = data[8]
    DATE = data[9]
    eval(parts)

def intro():
    """"starts the game"""
    intro = True
    gameDisplay.fill(white)
    bg = pygame.image.load('ProjectEureka.jpg')
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("NEW GAME", 800, 425, 200, 50, blue, lightblue, "start")
        button("LOAD GAME", 800, 500, 200, 50, blue, lightblue, "loadscreen")
        pygame.display.update()

def starting():
    """"starting scenes. all others that follor are similar"""
    global parts
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    parts = "starting()"
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: well One day Ericka, you are gonna do great things.You will have a greater impact in today’s society!", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen")
        pygame.display.update()

def screen1():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Mother: Calm down, don’t pressure her. Just let her grow up at her once pace.", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next1")
        global parts
        parts = "screen1()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen",1)
        pygame.display.update()
def screen2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: Okay, Honey. We love you, Ericka.", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next2")
        global parts
        parts = "screen2()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 2)
        pygame.display.update()
def screen3():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: Okay, Honey. We love you, Ericka.", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next3")
        global parts
        parts = "screen3()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 3)
        pygame.display.update()
def screen4():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: What a weird dream….. Who were those people? Nevermind, I’ll just go to breakfast.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next4")
        global parts
        parts = "screen4()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 4)
        pygame.display.update()
def screen5():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: Oh, hey Eureka, how was your sleep? We got a long day ahead of us.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next5")
        global parts
        parts = "screen5()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 5)
        pygame.display.update()
def screen6():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: Yeah, I know. I had this weird dream about two people, and they were like, talking to me. I can’t remember much anymore though.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next6")
        global parts
        parts = "screen6()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 6)
        pygame.display.update()
def screen7():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: Huh, that is weird. Maybe you have met them somewhere in the past before?", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next7")
        global parts
        parts = "screen7()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 7)
        pygame.display.update()
def screen8():
    global parts
    parts = "screen8()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: That’s impossible. For as long as I remember, I have grown up in this organization. Training day-by-day to become the best assassin to make my father proud.", 100, 700, 1500, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next8")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 8)
        pygame.display.update()
def screen9():
    global parts
    parts = "screen9()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: It must be hard to live up to your father, the head of the enterprise.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next9")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 9)
        pygame.display.update()
def screen10():
    global parts
    parts = "screen10()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: Yeah, but I won’t give up.  *ALARM RINGS*", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next10")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 10)
        pygame.display.update()
def screen11():
    global parts
    parts = "screen11()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: It’s time for training. Good luck out there.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next11")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 11)
        pygame.display.update()
def screen12():
    global parts
    parts = "screen12()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: Hello Eureka you know the drill (100HP,5 DEF, 10ATK)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next12")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 12)
        pygame.display.update()
def battle1():
    """"template for battles"""
    global parts
    parts = "battle1()"
    HP=100
    EHP=75
    Edamage = 10
    DEF = 5
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2-1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen13()
        pygame.display.update()
def screen13():
    global parts
    parts = "screen13()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(100g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next13")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 13)
        button(str(gold)+"g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen14():
    global parts
    parts = "screen14()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: Now head over to the armory to get suited up", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next14")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 14)
        pygame.display.update()
def screen15():
    global parts
    parts = "screen15()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.jpg')
    gold = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Blacksmith: I got 3 fine weapons for you take your pick", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next15")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 15)
        button(str(gold) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen16():
    global parts
    parts = "screen16()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene6Shop.jpg')
    gold = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        damage = button("Electric Sword (60g)", 300, 600, 1200, 50, blue, lightblue, "choice1")
        damage2 = button("Dagger (50g)", 300, 700, 1200, 50, blue, lightblue, "choice2")
        damage3 = button("Electric Warhammer (75g)", 300, 800, 1200, 50, blue, lightblue, "choice3")
        button(str(gold) + "g", 1500, 100, 150, 50, blue, lightblue)
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen",16)
        pygame.display.update()
def choice1():
    global parts
    parts = "choice1()"
    global gold1
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Blacksmith: Great choice! Your ATK is now at 12", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next16")
        button(str(gold-60) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
        gold1 = gold-60
        global ATK
        ATK = 12
def choice2():
    global parts
    parts = "choice2()"
    global gold1
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Blacksmith: Great choice! Your ATK is now at 9", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next16")
        button(str(gold-50) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
        gold1 = gold-50
        global ATK
        ATK = 9
def choice3():
    global parts
    parts = "choice3()"
    global gold1
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Blacksmith: Great choice! Your ATK is now at 15", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next16")
        button(str(gold-75) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
        gold1 = gold-75
        global ATK
        ATK = 15
def screen17():
    global parts
    parts = "screen17()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: Great youre back! time to choose the next mission", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next17")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 17)
        button(str(getgold()) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen18():
    global parts
    parts = "screen18()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Battle enemies (2 enemies with stats: Health: 60, Defense: 0, Damage: 15. Gold reward: 200)", 300, 600, 1200, 50, blue, lightblue, "battle2")
        button("Rescue. Gold reward(100g)", 300, 700, 1200, 50, blue, lightblue, "battle3")
        button("or training (After may choose to upgrade Health by 10, Damage by 5, or Defense by 5)", 300, 800, 1200, 50, blue, lightblue, "train")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 18)
        pygame.display.update()
def battle2():
    global parts
    parts = "battle2()"
    global HP
    HP=100
    EHP=60
    Edamage = 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            battle21()
        pygame.display.update()
def battle21():
    global parts
    parts = "battle21()"
    HP=getHP()
    EHP=60
    Edamage = 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen19()
        pygame.display.update()
def screen19():
    global parts
    parts = "screen19()"
    global gold1,HP
    HP = 100
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold()
    gold1 = gold + 200
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(200g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 19)
        button(str(gold1)+"g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def train():
    global parts
    parts = "train()"
    HP = 100
    EHP = 70
    Edamage = 0
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2-1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            level()
        pygame.display.update()
def level():
    global parts
    parts = "level()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("ADD 10 TO MAX HP", 300, 600, 1200, 50, blue, lightblue, "HP")
        button("ADD 5 TO MAX DAMAGE", 300, 700, 1200, 50, blue, lightblue, "ATK")
        button("ADD 5 TO MAX DEFENSE", 300, 800, 1200, 50, blue, lightblue, "DEF")
        pygame.display.update()
def lvl1():
    global parts
    parts = "lvl1()"
    global HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    HP = 110
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your HP is now at 110 ", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        pygame.display.update()
def lvl2():
    global parts
    parts = "lvl2()"
    global ATK,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    ATK = getATK() + 5
    HP = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your ATK is now at "+str(ATK), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        pygame.display.update()
def lvl3():
    global parts
    parts = "lvl3()"
    global DEF,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    DEF = getDEF()+5
    HP = 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("GOD: Great choice! Your DEF is now at "+str(DEF), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        pygame.display.update()
def rescue():
    global parts
    parts = "rescue()"
    global HP
    HP = 100
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Saving.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("You found her goodjob! now head back to the boss", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "pay")
        pygame.display.update()
def pay1():
    global parts
    parts = "pay1()"
    global gold1
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold()
    gold1 = gold + 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(100g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next19")
        button(str(gold1) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen20():
    global gold1
    global parts
    parts = "screen20()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Welcome back. Your next mission is to gather information on a possibly threatening corporation.", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next20")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 20)
        pygame.display.update()
def screen21():
    global parts
    parts = "screen21()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene5final.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: There seems to be an important conversation ongoing, moving in to eavesdrop", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next21")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 21)
        pygame.display.update()
def screen22():
    global parts
    parts = "screen22()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene5final.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: *that man seems familiar who could he be*", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next22")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 22)
        pygame.display.update()
def screen23():
    global parts
    parts = "screen23()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene5final.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Familiar man: WE ARE ABOUT TO MAKE A BREAKTHROUGH THAT CAN CHANGE THE FUTURE FOR HUMANS", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next23")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 23)
        pygame.display.update()
def screen24():
    global parts
    parts = "screen24()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene5final.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: Id better report this to the boss", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next24")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 24)
        pygame.display.update()
def screen25():
    global parts
    parts = "screen25()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: *relays information*", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next25")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 25)
        pygame.display.update()
def screen26():
    global parts
    parts = "screen26()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: this is quite the situation we have on our hands. Head over to the shop to gear up", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next26")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 26)
        pygame.display.update()
def screen27(part = 28):
    global parts
    parts = "screen27()"
    global HP,ATK,DEF,gold1
    goldminus = 0
    part = part
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Stats.jpg')
    HP = getHP()
    ATK = getATK()
    DEF = getDEF()
    DEF1 = getDEF()
    HP1 = getHP()
    ATK1 = getATK()
    gold = getgold()
    gold2 = getgold2()
    ans = "ey"
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("HP" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ATK" + str(ATK), 1500, 200, 150, 50, blue, lightblue)
        button("DEF" + str(DEF), 1500, 300, 150, 50, blue, lightblue)
        button(str(gold) + "g", 1200, 100, 150, 50, blue, lightblue)
        HPadd = button("ADD 2 TO MAX HP(5g)", 300, 600, 1200, 50, blue, lightblue, "HP+")
        ATKadd = button("ADD 1 TO MAX DAMAGE(5g)", 300, 700, 1200, 50, blue, lightblue, "ATK+")
        DEFadd = button("ADD 1 TO MAX DEFENSE(5g)", 300, 800, 1200, 50, blue, lightblue, "DEF+")
        button("next", 1600, 800, 100, 50, blue, lightblue, "next"+str(part))
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 27)
        if HPadd == None:
            HPadd = 0
        if ATKadd == None:
            ATKadd = 0
        if DEFadd == None:
            DEFadd = 0
        if gold <=0:
            button("NO MORE GOLD TO SPEND!!", 600, 350, 300, 50, blue, lightblue)
            button("next", 1600, 800, 100, 50, blue, lightblue, "next"+str(part))
        else:
            HP = getHP() + HPadd
            ATK = getATK() + ATKadd
            DEF = getDEF() + DEFadd
            goldminus = (HPadd/2)*5 + ATKadd*5 + DEFadd*5
            gold = gold - goldminus
        if DEF1 != DEF:
            button("are you happy with your selection of this number of points to DEF:" + str(DEF - DEF1), 600, 300, 600, 50, blue, lightblue)
            ans = button("Yes", 600, 400, 150, 50, blue, lightblue, "yes")
            ans2 = button("No", 800, 400, 150, 50, blue, lightblue, "no")
            if ans == "yes":
                button("UPGRADE SUCCESSFUL", 600, 350, 300, 50, blue, lightblue)
            elif ans2 == "no":
                HP = HP1
                ATK = ATK1
                DEF = DEF1
                screen27(part)
        if ATK1 != ATK:
            button("are you happy with your selection of this number of points to ATK:" + str(ATK - ATK1), 600, 250, 600, 50, blue, lightblue)
            ans = button("Yes", 600, 400, 150, 50, blue, lightblue, "yes")
            ans2 = button("No", 800, 400, 150, 50, blue, lightblue, "no")
            if ans == "yes":
                button("UPGRADE SUCCESSFUL", 600, 350, 300, 50, blue, lightblue)
            elif ans2 == "no":
                HP = HP1
                ATK = ATK1
                DEF = DEF1
                screen27(part)
        if HP1 != HP:
            button("are you happy with your selection of this number of points to HP:" + str(HP - HP1), 600, 200, 600, 50, blue, lightblue)
            ans = button("Yes", 600, 400, 150, 50, blue, lightblue, "yes")
            ans2 = button("No", 800, 400, 150, 50, blue, lightblue, "no")
            if ans == "yes":
                button("UPGRADE SUCCESSFUL", 600, 350, 300, 50, blue, lightblue)
            elif ans2 == "no":
                HP = HP1
                ATK = ATK1
                DEF = DEF1
                screen27(part)
        pygame.display.update()


def screen28():
    global parts
    parts = "screen28()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: While plans are being made i have other tasks for you", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next28")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 28)
        button(str(getgold2()) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen29():
    global parts
    parts = "screen29()"
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Battle enemies (2 enemies with stats: Health: 60, Defense: 0, Damage: 15. Gold reward: 200)", 300, 600, 1200, 50, blue, lightblue, "battle4")
        button("Rescue. Gold reward(100g)", 300, 700, 1200, 50, blue, lightblue, "battle5")
        button("or training (After may choose to upgrade Health by 10, Damage by 5, or Defense by 5)", 300, 800, 1200, 50, blue, lightblue, "train1")
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 29)
        pygame.display.update()
def battle4():
    global parts
    parts = "battle4()"
    global HP
    HP=getHP()
    EHP=60
    Edamage = 12
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            battle41()
        pygame.display.update()
def battle41():
    global parts
    parts = "battle41()"
    HP=getHP()
    EHP=60
    Edamage = 12
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen30()
        pygame.display.update()
def screen30():
    global gold,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold2()
    gold = gold + 200
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(200g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        button(str(gold)+"g", 1500, 100, 150, 50, blue, lightblue)
        global parts
        parts = "screen30()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 30)
        pygame.display.update()
def train1():
    global HP
    Edamage = 12
    EHP = 60
    HP = getHP()
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2-1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            level1()
        pygame.display.update()
def level1():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("ADD 10 TO MAX HP", 300, 600, 1200, 50, blue, lightblue, "HP2")
        button("ADD 5 TO MAX DAMAGE", 300, 700, 1200, 50, blue, lightblue, "ATK2")
        button("ADD 5 TO MAX DEFENSE", 300, 800, 1200, 50, blue, lightblue, "DEF2")
        pygame.display.update()
def lvl11():
    global HP
    HP = getHP() + 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your HP is now at " + str(HP), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        pygame.display.update()
def lvl22():
    global ATK,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    ATK = getATK() + 5
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your ATK is now at "+str(ATK), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        pygame.display.update()
def lvl33():
    global DEF,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    DEF = getDEF()+5
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("GOD: Great choice! Your DEF is now at "+str(DEF), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        pygame.display.update()
def rescue1():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Saving.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("You found her goodjob! now head back to the boss", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "pay1")
        pygame.display.update()
def pay11():
    global gold
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold2()
    gold = gold + 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(100g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next30")
        button(str(gold) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()
def screen31():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene8.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka: *HUH AM I DREAMING AGAIN?? WHAT IS THIS!??*", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next31")
        global parts
        parts = "screen31()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 31)
        pygame.display.update()
def screen32():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene8.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("SUPER HUMAN ARMY AND CHAOS REIGNS", 300, 700, 1200, 50,blue,lightblue )
        button("next", 1600, 800, 100, 50, blue, lightblue,"next32")
        global parts
        parts = "screen32()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 32)
        pygame.display.update()
def screen33():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("113: Hey you dont look so good?", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next33")
        global parts
        parts = "screen33()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 33)
        pygame.display.update()
def screen34():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Its nothing dont mind me", 300, 600, 1200, 50, blue, lightblue, "next341")
        button("I had this dream... (explain)", 300, 700, 1200, 50, blue, lightblue, "next342")
        global parts
        parts = "screen34()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 34)
        pygame.display.update()
def screen35():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("*EUREKA PLEASE HEAD TO THE HEAD OFFICE IMMEDIATELY*", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next35")
        global parts
        parts = "screen35()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 35)
        pygame.display.update()
def screen36():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop",36)
        button("BOSS: Your next mission is to infiltrate the corporation and kidnap an important asset", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next36")
        global parts
        parts = "screen36()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 36)
        pygame.display.update()
def screen37():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('EEE.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 37)
        button("EUREKA: looks like i can fight the guards or simply sneak through the ventilation shaft", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next37")
        global parts
        parts = "screen37()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 37)
        pygame.display.update()
def screen38():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('EEE.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 38)
        button("FIGHT GUARDS (earn 200g)", 300, 600, 1200, 50, blue, lightblue, "battle6")
        button("Sneak in", 300, 700, 1200, 50, blue, lightblue, "next38")
        global parts
        parts = "screen38()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 38)
        pygame.display.update()
def battle6():
    global HP
    HP=getHP()
    EHP=150
    Edamage = 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10guards.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop",)
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        HP -= (damage/getATK())*10 - damage2 + damage3
        EHP -= damage
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen39()
        pygame.display.update()
def screen39():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10guards.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 39)
        button("Eureka: id better head to the ventilation room", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next39")
        global parts
        parts = "screen39()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 39)
        pygame.display.update()
def screen40():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Vent.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 40)
        button("Eureka: I made it in alive", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next40")
        global parts
        parts = "screen40()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 40)
        pygame.display.update()
def screen41():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Vent.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 41)
        button("Eureka: Am i really doing the right thing right now?", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next41")
        global parts
        parts = "screen41()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 41)
        pygame.display.update()
def screen42():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Vent.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 42)
        button("Eureka: why am i suddenly thinking about this i should complete the mission", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next42")
        global parts
        parts = "screen42()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 42)
        pygame.display.update()
def screen43():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 43)
        button("Eureka: *there he is, i should capture him immediately*", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next43")
        global parts
        parts = "screen43()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 43)
        pygame.display.update()
def screen44():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 44)
        button("Familiar man: Ive been expecting you", 300, 700, 1200, 50, blue, lightblue, )
        button("next", 1600, 800, 100, 50, blue, lightblue, "next44")
        global parts
        parts = "screen44()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 44)
        pygame.display.update()
def screen45():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 45)
        button("Eureka: how did you know i was coming", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next45")
        global parts
        parts = "screen45()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 45)
        pygame.display.update()
def screen46():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 46)
        button("Familiar man: Its because you need my expertise to complete VENOM", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next46")
        global parts
        parts = "screen46()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 46)
        pygame.display.update()
def screen47():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene11.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 47)
        button("Familiar man: Youre not taking me alive if thats what you are thinking because VENOM will lead to the end of the Human race", 300, 700, 1200, 50, blue, lightblue, )
        button("next", 1600, 800, 100, 50, blue, lightblue, "next47")
        global parts
        parts = "screen47()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 47)
        pygame.display.update()
def screen48():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 48)
        button("Familiar man: ERICKA IS THAT YOU??", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next48")
        global parts
        parts = "screen48()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 48)
        pygame.display.update()
def screen49():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 49)
        button("Ericka: *where have i heard that name before*", 300, 700, 1200, 50, blue, lightblue, )
        button("next", 1600, 800, 100, 50, blue, lightblue, "next49")
        global parts
        parts = "screen49()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 49)
        pygame.display.update()
def screen50():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 50)
        button("Father: well One day Ericka, you are gonna do great things.You will have a greater impact in today’s society!",300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next50")
        global parts
        parts = "screen50()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 50)
        pygame.display.update()
def screen51():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 51)
        button("Ericka: WHO THE HELL ARE YOU AND WHY DID YOU CALL ME THAT NAME", 300, 700, 1200, 50, blue, lightblue, )
        button("next", 1600, 800, 100, 50, blue, lightblue, "next51")
        global parts
        parts = "screen51()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 51)
        pygame.display.update()
def screen52():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 52)
        button("Familiar man: because i am your father...", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next52")
        global parts
        parts = "screen52()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 52)
        pygame.display.update()
def screen53():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 53)
        button("Ericka: THATS IMPOSSIBLE MY FATHER IS THE BOSS OF EEE NOT YOU!", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next53")
        global parts
        parts = "screen53()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 53)
        pygame.display.update()
def screen54():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene12.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 54)
        button("Familiar man: Let me explain what happened", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next54")
        global parts
        parts = "screen54()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 54)
        pygame.display.update()
def screen55():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 55)
        button("Familiar man: Your mother and i were the leading experts in human genetics at our prime", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next55")
        global parts
        parts = "screen55()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 55)
        pygame.display.update()
def screen56():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 56)
        button("Familiar man: Then we got an offer from EEE but it seemed shady at the time so we declined", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next56")
        global parts
        parts = "screen56()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 56)
        pygame.display.update()
def screen57():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 57)
        button("Familiar man: we never heard from them since that time", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next57")
        global parts
        parts = "screen57()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 57)
        pygame.display.update()
def screen58():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 58)
        button("Familiar man: A few years later we had you", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next58")
        global parts
        parts = "screen58()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 58)
        pygame.display.update()
def screen59():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 59)
        button("Familiar man: however your mother had complications with your birth and she became weak", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next59")
        global parts
        parts = "screen59()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 59)
        pygame.display.update()
def screen60():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 60)
        button("Familiar man: after a few more years we had a picnic when we got ambushed", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next60")
        global parts
        parts = "screen60()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 60)
        pygame.display.update()
def screen61():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 61)
        button("Familiar man: we were tranquilized and when we woke up you were gone", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next61")
        global parts
        parts = "screen61()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 61)
        pygame.display.update()
def screen62():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 62)
        button("Familiar man: your mother became weaker and that motivated me to create a serum to keep her alive", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next62")
        global parts
        parts = "screen62()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 62)
        pygame.display.update()
def screen63():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene13.3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 63)
        button("Father: because i perfected the serum EEE wants to use me to create an army of superhumans", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next63")
        global parts
        parts = "screen63()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 63)
        pygame.display.update()
def screen64():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('SCENE14superfinal.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 64)
        button("Eureka: *what do i do now, do i go back to the boss or betray them*", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next64")
        global parts
        parts = "screen64()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 64)
        pygame.display.update()
def screen65():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('SCENE14superfinal.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 65)
        button("Father: Ericka do you want to see your mother", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next65")
        global parts
        parts = "screen65()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 65)
        pygame.display.update()
def screen66():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('SCENE14superfinal.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 66)
        button("go and see her", 300, 600, 1200, 50, blue, lightblue, "mommy")
        button("decline", 300, 700, 1200, 50, blue, lightblue, "next66")
        global parts
        parts = "screen66()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 66)
        pygame.display.update()
def mommy():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene15.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: There is your mother, she cant even move at all that is why i created the serum for her", 300, 700, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next66")
        pygame.display.update()
def screen67():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16-repeated.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 67)
        button("side with my father to stop EEE", 300, 600, 1200, 50, blue, lightblue, "next167")
        button("continue on with my mission", 300, 700, 1200, 50, blue, lightblue, "next266")
        global parts
        parts = "screen67()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 67)
        pygame.display.update()
def screen167():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16-repeated.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 167)
        button("Father: we need to start by taking out the rat thats in our company", 300, 600, 1200, 50, blue, lightblue,)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlegood1")
        global parts
        parts = "screen167()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 167)
        pygame.display.update()
def battlegood1():
    global HP
    HP = getHP()
    EHP = 70
    Edamage = 13
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen168()
        pygame.display.update()
def screen168():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 168)
        button("Let him go in exchange for entrance info to EEE", 300, 600, 1200, 50, blue, lightblue, "next1681")
        button("Kill him(200g)", 300, 700, 1200, 50, blue, lightblue, "next1682")
        global parts
        parts = "screen168()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 168)
        pygame.display.update()
def screen169():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16-repeated.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 169)
        button("Good job now lets head to EEE", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next169")
        global parts
        parts = "screen169()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 169)
        pygame.display.update()
def screen170():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene17good.jpg')
    if info == 1 and ally == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 170)
            button("Eureka: 113 you remember my dream? well now i have proof, lets take this company down", 300, 600, 1200, 50, blue, lightblue)
            button("next", 1600, 800, 100, 50, blue, lightblue, "next170")
            global parts
            parts = "screen170()"
            button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 170)
            pygame.display.update()
    elif info == 1 and ally == 0:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 170)
            button("Eureka: 113 i need you to help me destroy this company", 300, 600, 1200, 50, blue, lightblue, "next170")
            button("Eureka: 113 either you get out of my way or die", 300, 800, 1200, 50, blue, lightblue, "battlegood2")
            pygame.display.update()

            parts = "screen170()"
            button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 170)
    else:
        battlegood2()
def battlegood2():
    global HP
    HP = getHP()
    EHP = 90
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene17good.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen1711()
        pygame.display.update()
def screen1711():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene17bad.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 171)
        button("Eureka: im sorry my friend it had to be done", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next170")
        global parts
        parts = "screen1711()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 1711)
        pygame.display.update()
def screen171():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 171)
        button("Eureka: Why isnt the boss here?", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next171")
        global parts
        parts = "screen171()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 171)
        pygame.display.update()
def screen172():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18miniboss.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 172)
        button("Eureka: looks like he left one of his lackeys here. Time to take you out", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlegood3")
        global parts
        parts = "screen172()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 172)
        pygame.display.update()
def battlegood3():
    global HP
    HP = getHP()
    EHP = 120
    Edamage = 15
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18miniboss.jpg')
    if getALLY() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113 bonus(2x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage*2
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen173()
            pygame.display.update()
    else:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen173()
            pygame.display.update()
def screen173():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18dead.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 173)
        button("Eureka: now that he is taken care of time to search for clues", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next173")
        global parts
        parts = "screen173()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 173)
        pygame.display.update()
def screen174():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 174)
        button("Boss: well hello there Eureka, you must be wondering why i am not in my office right now", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next174")
        global parts
        parts = "screen174()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 174)
        pygame.display.update()
def screen175():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 175)
        button("Boss: Thats because i anticipated that you would betray me so i sent a different agent in your stead", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next175")
        global parts
        parts = "screen175()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 175)
        pygame.display.update()
def screen176():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 176)
        button("Boss: i now have the ability to create a superhuman army within 48 hours", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next176")
        global parts
        parts = "screen176()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 176)
        pygame.display.update()
def screen177():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 177)
        button("Boss: I guess this will serve as our goodbye because i placed a time bomb within the building :)", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next177")
        global parts
        parts = "screen177()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 177)
        pygame.display.update()
def screen178():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene18video.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 178)
        button("Boss: Goodbye Eureka it was fun while it lasted", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next178")
        global parts
        parts = "screen178()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 178)
        pygame.display.update()
def screen179():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene17good.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 179)
        button("Eureka: 113 TELL EVERYBODY TO EVACUATE THE BUILDING RIGHT NOW", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next179")
        global parts
        parts = "screen179()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 179)
        pygame.display.update()
def screen180():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene19.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 180)
        button("Eureka: Everybody got out safe, goodjob everyone", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next180")
        global parts
        parts = "screen180()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 180)
        pygame.display.update()
def screen181():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 181)
        button("Eureka: Father the boss has escaped, what do we do now", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next181")
        global parts
        parts = "screen181()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 181)
        pygame.display.update()
def screen182():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 182)
        button("Father: i think we could target one of his old associates", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next182")
        global parts
        parts = "screen182()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 182)
        pygame.display.update()
def screen183():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 183)
        button("Eureka: you must be the old associate, so are you gonna tell me where he is or do we have to make this complicated", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next183")
        global parts
        parts = "screen183()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 183)
        pygame.display.update()
def screen184():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 184)
        button("Associate: i dont even know what youre talking about", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next184")
        global parts
        parts = "screen184()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 184)
        pygame.display.update()
def screen185():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 185)
        button("Eureka: looks like this is going to be complicated", 300, 600, 1200, 50, blue,lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlegood4")
        global parts
        parts = "screen185()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 185)
        pygame.display.update()
def battlegood4():
    global HP
    HP = getHP()
    EHP = 120
    Edamage = 15
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21fightscene.jpg')
    if getALLY() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113 bonus(2x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage*2
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen186()
            pygame.display.update()
def screen186():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 186)
        button("kill him", 300, 600, 1200, 50, blue, lightblue, "next1861")
        button("let him go (gain berserk ability)", 300, 700, 1200, 50, blue, lightblue, "next1862")
        global parts
        parts = "screen186()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 186)
        pygame.display.update()
def screen187():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 187)
        button("Eureka: well i got what i needed time to head back", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next187")
        global parts
        parts = "screen187()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 187)
        pygame.display.update()
def screen188():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 188)
        button("Eureka: he is at the basement of EEE lets head out", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlegood5")
        global parts
        parts = "screen188()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 188)
        pygame.display.update()
def battlegood5():
    global HP
    HP = getHP()
    EHP = 150
    Edamage = 15
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.jpg')
    if getALLY() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113 bonus(2x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage * 2
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                battlegood51()
            pygame.display.update()
    else:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                battlegood51()
            pygame.display.update()
def battlegood51():
    global HP
    HP = getHP()
    EHP = 120
    Edamage = 15
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.1.jpg')
    if getALLY() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113 bonus(2x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage * 2
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen189()
            pygame.display.update()
    else:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen189()
            pygame.display.update()
def screen189():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24bad1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 189)
        button("Eureka: Time to take you out you piece of sht", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlegood6")
        global parts
        parts = "screen189()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 189)
        pygame.display.update()
def battlegood6():
    global HP
    HP = getHP()
    EHP = 250
    Edamage = 15
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24bad1.jpg')
    if getALLY() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113 bonus(2x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage * 2
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen190()
            pygame.display.update()
    else:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen190()
            pygame.display.update()
def screen190():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 190)
        button("Eureka: Father its finished we did it", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next190")
        global parts
        parts = "screen190()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 190)
        pygame.display.update()
def screen191():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 191)
        button("Boss: Dont celebrate just yet(uses VENOM on himself)", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlegood7")
        global parts
        parts = "screen191()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 191)
        pygame.display.update()
def battlegood7():
    global HP
    HP = getHP()
    EHP = 1000
    Edamage = 30
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24good1.jpg')
    bg2 = pygame.image.load("Scene24mutatedeureka.jpg")
    if getALLY() == 1 and getINFO()==1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("113+HELP bonus(4x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage * 4
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen192()
            pygame.display.update()
    elif getALLY() == 1 and getINFO() == 0:
        gooda1()
    elif getALLY() == 0 and getINFO() == 1:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg2, (0, 0))
            button("BERSERK bonus(4x ATK)", 100, 100, 200, 50, blue, lightblue)
            button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
            button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
            damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
            damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
            damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
            if damage == None:
                damage = 0
            if damage2 == None:
                damage2 = 0
            if damage3 == None:
                damage3 = 0
            if damage != 0:
                HP -= Edamage
                EHP -= damage * 4
            if damage2 != 0:
                HP += damage2 - Edamage
            if damage3 != 0:
                HP -= damage3
            if HP <= 0:
                fail()
            if EHP <= 0:
                screen192()
        else:
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                gameDisplay.blit(bg2, (0, 0))
                button("BERSERK bonus(4x ATK)", 100, 100, 200, 50, blue, lightblue)
                button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
                button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
                damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
                damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
                damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
                if damage == None:
                    damage = 0
                if damage2 == None:
                    damage2 = 0
                if damage3 == None:
                    damage3 = 0
                if damage != 0:
                    HP -= Edamage
                    EHP -= damage * 4
                if damage2 != 0:
                    HP += damage2 - Edamage
                if damage3 != 0:
                    HP -= damage3
                if HP <= 0:
                    fail()
                if EHP <= 0:
                    screen192()

def gooda1():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24good2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: Ill use VENOM as well, Ericka get your mother out of here and leave this to me", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "gooda1")
        pygame.display.update()
def gooda2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24good2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Father: Im happy that i get to help you my dear daughter, take care of your mother for me", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "gooda2")
        pygame.display.update()
def gooda3():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24eeedown.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Ericka: We got out mother all thanks to father", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "gooda3")
        pygame.display.update()
def gooda4():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene25motherfinal.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Mother: Lets live on my daughter, so that his sacrifice may not be in vain", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "gooda4")
        pygame.display.update()
def gooda5():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene25eureka.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Ericka: id like that mothe... mom", 300, 600, 1200, 50, blue, lightblue)
        button("end", 1600, 800, 100, 50, blue, lightblue, "credits")
        pygame.display.update()
def screen192():
    global parts
    if getALLY() == 1 and getINFO == 1:
        gameDisplay.fill(white)
        done = False
        bg = pygame.image.load('Scene24outeee.jpg')
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("Ericka: We did it, we can now live in peace", 300, 600, 1200, 50, blue, lightblue)
            button("end", 1600, 800, 100, 50, blue, lightblue, "credits")

            parts = "screen192()"
            button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 192)
            pygame.display.update()
    elif getALLY() == 1 and getINFO() == 0:
        gameDisplay.fill(white)
        done = False
        bg = pygame.image.load('Scene24outeee.jpg')
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("Ericka: Good job everyone we can now go on with our lives", 300, 600, 1200, 50, blue, lightblue)
            button("end", 1600, 800, 100, 50, blue, lightblue, "credits")

            parts = "screen192()"
            button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 192)
            pygame.display.update()
    elif getALLY() == 0 and getINFO() == 1:
        gameDisplay.fill(white)
        done = False
        bg = pygame.image.load('Scene24outeee.jpg')
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("Ericka: I almost died, its a good thing the associate came back with the antidote to berserk mode", 300, 600, 1200, 50, blue, lightblue)
            button("end", 1600, 800, 100, 50, blue, lightblue, "credits")

            parts = "screen192()"
            button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 192)
            pygame.display.update()
    else:
        gameDisplay.fill(white)
        done = False
        bg = pygame.image.load('Scene24dadeee.jpg')
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.blit(bg, (0, 0))
            button("Father: we just lost our daughter because she used a deadly ability, all we can do now is continue living for her sake",300, 600, 1200, 50, blue, lightblue)
            button("end", 1600, 800, 100, 50, blue, lightblue, "credits")

            parts = "screen192()"
            button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 192)
            pygame.display.update()

def screen267():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16kidnap.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 267)
        button("Eureka: im sorry father but i have to finish my job", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next267")
        global parts
        parts = "screen267()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 267)
        pygame.display.update()
def screen268():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16meetup.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 268)
        button("Eureka: you must be the rat, i got the asset lets head back to the boss", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next268")
        global parts
        parts = "screen268()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 268)
        pygame.display.update()
def screen269():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene16meetup.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 269)
        button("Rat: sure i was getting tired of this place anyway", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next269")
        global parts
        parts = "screen269()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 269)
        pygame.display.update()
def screen270():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 270)
        button("Boss: well done eureka, now we just need time to perfect VENOM, you can go on other missions while you wait", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next270")
        global parts
        parts = "screen270()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 270)
        pygame.display.update()
def screen271():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 271)
        button("Battle enemies (2 enemies with stats: Health: 60, Defense: 0, Damage: 15. Gold reward: 200)", 300, 600, 1200, 50, blue, lightblue, "battlebad1")
        button("Rescue. Gold reward(100g)", 300, 700, 1200, 50, blue, lightblue, "rescue2")
        button("or training (After may choose to upgrade Health by 10, Damage by 5, or Defense by 5)", 300, 800, 1200, 50, blue, lightblue, "train2")
        global parts
        parts = "screen271()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 271)
        pygame.display.update()
def battlebad1():
    global HP
    HP=getHP()
    EHP=60
    Edamage = 12
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            battlebad12()
        pygame.display.update()
def battlebad12():
    HP=getHP()
    EHP=60
    Edamage = 12
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Battle2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen272()
        pygame.display.update()
def screen272():
    global gold,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold2()
    gold = gold + 200
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 272)
        button("BOSS: You did well here is your reward(200g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        button(str(gold)+"g", 1500, 100, 150, 50, blue, lightblue)
        global parts
        parts = "screen272()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 272)
        pygame.display.update()
def train2():
    global HP
    Edamage = 12
    EHP = 60
    HP = getHP()
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2-1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            level2()
        pygame.display.update()
def level2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("ADD 10 TO MAX HP", 300, 600, 1200, 50, blue, lightblue, "HP2")
        button("ADD 5 TO MAX DAMAGE", 300, 700, 1200, 50, blue, lightblue, "ATK2")
        button("ADD 5 TO MAX DEFENSE", 300, 800, 1200, 50, blue, lightblue, "DEF2")
        pygame.display.update()
def lvl41():
    global HP
    HP = getHP() + 10
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your HP is now at " + str(HP), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        pygame.display.update()
def lvl42():
    global ATK,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    ATK = getATK() + 5
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("God: Great choice! Your ATK is now at "+str(ATK), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        pygame.display.update()
def lvl43():
    global DEF,HP
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    DEF = getDEF()+5
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("GOD: Great choice! Your DEF is now at "+str(DEF), 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        pygame.display.update()
def rescue2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene4Saving.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("You found her goodjob! now head back to the boss", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "pay2")
        pygame.display.update()
def pay12():
    global gold
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene2.jpg')
    gold = getgold2()
    gold = gold + 100
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("BOSS: You did well here is your reward(100g)", 300, 700, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next272")
        button(str(gold) + "g", 1500, 100, 150, 50, blue, lightblue)
        pygame.display.update()

def screen273():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 273)
        button("Eureka: A lot of things happened today, i didnt expect to meet my real father", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next273")
        global parts
        parts = "screen273()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 273)
        pygame.display.update()
def screen274():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene 1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 274)
        button("*ATTENTION ALL AGENTS PLEASE HEAD TO THE HEAD OFFICE, THERE HAS BEEN AN ESCAPE*", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next274")
        global parts
        parts = "screen274()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 274)
        pygame.display.update()
def screen275():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 275)
        button("Boss: YOUR FATHER JUST TOOK THE PERFECTED SERUM AND ESCAPED! I WANT HIM BACK DEAD OR ALIVE", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next275")
        global parts
        parts = "screen275()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 275)
        pygame.display.update()
def screen276():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene3.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 276)
        button("Eureka: I'll head to the company immediately", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next276")
        global parts
        parts = "screen276()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 276)
        pygame.display.update()
def screen277():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Guards.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 277)
        button("Eureka: Looks like i have to force myself in", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlebad2")
        global parts
        parts = "screen277()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 277)
        pygame.display.update()
def battlebad2():
    global HP
    HP=getHP()
    EHP=200
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene10Guards.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:"+str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:"+str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50,blue, lightblue,"ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen278()
        pygame.display.update()
def screen278():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 278)
        button("Eureka: Father youre going to have to come with me, if you resist you die", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next278")
        global parts
        parts = "screen278()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 278)
        pygame.display.update()
def screen279():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 279)
        button("Father: Eureka please think about what youre doing. The entire human race is in danger", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next279")
        global parts
        parts = "screen279()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 279)
        pygame.display.update()
def screen280():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene20.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 280)
        button("Eureka: I dont care im just here to do what the boss ordered me to do", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next280")
        global parts
        parts = "screen280()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 280)
        pygame.display.update()
def screen281():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21fight.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 281)
        button("Disguised113: EUREKA IM HERE TO STOP YOU BECAUSE I BELIEVE IN THE DOCTORS VISIONS SO I HELPED HIM ESCAPE", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlebad3")
        global parts
        parts = "screen281()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 281)
        pygame.display.update()
def battlebad3():
    global HP
    HP = getHP()
    EHP = 200
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21fight.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen282()
        pygame.display.update()
def screen282():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene21fight.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 282)
        button("Eureka: im sorry my friend it had to be done", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next282")
        global parts
        parts = "screen282()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 282)
        pygame.display.update()
def screen283():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 283)
        button("Eureka: looks like they hired more henchmen to stop me", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "battlebad4")
        global parts
        parts = "screen283()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 283)
        pygame.display.update()
def battlebad4():
    global HP
    HP = getHP()
    EHP = 150
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            battlebad41()
        pygame.display.update()
def battlebad41():
    global HP
    HP = getHP()
    EHP = 200
    Edamage = 14
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene22.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("EUREKA:" + str(HP), 1500, 100, 150, 50, blue, lightblue)
        button("ENEMY:" + str(EHP), 1500, 200, 150, 50, blue, lightblue)
        damage = button("ATTACK", 300, 600, 1200, 50, blue, lightblue, "ATK1")
        damage2 = button("DEFEND", 300, 700, 1200, 50, blue, lightblue, "DEF1")
        damage3 = button("PASS", 300, 800, 1200, 50, blue, lightblue, "PAS1")
        if damage == None:
            damage = 0
        if damage2 == None:
            damage2 = 0
        if damage3 == None:
            damage3 = 0
        if damage != 0:
            HP -= Edamage
            EHP -= damage
        if damage2 != 0:
            HP += damage2 - Edamage
        if damage3 != 0:
            HP -= damage3
        if HP <= 0:
            fail()
        if EHP <= 0:
            screen284()
        pygame.display.update()
def screen284():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23decision.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 284)
        button("Eureka: well hello there father", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next284")
        global parts
        parts = "screen284()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 284)
        pygame.display.update()
def screen285():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23decision.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 285)
        button("Father: i always wonder what could have happened if you were not kidnapped", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next285")
        global parts
        parts = "screen285()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 285)
        pygame.display.update()
def screen286():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23decision.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 286)
        button("Father: we could have changed the world for the better ericka please think this through", 300, 600, 1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "next286")
        global parts
        parts = "screen286()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 286)
        pygame.display.update()
def screen287():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene23decision.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("shop", 100, 100, 100, 50, blue, lightblue, "shop", 286)
        button("Bring them back to EEE", 300, 600, 1200, 50, blue, lightblue, "screenbad")
        button("Kill both of them", 300, 700, 1200, 50, blue, lightblue, "screenbadd")
        button("Change of heart and go fight EEE", 300, 800, 1200, 50, blue, lightblue, "screenbaddd")
        global parts
        parts = "screen287()"
        button("save", 100, 800, 100, 50, blue, lightblue, "savescreen", 287)
        pygame.display.update()
def screenbad():
    """"Bad Ending 1"""
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24bad1.1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Boss: good job eureka, now lets start this off by making your parents our first test subjects", 300, 600,1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "screenbadd2")
        pygame.display.update()
def screenbadd():
    """"Bad Ending 2"""
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24bad1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Boss: good job eureka, i can now appoint you as leader of the new superhuman army we are about to create", 300, 600,1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "credits")
        pygame.display.update()
def screenbadd2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene25bad.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Eureka went on to become the leader of an army to take down any resistance as EEE took over the world", 300, 600,1200, 50, blue, lightblue)
        button("end", 1600, 800, 100, 50, blue, lightblue, "credits")
        pygame.display.update()
def screenbaddd():
    """"Credits"""
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24bad3.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Mutated boss: you wont be able to survive this", 300, 600,1200, 50, blue, lightblue)
        button("next", 1600, 800, 100, 50, blue, lightblue, "screenbaddd2")
        pygame.display.update()
def screenbaddd2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Scene24dead.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("Mutated boss: such a shame to lose a possible test subject", 300, 600,1200, 50, blue, lightblue)
        button("end", 1600, 800, 100, 50, blue, lightblue, "credits")
        pygame.display.update()

def fail():
    gameDisplay.fill(black)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        messagescreen("YOU HAVE FAILED", white, 0, "large")
        messagescreen("THERE IS NO GOING BACK NOW", white, 100, "medium")
        button("START MENU", 800, 600, 200, 50, blue, lightblue, "intro")
        pygame.display.update()
def credits():
    """"Credits"""
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Credits1.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("next", 1600, 800, 100, 50, blue, lightblue, "credits2")
        pygame.display.update()
def credits2():
    gameDisplay.fill(white)
    done = False
    bg = pygame.image.load('Crredits2.jpg')
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(bg, (0, 0))
        button("main menu", 1600, 800, 150, 50, blue, lightblue, "intro")
        pygame.display.update()
intro()
pygame.quit()
quit()
