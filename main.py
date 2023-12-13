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


#Hier Startet das Spiel. 
def main():
    player_o = []  # [column, row, if CAP]
    player_x = []
    seq = " " + input("Press Enter oder gib eine Sequenz ein: ")

    if len(seq) > 1:
        seq_at = 1
        while True:  # gameloop for sequenz
            #Spieler O
            if seq_at > len(seq):
                return 0
            build_board(player_o, player_x)
            next_turn = turn("O", player_o, player_x, seq, seq_at)
            player_o.append(next_turn[0])
            if check_draw("O", player_o, player_x):
                build_board(player_o, player_x)
                print("Unentschieden")
                return 0
            if "r" in player_o:
                return 0
            try:
                seq_at = next_turn[1]
            except:
                print("index out of range. \nGib eine neue Sequenz ein.")
                return 0
            if check_win("O", player_o, player_x):
                build_board(player_o, player_x)
                print("Spieler O hat gewonnen.\n\n\n\n")
                return 0

            #Spieler X
            if seq_at > len(seq):
                return 0
            build_board(player_o, player_x)
            next_turn = turn("X", player_o, player_x, seq, seq_at)
            player_x.append(next_turn[0])
            if check_draw("X", player_o, player_x):
                build_board(player_o, player_x)
                print("Unentschieden")
                return 0
            if "r" in player_x:
                return 0
            try:
                seq_at = next_turn[1]
            except:
                print("index out of range. \nGib eine neue Sequenz ein.")
                return 0
            if check_win("X", player_o, player_x):
                build_board(player_o, player_x)
                print("Spieler X hat gewonnen. \n\n\n\n")
                return 0

    else:
        while True:  # gameloop
            seq_at = 0
            build_board(player_o, player_x)
            player_o.append(turn("O", player_o, player_x)[0])
            if check_draw("O", player_o, player_x):
                build_board(player_o, player_x)
                print("Unentschieden")
                return 0
            if "r" in player_o:
                return 0
            if check_win("O", player_o, player_x):
                build_board(player_o, player_x)
                print("Spieler O hat gewonnen.\n\n\n\n")
                return 0

            build_board(player_o, player_x)
            player_x.append(turn("X", player_o, player_x)[0])
            if check_draw("X", player_o, player_x):
                build_board(player_o, player_x)
                print("Unentschieden")
                return 0
            if "r" in player_x:
                return 0
            if check_win("X", player_o, player_x):
                build_board(player_o, player_x)
                print("Spieler X hat gewonnen. \n\n\n\n")
                return 0


# Verwaltet den Spielzug des Spielers
def turn(player, player_o, player_x, seq="", seq_at=0):
    choice = player_input(player, player_o, player_x, seq, seq_at)
    if choice == "r":
        return ["r", 0]
    try:
        seq_at = choice[1]
    except:
        print("index out of range. \nGib eine neue Sequenz ein.")
        choice = "r" 
    choice = choice[0]

    
    placement = place_choice(choice, player_o, player_x, player)
    return [placement, seq_at]  # [column, row, if CAP]


# Nimmt den Input der Spieler.
def player_input(player, player_o, player_x, seq, seq_at):
    choice = ""
    end = False
    while True:
        con = False
        if seq_at > 0:
            if seq_at >= len(seq):
                return "r"
            try:
                choice = seq[seq_at]
            except:
                return "r"

            try:
                if seq[seq_at + 1] in ["x", "o"]:
                    choice = seq[seq_at:seq_at + 2]
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
            if 0 <= int(choice[0]) <= 9:
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
        elif 0 <= int(choice[0]) <= 9:
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
    return [choice, seq_at]  # [column, if CAP]


# Nimmt die Spalte und gibt aus wo das Stück hin fällt
def place_choice(choice, player_o, player_x, player):
    if choice[1]:
        if choice[0] >= 5:
            if player == "O":
                for i in range(5, 2, -1):
                    if [choice[0], i, 0] in player_o:
                        return [choice[0], i + 1, 1]
                    if [choice[0], i, 1] in player_o:
                        return [choice[0], i + 1, 1]
                    if [choice[0], i, 0] in player_x:
                        player_x.remove([choice[0], i, 0])
                        return [choice[0], i, 1]
                    if [choice[0], i, 1] in player_x:
                        return [choice[0], i + 1, 1]
                return [choice[0], 3, 1]
            else:
                for i in range(5, 2, -1):
                    if [choice[0], i, 0] in player_o:
                        player_o.remove([choice[0], i, 0])
                        return [choice[0], i, 1]
                    if [choice[0], i, 1] in player_o:
                        return [choice[0], i + 1, 1]
                    if [choice[0], i, 0] in player_x:
                        return [choice[0], i + 1, 1]
                    if [choice[0], i, 1] in player_x:
                        return [choice[0], i + 1, 1]
                return [choice[0], 3, 1]

        if choice[0] < 5:
            if player == "O":
                for i in range(0, 3):
                    if [choice[0], i, 0] in player_o:
                        return [choice[0], i - 1, 1]
                    if [choice[0], i, 1] in player_o:
                        return [choice[0], i - 1, 1]
                    if [choice[0], i, 0] in player_x:
                        player_x.remove([choice[0], i, 0])
                        return [choice[0], i, 1]
                    if [choice[0], i, 1] in player_x:
                        return [choice[0], i - 1, 1]
                return [choice[0], 2, 1]
            else:
                for i in range(0, 3):
                    if [choice[0], i, 0] in player_o:
                        player_o.remove([choice[0], i, 0])
                        return [choice[0], i, 1]
                    if [choice[0], i, 1] in player_o:
                        return [choice[0], i - 1, 1]
                    if [choice[0], i, 0] in player_x:
                        return [choice[0], i - 1, 1]
                    if [choice[0], i, 1] in player_x:
                        return [choice[0], i - 1, 1]
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
            return [choice[0], i, 0]


