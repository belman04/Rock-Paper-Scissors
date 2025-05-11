import pygame # importing the pygame library
import random # importing the random library

def main():
    pygame.init() # calling funtion init to initialize pygame

    window = pygame.display.set_mode((600, 500)) # creating the window 
    pygame.display.set_caption("Rock Paper Scissors") # setting the window title
    pygame.display.set_icon(pygame.image.load("assets/icon.jpg")) # setting icon 
    
    # setting fonts size and style
    font_title = pygame.font.SysFont("Arial", 40,)
    font_choices = pygame.font.SysFont("Arial", 30, italic=True)
    font_result = pygame.font.SysFont("Arial", 35, bold=True)
    
    # rendering the text
    text_title = font_title.render("Chose", True, "black", "green")    
    text_rock = font_choices.render("Rock", True, "black", "blue")
    text_paper = font_choices.render("Paper", True, "black", "blue")
    text_scissors = font_choices.render("Scissors", True, "black", "blue")
    text_result = font_result.render("", True, "black", "purple")
    
    # text position
    title_rect = text_title.get_rect(center=(300, 50))
    rock_rect = text_rock.get_rect(center=(130, 150))
    paper_rect = text_paper.get_rect(center=(300, 150))
    scissors_rect = text_scissors.get_rect(center=(470, 150))
    result_rect = text_result.get_rect(center=(300, 250))
    
    def play_game(choice):
        choices = ["rock", "paper", "scissors"] # list of choices

        nonlocal text_result, result_rect # to modify the variable 
        
        print("You chose ", choice)
        
        computer_choice = random.choice(choices) # random choice for the computer
        print("Computer chose", computer_choice)
        
        result = check_winner(choice, computer_choice)
        print(result)
        
        text_result = font_result.render(f"Computer: {computer_choice} - {result}", True, "black", "purple")
        result_rect = text_result.get_rect(center=(300, 250))

    # closing the window if the user clicks the close button
    running = True

    while running: # infinite loop to keep the window open
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # if the user click the mouse
                if rock_rect.collidepoint(event.pos): 
                    play_game("rock")
                elif paper_rect.collidepoint(event.pos):
                    play_game("paper")
                elif scissors_rect.collidepoint(event.pos):
                    play_game("scissors")
                
        window.fill("white") # to clear the window
        
        # drawing the text
        window.blit(text_title, title_rect) 
        window.blit(text_rock, rock_rect) 
        window.blit(text_paper, paper_rect) 
        window.blit(text_scissors, scissors_rect)
        window.blit(text_result, result_rect)
        
        pygame.display.flip() # to update the window

    pygame.quit() # calling function quit to quit pygame, always at the end

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