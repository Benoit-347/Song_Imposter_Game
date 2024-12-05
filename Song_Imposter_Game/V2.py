import random

def main():
    a1 = 'y'
    n1 = 0
    while a1 == 'y':
        d = ['Jimikki Kammal\n', '1234 get on the dance floor\n', 'Appangal Eambadum\n', 'thodakum maankalyam\n', 'pasuli\n', 'dholbaaje\n','beiliever\n']
        t = ['levitating\n', 'perfect\n', 'summertime\n', 'snowman\n', 'girls like you\n','despacito\n','dandelions']
        z = []
        print(len(d), len(t), "is number of elements")
        while True:
            if len(d) == 0 or len(t) == 0:
                print("Oops! Ran out of songs")
                break
            o = 'y'
            if o == 'y':
                a = random.choice(d)
                d.remove(a)
                e = random.choice(t)
                t.remove(e)
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

                print("File2 edited successfully.")


                with open('3.txt', 'r') as file3:
                    content3 = file3.readlines()
                content3.append(p)

                with open('3.txt', 'w') as file3:
                    file3.writelines(content3)

                print("File3 edited successfully.")


                with open('4.txt', 'r') as file4:
                    content4 = file4.readlines()
                content4.append(q)

                with open('4.txt', 'w') as file4:
                    file4.writelines(content4)
                n1 = n1 + 1
                print("File4 edited successfully.")
            else:
                break
            o = input("Continue? (y/n):")
        print("This game session has ended")
        a1 = input("Play game again? (y/n):")

    return n1

def clear_file_dat():
    with open('1.txt', 'w') as file3:
        pass
    with open('2.txt', 'w') as file3:
        pass
    with open('3.txt', 'w') as file3:
        pass
    with open('4.txt', 'w') as file3:
        pass
n1 = main()

print("Number of games played:", n1)
#if main() in print it will run again
clear = input("clear prev log data? (y/n):")
if clear == 'y':    
    clear_file_dat()