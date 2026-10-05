def sufficienze(voti): 
    voti = [x for x in voti if x >= 6]
    print(voti)

voti = [4, 7, 5, 8, 6, 3]
print(sufficienze([4, 7, 5, 8, 6, 3]))