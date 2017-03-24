''' Exercise #1. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
print('Question 1:') 
a = 3 # Replace ??? with a positive number (int/float) of your choice.
b = 4 # Replace ??? with a positive number (int/float) of your choice.

# Write the rest of the code for question 1 below here.

c = (a**2-(b/2)**2)*2.0
print "the length of c is :",c
area = (a*c)/2
print "the area is: ",area
circ = a*4.0
print "the circumference is: ",circ 

#########################################
# Question 2 - do not delete this comment
#########################################
print('Question 2:') 
some_str = 'xz%xxabycw' # Replace ??? with string of your choice.

# Write the rest of the code for question 2 below here.
if len(some_str) >= 6:
    if some_str[5] == 'a':
        if some_str[6] == 'b':
            if some_str[-2] == 'c':
                print "yes"
else:
    print  "no"


#########################################
# Question 3 - do not delete this comment
#########################################
print('Question 3:') 
x = 3 # Replace ??? with a positive number (int/float) of your choice.
y = 4 # Replace ??? with a positive number (int/float) of your choice.
z = 3 # Replace ??? with a positive integer of your choice.

# Write the rest of the code for question 3 below here.
if ( x+y>z) and (x+z>y) and (y+z>x):
    s = (x+y+z)/2
    area = (s*(s-x)*(s-y)*(s-z))**0.5
    print "the triangles area is: ",area
    circ = x+y+z
    print "the triangls circumference is: ",circ
else:
    print (" these edges cannot form a triagle ")
    z = (x**2 + y**2)**0.5
    m = (x*y)/2
    print "the triangles area is: ",m
    n = (x+z+y) 
    print "the triangls circumference is: ",n
    

#########################################
# Question 4 - do not delete this comment
#########################################
print('Question 4:') 
a1 = 3 # Replace ??? with a positive number (int/float) of your choice.
a2 = 15 # Replace ??? with a positive number (int/float) of your choice.
n  = 4 # Replace ??? with an integer > 2 of your choice.

# Write the rest of the code for question 4 below here.
if (n%2==0) or (n%2==1):
    q = float (a2/a1) 
    an = a1*(q**(n-1)) 
    print (an)
    
#########################################
# Question 5 - do not delete this comment
#########################################
print('Question 5:') 
donor='AB' # Replace ??? with ('AB'/'A'/'B','O').
recipient = 'A'# Replace ??? with ('AB'/'A'/'B','O').

# Write the rest of the code for question 5 below here.
if(donor == donor.upper()) and (recipient == recipient.upper()):
    if(donor == recipient):
        print "yes"
    if(donor == 'AB'):
        print "yes"
    if(recipient == 'O'):
        print "yes"
else:
    print "no"

#########################################
# Question 6 - do not delete this comment
#########################################
print('Question 6:') 
str1 = 'abxGr7ba'  # Replace ??? with a string of your choice.
result = 'no'

# Write the rest of the code for question 6 below here.
if (len(str1) >= 4):
    if(len(str1)%2 == 0):
        if (str1[-1]==str1[0]) and (str1[-2]==str1[1]):
            position = len(str1)/2-1
            if (str1[position] == 'g') or (str1[position] == 'G'):
                   result = 'yesFirst'
    else:
        if(len(str1)%2 == 1):
            if (str1[-1]==str1[0]) and (str1[-2]==str1[1]):
                position = len(str1)/2
                if (str1[position] == 'g') or (str1[position] == 'G'):
                       result = 'yesSecond'
        
        

print(result)

#########################################
# Question 7 - do not delete this comment
#########################################
print('Question 7:') 
str2 ='abtjgke' # Replace ??? with a string of your choice.

# Write the rest of the code for question 7 below here.
if len(str2)>4:
    isDigit = str2[2].isdigit() # 4
    if isDigit:
        thirdCharacter = int(str2[2]) + 1  
        newString = str2[-1] + str(thirdCharacter) + str2[3:-1] + str2[0]
    else:
        newString = str2[-1] + str2[2:-1] + str2[0]
print(newString)
