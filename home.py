
name = None
sub = None
color = None
suba = None
colora = None
def start():
    global name
    print("Welcome to the friendship game. What is your name? ")
    name = input(">")
    print("Hello, " + name + ". I think you're going to like this game.")
    knowhow()
    return name

def directions():
    print("Okay, " + name + " here's how to play the game:\nFirst you are going to answer the questions that are asked of you. Once you are done, you will hand the device over to your friend, and they will try to answer the questions how they think you would have answered them. Depending on the score, you can know whether they are a real friend or not >:) -- or maybe just how good their memory is.")
    print("Okay, now on to the game!")
    subjects()

def knowhow():
    print("\nIf you already know how to play this game, enter 'c' for continue, if you need to go over the directions, enter 'd' ")
    ducks = input(">")
    if ducks == "c":
        subjects(),
    elif ducks == "d":
        directions(),
    else:
        print("Sorry, please choose an appropriate answer:")
        knowhow()

def subjects():
    global sub
    print("\nSo, " + name + " the first thing I must know is what is your favourite school subject?")
    print("\n1:Math\n2:Science\n3:Literature\n4:Foreign Language\n5:History\n6:Lunch")
    sub = input(">")
    if sub == "1":
        print("\nGot it! Your favorite subject is math!")
    elif sub == "2":
        print("\nGot it! Your favorite subject is science!")
    elif sub == "3":
        print("\nGot it! Your favorite subject is literature!")
    elif sub == "4":
        print("\nGot it! Your favorite subject is foreign language!")
    elif sub == "5":
        print("\nGot it! Your favorite subject is history!")
    elif sub == "6":
        print("\nGot it! Your favorite subject is lunch!")
    else:
        print("Sorry, please choose an appropriate option: ")
        subjects()
    colors()
    return sub

def colors():
    global color
    print("Next, what is your favorite color? - make sure to spell it right!")
    color = input("> ")
    print("Got it! Your favorite color is " + color + "!")
    switchturn()
    return color

def switchturn():
    print("Wonderful job, " + name + "! Now let's pass it off to your friend!")
    print("Once you pass the device, please type 1 ")
    answer = input(">")
    if answer == "1":
        subjectsa()
    else:
        print("Sorry, you have to type 1 to move on ")
        switchturn()
def subjectsa():
    global suba
    print("\nQuestion 1: What is " + name + "'s favorite school subject?")
    print("\n1:Math\n2:Science\n3:Literature\n4:Foreign Language\n5:History\n6:Lunch")
    suba = input(">")
    if suba == "1":
        print("\nGot it! " + name + "'s favorite subject is math!")
    elif suba == "2":
        print("\nGot it! " + name + "'s favorite subject is science!")
    elif suba == "3":
        print("\nGot it! " + name + "'s favorite subject is literature!")
    elif suba == "4":
        print("\nGot it! " + name + "'s favorite subject is foreign language!")
    elif suba == "5":
        print("\nGot it! " + name + "'s favorite subject is history!")
    elif suba == "6":
        print("\nGot it! " + name + "'s favorite subject is lunch!")
    else:
        print("Sorry, please choose an appropriate option: ")
        subjectsa()
    colorsa()
    return suba

def colorsa():
    global colora
    print("Next, what is " + name + "'s favorite color? - make sure to spell it right!")
    colora = input("> ")
    print("Got it! " + name +"'s favorite color is " + colora + "!")
    endgame()
    return colora
def endgame():
    i = 0
    if sub == suba:
        i += 1
    if color == colora:
        i += 1
    print("Final score: " + str(i))
start()
