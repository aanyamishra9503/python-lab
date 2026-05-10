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
            print("Rolled a 1! Turn over, score reset!")
            player_turnscore = 0
            break  # end turn immediately if 1 is rolled
        
        player_turnscore += player_turn
        print(f"Turn score: {player_turnscore}")
        
        roll_hold = input("Roll again or hold? (r/h): ").lower()
        if roll_hold == 'h':
            total_score += player_turnscore
            print(f"Total score: {total_score}")
            break
        elif roll_hold != 'r':
            print("Invalid input! Turn ended.")
            break

    if total_score >= 100:
        print("YOU WIN!")
        break

    