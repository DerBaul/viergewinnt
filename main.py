import time

"""
    ["   5 6 7 8 9     "],
    [" ┌ ─ ─ ─ ─ ─ ┐   "],
    [" |           | 5 "],
    [" |           | 4 "],
    [" |           | 3 "],
    [" |           | 2 "],
    [" |           | 1 "],
    [" |           | 0 "],
    [" └ ─ ─ ─ ─ ─ ┘   "],
    ["   0 1 2 3 4     "]
"""

#Hier geht die Action ab
def main():
    player_o = []      #[column, row, if CAP]
    player_x = []
    seq = " " + input("Press Enter oder gib eine Sequenz ein: ")

    if len(seq) > 0:
        seq_at = 1
        while True:     #gameloop for sequenz
            if seq_at > len(seq):
                return 0
            build_board(player_o, player_x)
            player_o.append(turn("O", player_o, player_x, seq, seq_at))
            seq_at += 1
            if "r" in player_o:
                return 0
            print("Das is Player O: " + str(player_o))
            if check_win("O", player_o, player_x):
                build_board(player_o, player_x)
                print("Spieler O hat gewonnen.\n\n\n\n")
                return 0
            time.sleep(3)

            if seq_at > len(seq):
                return 0
            build_board(player_o, player_x)
            player_x.append(turn("X", player_o, player_x, seq, seq_at))
            seq_at += 1
            if "r" in player_x:
                return 0
            print("Das is Player X: " + str(player_x))
            if check_win("X", player_o, player_x):
                build_board(player_o, player_x)
                print("Spieler X hat gewonnen. \n\n\n\n")
                return 0    
            time.sleep(3)
    
    else: 
        while True:     #gameloop
            seq_at = 0
            build_board(player_o, player_x)
            player_o.append(turn("O", player_o, player_x))
            if "r" in player_o:
                return 0
            print("Das is Player O: " + str(player_o))
            if check_win("O", player_o, player_x):
                build_board(player_o, player_x)
                print("Spieler O hat gewonnen.\n\n\n\n")
                return 0

            build_board(player_o, player_x)
            player_x.append(turn("X", player_o, player_x))
            if "r" in player_x:
                return 0
            print("Das is Player X: " + str(player_x))
            if check_win("X", player_o, player_x):
                build_board(player_o, player_x)
                print("Spieler X hat gewonnen. \n\n\n\n")
                return 0


#Verwaltet den Spielzug des Spielers
def turn(player, player_o, player_x, seq, seq_at):
    choice = player_input(player, player_o, player_x, seq, seq_at)
    if choice == "r":
        return "r"         
    placement = place_choice(choice, player_o, player_x, player)
    return placement    #[column, row, if CAP]


#Nimmt den Input der Spieler.
def player_input(player, player_o, player_x, seq, seq_at):
    choice = ""
    end = False
    while True:
        con = False
        #!
        #!
        #!
        #!
        #!
        #!
        #Hier weiter machen. Du musst wahrscheinlich die seq_at aus dieser Funktion zurück zur main Bringen. Die beiden werden bei inputs wie "55aab3" mit jedem "a" usw. immer weniger sync. 
        if seq_at > 0:
            try: 
                choice = seq[seq_at]
            except:
                return "r"

            try: 
                if seq[seq_at+1] in ["x", "o"]:
                    choice = seq[seq_at:seq_at+2]
            except:
                choice = seq[seq_at]
            
            seq_at += 1
        else: 
            choice = input("akt. Spieler: " + str(player) + "\nSpalte eingeben: ")
        if choice == "r":
            return "r"
        elif len(choice) > 2:
             continue
        try:
            int(choice[0])
        except:
            continue
        if len(choice) == 2:
            if 0<=int(choice[0])<=9:
                if choice[1] in player.lower():
                    if player == "O":
                        for s in range(len(player_o)):
                            if player_o[s][2]:
                                con = True
                    if player == "X":
                        for s in range(len(player_x)):
                            if player_x[s][2]:
                                con = True
                    if con:
                        continue
                    choice = [int(choice[0]), 1]
                    end = True
                else:
                    continue
        elif 0<=int(choice[0])<=9:
            choice = [int(choice[0]), 0]
            end = True

        if choice[1]:
            if player == "O":
                    if [choice[0], 0, 0] in player_o:
                        continue
                    if [choice[0], 0, 1] in player_o:
                        continue
                    if [choice[0], 0, 1] in player_x:
                        continue
            if player == "X":
                    if [choice[0], 0, 0] in player_x:
                        continue
                    if [choice[0], 0, 1] in player_x:
                        continue
                    if [choice[0], 0, 1] in player_o:
                        continue
        else:    
            if [choice[0], 0, 0] in player_o + player_x:
                continue
            if [choice[0], 0, 1] in player_o + player_x:
                continue
            if [choice[0], 5, 0] in player_o + player_x:
                continue
            if [choice[0], 5, 1] in player_o + player_x:
                continue
         
        if end:
            break
    print("This is the choice: " + str(choice))
    return choice   #[column, if CAP]


