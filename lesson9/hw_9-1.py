def popular_words (text, words):
    """
    The function popular_words takes a text and a set of words and returns a dictionary of words and their frequencies.

    :param text:
    :param words:
    :return: dictionary with words as keys and their frequencies as values.
    """
    words = list(words)
    words_in_text = (str(text)).strip().lower().split()
    result = {}
    for raw_word in words_in_text:
        for word in words:
            if word in words_in_text:
                find = words_in_text.index(word)
                if find >= 0:
                    if not word in result:
                        result.update({word: 1})
                    else:
                        result[word] = result[word] + 1
                words_in_text.remove(word)
            elif word not in result:
                result.update({word: 0})
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
