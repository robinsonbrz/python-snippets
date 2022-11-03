import itertools

ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
ranks = [str(rank) for rank in ranks]

print("######## Ranks ########")
print(ranks)

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades' ]
deck = [card for card in itertools.product(ranks, suits) ]

print("\n\n\n######## Deck ########")
for (index, card) in enumerate(deck):
    print(1 + index, card)

print("\n\n\n#### Possibilities ####")
hands = [hand for hand in itertools.combinations(deck, 1)]
print(f"The number of 1-card poker hands is: \n{len(hands)}.\n\n")

hands = [hand for hand in itertools.combinations(deck, 2)]
print(f"The number of 2-card poker hands is: \n{len(hands)}.\n\n")
# print(hands) # print all the pssible combinations

hands = [hand for hand in itertools.combinations(deck, 3)]
print(f"The number of 3-card poker hands is: \n{len(hands)}.\n\n")

hands = [hand for hand in itertools.combinations(deck, 4)]
print(f"The number of 4-card poker hands is: \n{len(hands)}.\n\n")

hands = [hand for hand in itertools.combinations(deck, 5)]
print(f"The number of 5-card poker hands is: \n{len(hands)}.\n\n")

hands = [hand for hand in itertools.combinations(deck, 6)]
print(f"The number of 6-card poker hands is: \n{len(hands)}.\n\n")