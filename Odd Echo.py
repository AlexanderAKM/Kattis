number_words = int(input())
odd_words = []

for i in range(number_words):
    word = input()
    if i % 2 == 0:
        odd_words.append(word)

for word in odd_words:
    print(word)