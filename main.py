#Everything is still hard to read. Try and find a better way to make it easier to read the dictionaries.
import json

# with open('oracle-cards-20211214100357.json') as json_file:
f = open('card_data.json', encoding="utf-8")
card_data = json.load(f)

# This is the dictionary everything gets added to using the name of the card as a key and some arrays
# The goal is to make these two arrays and the conbine them as a dictionary with names being the key and oracle_text being the value
names = []
oracle_text = []
cmc = []

#I got the names to work, but the oracle text still isn't working for some reason.
#I have tried color identity, CMC, type_line and they all work, but not oracle_text!
for card in card_data:
  names.append(card['name'])
  cmc.append(card['cmc'])
  oracle_text.append(card['oracle_text'])
print(card_data[100]['name'])
print(card_data[100]['oracle_text'])

# for card in card_data:
#   for i in range(len(card_data)):
#     oracle_text.append(card['oracle_text'])

print('top')
print(names[0], names[100], names[1000])
print('middle')
print(len(names))
print(cmc[0], cmc[100], cmc[1000])
print('end')
print(card_data[100].keys(), card_data[100]['colors'])