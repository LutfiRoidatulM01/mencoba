import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("haruskah kau ku beri kesempatan", 0.07),
        ("ingin aku jadi kekasih yang baik", 0.07),
        ("berikan aku kesempatan oh", 0.08),
        ("tahukah dirimu, tahukah hatimu?", 0.06),
        ("berulang kuketuk, aku mencintamu", 0.08),
        ("tapi dirimu tak pernah sadari", 0.05),
        ("AKU YANG JATUH CINTA", 0.10)
    ]
    delays = [3, 2.5, 6.2, 3.5, 4, 3.5, 3.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
print_lyrics()