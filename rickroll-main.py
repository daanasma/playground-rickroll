import subprocess
import time

url_rick_roll = r'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
reversed_friendship_score = 5

def rick_roller(link_to_open, amount_of_rolls=2):
    i = 0
    command = "cmd /c start chrome {} --new-window".format(link_to_open)
    while i < amount_of_rolls:
        subprocess.call(command, shell=True)
        time.sleep(1)
        i+=1
        print('ha')

if __name__ == '__main__':
    rick_roller(url_rick_roll, reversed_friendship_score)
    print('Daan sends his regards.')

