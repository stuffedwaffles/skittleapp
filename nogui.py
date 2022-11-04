import json
import time as t
import math
from math import *

print("Welcome to the Skittle Stats App!")
print()

def inputData():
    totalPerPack = int(input("Please enter the total number of skittles in the pack: "))
    color = input("Please enter the color of the skittle (green, red, orange, yellow, purple): ")
    totalColor = int(input("Please enter the total number of " + color + " skittles in the pack: "))
    percentAsDecimalColor = round(totalColor/totalPerPack, 4)
    percentColor = percentAsDecimalColor *100

    with open(r'stuf\actual projects\skittleapp\skittlestat.txt', 'r') as f:
        file = f.read()
        skittle_dict = eval(file)

    skittle_dict[color].append(percentAsDecimalColor)
    print()
    print(f"The pack of {totalPerPack} skittles was {percentColor}% {color}. \nData has been added to the Skittle Stats!")
    print()

    with open(r'stuf\actual projects\skittleapp\skittlestat.txt', 'w') as f:
            file = f.write(str(skittle_dict))

def showStats():
    totalPerPack = int(input("Please enter the total number of skittles in the pack: "))

    with open(r'stuf\actual projects\skittleapp\skittlestat.txt', 'r') as f:
        file = f.read()
        skittle_dict = eval(file)
    
    for color, percent_list in skittle_dict.items():
        if len(percent_list) == 0:
            print()
            print("There is currently no data in the Skittle Stat machine.")
            print()
            break
        else:
            percent_sum = 0
            for percent in percent_list:
                percent_sum += percent

            percent_avgdec = (percent_sum/len(percent_list))
            percent_avg = (percent_sum/len(percent_list))*100
            number_per_pack = percent_avgdec*totalPerPack

            print()
            print(f"Color: {color} \tAverage Percent: {percent_avg} \tEstimated Number in Pack: {number_per_pack}")
            print()

        

while True:
    option = input("Would you like to input data (in) or see the Skittle Stats (stat) or leave(break)? ")
    if option == "in":
            inputData()
    elif option == "stat":
            showStats()
    elif option == "break":
        break
