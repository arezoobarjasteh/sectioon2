listofscores = []

numberofscores = int(input("Please Enter count of Scores= "))
average = 0
students_num = 0

for i in range(numberofscores):
    students_num += 1
    #score = int(input(f"enter the scores of student number{students_num}:"))
    score=float(input("Please enter a Score="))
    if score>20 or score<0:
        print("Error... Score bigger than 20 0r smaller than 0")
        break
    else:
        average = float(score+average)
        listofscores.append(score)
print("average score is= ",average/numberofscores)
print("Maximum score is =" , max(listofscores))
print("minimum score is = " , min(listofscores))