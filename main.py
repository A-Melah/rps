import random

while True:
    
    print(""" Pick a play:
          R for Rock
          P for paper
          S for Scissors""")
    allowed_inputs = ["r", "p", "s"]
    allowed_inputs_descr = ["Rock", "Paper", "Scissors"]
    
    player = input("Enter a letter...  ")
    if player not in allowed_inputs:
        print("wrong input, please try again.")
    elif player in allowed_inputs:
        cpu = random.choice(allowed_inputs)
        print("Player (" + allowed_inputs_descr[allowed_inputs.index(player)] + ")" +":" + "CPU (" + allowed_inputs_descr[allowed_inputs.index(cpu)] + ")")
        if player == cpu:
            print(f"It's a tie!")
        elif player == "r":
            if cpu == "s":
                print(f"{allowed_inputs_descr[allowed_inputs.index(player)]} smashes {allowed_inputs_descr[allowed_inputs.index(cpu)]}! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif player == "p":
            if cpu == "r":
                print(f"{allowed_inputs_descr[allowed_inputs.index(player)]} covers {allowed_inputs_descr[allowed_inputs.index(cpu)]}! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif player == "s":
            if cpu == "p":
                print(f"{allowed_inputs_descr[allowed_inputs.index(player)]} cuts {allowed_inputs_descr[allowed_inputs.index(cpu)]}! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
            
        
