import random

'''die_roll= input("Do you want to roll the die?(y/n): ").lower()
while True:
    if die_roll== 'y':
        die_1= random.randint(1,6)
        die_2= random.randint(1,6)

        total_die= die_1 + die_2
        print(f"{die_1}, {die_2}")
        print(f"Your die roll is:{ total_die}")

    elif die_roll== 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid Character")'''


#PIG 
import random

total_score = 0

while True:
    player_turnscore = 0
    while True:
        player_turn = random.randint(1, 6)
        print(f"You rolled: {player_turn}")
        
        if player_turn == 1:
            print("Rolled a 1, score reset!")
            player_turnscore = 0
            break  
        
        player_turnscore += player_turn
        print(f"Turn score: {player_turnscore}")
        
        roll_hold = input("Roll again (yes or no)? (y/n): ").lower()
        if roll_hold == 'n':
            total_score += player_turnscore
            print(f"Total score: {total_score}")
            break
        elif roll_hold != 'y':
            print("Invalid input! Turn ended.")
            break

    if total_score >= 100:
        print("YOU WIN!")
        break

    
