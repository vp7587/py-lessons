import string, re
def first_word(text):
    """ Пошук першого слова """
    #replace "." by space
    text = text.replace('.', ' ')
    punctuation = string.punctuation.replace('\'', '')
    text = list(text)

    #replace punctuation
    for i in text:
        if i in punctuation:
            text.remove(i)
    text = ''.join(text).strip()

    #finding first any character combination
    text = re.match(r'[\w|\']*', text)

    #return group
    return text.group(0)

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')