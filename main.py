#Everything is still hard to read. Try and find a better way to make it easier to read the dictionaries.
import json
print('hello')

# with open('oracle-cards-20211214100357.json') as json_file:
f = open('card_data.json', encoding="utf-8")
card_data = json.load(f)

# This is the dictionary everything gets added to using the name of the card as a key and some arrays
# The goal is to make these two arrays and the conbine them as a dictionary with names being the key and oracle_text being the value
by_names = {}
names = []
oracle_text = []

# This is the loop that takes all of the cards and puts them in the by_names dictionary
for card in card_data:
  for name in card:
    by_names[card['name']] = card

print(by_names['Static Orb']['oracle_text'])


#I got the names to work, but the oracle text still isn't working for some reason.
for card in card_data:
  names.append(card['name'])
  # oracle_text.append(card['oracle_text'])


print('top')
print(names[0], names[100], names[1000])
print('middle')
# print(oracle_text[0], oracle_text[100], oracle_text[1000])
print('end')