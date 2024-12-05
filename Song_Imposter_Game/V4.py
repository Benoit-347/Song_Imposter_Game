#optimized by code gpt
import random

def main():
    global n1
    n1 = 0
    while True:
        o = 'y' #if o outside, it will only assign when inside if and not ask again when outside if, if input n then change mind and play again need to change n too
        d = ['Jimikki Kammal\n', '1234 get on the dance floor\n', 'Appangal Eambadum\n', 'thodakum maankalyam\n', 'pasuli\n', 'dholbaaje\n','beiliever\n']
        t = ['levitating\n', 'perfect\n', 'summertime\n', 'snowman\n', 'girls like you\n','despacito\n','dandelions']
        print(len(d), len(t), "is number of elements")
        while len(d) > 0 and len(t) > 0:
            a = random.choice(d)
            d.remove(a)
            e = random.choice(t)
            t.remove(e)
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

main()