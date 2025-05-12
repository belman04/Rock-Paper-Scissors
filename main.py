import pygame # importing the pygame library
import random # importing the random library
                
def main():
    pygame.init() # calling funtion init to initialize pygame

    window = pygame.display.set_mode((700, 500)) # creating the window 
    pygame.display.set_caption("Rock Paper Scissors") # setting the window title
    pygame.display.set_icon(pygame.image.load("assets/icon.jpg")) # setting icon 
    
    # setting fonts size and style
    font_title = pygame.font.SysFont("Albert Sans", 60)
    font_subtitle = pygame.font.SysFont("Albert Sans", 40)
    font_score = pygame.font.SysFont("Albert Sans", 22, italic=True)
    
    # rendering the text
    text_title = font_title.render("CHOOSE", True, (220, 156, 99))
    
    text_result = font_title.render("", True, (90, 115, 238))
    result_rect = text_result.get_rect(center=((260, 100)))
    
    text_winner = font_subtitle.render("", True, (65, 54, 54)) # to render the result
    winner_rect = text_winner.get_rect(center=(320, 150))
    
    text_win = font_score.render(f"Win: 0", True, (90, 115, 238))
    text_tie = font_score.render(f"Ties: 0", True, (65, 54, 54))
    text_lose = font_score.render(f"Loses: 0", True, (249, 95, 95))
    
    # rendering and positioning the images
    rock_img = pygame.image.load("assets/rock.png") 
    rock_img = pygame.transform.scale(rock_img, (185, 250)) # resizing the image
    rock_rect = rock_img.get_rect(center=(130, 250))
    
    paper_img = pygame.image.load("assets/paper.png") 
    paper_img = pygame.transform.scale(paper_img, (185, 250))
    paper_rect = paper_img.get_rect(center=(345, 250))
    
    scissors_img = pygame.image.load("assets/scissors.png") 
    scissors_img = pygame.transform.scale(scissors_img, (185, 250))
    scissors_rect = scissors_img.get_rect(center=(560, 250))
    
    restart_img = pygame.image.load("assets/restart.png")
    restart_img = pygame.transform.scale(restart_img, (50, 80))
    restart_rect = restart_img.get_rect(center=(640, 440))
    
    # initializing scores
    score_win = 0
    score_tie = 0
    score_lose = 0
    
    def play_game(choice):
        choices = ["Rock", "Paper", "Scissors"] # list of choices

        # to modify the variables 
        nonlocal text_result, result_rect, text_winner, winner_rect
        nonlocal game_state, your_choice, computer_choice
        nonlocal score_win, score_tie, score_lose
        nonlocal text_win, text_tie, text_lose
    
        game_state = "playing" 
        your_choice = choice 
        # print("You chose", your_choice) # in console
        computer_choice = random.choice(choices) # random choice for the computer
        # print("Computer chose", computer_choice) # in console
        
        result = check_result(your_choice, computer_choice)
        # print(result + "\n------------------------") # in console
        
        winner = show_winner(your_choice, computer_choice)
        
        if result == "YOU WIN!":
            score_win += 1
            text_result = font_title.render(result, True, (90, 115, 238)) 
            result_rect = text_result.get_rect(center=(345, 100))
        elif result == "YOU LOSE!":
            score_lose += 1
            text_result = font_title.render(result, True, (249, 95, 95)) 
            result_rect = text_result.get_rect(center=(345, 100))
        else:
            score_tie += 1
            text_result = font_title.render(result, True, (99, 164, 3)) 
            result_rect = text_result.get_rect(center=(345, 100))
        
        text_win = font_score.render(f"Win: {score_win}", True, (90, 115, 238))
        text_tie = font_score.render(f"Ties: {score_tie}", True, (65, 54, 54))
        text_lose = font_score.render(f"Loses: {score_lose}", True, (249, 95, 95))
        
        text_winner = font_subtitle.render(winner, True, (65, 54, 54)) 
        winner_rect = text_winner.get_rect(center=(345, 150))
    
    # setting game state
    game_state = "waiting"
    
    # to store the choices
    your_choice = None # 
    computer_choice = None
    
    # closing the window if the user clicks the close button
    running = True

    while running: # infinite loop to keep the window open
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # if the user click the mouse 
                if rock_rect.collidepoint(event.pos) and game_state == "waiting":
                    play_game("Rock")
                elif paper_rect.collidepoint(event.pos) and game_state == "waiting":
                    play_game("Paper")
                elif scissors_rect.collidepoint(event.pos) and game_state == "waiting":
                    play_game("Scissors")
                elif restart_rect.collidepoint(event.pos): # if the user clicks the restart button
                    game_state = "waiting"
                    
        window.fill("white") # to clear the window
        
        # starting the game
        if game_state == "waiting":
            # drawing the text
            window.blit(text_title, (260, 100)) 
            window.blit(text_win, (50, 400))
            window.blit(text_tie, (50, 430))
            window.blit(text_lose, (50, 460))
            # drawing the images
            window.blit(rock_img, rock_rect) 
            window.blit(paper_img, paper_rect) 
            window.blit(scissors_img, scissors_rect)
        # playing the game
        elif game_state == "playing":
            # drawing the text
            window.blit(text_result, result_rect)
            window.blit(text_winner, winner_rect)
            window.blit(text_win, (50, 400))
            window.blit(text_tie, (50, 430))
            window.blit(text_lose, (50, 460))
        
            # drawing your choice
            if your_choice == "Rock":
                window.blit(rock_img, (130, 150))
            elif your_choice == "Paper":
                window.blit(paper_img, (130, 150))
            elif your_choice == "Scissors":
                window.blit(scissors_img, (130, 150))
            
            # drawing computer choice
            if computer_choice == "Rock":
                window.blit(rock_img, (380, 150))
            elif computer_choice == "Paper":
                window.blit(paper_img, (380, 150))
            elif computer_choice == "Scissors":
                window.blit(scissors_img, (380, 150))
            
            window.blit(restart_img, restart_rect)
        
        pygame.display.flip() # to update the window

    pygame.quit() # calling function quit to quit pygame, always at the end

# function to compare choices and check winner in console
def check_result(your_choice, computer_choice):
    if your_choice == computer_choice:
        return "It's a tie"
    elif(your_choice == "Rock" and computer_choice == "Scissors") or \
        (your_choice == "Paper" and computer_choice == "Rock") or \
        (your_choice == "Scissors" and computer_choice == "Paper"):
        return "YOU WIN!" 
    else: 
        return "YOU LOSE!"

# function to show the winner
def show_winner(your_choice, computer_choice):
    result = check_result(your_choice, computer_choice)
    if result == "YOU WIN!":
        return f"{your_choice} beats {computer_choice}" 
    elif result == "YOU LOSE!":
        return f"{computer_choice} beats {your_choice}"
    else:
        return f"Both chose {your_choice}"

if __name__ == "__main__": main()