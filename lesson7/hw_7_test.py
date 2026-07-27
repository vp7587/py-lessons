def reverse_words(sentence):
    sentence = str(sentence)
    reversed_sentence = ""
    print(sentence.find(" "))

    while True:
        if sentence.find(" ") > 0:
            part = ''.join(reversed(sentence[0:sentence.find(" ")]))
            reversed_sentence = reversed_sentence + part + " "
            sentence = sentence[(sentence.find(" "))+1:]
        else:
            part = ''.join(reversed(sentence))
            reversed_sentence = reversed_sentence +part
            break
    return(reversed_sentence)


#assert reverse_words("Hello world") == "olleH dlrow"
print(reverse_words("Hello world"))


