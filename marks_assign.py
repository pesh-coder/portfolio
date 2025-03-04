#integer
num = 50 
print(type(num))

#when you repeat a num it overrites the previous value
#float
num2 = 10.0 
print(type(num2))

#complex.
#with complex numbers, you can only use either "j" or "J"
num3 = 100 + 2j 
print(type(num3))

#string is a collection of characters enclosed in quotes
word = "hello" 
print(type(word))
print (word [0])

#set
#set data type - when you don't want duplicates and want random access to the data
student_id = {11, 2, 31, 44, 5, 6, 7, 88, 9, 102}

#boolean
#True or False
comp1, comp2 = 100, 200
#less than to
print(comp1 < comp2) 
#greater than to
print(comp1 > comp2) 
 #equal to
print(comp1 == comp2)

#sequence
#list
#uses square brackets
num1 = [100, 300, 500]

#tuple
#use parenthesis
numbers2 = (num1, num2, num3)

#range
def enter_number():
    number = int(input("the number of entries"))
    capture = {input("enter the key: "): input("enter value.") for _ in range(number)}
    
    print(capture)

enter_number()    

#dictionary
student_detail = {"name": "patience", "track": "python", "gender": "female", "age": 25}
#prints all the values with the brackets
print(student_detail)
#prints patience
print(student_detail["name"])

#prints the values only dic_keys and () takes no arguments
print(student_detail.keys())

#prints the values only dic_values and () takes no arguments
print(student_detail.values())

#giving the user the ability to input a number
num1  = input ("input your number here")
print ("your number is: ", num1)

# \n takes the output to be printed in the next line
a = int(input("please enter your first number:\n "))



