# a=10 #int
# b="suraj" #string
# c=2.12 #float
# d='a' #string
# e=a>c #bool
# f=['Suraj','Dhiraj','Gude'] #list
# g=('Suraj','Dhiraj','Gude') #tuple
# h={'Suraj','Dhiraj','Gude','Gude'} #set
# i={'Suraj':'Dhiraj','GG':'Gude', 'Gude':'Dhiraj'} #dict
# j=int(c)
# k=([[1,2,3,4,5],[6,7,8,9]],"Suraj","Gude") #tuple

# print(type(a),a)
# print(type(b),b,b[1:2])
# print(type(c),c)
# print(type(d),d)
# print(type(e),e)
# print(type(f),f)
# print(type(g),g)
# print(type(h),h)
# print(type(i),i)
# print(type(c),j)
# print(type(k),k)
# print(b.find('a'))
# print(g+k)
   
# list = [1,'2']
# print(list)
# tuple = tuple(list)
# print(tuple)

# a=5
# b=3
# print(a/b)
# print(a//b)

# a=[]
# b=[]
# c=[]
# for i in range(0,3):
#     a.append(int(input()))
#     b.append(int(input()))
#     c.append(a)
#     c.append(b)

# print(a, b, c)

n=int(input("Enter any positive number: "))   
num=n
sum=0
d=0
while n!=0:
    d=n/10
    sum=sum*10+d
    n=n//10

print(int(sum),num)
if num==sum:
    print("palindrome")

else:
    print("Not palindrome")    