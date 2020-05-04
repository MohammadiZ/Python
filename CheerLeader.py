#April 13 2020
a_lib = "aeioAEIO"
word = input("I will cheer for you! Enter a word:" )
times = int(input("Enthusiastics level. (1-10):" ))
i = 0
while i < len(word):
    char = word[i]
    if char in a_lib:
        print("Give me an", char, "!", char)
    else:
        print("Give me a", char, "!", char)
    i = i + 1
print("What does that Spell?")
for i in range(times):
    print(word, "!!!")


