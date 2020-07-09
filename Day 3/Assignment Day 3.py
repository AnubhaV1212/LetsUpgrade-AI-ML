#Question 1
print("Question 1")
complex_no_1 = complex(input("Enter first complex no "))
complex_no_2 = complex(input("Enter second complex no "))
result = complex_no_1 - complex_no_2
print(result)

#Question 2
print("Question 2")
number= int(input("Enter No "))
result = (number)**(1/4)
print(result)

#Question 3
print("Question 3")
a=int(input("Enter first no "))
b=int(input("Enter second no "))
temp = b
b=a
a=temp

print("First no =",a)
print("Second no =",b)

#Question 4
print("Question 4")
a=int(input("Enter first no "))
b=int(input("Enter second no "))
a,b = b,a
print("First no =",a)
print("Second no =",b)

#Question 5
print("Question 5")
temp_fahrenheit = float(input("Enter temperature in fahrenheit :"))
temp_celcius = (temp_fahrenheit - 32 ) * (5/9)
temp_kelvin = temp_celcius + 32+273.15

print('temp in degree celcius =' ,temp_celcius)
print('temp in degree fahrenheit = ' ,temp_kelvin)


#Question 6
print("Question 6")
str1 = "Anubhav"
print(type(str1))
int1=23
print(type(int1))
int3=23+43j
print(type(int3))
int2=23.23
print(type(int2))
list1=[1,2,3]
print(type(list1))
tuple1=(2,3,4)
print(type(tuple1))
bool1 = True
print(type(bool1))
set1 = {1,2,3}
print(type(set1))
dict1={1:2,3:4}
print(type (dict1))

#Question 7
print("Question 7")
print('''Step 1 : Sign Up in github.com 
Step 2 : Create a Github public repo and name it LetsUpgrade AI/ML
Step 3 : Upload the files/solution in the repo in day wise manner.
Step 4 : Copy the URL of the Folder of that day and paste in the Assignment Submission Form (Google Form)
Step 5 : Make sure you are filling correct details in the Assignment Submission Form.''')

