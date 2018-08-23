import random

def comp(name):
    with open("compliments.txt", "r") as file:
        comps = file.readlines()	
    compStr = random.choice(comps)
    compStr = compStr.replace("$name", name)
    return compStr
