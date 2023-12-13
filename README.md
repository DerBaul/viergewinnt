Vier Gewinnt von Paul Zintl
Python 3.10.8


Beim Start des Programs erscheint folgender Aufforderung:
    "Press Enter oder gib eine Sequenz ein: "

Debug/Sequenz:
    Gebe die Sequenz am Anfang des Spieles ein. 
    Die Sequenz wird jetzt abgearbeitet so als wäre sie eine Reihe von "echten" Eingaben.
    Das heißt das auch fehlerhafte Eingaben wie die eines Nutzers behandelt werden.
    Bei fehlerhafter Eingabe wird diese abgelehnt und die nächste Eingabe in der Sequenz gelesen.
    Ist "O" am Zug und eine Folge wie "0x1" wir eingelesen, wird sie so aufgehteilt: "0x"(fehlerhaft) "1"(richtig).
    Eine Folge "0x1" für "O" wird NICHT so verarbeitet: O: "0"(richtig) X: "x"(fehlerhaft) "1"(richtig).
    Das Selbe gilt anders herum wenn "X" am Zug ist.
    Befindet sich ein "r" in der Sequenz, wird die Runde beendet.
    Nach Beendigung einer Runde hat man wieder die Möglichkeit eine Sequenz einzugeben.

Selbst spielen:
    Um selbst zu Spielen einfach die Aufforderung am Anfang mit Enter überspringen.
    Jetzt wechseln sich "O" und "X" mit ihren Zügen ab.
    "O" beginnt. 
    Wenn ein Spieler eine falsche Eingabe macht, wird sie abgelehnt und der Spieler ist erneut am Zug.
    
Unentschieden:
Unentschieden ist dann erreicht, wenn kein Spieler mehr einen legalen Zug spielen kann.
Wenn das Spielfeld voll ist, ist es ein legaler Zug einen großen Stein auf eine passende Stelle zu werfen.
In disem Beispiel ist "8x" der letzte legale Zug für "X".
Bsp.:
   5 6 7 8 9                                       5 6 7 8 9        
 ┌ ─ ─ ─ ─ ─ ┐                                   ┌ ─ ─ ─ ─ ─ ┐
 | x x o o O | 5                                 | x x o X O | 5
 | o o o x x | 4                 \               | o o o x x | 4
 | x x x o o | 3             ==== \              | x x x o o | 3
 | o o o x x | 2             ==== /              | o o o x x | 2
 | x x x o o | 1                 /               | x x x o o | 1
 | o x o o x | 0                                 | o x o o x | 0
 └ ─ ─ ─ ─ ─ ┘                                   └ ─ ─ ─ ─ ─ ┘
   0 1 2 3 4                                       0 1 2 3 4
Nach dem Zug "8x" ist das Spiel Unentschieden, denn "O" bleiben keine legalen Züge mehr Übrig.
