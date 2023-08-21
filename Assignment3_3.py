#Assignment 3.3 - write a program to return one of a range of values

score = input("Enter Score: ")

#test if input is a number
try :
    fscore = float(score)
except :
    print("Must be a number between 0.0 and 1.0")
    quit()

#test if input is in acceptable range
if fscore < 0.0 :
    print("Must be a number between 0.0 and 1.0")
    quit()
    
if fscore > 1.0 :
    print("Must be a number between 0.0 and 1.0")
    quit()

#with valid input, assign a grade
if fscore >= 0.9 :
    print("A")
elif fscore >= 0.8 :
    print("B")
elif fscore >= 0.7 :
    print("C")
elif fscore >= 0.6 :
    print("D")
else :
    print("F")
    
quit()
