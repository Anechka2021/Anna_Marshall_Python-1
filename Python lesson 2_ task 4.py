my_string = input('Enter a sentence with spaces between words: ').split()

for i, word in enumerate(my_string, 1):
    print(f'{i}. {word[:10]}')

    