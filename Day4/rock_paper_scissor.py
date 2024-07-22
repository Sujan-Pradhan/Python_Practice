import random
rock = '''                               88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                             
                                              '''
paper = '''8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88 '''
scissors = ''' d8b                                        
                Y8P                                        
                                                           
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
                                                            '''

game_images = [rock, paper, scissors]
choice1= int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if choice1 >= 3 or choice1 < 0:
    print ("You typed an invalid number, you lose!")
else:
    print(game_images[choice1])
# if choice1 == 0:
#     print (rock)
# elif choice1 == 1:
#     print (paper);
# else:
#     print (scissors)
computer_chose = random.randint(0,2)
print("Computer chose\n")
print(game_images[computer_chose])
# if computer_chose == 0:
#     print(rock)
# elif computer_chose == 1:
#     print (paper);
# else:
#     print (scissors)

if choice1 == computer_chose :
    print("Draw")
elif choice1 == 0 and computer_chose == 1:
    print("You lose")
elif choice1 == 0 and computer_chose == 2:
    print("You win")
elif choice1 == 1 and computer_chose == 2:
    print("You lose")
elif choice1 == 1 and computer_chose == 0:
    print("You win")
elif choice1 == 2 and computer_chose == 0:
    print("You lose")
elif choice1 == 2 and computer_chose == 1:
    print("You win")
else:
    print("An invalid choice")

