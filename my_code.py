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
    fruit_1 = int(input("Your first number (from 0 to 10): "))
    fruit_2 = int(input("Your second number (from 0 to 10): "))
    fruit_3 = int(input("Your third number (from 0 to 10): "))
    while fruit_1 > 0 or fruit_1 < 10 or fruit_2 > 0 or fruit_2 < 10 or fruit_3 > 0 or fruit_3 < 10:
        print ("Based on these number, I suggest you to plant " + plant_list[fruit_1] + ", " + plant_list[fruit_2] + ", and " + plant_list[fruit_3])
except:
    print ("Please type the a number in the range of 1 to 10")
print ("Based on these number, I suggest you to plant " + plant_list[fruit_1] + ", " + plant_list[fruit_2] + ", and " + plant_list[fruit_3])




