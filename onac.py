# made by Goov.
# ver 1.0 RELEASEs.
from random import *
import time
import sys

i = 0
ldoor = "open"
rdoor = "open"
energy = 4

class WCat():
	def __init__(self, speed, sps):
		self.speed = speed
		self.sps = sps
		

	
print("----------ONAC----------")
print("----------START (s)----------")
a = input("1~")
if a == "s" or a == "S":
	white_cat = WCat(30, 1)
	while i != 3:
	    rand = randint(1, 2)
	    camw = 1
	    camwg = 4 - camw
	    print("Показалось...")
	    b = input("1~ ")
	    if b == "lc" or b == "Lc":
		    ldoor = "close"
		    print("+ Левая дверь закрылась. +")
		    energy -= 1
		    print("+ Утрата енергии! У вас осталось " + str(energy) + " енергии. +")
	    if b == "lo" or b == "Lo":
		     ldoor = "open"
		     print("+ Левая дверь открылась. +")
	    if b == "rc" or b == "Rc":
		     rdoor = "close"
		     print("+ Правая дверь закрылась. +")
		     energy -= 1
		     print("+ Утрата енергии! У вас осталось " + str(energy) + " енергии. +")
	    if b == "ro" or b == "Ro":
		     rdoor = "open"
		     print("+ Правая дверь открылась. +")
	    if b == "cam" or b == "Cam":
	         print("+ Белый кот на " + str(camwg) + " камер от вас.")
	    if b == "cupoftea":
	    	if rand == 1:
	    	    print("- Кот будет нападать с левой стороны. -")
	    	elif rand == 2:
	    	    print("- Кот будет нападать с правой стороны. -")
	    if energy <= 0:
	    	    print("+ Энергия закончилась. Игра проиграна. +")
	    	    sys.exit()
	    camw = 2
	    camwg = 4 - camw
	    print("Где коты?")
	    b = input("1~ ")
	    if b == "lc" or b == "Lc":
		    ldoor = "close"
		    print("+ Левая дверь закрылась. +")
		    energy -= 1
		    print("+ У вас осталось " + str(energy) + " енергии. +")
	    if b == "lo" or b == "Lo":
		    ldoor = "open"
		    print("+ Левая дверь открылась. +")
	    if b == "rc" or b == "Rc":
		    rdoor = "close"
		    print("+ Правая дверь закрылась. +")
		    energy -= 1
		    print("+ У вас осталось " + str(energy) + " енергии. +")
	    if b == "ro" or b == "Ro":
		    rdoor = "open"
		    print("+ Правая дверь открылась. +")
	    if b == "cam" or b == "Cam":
	        print("+ Белый кот на " + str(camwg) + " камер от вас.")
	    if b == "cupoftea":
	    	if rand == 1:
	    	    print("- Кот будет нападать с левой стороны. -")
	    	elif rand == 2:
	    	    print("- Кот будет нападать с правой стороны. -")
	    if energy == 0:
	    	    print("+ Энергия закончилась. Игра проиграна. +")
	    	    sys.exit()
	    camw = 3
	    camwg = 4 - camw
	    print("Я слышу шорох...")
	    b = input("1~ ")
	    if b == "lc" or b == "Lc":
		    ldoor = "close"
		    print("+ Левая дверь закрылась. +")
		    energy -= 1
		    print("+ У вас осталось " + str(energy) + " енергии. +")
	    if b == "lo" or b == "Lo":
		     ldoor = "open"
		     print("+ Левая дверь открылась. +")
	    if b == "rc" or b == "Rc":
		     rdoor = "close"
		     print("+ Правая дверь закрылась. +")
		     energy -= 1
		     print("+ У вас осталось " + str(energy) + " енергии. +")
	    if b == "ro" or b == "Ro":
		     rdoor = "open"
		     print("+ Правая дверь открылась. +")
	    if b == "cam" or b == "Cam":
	         print("+ Белый кот на " + str(camwg) + " камер от вас.")
	    if b == "cupoftea":
	    	if rand == 1:
	    	    print("- Кот будет нападать с левой стороны. -")
	    	elif rand == 2:
	    	    print("- Кот будет нападать с правой стороны. -")
	    if energy == 0:
	    	    print("+ Энергия закончилась. Игра проиграна. +")
	    	    sys.exit()
	    camw = 4
	    camwg = 4 - camw
	    print("Привет?...")
	    b = input("1~ ")
	    if b == "lc" or b == "Lc":
		    ldoor = "close"
		    print("+ Левая дверь закрылась. +")
		    energy -= 1
		    print("+ У вас осталось " + str(energy) + " енергии. +")
	    if b == "lo" or b == "Lo":
		    ldoor = "open"
		    print("+ Левая дверь открылась. +")
	    if b == "rc" or b == "Rc":
		    rdoor = "close"
		    print("+ Правая дверь закрылась. +")
		    energy -= 1
		    print("+ У вас осталось " + str(energy) + " енергии. +")
	    if b == "ro" or b == "Ro":
		    rdoor = "open"
		    print("+ Правая дверь открылась. +")
	    if b == "cam" or b == "Cam":
	        print("+ Белый кот у вас в двери! +")
	    if b == "cupoftea":
	    	if rand == 1:
	    	    print("- Кот будет нападать с левой стороны. -")
	    	elif rand == 2:
	    	    print("- Кот будет нападать с правой стороны. -")
	    if energy == 0:
	    	 print("+ Энергия закончилась. Игра проиграна. +")
	    	 sys.exit()
		
	    if rand == 1:
	        if ldoor == "open":
	    	    print("Игра проиграна.")
	    	    sys.exit()
	        elif ldoor == "close":
	    	    print("+ Вы отбились от атаки слева. +")
	    	    print("+ Все двери открылись. +")
	    	    ldoor = "open"
	    	    rdoor = "open"
	    	    i += 1
	    if rand == 2:
	        if rdoor == "open":
	    	    print("Игра проиграна.")
	    	    sys.exit()
	        elif rdoor == "close":
	    	    print("+ Вы отбились от атаки справа. +")
	    	    print("+ Все двери открылись. +")
	    	    ldoor = "open"
	    	    rdoor = "open"
	    	    i += 1
print("+ Спасибо за игру! +")
print("+ Субтитров не будет, всё зделал Goov;) +")