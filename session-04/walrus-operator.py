num = 13
print(num)

print(num := 5)

# example 01
while value := int(input('num: ')):
    if value == 0:
        break
    else:
        print(value)

# example 02
while (value := int(input('num: '))) != 0:
    print(value)


# example 03
words = []

while (word := input("Enter word: ")) != "quit":
    words.append(word)

print(words)

# example 04
total = 0
while (num := float(input("Enter a Number: "))) != 0:
    total += num

print(total)


while (num := float(input("Enter a Number: "))) != 0:
    print(num)
