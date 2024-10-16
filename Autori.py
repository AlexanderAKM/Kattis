full_word = str(input())
abbreviation = [full_word[0]]

for i in range(1, len(full_word)):
    if full_word[i] == "-":
        abbreviation.append(full_word[i+1])
        i += 1

print(''.join(abbreviation))