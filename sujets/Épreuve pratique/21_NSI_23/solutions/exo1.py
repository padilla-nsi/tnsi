def occurence_lettres(phrase):
    occurences = {}
    for lettre in phrase:
        if lettre in occurences:
            occurences[lettre] += 1
        else:
            occurences[lettre] = 1
    return occurences


assert occurence_lettres('Hello world !') == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}