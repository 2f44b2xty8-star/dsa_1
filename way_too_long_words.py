num_words = int(input())# typecasting string to integer

for i in range(num_words):
    word = input()
    word_length = len(word)
    # Finding its length
    
    if word_length > 10:
        print(word[0], word_length - 2, word[word_length - 1], sep="") # using sep
        print(f"{word[0]}{word_length - 2}{word[word_length - 1]}") # f-string
        print(word[0] + str(word_length - 2) + word[word_length - 1]) # string concatenation
    else:
        print(word)

