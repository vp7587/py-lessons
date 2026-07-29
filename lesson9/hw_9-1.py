def popular_words (text, words):
    text = (str(text)).strip().lower()
    print(text)
    words = list(words)
    result = {}
    i = 1
    count_words = text.count(" ")+1
    while i <= count_words:
        for word in words:
            find = text.find(word)
            if  find >0  and word in result:
                result[word] = result[word] + 1
            elif find >0 :
                result[word] = 1
                result.update({word: result[word]})
            elif  word not in result:
                result[word] = 0
                result.update({word: result[word]})
            text = text.replace(word, "", 1)
        i = i + 1
    return result

#assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1' print('OK')
popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])