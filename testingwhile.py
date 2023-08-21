#using the while statement

x = input("Enter a number less than 10: ")
x = int(x)

if x >= 10 :
    x = input("Enter a number less than 10: ")
    x = int(x)
while x < 10 :
    print("Still less than 10")
    x=x+1
print("now you are done")
