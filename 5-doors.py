# After door 6 I should have at least 4 coins with me, so I can bribe the remaining 4 guards. 
# After door 5 I need 7 coins (double - 1, as I don't end where I started). 
# After door 4 I need 12 (double - 2)
# At door 4, again double -1...
# Let's python calculate the rest

coins = 4
for door in range(5,-1,-1):
    if coins % 2 == 0:
        coins = coins * 2 - 1
    else:
        coins = coins * 2 -2
    #print(door, coins)
print(coins)
# 172 coins
