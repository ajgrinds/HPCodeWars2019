io = open("prob9.txt").read().split(" ")
if io[0] == io[1]:
    print(f"TIE, {io[0].upper()} does not affect {io[1].upper()}")

results = {"SL": "Scissors decapitates Lizard",
           "SP": "Scissors cuts Paper",
           "PR": "Paper covers Rock",
           "RL": "Rock crushes Lizard",
           "LSp": "Lizard poisons Spock",
           "SpS": "Spock smashes Scissors",
           "LP": "Lizard eats Paper",
           "PSp": "Paper disproves Spock",
           "SpR": "Spock vaporizes Rock",
           "RS": "Rock crushes Scissors"
           }

if io[0] == "Rock":
    if io[1] == "Paper":
        print(f"ROCK LOSES, {results['PR']}")
    if io[1] == "Scissors":
        print(f"ROCK WINS, {results['RS']}")
    if io[1] == "Lizard":
        print(f"ROCK WINS, {results['RL']}")
    if io[1] == "Spock":
        print(f"ROCK LOSES, {results['SpR']}")
if io[0] == "Paper":
    if io[1] == "Rock":
        print(f"PAPER WINS, {results['PR']}")
    if io[1] == "Scissors":
        print(f"PAPER LOSES, {results['SP']}")
    if io[1] == "Lizard":
        print(f"PAPER LOSES, {results['LP']}")
    if io[1] == "Spock":
        print(f"PAPER WINS, {results['PSp']}")
if io[0] == "Scissors":
    if io[1] == "Lizard":
        print(f"SCISSORS WINS, {results['SL']}")
    if io[1] == "Paper":
        print(f"SCISSORS WINS, {results['SP']}")
    if io[1] == "Spock":
        print(f"SCISSORS LOSES, {results['SpS']}")
    if io[1] == "Rock":
        print(f"SCISSORS LOSES, {results['RS']}")
if io[0] == "Lizard":
    if io[1] == "Scissors":
        print(f"LIZARD LOSES, {results['SL']}")
    if io[1] == "Paper":
        print(f"LIZARD WINS, {results['LP']}")
    if io[1] == "Spock":
        print(f"LIZARD WINS, {results['LSp']}")
    if io[1] == "Rock":
        print(f"LIZARD LOSES, {results['RL']}")
if io[0] == "Spock":
    if io[1] == "Rock":
        print(f"SPOCK WINS, {results['SpR']}")
    if io[1] == "Paper":
        print(f"SPOCK LOSES, {results['PSp']}")
    if io[1] == "Scissors":
        print(f"SPOCK WINS, {results['SpS']}")
    if io[1] == "Lizard":
        print(f"SPOCK LOSES, {results['LSp']}")
