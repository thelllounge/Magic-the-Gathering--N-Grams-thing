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
cmc = []

# This is the loop that takes all of the cards and puts them in the by_names dictionary
#I don't think I need this... but I'm leaving it for now. I think the other loop does all of this better by itself.
# for card in card_data:
#   for name in card:
#     by_names[card['name']] = card

print(card_data[0]['cmc'])

#I got the names to work, but the oracle text still isn't working for some reason.
#I have tried color identity, CMC, type_line and they all work, but not oracle_text!
for card in card_data:
  names.append(card['name'])
  cmc.append(card['oracle_text'])
  # oracle_text.append(card['oracle_text'])

# for card in card_data:
#   for i in range(len(names)):
#     oracle_text.append(card[i]['oracle_text'])

print(type(card_data[0]['name']))
print(type(card_data[0]['type_line']))
print(type(card_data[0]['oracle_text']))

print('top')
print(names[0], names[100], names[1000])
print('middle')
print(len(names))
print(cmc[0], cmc[100], cmc[1000])
print('end')