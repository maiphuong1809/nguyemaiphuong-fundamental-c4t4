# cách 1
alphabet ={}
word = input("Enter a word of choice: ").lower()
for i in word:
    alphabet[i] = alphabet.get(i, 0) + 1

for i, j in sorted(alphabet.items()):
    print(i, j)

