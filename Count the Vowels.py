vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
text = input()
total = 0

for n in range(len(text)):
    if text[n] in vowels:
        total += 1

print(total)