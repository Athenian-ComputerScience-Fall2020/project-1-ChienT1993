# Collaborators (including web sites where you got help: https://www.w3schools.com/python/default.asp, https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running#:~:text=To%20stop%20a%20running%20program,want%20to%20terminate%20the%20program.&text=Ctrl%20%2B%20Z%20should%20do%20it,caught%20in%20the%20python%20shell.
#  
import sys
#This is the rock paper scissors game, it will decide wether the game will continue or stop
def RPS():
    user = int(input("Type 1 for rock, 2 for paper, and 3 for scissors: "))
    if user == 1:
        print ("It's a tie, play again.")
        RPS()
    elif user == 2:
        print ("You won.")
    elif user == 3:
        print ("The monster has defeated you. Game over.")
        sys.exit()
#Here are 4 choices that player will have to choose, each will lead to a different ending
def North():
    print ("There is nothing here other than Mars cactus.")
    print ("You die due to exhaustion. Game over.")

def East():
    print ("Android: Oh no, there's a monster ahead, prepare for a battle of rock, paper, scissors!")
    RPS()
    print ("Android: Yay, we did it, we manage to defeat the monster!")
    print ("Android: It turns out, the monster we defeat earlier was guarding this lake.")
    print ("Android: But, we only have 100 liters of water, how do you want to distribute it?")
    print ("Water have 2 main purposes, to drink (use) and to water the plant.")
    liter = int(input("How much water will you save for the purpose of drinking (use)?: "))
    for liter in range (0, 80):
        print ("You die because you run out of water. Game over.")
        break
    else:
        print ("You survived a month on Mars but your plants run out of water and die out. You live for another 2 weeks then die.")
        print ("Game over.")

def West():
    print ("Android: Hey, I found a shiny item. It looks like a diamond, but is not made out of Carbon.")
    print ("Android: Do you want to leave this planet with this special artifact?")
    decision = input("Type 'leave' to leave this planet or 'stay' to stay here: ")
    if decision == "leave":
        print ("You decided to leave Mars, but you run out of food and water supplies on your way back to Earth, you die.")
        print ("Game over.")
    if decision == "stay":
        print ("Android: Look, there is a monster heading toward us. Quick ready your fingers, we are going to have a rock, paper, scissors game.")
        RPS()
        print ("Moster: foiuaefpijfuiaefjiogegdiojefoingwebiueioudsvnioeiubhrpimaweaoihhookerwiubrgwoifuifeq!")
        print ("Android: The moster acknowledge your strength and decided to crowned you as the king/queen of Mars!")
        print ("You live a happy life on Mars, marry a Mars-ian citizen and give birth to a son. Congratulation")

def South():
    print ("Android: Oh look, there's a lake over there.")
    print ("Android: With this amount of water, we can last at least 10 more years on Mars.")
    print ("Congratulation, you survive.")
#This is just a function to manipulate the list
def Choosing_plant():
    while True:
        try:
            fruit_1 = int(input("Your first number (from 0 to 10): "))
            fruit_2 = int(input("Your second number (from 0 to 10): "))
            fruit_3 = int(input("Your third number (from 0 to 10): "))
            print ("Based on these number, I suggest you to plant " + plant_list[fruit_1] + ", " + plant_list[fruit_2] + ", and " + plant_list[fruit_3])
            break
        except:
            print ("Sorry, your input is invalid, please re-enter the values.")

#main part (mostly print statement)
print ("Android: Hello there stranger, my name is Android and I'm your personal adviser on Mars.")
print ("Android: So, what is your name?")
name = input("Your name: ")
print ("Android: It's a pleasure to meet you", name)
print ("Android: On Mars, foods and water are limited, so we need to plant fruits and search for water.")
print ("Android: Now, let me pick out 3 plants based on 3 of your number inputs.")
plant_list = ["avocados", "bananas", "grapefruits", "jackfruits", "kiwis", "lychees", "mangoes", "papayas", "peaches", "strawberries", "watermelons"]
print (Choosing_plant())
print ("Android: Great, now all we need is water for the plant.")
print ("Android: Since we are on Mars and we can easily get lost, I suggest we either go straight North, East, West, or South.")

direction = str(input("Which direction will you take?(North, East, West, South): "))
if direction == "North":
    North()
if direction == "East":
    East()
if direction == "West":
    West()
if direction == "South":
    South()