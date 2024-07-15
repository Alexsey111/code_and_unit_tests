letters = ['а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'ю', 'е', 'и']

def glossary_letters(text):
    count = 0
    text = text.lower()
    for i in text:
        if i in letters:
            count += 1
    return count




