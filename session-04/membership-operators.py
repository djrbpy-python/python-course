fruits = 'apple orange banana'
#
print('apple' in fruits)
print('Orange' in fruits)
print(' ' in fruits)

print('--------------')

numbers = range(-9, 13)

print(-3 in numbers)
print(13 in numbers)
print(13 not in numbers)
print(-9 not in numbers)

# example 01
for item in fruits:
    print(item, end='')

# example 02
for i in range(10):
    print(i)
    i += 3

# "for" target_list "in" expression_list ":" suite
#               ["else" ":" suite


# example 03
for _ in range(5):
    print('Hello', _)


# example 04
for _ in range(5):
    print('Hello')


# example 05
for num in range(5):
    print(num)
