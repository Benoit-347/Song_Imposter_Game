import random
d = ['despacito\n,', 'gimmeky kammal\n', '1234 get on the dance floor\n', 'appangalum paadum\n', 'thodakum maankalyam\n', 'pasuli\n', 'dholbaaje\n']
t = ['levitating\n,''beiliever\n,','perfect\n', 'summertime\n', 'snowman\n', 'girls like you\n']
z = []
a= b = c = random.choice(d)
e = random.choice(t)
for i in range (3):
    z.append(a)
z.append(e)
x = random.choice(z)
z.remove(x)
y = random.choice(z)
z.remove(y)
p = random.choice(z)
z.remove(p)
q = random.choice(z)
z.remove(q)

with open('1.txt', 'r') as file1:
    content1 = file1.readlines()
content1.append(x)

with open('1.txt', 'w') as file1:
    file1.writelines(content1)

print("File1 edited successfully.")

with open('2.txt', 'r') as file2:
    content2 = file2.readlines()
content2.append(y)

with open('2.txt', 'w') as file2:
    file2.writelines(content2)

print("File1 edited successfully.")


with open('3.txt', 'r') as file3:
    content3 = file3.readlines()
content3.append(p)

with open('3.txt', 'w') as file3:
    file3.writelines(content3)

print("File1 edited successfully.")


with open('4.txt', 'r') as file4:
    content4 = file4.readlines()
content4.append(q)

with open('4.txt', 'w') as file4:
    file4.writelines(content4)

print("File1 edited successfully.")

#csn repeate songs 
#need to press run to play again
#cannot easily count number of songs in list
#cannot view number of times played
#cannot clear prev game log files from here automatically