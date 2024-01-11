import time, os, random

t=('\n\n🌟Idea Storage🌟\n\n')
# Prompt the user to add an idea, or load a random one.
while True:
    print(t)
    option=input('Please select an option:\n\n1. Add an idea (a)\n\n2. Load a random idea (r)\n\n> ').lower()
    if option=='1' or option=='r':    
        # Choosing 'Add an idea' results in:
        os.system('clear')
        print(t)
        print("Add an idea...")
        print()
        # A prompt for the user to input their idea.
        idea=input('Input the idea you want to add:\n\n> ')
        # Add the idea to a text file called 'my.ideas'.
        f=open("my.ideas", "a+")
        # Add the idea in append mode, with every new idea on a brand new line.
        f.write(f'{idea}\n')
        f.close()
        print()
        print('Idea added!')
        print()
        time.sleep(1)
        os.system('clear')
        continue
    elif option=='2' or option=='r':
        # Choosing 'Load random' results in:
        # Load the list of ideas.
        print()
        print('Random idea:\n\n')
        f=open("my.ideas", "r")
        x=0
        ideasAll={}
        while True:
            idea=f.readline().strip()
            if idea=="":
                break
            ideasAll[x]=idea
            x+=1
        # Choose one at random.
        randomNum=random.randint(0, x)
        print(ideasAll[randomNum])
        # Display it on screen for a few seconds.
        f.close()
        time.sleep(2)
        os.system('clear')
        # Return to the menu.
        continue
    else:
      print()
      print('Not a supported input, try again...')
      time.sleep(1)
      os.system('clear')
      continue

import os, time, random

# Official Solution:
# def add():
#   os.system("clear")
#   idea = input("Idea > ")
#   f = open("my.ideas", "a+")
#   f.write(f"{idea}\n")
#   f.close()
#   time.sleep(1)
#   os.system("clear")

# def show():
#   os.system("clear")
#   f = open("my.ideas", "r")
#   ideas = f.read().split("\n")
#   f.close()
#   ideas.remove("")
#   idea = random.choice(ideas)
#   print(idea)
#   time.sleep(2)
#   os.system("clear")

# while True:
#   menu = input("1: Add idea\n2: Show a random idea\n> ")
#   if menu == "1":
#     add()
#   else:
#     show()