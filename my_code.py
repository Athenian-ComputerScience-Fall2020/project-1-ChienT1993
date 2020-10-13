# Collaborators (including web sites where you got help: https://www.w3schools.com/python/default.asp
#  

print ("Android: Hello there stranger, my name is Android and I'm your personal adviser on Mars.")
print ("Android: So, what is your name?")
name = input("Your name: ")
print ("Android: It's a pleasure to meet you", name)
print ("Android: On Mars, foods and water are limited, so we need to plant fruits and search for water.")
print ("Android: Now, let me pick out 3 plants based on 3 of your number inputs.")
plant_list = ["avocado", "banana", "grapefruit", "jackfruit", "kiwi", "lychee", "mango", "papaya", "peaches", "strawberry", "watermelon"]
try:
    fruit_1 = int(input("Your first number (from -11 to 10): "))
    fruit_2 = int(input("Your second number (from -11 to 10): "))
    fruit_3 = int(input("Your third number (from -11 to 10): "))
    while fruit_1 > 0 or fruit_1 < 10 or fruit_2 > 0 or fruit_2 < 10 or fruit_3 > 0 or fruit_3 < 10: #need to look back at this later
        print ("Based on these number, I suggest you to plant " + plant_list[fruit_1] + ", " + plant_list[fruit_2] + ", and " + plant_list[fruit_3])
        break
except:
    print ("Please type a number in the range of 0 to 10")

print ("Android: Great, now all we need is water for the plant.")
print ("Android: Since we are on Mars and we can easily get lost, I suggest we either go straight North, East, West, or South.")

def RPS(): # I will assume that these monsters don't have fingers
    user = int(input("Type 1 for rock, 2 for paper, and 3 for scissors: "))
    if user == 1:
        print ("It is a tie, play again.")
        RPS()
    elif user == 2:
        print ("You won, the game shall continue.")
    elif user == 3:
        print ("The monster has defeated you. Game over.")
        #break# need a break here

def North():
    print ("There is nothing here other than Mars cactus.")
    print ("You die due to exhaustion. Game over.")

def East():
    print ("Android: Oh no, there's a monster ahead, prepare for a battle of rock, paper, scissors!")
    RPS()

def West():
    print ("Android: Hey, I found a shiny item. It looks like a diamond, but is not made out of Carbon.")
    #leave the planet or not

def South():
    print ("Android: Oh look, there's a lake over there.")
    print ("Android: With this amount of water, we can last at least 10 more years on Mars.")
    print ("Congratulation, you survive.")

