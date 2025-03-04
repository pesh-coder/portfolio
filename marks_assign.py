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

#boolean

#sequence
#list
#uses square brackets
num1 = [100, 300, 500]

#tuple
#use parenthesis
numbers2 = (num1, num2, num3)

#range

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



