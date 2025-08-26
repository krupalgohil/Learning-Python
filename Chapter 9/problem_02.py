import random

def game():
    # Starting the game
    print("You are playing the game")
    
    # Generate a random score between 1 and 50
    score = random.randint(1, 50)
    
    # Open the file to fetch the high score
    with open("chapter 9\\problem_02.txt") as f:
        hiscore = f.read()   # Read the content of the file
        
        # If file is not empty, convert high score to integer
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            # If file is empty, set high score = 0
            hiscore = 0
    
    # Print the player's current score
    print(f"Your score is {score}")
    
    # Check if the new score is greater than the high score
    if(score > hiscore):
        # Update the file with the new high score
        with open("chapter 9\\problem_02.txt", "w") as f:
            f.write(str(score))
    
    # Return the score (optional, for later use)
    return score

# Run the game function
game()
