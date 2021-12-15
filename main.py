#Everything is still hard to read. Try and find a better way to make it easier to read the dictionaries.

import json
print('hello')
cards = open('oracle-cards-20211214100357.json')
card_data = json.load(cards)

# with open('oracle-cards-20211214100357.json') as json_file:
#     card_data = json.load(json_file)

#This is the dictionary everything gets added to using the name of the card as a key
by_names = {}

#This is the loop that takes all of the cards and puts them in the by_names dictionary
for card in card_data:
  for name in card:
    by_names[card['name']] = card

#Finally getting to access things the way I want to.
print(type(by_names))
print(by_names['Slow Motion'])

#These are how I figured out how I needed to access what. Keeping for now in case I need them again in the future and they help me know when something is done loading.
print(type(card_data))
print(type(card_data[0]))
print(type(card_data[0]['name']))