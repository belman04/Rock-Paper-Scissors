# import sys
import pygame # importing the pygame library
import random # importing the random library

def main():
    pygame.init() # calling funtion init to initialize pygame

    window = pygame.display.set_mode((600, 600)) # creating the window 
    pygame.display.set_caption("Rock Paper Scissors") # setting the window title
    pygame.display.set_icon(pygame.image.load("icon.jpg")) # setting icon 
    
    choices = ["rock", "paper", "scissors"] # list of choices

    choice = input("Chose rock, paper or scissors: ") # asking the user for their choice in console

    if choice in choices:
        show_choice(choice)
        computer_choice = random.choice(choices) # random choice for the computer
        print("Computer chose", computer_choice)
        result = check_winner(choice, computer_choice)
        print(result)
    else:
        print("Invalid choice, try again")

    # closing the window if the user clicks the close button
    running = True

    while running: # infinite loop to keep the window open
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill("white") # to clear the window
        pygame.display.flip() # to update the window
        

    pygame.quit() # calling function quit to quit pygame, always at the end
    # sys.exit() # calling the exit funtion to exit the window, not neccesary

# funtion just to show your choice in console
def show_choice(choice):
    match choice:
        case "rock":
            print("You chose rock")
        case "paper":
            print("You chose paper")
        case "scissors":
            print("You chose scissors")

# function to compare choices and check winner in console
def check_winner(your_choice, computer_choice):
    if your_choice == computer_choice:
        return "It's a tie"
    elif(your_choice == "rock" and computer_choice == "scissors") or \
        (your_choice == "paper" and computer_choice == "rock") or \
        (your_choice == "scissors" and computer_choice == "paper"):
        return "You win"
    else: 
        return "You lose"

if __name__ == "__main__": main()