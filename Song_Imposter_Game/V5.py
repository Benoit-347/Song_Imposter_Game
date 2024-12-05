#added get_songname fn that reads songs from 2 files and uses its data
import random

def main():
    global n1
    n1 = 0
    while True:
        s1 = get_songname('Song_imposter_game_files/songs1.txt')
        s2 = get_songname('Song_imposter_game_files/songs2.txt')
        while len(s1) > 0 and len(s2) > 0:
            a = random.choice(s1)
            s1.remove(a)
            e = random.choice(s2)
            s2.remove(e)
            z = [a]*3 + [e]
            random.shuffle(z)
            x, y, p, q = z #unpacks list to the multiple var only when no of list elements macth var no
            write_myfiles(x, y, p, q)
            n1 = n1 + 1
            o = input("Continue? (y/n):")
            if o != 'y':
                break
        print("This game session has ended")
        if (input("Play game again? (y/n):")) != 'y':
            break
    print("Number of games played:", n1)
    #if main() in print it will run again
    clear = input("clear prev log data? (y/n):")
    if clear == 'y':    
        clear_file_data()

def write_myfiles(a, b, c, d):
    a0 = ["Song_imposter_game_files/1.txt", "Song_imposter_game_files/2.txt", "Song_imposter_game_files/3.txt", "Song_imposter_game_files/4.txt"]
    b0 = [a, b, c, d]
    for _, _1 in zip(a0, b0): #The zip function combines these two lists, allowing you to iterate over both simultaneously

        with open(_, 'r') as file:
            content = file.readlines()
        content.append(_1)

        with open(_, 'w') as file:
            file.writelines(content)

        print(_, "edited successfully.")

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

#copy data from file, convert to list and store to a variable
def get_songname(a):
    with open(a, 'r') as file_s:
        content = file_s.read()
    s  = []
    content = content.split('\n')
    for i in content:
        s = s + [i]
    if s[-1] == '':
        s.pop()
    #s = [i for i in content if i.strip() != ""]
    print(f"{len(s)}, is number of elements",s)
    return s
main()