
my_f = open('test.txt', 'w')
line = input('Enter your text: \n')
while line:
    my_f.writelines(line)
    line = input('Enter your text \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()
