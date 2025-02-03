# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String  S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Your task is to determine the winner of the game and their score.

def minion_game(string):
    vowels = "aeiou"
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        score = len(string) - i
        if string[i] in vowels:
            kevin_score += score
        else:
            stuart_score += score
        
    if kevin_score > stuart_score:
        print(f"Kevin win {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart win {stuart_score}")
    else:
        print("Draw")
        

if __name__ == "__main__":
    s = input()
    minion_game(s)
        