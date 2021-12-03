

name = str(input("Enter your name: "))

totalExam = int(input("How much exams do you have in this year? : "))

maxPoint = totalExam*50

minPoint = totalExam*-50

def intro(intro):
    print("Hi ",name,"! This program helps you to calculate your points according to your exam results. You can get maximum ",
maxPoint," points, and minimum ",minPoint," points in this year.",sep="",)

intro(intro)
