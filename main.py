import poker as pkr
    
nr_players = eval (input ('Enter number of players: '))
while (nr_players < 2 or nr_players > 6):
    nr_players = eval( input ('Enter number of players: ') )  

multiple_games_list = []
counter = 0
for i in range(nr_players):
    multiple_games_list.append(0)
    counter += 1

game_won = counter
while (game_won == counter):                        #a little ambiguous, but as long as nobody hit 52 points, this while loop will not end
    game = pkr.Poker (nr_players)
    game.play()
    print('\n')
    for i in range(nr_players):
        current_hand = game.hands[i]
        print ("Player "+ str(i+1) + ": " , end="")
        game.isRoyal(current_hand)

    maxpoint = max(game.tlist)
    maxindex = game.tlist.index(maxpoint)

    print ('\nPlayer %d wins'% (maxindex+1))
    multiple_games_list[maxindex] += game.multiple_games_list[maxindex]

    for i in range(nr_players):
        if multiple_games_list[i] >= 52:
            game_won -= 1                           #so as to exit the while loop and declare the winner
            print(multiple_games_list)
            print(f"Player {maxindex + 1} has won the game!")