#Nimmt die Spalte und gibt aus wo das Stück hin fällt
def place_choice(choice, player_o, player_x, player):
    if choice[1]:
        if choice[0] >= 5:
            if player == "O":
                for i in range(5, 2, -1):
                    if [choice[0], i, 0] in player_o: 
                        return [choice[0], i+1, 1]
                    if [choice[0], i, 1] in player_o: 
                        return [choice[0], i+1, 1]
                    if [choice[0], i, 0] in player_x:
                        player_x.remove([choice[0], i, 0])
                        return [choice[0], i, 1]
                    if [choice[0], i, 1] in player_x:  
                        return [choice[0], i+1, 1]
                return [choice[0], 3, 1]            
            else:
                for i in range(5, 2, -1):
                    if [choice[0], i, 0] in player_o:
                        player_o.remove([choice[0], i, 0]) 
                        return [choice[0], i, 1]
                    if [choice[0], i, 1] in player_o: 
                        return [choice[0], i+1, 1]
                    if [choice[0], i, 0] in player_x:
                        return [choice[0], i+1, 1]
                    if [choice[0], i, 1] in player_x:  
                        return [choice[0], i+1, 1]
                return [choice[0], 3, 1]
                
        if choice[0] < 5:
            if player == "O":
                for i in range(0, 3):
                    if [choice[0], i, 0] in player_o: 
                        return [choice[0], i-1, 1]
                    if [choice[0], i, 1] in player_o: 
                        return [choice[0], i-1, 1]
                    if [choice[0], i, 0] in player_x:  
                        player_x.remove([choice[0], i, 0])
                        return [choice[0], i, 1]
                    if [choice[0], i, 1] in player_x:  
                        return [choice[0], i-1, 1]
                return [choice[0], 2, 1]
            else:
                for i in range(0, 3):
                    if [choice[0], i, 0] in player_o: 
                        player_o.remove([choice[0], i, 0])
                        return [choice[0], i, 1]
                    if [choice[0], i, 1] in player_o: 
                        return [choice[0], i-1, 1]
                    if [choice[0], i, 0] in player_x:  
                        return [choice[0], i-1, 1]
                    if [choice[0], i, 1] in player_x:  
                        return [choice[0], i-1, 1]
                return [choice[0], 2, 1]
            
    if choice[0] >= 5:
        for i in range(3, 6):
            if [choice[0], i, 0] in player_o: 
                continue
            if [choice[0], i, 1] in player_o: 
                continue
            if [choice[0], i, 0] in player_x:  
                continue
            if [choice[0], i, 1] in player_x:  
                continue
            print("Das ist placement: " + str([choice[0], i, 0]))
            return [choice[0], i, 0]
    if choice[0] < 5:
        for i in range(2, -1, -1):
            if [choice[0], i, 0] in player_o: 
                continue
            if [choice[0], i, 1] in player_o: 
                continue
            if [choice[0], i, 0] in player_x:  
                continue
            if [choice[0], i, 1] in player_x:  
                continue
            print("Das ist placement: " + str([choice[0], i, 0]))
            return [choice[0], i, 0]
        

#Baut den Ramen auf und ruft check_row()
def build_board(player_o, player_x):
    print("   5 6 7 8 9     \n ┌ ─ ─ ─ ─ ─ ┐  ")
    for i in range(5, -1, -1):
        print(" |", end="")
        check_row(i, player_o, player_x)
        print("| " + str(i))
    print(" └ ─ ─ ─ ─ ─ ┘ \n   0 1 2 3 4     ")