# Baut den Ramen auf und ruft check_row()
def build_board(player_o, player_x):
    print("\n\n\n\n\n")
    print("   5 6 7 8 9     \n ┌ ─ ─ ─ ─ ─ ┐  ")
    for i in range(5, -1, -1):
        print(" |", end="")
        check_row(i, player_o, player_x)
        print("| " + str(i))
    print(" └ ─ ─ ─ ─ ─ ┘ \n   0 1 2 3 4     ")


# Geht die aktuelle Reihe ab und zeichnet wenn noetig x, o.
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


# Schaut ob der Spieler gewonnen hat.
def check_win(player, player_o, player_x):
    player_o_pos = [sub[: -1] for sub in player_o]
    player_x_pos = [sub[: -1] for sub in player_x]
    player_o_big = [sub[2:] for sub in player_o]
    player_x_big = [sub[2:] for sub in player_x]
    
    # links nach rechts
    for c in range(2):
        for r in range(6):
            cur = 1
            if [c, r] in player_o_pos:
                for n in range(1, 5):
                    if cur == 4:
                        # Spieler O hat gewonnen.
                        return 1
                    if [c + n, r] in player_o_pos:
                        cur += 1
                        continue
                    else:
                        break
            elif [c, r] in player_x_pos:
                for n in range(1, 5):
                    if cur == 4:
                        # Spieler X hat gewonnen.
                        return 1
                    if [c + n, r] in player_x_pos:
                        cur += 1
                        continue
                    else:
                        break
                    
    # unten nach oben
    for c in range(5):
        for r in range(3):
            cur = 1
            if [c, r] in player_o_pos:
                for n in range(1, 5):
                    if cur == 4:
                        # Spieler O hat gewonnen.
                        return 1
                    if r + n >= 3:
                        if [c + 5, r + n] in player_o_pos:
                            cur += 1
                            continue
                    if [c, r + n] in player_o_pos:
                        cur += 1
                        continue
                    else:
                        break
            elif [c, r] in player_x_pos:
                for n in range(1, 5):
                    if cur == 4:
                        # Spieler X hat gewonnen.
                        return 1
                    if r + n >= 3:
                        if [c + 5, r + n] in player_x_pos:
                            cur += 1
                            continue
                    elif [c, r + n] in player_x_pos:
                        cur += 1
                        continue
                    else:
                        break

    # schräg nach oben
    for c in range(2):
        for r in range(3):
            cur = 1
            if [c, r] in player_o_pos:
                for n in range(1, 5):
                    if cur == 4:
                        # Spieler O hat gewonnen.
                        return 1
                    if r + n >= 3:
                        if [c + 5 + n, r + n] in player_o_pos:
                            cur += 1
                            continue
                    if [c + n, r + n] in player_o_pos:
                        cur += 1
                        continue
                    else:
                        break
            elif [c, r] in player_x_pos:
                for n in range(1, 5):
                    if cur == 4:
                        # Spieler X hat gewonnen.
                        return 1
                    if r + n >= 3:
                        if [c + 5 + n, r + n] in player_x_pos:
                            cur += 1
                            continue
                    elif [c + n, r + n] in player_x_pos:
                        cur += 1
                        continue
                    else:
                        break

    # schräg nach unten
    for c in range(5, 7):
        for r in range(5, 2, -1):
            cur = 1
            if [c, r] in player_o_pos:
                for n in range(1, 5):
                    if cur == 4:
                        # Spieler O hat gewonnen.
                        return 1
                    if r - n <= 2:
                        if [c - 5 + n, r - n] in player_o_pos:
                            cur += 1
                            continue
                    if [c + n, r - n] in player_o_pos:
                        cur += 1
                        continue
                    else:
                        break
            elif [c, r] in player_x_pos:
                for n in range(1, 5):
                    if cur == 4:
                        # Spieler X hat gewonnen.
                        return 1
                    if r - n <= 2:
                        if [c - 5 + n, r - n] in player_x_pos:
                            cur += 1
                            continue
                    elif [c + n, r - n] in player_x_pos:
                        cur += 1
                        continue
                    else:
                        break

def check_draw(player, player_o, player_x):
    player_o_pos = [sub[: -1] for sub in player_o]
    player_x_pos = [sub[: -1] for sub in player_x]
    all_player_pos = player_o_pos
    all_player_pos.extend(player_x_pos)
    player_o_big = [sub[2:] for sub in player_o]
    player_x_big = [sub[2:] for sub in player_x]

    #Wenn der Spieler seinen großen Stein noch hat, kann es nicht unentschieden sein.
    if player == "O":
        if not ([1] in player_o_big[:-1]):
            return 0
    if player == "X":
        if not ([1] in player_x_big[:-1]):
            return 0

    #Schau ob die obersten Reihen gefüllt sind.
    for c in range(5):
        if not ([c, 0] in all_player_pos):
            return 0
        if not ([c+5, 5] in all_player_pos):
            return 0
    
    #Alle Felder belegt und Spieler hat keinen großen Stein
    return 1

while True:
    main()
