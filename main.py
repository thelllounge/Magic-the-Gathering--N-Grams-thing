#Everything is still hard to read. Try and find a better way to make it easier to read the dictionaries.
import json

# with open('oracle-cards-20211214100357.json') as json_file:
f = open('card_data.json', encoding="utf-8")
card_data = json.load(f)

# This is the dictionary everything gets added to using the name of the card as a key and some arrays
# The goal is to make these two arrays and the conbine them as a dictionary with names being the key and oracle_text being the value
### This isn't where I'm having trouble. These are notes for me to remind me what to do after I figure everything out with the key trouble.
### I want to get all of the oracle text of cards so I can eventually run an n-gram thing on them to get the most common phrases/grammar used on cards so I can make better study material based on Magic the Gathering.
names = []
oracle_text = []
cmc = []

#I got the names to work, but the oracle text still isn't working for some reason.
#I have tried color identity, CMC, type_line and they all work, but not oracle_text!
for card in card_data:
  names.append(card['name'])
  cmc.append(card['cmc'])
  # oracle_text.append(card['oracle_text']) ###this is where the trouble is. i'm getting KeyError: 'oracle_text'

### here are the keys from the json that contain every card printed in magic. 'oracle_text' SHOULD work, right? I have even tried copying and pasting it in case it was a spelling mistake.

print(card_data[10].keys())

# ###I can access every key I've tried this way. 'oracle_text' works here, but it doesn't work above when trying to add everything into an array although MOST of the keys do.
# print(card_data[100]['name'])
# print(card_data[100]['oracle_text'])


# #This is just me testing things out to make sure things line up, testing where mistakes could have been. top, middle, end were so when I DID make mistakes I could more easily see where they were.
# print('top')
# print(names[0], names[100], names[1000])
# print('middle')
# print(len(names))
# print(cmc[0], cmc[100], cmc[1000])
# print('end')