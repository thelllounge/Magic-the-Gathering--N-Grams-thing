import json
print('hello')
cards = open('oracle-cards-20211214100357.json')
card_data = json.load(cards)
print(card_data[0]['name'], card_data[0]['oracle_text'])
print('seriously?')