#Geht die aktuelle Reihe ab und zeichnet wenn noetig x, o.
def check_row(row, player_o, player_x):
    
    print(" ", end="")
    if row >= 3:
        for i in range(5, 10):
            if [i, row, 0] in player_o:
                print("o", end="")
            elif [i, row, 1] in player_o:
                print("O", end="")
            elif [i, row, 0] in player_x:
                print("x", end="")
            elif [i, row, 1] in player_x:
                print("X", end="")
            else:
                print(" ", end="")
            print(" ", end="")
    else:
        for i in range(0, 5):
            if [i, row, 0] in player_o:
                print("o", end="")
            elif [i, row, 1] in player_o:
                print("O", end="")
            elif [i, row, 0] in player_x:
                print("x", end="")
            elif [i, row, 1] in player_x:
                print("X", end="")
            else:
                print(" ", end="")
            print(" ", end="")


#Schaut ob der Spieler gewonnen hat.
def check_win(player, player_o, player_x):
    player_o_pos = [sub[: -1] for sub in player_o]
    player_x_pos = [sub[: -1] for sub in player_x]

    #links nach rechts
    for c in range(2):
        for r in range(6):
            cur = 1
            if [c, r] in player_o_pos:
                for n in range(1, 5):
                    if cur == 4:
                        #Spieler O hat gewonnen.
                        return 1
                    if [c+n, r] in player_o_pos:
                        cur += 1
                        continue
                    else:
                        break
            elif [c, r] in player_x_pos:
                for n in range(1, 5):
                    if cur == 4:
                            #Spieler X hat gewonnen.
                            return 1
                    if [c+n, r] in player_x_pos:
                        cur += 1
                        continue
                    else:
                        break
        #unten nach oben
        for c in range(5):
            for r in range(3):
                cur = 1
                if [c, r] in player_o_pos:
                    for n in range(1, 5):
                        if cur == 4:
                            #Spieler O hat gewonnen.
                            return 1
                        if r+n>=3:
                            if [c+5, r+n] in player_o_pos:
                                cur += 1
                                continue
                        if [c, r+n] in player_o_pos:
                            cur += 1
                            continue
                        else:
                            break
                elif [c, r] in player_x_pos:
                    for n in range(1, 5):
                        if cur == 4:
                                #Spieler X hat gewonnen.
                                return 1
                        if r+n>=3:
                            if [c+5, r+n] in player_x_pos:
                                cur += 1
                                continue
                        elif [c, r+n] in player_x_pos:
                            cur += 1
                            continue
                        else:
                            break 
            
        #schräg nach oben
        for c in range(2):
            for r in range(3):
                cur = 1
                if [c, r] in player_o_pos:
                    for n in range(1, 5):
                        if cur == 4:
                            #Spieler O hat gewonnen.
                            return 1
                        if r+n>=3:
                            if [c+5+n, r+n] in player_o_pos:
                                cur += 1
                                continue
                        if [c+n, r+n] in player_o_pos:
                            cur += 1
                            continue
                        else:
                            break
                elif [c, r] in player_x_pos:
                    for n in range(1, 5):
                        if cur == 4:
                                #Spieler X hat gewonnen.
                                return 1
                        if r+n>=3:
                            if [c+5+n, r+n] in player_x_pos:
                                cur += 1
                                continue
                        elif [c+n, r+n] in player_x_pos:
                            cur += 1
                            continue
                        else:
                            break             

        #schräg nach unten
        for c in range(5, 7):
            for r in range(5, 2, -1):
                cur = 1
                if [c, r] in player_o_pos:
                    for n in range(1, 5):
                        if cur == 4:
                            #Spieler O hat gewonnen.
                            return 1
                        if r-n<=2:
                            if [c-5+n, r-n] in player_o_pos:
                                cur += 1
                                continue
                        if [c+n, r-n] in player_o_pos:
                            cur += 1
                            continue
                        else:
                            break
                elif [c, r] in player_x_pos:
                    for n in range(1, 5):
                        if cur == 4:
                                #Spieler X hat gewonnen.
                                return 1
                        if r-n<=2:
                            if [c-5+n, r-n] in player_x_pos:
                                cur += 1
                                continue
                        elif [c+n, r-n] in player_x_pos:
                            cur += 1
                            continue
                        else:
                            break     


            

while True:
    main()
