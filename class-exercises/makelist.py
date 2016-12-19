file = open('list.txt','w')
n=1
while n<= 10:
    file.write(input('What groceries do you need?') + '\n')
    n+=1