fruit = 'Banana'
fruitRipeness = {'Green': 'unripe', 'Yellow': 'ripe', 'Brown': 'overripe'}
userInput = input('What color is the banana? ')
if userInput in fruitRipeness:
    print(f'The banana is {fruitRipeness[userInput]}')
else:
    print('I don\'t know what that means')