import random

def main():
    a1 = 'y'
    global n1, x, y, p, q  # Declares n1 as a global variable
    n1 = 0
    while a1 == 'y':
        o = 'y' #if o outside, it will only assign when inside if and not ask again when outside if, if input n then change mind and play again need to change n too
        d = ['Jimikki Kammal\n', '1234 get on the dance floor\n', 'Appangal Eambadum\n', 'thodakum maankalyam\n', 'pasuli\n', 'dholbaaje\n','beiliever\n','taki taki\n','drag me down\n']
        t = ['levitating\n', 'perfect\n', 'summertime\n', 'snowman\n', 'girls like you\n','despacito\n','dandelions\n','love me like you do\n','love story\n']
        print(len(d), len(t), "is number of elements")
        while True:
            if len(d) == 0 or len(t) == 0:
                print("Oops! Ran out of songs")
                break
            if o == 'y':
                a = random.choice(d)
                d.remove(a)
                e = random.choice(t)
                t.remove(e)
                z = []
                [z.append(a) for _ in range(3)]
                z.append(e)
                random.shuffle(z)
                x, y, p, q = z #unpacks list to the multiple var only when no of list elements macth var no
                write_myfiles()
            else:
                break
            o = input("Continue? (y/n):")
        print("This game session has ended")
        a1 = input("Play game again? (y/n):")

def write_myfiles():
    with open('Song_imposter_game_files/1.txt', 'r') as file1:
        content1 = file1.readlines()
    content1.append(x)

    with open('Song_imposter_game_files/1.txt', 'w') as file1:
        file1.writelines(content1)

    print("File1 edited successfully.")

    with open('Song_imposter_game_files/2.txt', 'r') as file2:
        content2 = file2.readlines()
    content2.append(y)

    with open('Song_imposter_game_files/2.txt', 'w') as file2:
        file2.writelines(content2)

    print("File2 edited successfully.")


    with open('Song_imposter_game_files/3.txt', 'r') as file3:
        content3 = file3.readlines()
    content3.append(p)

    with open('Song_imposter_game_files/3.txt', 'w') as file3:
        file3.writelines(content3)

    print("File3 edited successfully.")


    with open('Song_imposter_game_files/4.txt', 'r') as file4:
        content4 = file4.readlines()
    content4.append(q)

    with open('Song_imposter_game_files/4.txt', 'w') as file4:
        file4.writelines(content4)
    global n1
    n1 = n1 + 1
    print("File4 edited successfully.")

def clear_file_data():
    with open('Song_imposter_game_files/1.txt', 'w') as file3:
        pass
    with open('Song_imposter_game_files/2.txt', 'w') as file3:
        pass
    with open('Song_imposter_game_files/3.txt', 'w') as file3:
        pass
    with open('Song_imposter_game_files/4.txt', 'w') as file3:
        pass
    print("data deleted")
main()
print("Number of games played:", n1)
#if main() in print it will run again
clear = input("clear prev log data? (y/n):")
if clear == 'y':    
    clear_file_data()