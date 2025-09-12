# LESSON 4 STARTER CODE: VARIABLES AND DATA TYPES

# ========================================
# PART 1: Creating Variables Practice
# ========================================
name = "Sasha"
age = 15
gpa = 3.77
grade = 10

print('Student name: '+ name)
# print('Student age:'+ age) does not work bcs can only concatenate str to str
print('Student age:',age) #comma is ok tho

# variables can change
age = 16
# can do multiple assignments
subject, period = 'CS100', 1
# ========================================
# PART 2: Data Types Practice
# ========================================
# 4 main (primitive) data types
name = "Sasha" #str
age = 15 #int
gpa = 3.77  #float (w/ decimal)
is_present = True #bool

# check data types by the type function
print(f"Name: {name} Type: {type(name)}")
print(f"Age: {age} Type: {type(age)}")
print(f"GPA: {gpa} Type: {type(gpa)}")
print(f"Present: {is_present} Type: {type(is_present)}")


# ========================================
# PART 3: Type Conversion Practice
# ========================================
# convert between types
grade_text = '95'
# grade_text2 = "'95'"
print(f'Original: {grade_text} {type(grade_text)}')
grade_number = int(grade_text)
print(f'As number: {grade_number} {type(grade_number)}')
gpa_number = float(gpa)
print(f'GPA: {gpa_number} {type(gpa_number)}')
gpa_text = str(gpa_number)
print(f'GPA: {gpa_text} {type(gpa_text)}')

#practice w bool() func
print(f'bool(0) - {bool(0)}') #False
print(f'bool(1) - {bool(1)}') #True
print(f'bool(10) - {bool(10)}') #True
print(f'bool("") - {bool("")}') #False
print(f'bool("hi") - {bool("hi")}') #True
print(f'bool(" ") - {bool(" ")}') #True
# ========================================
# PART 4: Variable Operations Practice  
# ========================================
#Swapping variables
color1 = 'red'
color2 = 'blue'
print(f'{color1}, {color2}')
color1, color2 = color2, color1
print(f'{color1}, {color2}')



