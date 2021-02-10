def anagram(word1, word2):
    list_word1 = list(word1)
    list_word1.sort()
    list_word2 = list(word2)
    list_word2.sort()

    return(list_word1 == list_word2)

print(anagram('car', 'arc'))
print(anagram('bad', 'mad'))
