import random

numbers = open('numbers.txt', mode = 'at', encoding = 'utf-8')

for i in range(100):
    number = str(random.randint(1, 100))
    numbers.writelines("%s\n" % number)

numbers.close()

numbers = open('numbers.txt', encoding = 'utf-8')
even = open('even.txt', mode = 'at', encoding = 'utf-8')
odd = open('odd.txt', mode = 'at', encoding = 'utf-8')

line_list = numbers.read().splitlines()

for line in line_list:
    if int(line) % 2 == 0:
        even.writelines("%s\n" % line)
    else:
        odd.writelines("%s\n" % line)

odd.close()
even.close()
numbers.close()