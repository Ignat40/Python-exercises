#Let's play! You have to return which player won! In case of a draw return Draw!.

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    
    
print(rps("rock", "paper"))
print(rps("rock", "scissors"))
print(rps("rock", "rock"))
print(rps("scissors", "paper"))
print(rps("scissors", "rock"))
print(rps("scissors", "scissors"))
print(rps("paper", "paper"))
