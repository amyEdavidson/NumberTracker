from datetime import datetime, timedelta

print("Let's track numbers! Please enter a number. Press 'Q' or type 'quit' to quit.")
x = input()
numList = []

while x != 'q' and x != 'Q' and x !='quit':
    if(x.isdigit):
        x = int(x)
        numList.append(x)
    else:
        print("Please enter a number or quit the game.")
    print("Let's track numbers! Please enter a number. Press 'Q' or type 'quit' to quit.")
    x = input()

listMax = max(numList)
listMin = min(numList)
listTotal = sum(numList)
listCount = len(numList)
listAvg = listTotal/listCount

print("The max is: ", end="") 
print(listMax)
print("The min is: ", end="")
print(listMin)
print("The average is: ", end="")
print(listAvg)
