import random


rozdelovnik = "-"*50


def ziskani_cisla(num):
    return [int(i) for i in str(num)]

def noDuplicate(num):
    num_li = ziskani_cisla(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False

def cislo_pocitac():
    #while True:
        num = random.randint(1000, 9999)
        if noDuplicate(num):
            return num


def numOfBullsCows(num, tip):
    bull_cow = [0, 0]
    num_li = ziskani_cisla(num)
    tip_li = ziskani_cisla(tip)

    for i, j in zip(num_li, tip_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

def overeni_cisla(tip):
    if len(tip) != 4:
        print ("not a four digit number")
        return False
    if tip[0] == '0':
        print ("1st digit cannot be 0")
        return False
    if not tip.isdigit():
        print ("it is not a number")
        return False
    for i in tip:
        if tip.count(i) != 1:
            print ("number cannot have repeated digits")
            return False
    return True
