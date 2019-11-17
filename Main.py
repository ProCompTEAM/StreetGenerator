# (c) Kirill Poroh : 16.11.2019 > Street Generator

import os.path
import io
import random


def readlines(source):
    file = io.open(source, encoding='utf-8')
    with file as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
    return lines


def rnd(rmax):
    return random.randint(0, rmax - 1)


def makemistakes(str, mcount):
    if mcount < 1:
        return str
    else:
        for i in range(mcount):
            r = random.randint(1, len(str) - 1)
            str = str[:r] + chr(i % r) + str[r + 1:]
        return str


data = input("Input: <lines count> <region: RU, BY, EN> <mistakes> ? ")

args = data.split(' ')

if len(args) < 3:
    exit("Too few argumets :(")

count = int(args[0])
region = args[1].lower()
mistakes = float(args[2])

if count < 1 or mistakes < 0:
    exit("Invalid input data format :(")

region_file_s = "pattern/" + region + "/begin.txt"
region_file_m = "pattern/" + region + "/middle.txt"
region_file_e = "pattern/" + region + "/end.txt"
names_file = "pattern/" + region + "/names.txt"

if os.path.exists(region_file_s):
    print("Reading and forming...")

    rg_s = readlines(region_file_s)
    rg_m = readlines(region_file_m)
    rg_e = readlines(region_file_e)
    names = readlines(names_file)

    chance = round(mistakes / count)

    for i in range(count):
        rg = rg_s[rnd(len(rg_s))] + rg_m[rnd(len(rg_m))] + rg_e[rnd(len(rg_e))]
        name = names[rnd(len(names))]
        phone = str(random.randint(100, 999)) + "-" + str(random.randint(10, 99)) + "-" + str(random.randint(10, 99));

        result = " => " + name + "; " + rg.title() + ", " + str(random.randint(1, 120)) + "; tel: " + phone

        print(makemistakes(result, chance))
else:
    exit("Bad region :(")
