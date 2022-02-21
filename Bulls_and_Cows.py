from Help_func import *

print()
print("Hi there!")
print(rozdelovnik)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(rozdelovnik)

num = cislo_pocitac()

pokusy = int(input('Zadej pocet pokusu: '))

while pokusy > 0:
    tip = input("Enter a number: ")
    if overeni_cisla(tip):
        bull_cow = numOfBullsCows(num, tip)

        if bull_cow[0] < 1 and bull_cow[1] > 1:
            print(f"{bull_cow[0]} bull, {bull_cow[1]} cows")
        elif bull_cow[0] > 1 and bull_cow[1] < 1:
            print(f"{bull_cow[0]} bulls, {bull_cow[1]} cow")
        else:
            print(f"{bull_cow[0]} bull, {bull_cow[1]} cow")
        if bull_cow[0] == 4:
            print("Correct, you've guessed the right number in 4 guesses")
            break

    else:
        print("Spatne cislo")
    pokusy -= 1
else:
    print(f"You ran out of tries. Number was {num}")
