'''Basic programs in Python'''

#buble sort
def bs(a):             # a = name of list
    b=len(a)-1         # minus 1 because we always compare 2 adjacent values
                             
    for x in range(b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
    return a
a=[32,5,3,6,7,54,87]
bs(a)

#star triangle
def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))    
pyfunc(9)

#Fibbonaci sequence
n = int(input("How many terms? "))
n1, n2 = 0, 1   # first two terms
count = 0
if n <= 0:     # check if the number of terms is valid
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto {} : {}".format(n, n1))
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2    # update values
       n1 = n2
       n2 = nth
       count += 1

#check if a number is prime or not
a=int(input("Enter number "))     
if a>1:
    for x in range(2,a):
        if(a%x)==0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")

#verify if a word is palindrome
a=input("Enter string ")
b=a[::-1]
if a==b:
    print("Is palindrome")
else:
    print("Is not a palindrome")


#a sorting algorithm for a numerical data set
list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)

#count the number of lower letters in a file
with open(file.txt) as f:
    count = 0
    text = f.read()
    for character in text:
        if character.islower():
            count += 1

#a view in Django
from django.http import HttpResponse
import datetime
 
def Current_datetime(request):
     now = datetime.datetime.now()
     html = "<html><body>It is now %s</body></html> % now
     return HttpResponse(html)
    
#save an image locally using python whose URL address I already know
import urllib.request
urllib.request.urlretrieve("URL", "local-filename.jpg")
