import json
print('hello')
cards = open('oracle-cards-20211214100357.json')
card_data = json.load(cards)
print(card_data[0])
print('seriously?')