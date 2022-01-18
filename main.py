from random import randint



def throwDice(ma):
    return randint(1, ma)




def play(size, ma):
    p1_position = 0
    p2_position = 0

    while True:
        p1x = throwDice(ma)
        p1_position+=p1x

        if p1_position>=size:
            return "P1"

        p2x = throwDice(ma)
        p2_position+=p2x

        if p2_position>=size:
            return "P2"








#tests = int(input("Enter number of tests: "))
n = int(input("Enter Board length: "))
#ma = int(input("Enter max value od Dice: "))

tests=int(input("Enter number of tests: "))
ta=tests
ma=6
p1c = 0
p2c = 0
games = 0
while tests > 0:
    games += 1

    t = play(n, ma)
    print(t)
    if t == "P1":
        p1c += 1
    else:
        p2c += 1
    p1p = p1c * 100 / games
    p2p = p2c * 100 / games
    print(games, ") ", "P1%=", p1p)
    print(games, ") ", "P2%=", p2p)

    tests -= 1

print("-------------------------------------------------")
print("-------------------------------------------------")
print("Board Order= ", n)
print("No. of games played= ", ta)
print("Max dice value= ", ma)

print("P1 won: ", p1c, ", Win rate= ", p1c * 100 / ta)
print("P2 won: ", p2c, ", Win rate= ", p2c * 100 / ta)
print()
print("P1 Deviation from 50% = ",((p1c * 100 / ta)-50))
print("P2 Deviations = ",((p2c * 100 / ta)-50))




