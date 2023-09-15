
gradeDic = {"A+" : 4.5, "A0":4.0, "B+"	:3.5,"B0"	:3.0,"C+"	:2.5,"C0"	:2.0,"D+"	:1.5,"D0"	:1.0,"F":0.0}

aveGrade = 0
gradeCount = 0
count = 0
while ( count < 20 ) :
    inputStr = input()
    gradeList = inputStr.split()
    if (gradeList[2] != "P") :
        gradeCount += float(gradeList[1])
        aveGrade += gradeDic[gradeList[2]] * float(gradeList[1])
    count = count + 1

aveGrade = aveGrade / gradeCount
print(aveGrade)