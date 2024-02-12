# a=int(input("Enter Vehicle number: "))

# if a % 5 == 0 and a % 3 == 0:
#      print("Vehicle moves on for free of cost")

# elif a % 5 == 0 or a % 3 == 0:
#      print("Pay half of the fee")

# else:
#     print("Pay the full amount")
        

# BEGIN
# DECLARE variables vechicle_number
#     READ vechicle_number
#     IF (vechicle_number%3==0 AND vechicle_number%5==0) THEN
#         PRINT "Vehicle moves on for free of cost"
#     ELSE IF (vechicle_number%3==0 OR vechicle_number%5==0) THEN   
#         PRINT "Pay half of the fee"
#     ELSE 
#         PRINT "Pay the full amount"  
# END                



# BEGIN
#     DECLARE basicCost, exciseDutyRate, salesTaxRate, roadTaxRate, exciseDuty, salesTax, roadTax, totalCost 

#     READ "Enter the basic cost of the Flying Spur car model: " basicCost

#     READ "Enter the excise duty rate in percentage: " exciseDutyRate
#     READ "Enter the sales tax rate in percentage: " salesTaxRate
#     READ "Enter the road tax rate in percentage: " roadTaxRate

#     SET exciseDuty = basicCost * exciseDutyRate / 100
#     SET salesTax = basicCost * salesTaxRate / 100
#     SET roadTax = basicCost * roadTaxRate / 100

#     SET totalCost = basicCost + exciseDuty + salesTax + roadTax

#     PRINT "Estimated Total Cost of Flying Spur Car Model:"
#     PRINT "Basic Cost: " + basicCost
#     PRINT "Excise Duty: " + exciseDuty
#     PRINT "Sales Tax: " + salesTax
#     PRINT "Road Tax: " + roadTax
#     PRINT "Total Cost: " + totalCost

# END

# BEGIN

# DECLARE score

#     IF score>80 AND score<=100 THEN
#         PRINT "grade 'O'"      
#     ELSE IF score>70 AND score<=80 THEN
#         PRINT "grade 'A'"      
#     ELSE IF score>50 AND score<=70 THEN
#         PRINT "grade 'B'"      
#     ELSE IF score>=40 AND score<=50 THEN
#         PRINT "grade 'C'" 
#     ELSE IF score>=0 AND score<40 THEN
#         PRINT "grade 'F'"    
#     ELSE
#         PRINT "Invalid Input"  

# END                                  


# Pseudocode for finding the oldest and youngest among Rocky, Sam, and Richie

# BEGIN

# DECLARE RockyAge, SamAge, RichieAge

# PRINT "Enter the age of Rocky, Sam, and Richie"

# READ RockyAge
# READ SamAge
# READ RichieAge


#     IF RockyAge > 0 AND RockyAge <= 150 AND SamAge > 0 AND SamAge <= 150 AND RichieAge > 0 AND RichieAge <= 150 THEN
    
#         IF RockyAge >= SamAge AND RockyAge >= RichieAge THEN
#             PRINT "Richie is the oldest"
#         ELSE IF SamAge >= RockyAge AND SamAge >= RichieAge THEN
#             PRINT "Sam is the oldest"
#         ELSE
#             PRINT "Rocky is the oldest"
#         END IF
        
#         IF RockyAge <= SamAge AND RockyAge <= RichieAge THEN
#             PRINT "Rocky is the youngest"
#         ELSE IF SamAge <= RockyAge AND SamAge <= RichieAge THEN
#             PRINT "Sam is the youngest"
#         ELSE
#             PRINT "Richie is the youngest"
#         END IF
#     ELSE
#         PRINT "Invalid age entered. Please enter ages within the valid range (1-150)"
#     END IF

# END



# Age>=20 and age<60 and income<= 2, 50,000 :    0% tax

# Age>=20 and age<60 and income>2,50,000  and income<=  5,00,000 :    10% tax

# Age>=20 and age<60  and income>5,00,000  and income<=  10,00,000 :    20% tax

# Age>=20 and age<60  and income    above 10, 00,000 :    30% tax

 

# Age >=60 and age<=80  , income<= 3, 00,000 :    0% tax

# Age >=60 and age<=80 ,  income > 3,00,000 and income <=5,00,000 :10% tax

# Age >=60 and age<=80 ,  income > 5,00,000 and income <=10,00,000 : 20% tax

# Age >=60 and age<=80 ,  income>10,00,000 : 30% tax

 

# Age >80  and age<=100, income<= 5, 00,000 :    0% tax

# Age >80  and age<=100,  income > 5,00,000 and income <=10,00,000 : 20% tax

# Age >80  and age<=100,  income >10,00,000 : 30% tax

# def calculate_income_tax(age, income):
#     if age < 20:
#         print("Age is less")
#     elif age > 100 or age < 0 or income <= 0:
#         print("Invalid input")
#     elif 20 <= age < 60:
#         if income <= 250000:
#             tax_percentage = 0
#         elif 250000 < income <= 500000:
#             tax_percentage = 0.10
#         elif 500000 < income <= 1000000:
#             tax_percentage = 0.20
#         else:
#             tax_percentage = 0.30
#     elif 60 <= age <= 80:
#         if income <= 300000:
#             tax_percentage = 0
#         elif 300000 < income <= 500000:
#             tax_percentage = 0.10
#         elif 500000 < income <= 1000000:
#             tax_percentage = 0.20
#         else:
#             tax_percentage = 0.30
#     elif 80 < age <= 100:
#         if income <= 500000:
#             tax_percentage = 0
#         elif 500000 < income <= 1000000:
#             tax_percentage = 0.20
#         else:
#             tax_percentage = 0.30
#     else:
#         print("Invalid input")

#     if "tax_percentage" in locals():
#         tax_amount = income * tax_percentage
#         print(f"Income Tax: {tax_amount}")

# # Example usage:
# age = int(input("Enter age: "))
# income = float(input("Enter income: "))
# calculate_income_tax(age, income)


# BEGIN

# DECLARE variables age, income
# READ age
# READ income

#     IF age < 20 THEN
#             PRINT "Age is less"
#         ELSEIF age > 100 OR age < 0 OR income <= 0 THEN
#             PRINT "Invalid input"
#         ELSE
#             IF age >= 20 AND age < 60 THEN
#                 IF income <= 250000 THEN
#                     tax = 0
#                 ELSEIF income <= 500000 THEN
#                     tax = 0.1 * (income - 250000)
#                 ELSEIF income <= 1000000 THEN
#                     tax = 0.2 * (income - 500000) + 25000
#                 ELSE
#                     tax = 0.3 * (income - 1000000) + 125000
#                 ENDIF
#             ELSEIF age >= 60 AND age <= 80 THEN
#                 IF income <= 300000 THEN
#                     tax = 0
#                 ELSEIF income <= 500000 THEN
#                     tax = 0.1 * (income - 300000)
#                 ELSEIF income <= 1000000 THEN
#                     tax = 0.2 * (income - 500000) + 20000
#                 ELSE
#                     tax = 0.3 * (income - 1000000) + 120000
#                 ENDIF
#             ELSEIF age > 80 AND age <= 100 THEN
#                 IF income <= 500000 THEN
#                     tax = 0
#                 ELSEIF income <= 1000000 THEN
#                     tax = 0.2 * (income - 500000)
#                 ELSE
#                     tax = 0.3 * (income - 1000000) + 100000
#                 ENDIF
#             ENDIF
#             PRINT "Income Tax:", tax
#     ENDIF

# END

 
# def find_closest_floor(target_floor, stop_floors):
#     if target_floor < 0:
#         return "Invalid Floor number"

#     closest_floor = None
#     min_distance = float('inf')

#     for stop_floor in stop_floors:
#         distance = abs(target_floor - stop_floor)
        
#         if distance < min_distance or (distance == min_distance and target_floor < closest_floor):
#             min_distance = distance
#             closest_floor = stop_floor

#     return f"You may get down at floor number {closest_floor}"

# # Get inputs from Annie
# target_floor = int(input("Get floor number you want to get down: "))
# stop_floors = []
# for _ in range(3):
#     stop_floor = int(input("Enter the floors in which the lift will stop: "))
#     stop_floors.append(stop_floor)

# # Find the closest floor
# result = find_closest_floor(target_floor, stop_floors)

# # Display the result
# print(result)

# BEGIN
# DECLARE variables n,n1,n2,n3, distance_to_n1, distance_to_n2, distance_to_n3

# PRINT "Get floor number you want to get down:"
#     READ n

# PRINT "Enter the floors in which the lift will stop:"
#     READ n1
#     READ n2
#     READ n3

#     IF n < 0 or n1 < 0 or n2 < 0 or n3 < 0 THEN
#         PRINT "Invalid Floor number"
#     ELSE
#         SET distance_to_n1 <- abs(n - n1)
#         SET distance_to_n2 <- abs(n - n2)
#         SET distance_to_n3 <- abs(n - n3)

#         IF distance_to_n1 <= distance_to_n2 and distance_to_n1 <= distance_to_n3 THEN
#             PRINT "You may get down at floor number", n1
#         ELSE IF distance_to_n2 <= distance_to_n1 and distance_to_n2 <= distance_to_n3 THEN
#             PRINT "You may get down at floor number", n2
#         ELSE
#             PRINT "You may get down at floor number", n3
#     ENDIF
# END    

# n=int(input("Enter posivitve number: "))
# fact=1

# for i in range(1, n+1):
# 	fact=fact*i

# print(fact)

# if n==0 or n==1:
#    print(1)
# else:
#     while(n>0):
#         fact=fact*n
#         n=n-1
#     print(fact)        


# count=0
# sum=0

# while sum<=100:
# 	number=int(input("Number: "))
# 	sum=sum+number
# 	count=count+1
# print("The number of turns is ",count)

# customer_id = input("Please enter your Customer Id\n")

# pc=0
# while True:
# 	n=float(input("Enter Page: "))
# 	if n>0:
# 		pc+=1
# 	else:
# 		print(pc)	

# number=int(input("Enter number: "))

# s=str(number)

# c0=0
# c1=0
# c2=0
# c3=0
# c4=0
# c5=0
# c6=0
# c7=0
# c8=0
# c9=0

# for digit_char in s:
# 	# digit = int(digit_char)
# 	if digit_char=="0":
# 		c0+=1
		
# 	elif digit_char=="1":
# 		c1+=1
		
# 	elif digit_char=="2":
# 		c2+=1

# 	elif digit_char=="3":
# 		c3+=1
		
# 	elif digit_char=="4":
# 		c4+=1	

# 	elif digit_char=="5":
# 		c5+=1
		
# 	elif digit_char=="6":
# 		c6+=1	

# 	elif digit_char=="7":
# 		c7+=1
		
# 	elif digit_char=="7":
# 		c7+=1	

# 	elif digit_char=="8":
# 		c8+=1
		
# 	elif digit_char=="9":
# 		c9+=1	

# 	else:
# 		print("Invalid Input")	
						
# print("Frequency of 0 is: ",c0)
# print("Frequency of 1 is: ",c1)
# print("Frequency of 2 is: ",c2)
# print("Frequency of 3 is: ",c3)
# print("Frequency of 4 is: ",c4)
# print("Frequency of 5 is: ",c5)
# print("Frequency of 6 is: ",c6)
# print("Frequency of 7 is: ",c7)
# print("Frequency of 8 is: ",c8)
# print("Frequency of 9 is: ",c9)






# def count_digit_frequency(number):
#     # Initialize a list to store digit frequencies (index represents the digit)
#     digit_frequency = [0] * 10

#     # Convert the number to a string to iterate over each digit
#     number_str = str(number)

#     # Iterate over each digit in the number
#     for digit_char in number_str:
#         digit = int(digit_char)
#         # Increment the count for the current digit in the list
#         digit_frequency[digit] += 1

#     return digit_frequency

# # Example usage
# user_number = int(input("Enter the number: "))
# result = count_digit_frequency(user_number)

# # Display the frequency of each digit
# print(f"\nFrequency of each digit in {user_number} is:\n")
# for digit, frequency in enumerate(result):
#     print(f"Frequency of {digit} = {frequency}")


# n1=int(input("Enter start: "))	
# n2=int(input("Enter End: "))
# for i in range(n1,n2+1):
# 	a=int(i%10)
# 	b=int(i/10%10)
# 	c=int(i/100%10)
# 	if (a+c)==b:
# 		print(i)

# BEGIN
# DECLARE variables a, b
# READ a
# READ b

# FOR n is between(a and b)
# 	SET a = n%10
# 	SET b = n/10%10
# 	SET c = n/100%10

# 	IF (a+c)==b THEN
# 		PRINT n
# END FOR		
# END

# Armstrong number 

# n=int(input('Enter 3 digit number: '))
# n2=n
# sum_of_cube=0
# while n>0:
# 	d=int(n%10)
# 	sum_of_cube=sum_of_cube+(d*d*d)
# 	n=n/10

# if n2==sum_of_cube:
# 	print(n2, "is an Armstrong number")
# else:
# 	print(n2, "is not an Armstrong number")

# BEGIN
# DECLARE variables n1, n2, digit, cubesSum=0
# PRINT "Enter the number"
# READ n1
# SET n2=n1

# WHILE n1>0 THEN do
# 	SET digit=n1%10
# 	cubesSum=cubesSum+(digit*digit*digit)
# 	SET n1=n1/10
# END WHILE

# IF n2==cubesSum THEN
# 	PRINT n2, "is an Armstrong number"
# ELSE
# 	PRINT n2, "is not an Armstrong number"
# END


# n = 100
# num1 = 0
# num2 = 1
# next_number = num2 
# count = 1
# print(num1,num2, end=" ")
# while count <= n:
# 	print(next_number, end=" ")
# 	count += 1
# 	num1 = num2 
# 	num2 = next_number
# 	next_number = num1 + num2
# print()

# BEGIN
# DECLARE variables n=100,count=1,num1=0,num2=1,next_number=num2
# WHILE count<=n THEN DO
# 	PRINT next_number, " "
# 	SET num1 = num2
# 	SET num2 = next_number
# 	SET next_number = num1 + num2
# END WHILE
# END	

# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)


# BEGIN
# DECLARE variables num, i, is_prime
#     FOR num=2 to 100 DO
#         SET is_prime=1
#             FOR i=2 to num/2 DO
#                 IF num%i==0 THEN
#                     SET is_prime=0
#                     BREAK
#             IF is_prime==1 THEN 
#                 PRINT num  
#             END FOR
#     END FOR
# END                                 

# while True:
#     n=int(input("Please, enter the number between 0 and 20: "))
#     if n>=0 and n<=20:
#         print(n+17)
#         break

# BEGIN
# DECLARE variables n
#     WHILE True DO
#         PRINT "Please, enter the number between 0 and 20: "
#         READ n  
#         IF n>=0 AND n<20 THEN
#             PRINT n+17
#             BREAK
#     END WHILE
# END                
        

# number = int(input("Enter a number: "))
# # Store the original number in a temporary variable
# temp = number
# reversed_number = 0

#     # Reverse the digits of the number
# while number > 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number = number // 10

# # Check if the reversed number is equal to the original number
# if temp == reversed_number:
#     print(f"{temp} is a palindrome")
# else:
#     print(f"{temp} is not a palindrome")
    
  
# BEGIN

# DECLARE variables n, reverse=0, reminder, temp
# PRINT "Enter any number to check for palindrome: "
# READ n
# SET temp = n
#     WHILE n>0 THEN DO
#         reminder = n % 10
#         reverse = reverse * 10 +  reminder
#         n = n / 10
#     END WHILE
# IF reverse==temp THEN
#     PRINT "{temp}, is a palindrome number"   
# ELSE 
#     PRINT "{temp}, is not a palindrome number" 

# END               

# sum=0
# while True:
#     n=int(input("Enter number: "))
#     if n>0:
#         sum=sum+n
#     elif n<0:
#         continue
#     if n==0:
#         break

# print(sum)    

# BEGIN

# DECLARE variables sum=0
#     WHILE True DO
#         DEACLARE variables n
#         READ n
#         IF n>0 THEN
#         sum=sum+n
#         ELSE IF n<0 THEN
#         CONTINUE
#         ELSE IF n==0 THEN
#         BREAK
#     END WHILE 

# PRINT sum  

# END

# n=int(input("Enter number: "))
# temp=n
# evenSum=0
# oddSum=0
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         evenSum+=digit
#     else:
#         oddSum+=digit
#     n=n//10    

# if evenSum==oddSum:
#     print(temp, "is Lucky number")
# else:    
#     print(temp, "is unLucky number")

# BEGIN

# DECLARE variables number evenSum=0, oddSum=0, digit
# PRINT "Enter the number"
# READ number
#     WHILE number>0 THEN DO
#         digit = number % 10
#         IF digit % 2 == 0 THEN
#             evenSum += digit
#         ELSE    
#             oddSum += digit
#         number = number/10
#     END WHILE
# IF evenSum == oddSum THEN
#     PRINT "Number is Lucky"  
# ELSE
#     PRINT "Number is not Lucky" 

# END


# n=int(input("Enter the bill amount"))

# if n==0:
#     print("Invalid Amount")
# elif n<0:
#     print("Cannot Generate Bill")
# elif n>=5000:
#     print("You get a discount of 10%. Pay",int(n-n*0.1))   
# elif n<5000 and n>2500:
#     print("You get a discount of 8%. Pay",int(n-n*0.08)) 
# elif n<=2500:
#     print("You get a discount of 5%. Pay",int(n-n*0.08)) 

# BEGIN

# DECLARE variables billAmount
# PRINT "Enter the bill amount"
# READ billAmount

#     IF billAmount==0 THEN
#         PRINT "Invalid Amount"
#     ELSE IF billAmount<0 THEN
#         PRINT "Cannot Generate Bill" 
#     ELSE IF billAmount>=5000 THEN
#         PRINT "You get a discount of 10%. Pay",{n-n*0.1}   
#     ELSE IF billAmount<5000 AND billAmount>2500 THEN
#         PRINT "You get a discount of 8%. Pay",{n-n*0.08} 
#     ELSE IF billAmount<=2500 AND THEN
#         PRINT "You get a discount of 5%. Pay",{n-n*0.05} 

# END

# a=30
# while a>0:
#     a=a-4
# print(a)

# i=1
# while i<=15:
#     print(i)
#     i=i+3


# # creating an empty list
# lst = []

# number of elements as input
# n = int(input("Enter number of elements : "))

# # iterating till the range
# for i in range(0, n):
# 	ele = int(input())
# 	# adding the element
# 	lst.append(ele) 

# print(lst)

# lst = []






# BEGIN

# DECLARE variables mobileNumber[10]

# PRINT "Enter the digits of the mobile number :"
# FOR index in 0 TO 9 DO
#     READ mobileNumber[index]

#     WHILE (mobileNumber[index]<0 OR mobileNumber[index]>9) DO
#         PRINT "Enter the digits of the mobile number :"
#         READ mobileNumber[index]
#     END WHILE 
# END FOR 

# PRINT "The number you entered is "    
# FOR index in 0 TO 9 DO
#     PRINT mobileNumber[index] 
# END FOR 

# END



# Not working ids************************************************************************
# id1Status=0
# id2Status=0
# n1=int(input("Enter the size of first array\n"))
# n2=int(input("Enter the size of second array\n"))

# if n1<=0 and n2<=0:
#     print("Invalid array size")
    

# print("Enter the values")
# id1 = []
# for i in range(0,n1):
#     ele = int(input())
#     id1.append(ele) 
#     if ele<=0:
#         id1Status=1
#         break 

# id2 = []
# if id1Status==0:
#     print("Enter the values")
#     for i in range(0,n2):
#         ele = int(input())
#         id2.append(ele) 
#         if ele<=0:
#             id2Status=1
#             break 
# print("Not working ids")            
# if id1Status==0 and id2Status==0:
#     for i in range(0,n1):
#         count=0
#         for j in range(0,n2):
#             if id1[i]==id2[j]:
#                 count+=1
#                 break 
#         if count==0:
#             print(id1[i])             


# BEGIN
# DECLARE variables n1,n2,id1[20],id2[20],id1status,id2status
#     SET id1status = 0,id2status = 0

# PRINT "Enter the size of first array"
# READ n1
# PRINT "Enter the size of second array"
# READ n2
# IF n1<=0 AND n2<=0
#     PRINT  "Invalid array size"
# ELSE
#     FOR i in 0 to n1-1 DO
#         READ id1[i];
#         IF id1[i] <= 0 THEN
#             id1status=1
#             BREAK
#         ENDIF
#     ENDFOR
        
# IF id1status ==0 THEN
#     FOR i in 0 to n2-1 DO
#         READ id2[i]  
#         IF id2[i] <= 0 THEN
#             id2status=1
#             BREAK
#         ENDIF
#     ENDFOR
# END IF 

# PRINT "Not Working IDs"
# IF id1status==0 AND id2status==0 THEN
#     FOR i in 0 to n1-1                                           
#         SET count=0                                               
#             FOR j in 0 to n2-1                                          
#                 IF id1[i]==id2[j] THEN                           
#                     count = count+1;
#                     BREAK;                                        
#                 END IF
#             END FOR                                                      
#             IF count==0 THEN                                    
#                 PRINT id1[i]
#             END IF
#     END FOR                                                      
# ENDIF 

# END  

# score=[]
# n=int(input())
# sum=0
# for i in range (0,n):
#     ele=int(input())
#     score.append(ele)

#     sum+=ele

# avg=sum/n
# print(sum, avg)  

# if avg >=80:
#     print("Real project")
# else:
#     print("more projects")    

# BEGIN 

# DEACLARE variables numberOfProjects, projectScore[], sumProjectScore=0, avg
# PRINT "Enter the number of projects"
# READ numberOfProjects
# IF numberOfProjects<=10 THEN
#     PRINT "Enter the project score"
#     FOR i in 0 to numberOfProjects-1 DO
#         READ projectScore[i]
#         SET sumProjectScore+=projectScore[i]
#     END FOR  
# END IF     
# SET avg=sumProjectScore/numberOfProjects
# IF avg>80 THEN
#     PRINT "Allocate a real project"  
# ELSE
#     PRINT "Assign more assignments"   

# END

# marks=[]
# n=int(input("Enter the number of Students \n"))
# max=0
# if n<=50:
#     print("Enter the marks")
#     for i in range(0,n):
#         ele=int(input())
#         if ele>max:
#             max=ele
#     print("max marks are", max)  

# BEGIN 

# DECLARE variables numberOfStudents, marks[], maxMarks=0
# PRINT "Enter the number of students"
# READ numberOfStudents

# IF numberOfStudents<=50 THEN
#     FOR index in 0 to numberOfStudents-1 DO
#         READ marks[index]
#         IF marks[index]>max THEN
#             SET max=marks[index]
#         END IF    
#     END FOR 
# PRINT "Maximum mark is ",{max} 
# END IF   
# END



# matrix addition******************************************************************
# Declare 2D arrays a, b, and c of size 2x2
# a = [[1, 0], [0, 1]]
# b = [[0, 0], [0, 0]]
# c = [[0, 0], [0, 0]]

# # Get input for array b
# print("Enter the matrix values:")
# for i in range(2):
#     for j in range(2):
#         b[i][j] = int(input())

# # Find the sum of a and b and store in array c
# for i in range(2):
#     for j in range(2):
#         c[i][j] = a[i][j] + b[i][j]

# # Print the result in array c
# print("\nSample Output:")
# for i in range(2):
#     for j in range(2):
#         print(c[i][j], end="   ")
#     print()

# # Terminate the program
# print("Matrix b is:")
# for i in range(2):
#     for j in range(2):
#         print(b[i][j], end="   ")
#     print()        


# Addtion of two matrix**********************************************************************************
# a=[]
# b=[]
# c=[]

# m=int(input("Enter rows: "))
# n=int(input("Enter columns: "))

# for i in range(m):
#     a1=[]
#     for j in range(n):
#         ele=int(input())
#         a1.append(ele)
#     a.append(a1) 

# print("Values of matrix a are: ")    
# for i in range(m):
#     for j in range(n): 
#         print(a[i][j], end=" ")
#     print()                   

# print("Enter values for matrix b: ")
# for i in range(m):
#     b1=[]
#     for j in range(n):
#         ele=int(input())
#         b1.append(ele)
#     b.append(b1) 

# print("Values of matrix b are: ")    
# for i in range(m):
#     for j in range(n): 
#         print(b[i][j], end=" ")
#     print() 

# print("Sum of matrix a and b is: ") 
# for i in range(m):
#     c1=[]
#     for j in range(n): 
#         ele=a[i][j]+b[i][j]
#         c1.append(ele)
#     c.append(c1)        

# for i in range(m):
#     for j in range(n): 
#         print(c[i][j], end=" ")
#     print() 






# Matrix input////////////////////////////////////////////////////////////////////////////
# m=int(input("Enter number of rows: "))
# n=int(input("Enter number of columns: "))
# a=[]

# for i in range(m):
#     b=[]
#     for j in range(n):
#         b.append(int(input()))
#     a.append(b)

# for i in range(m):
#     for j in range(n):
#         print(a[i][j], end=" ") 
#     print() 

# print(a)   

# BEGIN

# DECLARE variables  a[2][2], b[2][2], c[2][2]
# SET a={{1,0},{0,1}}
# PRINT "Enter the matrix values"
# FOR i IN 0 to 1 DO
#     FOR j in 0 to 1 DO
#         READ b[i][j]
#     END FOR
# END FOR

# PRINT "Addition of 2X2 matrix {b} with identity matrix {a}: "
# FOR i IN 0 to 1 DO
#     FOR j IN 0 to 1 DO
#         c[i][j] = a[i][j] + b[i][j]           
#         PRINT c[i][j], " " 
#     END FOR    
#     PRINT                          
# END FOR

# END




# Hello Pihu,
# I know since yesterday you are not feeling well, looking little bit tensed and worried.
# The reasons you shared with me are completely acceptable and I can understand your current situation.
# But pihu dont worry, everything will be happen better only. Trust me.
# Poulo you are come form west bengal to complete your dreams and make yoyr parents proud.
# This shows that how much your are serious about your career. You are trongest girl I have ever seen.
# I always learnt new things from you and you also behave with me or others so friendly.
# Other than yesterday's concerns please share if you have any issues, please. I will definitely help you.



# Addition of two arrays **********************************************
# a=[]
# b=[]
# c=[]

# print("Enter values for a: ")
# for i in range(10):
#     e=int(input())
#     a.append(e)

# print("Enter values for b: ")
# for i in range(10):
#     e=int(input())
#     b.append(e)

# for i in range(10):
#     ele=a[i]+b[i]
#     c.append(ele)
#     print(ele, end=" ")    

# BEGIN

# DECLARE variables firstArray[10], secondArray[10], addResult[10]

# PRINT "Enter the values for first array"
# FOR i IN 0 to 9 DO
#     READ firstArray[i]
# END FOR    

# PRINT "Enter the values for seconnd array"
# FOR i IN 0 to 9 DO
#     READ secondArray[i]
# END FOR     

# PRINT "Addition of two arrays"
# FOR i IN 0 to 9 DO
#     addResult[i]=firstArray[i]+secondArray[i]
#     PRINT addResult[i]
# END FOR   

# END


# a=[]
# r=[]
# n=int(input("Enter the number of products\n"))
# if n<=10:
#     print("Enter the price for ",n," products by 3 sellers")
#     for i in range(n):
#         b=[]
#         min=0
#         for j in range(3):
#             e=int(input())
#             b.append(e)
#         a.append(b)
               
        
# for i in range(n):
#     min=0
#     for j in range(3):
#         print(a[i][j], end=" ") 
#         if a[i][j]<min:
#             min=a[i][j]
#     r.append(min)            
#     print() 

# print(r)    


# a = []
# r = []
# n = int(input("Enter the number of products\n"))

# if n <= 10:
#     print("Enter the price for", n, "products by 3 sellers")
#     for i in range(n):
#         b = []
#         for j in range(3):
#             e = int(input())
#             b.append(e)
#         a.append(b)

# for i in range(n):
#     min_price = float('inf')  # Initialize min_price to positive infinity
#     for j in range(3):
#         print(a[i][j], end=" ")
#         if a[i][j] < min_price:
#             min_price = a[i][j]
#     r.append(min_price)
#     print()

# print(r)

# sum=0
# for i in range(n):
#     sum+=r[i]

# print()
# print(sum)

# BEGIN

# DECLARE variables n, productPrice[][], minPrice, sum

# PRINT "Enter the number of products"
# READ n
# SET sum=0

# IF n<=10 THEN 
#     FOR i IN 0 to n-1 DO 
#         FOR j IN 0 to 2 DO
#             READ productPrice[i][j]
#             PRINT

# FOR i IN 0 to n-1 DO 
#     SET minPrice=Positive infinity
#     FOR j IN 0 to 2 DO
#         IF productPrice[i][j]<minPrice THEN
#             minPrice=productPrice[i][j] 
#     sum+=min 

# PRINT sum

# END     

# n=int(input("Enter the number of players: "))
# a=[]
# b=[]

# print("Enter the score of Group A")
# for i in range(n):
#     a.append(int(input()))

# print("Enter the score of Group B")
# for i in range(n):
#     b.append(int(input()))

# count=0
# for i in range(n):
#     if a[i]>b[i]:
#         continue
#     else:
#         count+=1

# if count==0:
#     print("Teams are compatible")
# else:
#     print("Teams are not compatible")


# BEGIN

# DECLARE variables numberOfPlayers, count, scoreOfGroupA[], scoreOfGroupB[]
# PRINT "Enter the number of players"
# READ numberOfPlayers
# SET count=0

# PRINT "Enter the score of Group A"
# FOR i IN 0 to numberOfPlayers-1 DO
#     READ scoreOfGroupA[i]

# PRINT "Enter the score of Group B"
# FOR i IN 0 to numberOfPlayers-1 DO
#     READ scoreOfGroupB[i]

# FOR i IN 0 to numberOfPlayers-1 DO
#     IF scoreOfGroupA[i] > scoreOfGroupB THEN
#         CONTINUE
#     ELSE
#         count+=1

# IF count==0 THEN
#     PRINT "Teams are compatible"
# ELSE
#     PRINT "Teams are not compatible"


# n=int(input("size: "))
# arr=[]
# if n<=10:
#     for i in range(n):
#         arr.append(int(input()))

#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 # Swap elements
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp

# print(arr)
# for i in range(n-1):
#     print(arr[i],end=" ")

# BEGIN
# DECLARE variable arr[10], n
# PRINT "Enter value for n"
# READ n

# PRINT "Enter time taken"
# FOR i in 0 to n-1 DO
#     READ arr[i]
# END FOR

# FOR i IN 0 to n-1 DO
#     FOR j IN 0 to n-1-i DO
#             IF arr[j]>arr[j+1] THEN ------------>swap
#                 temp=arr[i]
#                 arr[i]=arr[j+1]
#                 arr[j+1]=temp
#             END IF
#     END FOR
# END FOR

# FOR i in 0 to 2 DO
#     PRINT arr[i]
# END FOR

# END

# a=[]
# b=[]
# c=[]
# print("friend 1: ")
# for i in range(3):
#     e=int(input())
#     a.append(e)
# print("friend 2: ")    
# for i in range(3):
#     b.append(int(input())) 
# print("Enter prices: ")    
# for i in range(3):
#     c.append(int(input()))

# sum1=0
# sum2=0

# for i in range(3):
#     sum1=sum1+a[i]*c[i]


# for i in range(3):
#     sum2=sum2+b[i]*c[i]

# print(sum1, " ", sum2)    
        
# a=[]
# b=[]
# c=[]
# print("Enter the no of kgs of apples, oranges and grapes bought by you")
# for i in range(3):
#     a.append(int(input()))
#     if a[i] < 0:
#         print("Invalid Input")
#         break
# print("Enter the no of kgs of apples, oranges and grapes bought by your friend")        
# for i in range(3):
#     b.append(int(input()))
#     if b[i] < 0:
#         print("Invalid Input")
#         break  
# print("Enter the price of apple, orange and grapes per kg")        
# for i in range(3):
#     c.append(int(input()))
#     if c[i] < 0:
#         print("Invalid Input")
#         break 

# sum1=0
# sum2=0
# for i in range(3):
#     sum1+=a[i]*c[i]
# for i in range(3):
#     sum2+=b[i]*c[i]  

# print("You need to pay Rs.",sum1, "and", "your friend needs to pay Rs.", sum2, ".")

# a=[]
# b=[]
# c=[]

# print("Values for you: ")
# for i in range(3):
#     a.append(int(input()))

# print("Values for your friend: ")
# for i in range(3):
#     b.append(int(input()))

# print("Prices: ")
# for i in range(3):
#     c.append(int(input()))

# sum1=0
# sum2=0
# for i in range(3):
#     if (a[i] or b[i] or c[i])<0:
#         print("Invalid input")
#         break
#     else:
#         sum1=sum1+a[i]*c[i]
#         sum2=sum2+b[i]*c[i]

# print("You need to pay Rs.",sum1,"and your friend needs to pay Rs.",sum2,".")


# BEGIN

# DECLARE variables arr1[3], arr2[3], price[3], amount1=0, amount2=0

# PRINT "Enter the no of kgs of apples, oranges and grapes bought by you 4"
# FOR i IN 0 to 2 DO
#     READ arr1[i]

# PRINT "Enter the no of kgs of apple, orange and grapes bought by your friend 3"
# FOR i IN 0 to 2 DO
#     READ arr2[i]

# PRINT "Enter the price of apple, orange and grapes per kg"
# FOR i IN 0 to 2 DO
#     READ price[i]

# FOR i IN 0 to 2 DO
#     IF (arr1[i] OR arr2[i] OR price[i])<0 THEN
#         BREAK    
#     ELSE 
#         amoun1+=arr1[i]*price[i]
#         amoun1+=arr2[i]*price[i]

# PRINT "You need to pay Rs.{amount1} and your friend needs to pay Rs.{amount2}."

# END




# a=int(input())
# b=int(input())
# c=int(input())

# d=int(input())
# e=int(input())
# f=int(input())

# g=int(input())
# h=int(input())
# i=int(input())

# j=int(input())
# k=int(input())
# l=int(input())

# m=int(input())
# n=int(input())
# o=int(input())


# if a or b or c or d or e or f or g or h or i or j or k or l or m or n or o<0:
#     print("Invalid Input")
# else:
#     if (a<b and a<c):
#         print("Buy mobile from Flipkart")   
#     elif (b<c):     
#         print("Buy mobile from Amazon")  
#     else:
#         print("Buy mobile from Snapdeal")

#     if (d<e and d<f):
#         print("Buy laptop from Flipkart")   
#     elif (e<f):     
#         print("Buy laptop from Amazon")  
#     else:
#         print("Buy laptop from Snapdeal") 

#     if (g<h and g<i):
#         print("Buy speakers from Flipkart")   
#     elif (h<i):     
#         print("Buy speakers from Amazon")  
#     else:
#         print("Buy speakers from Snapdeal") 

#     if (j<k and j<l):
#         print("Buy power bank from Flipkart")   
#     elif (k<l):     
#         print("Buy power bank from Amazon")  
#     else:
#         print("Buy power bank from Snapdeal") 

#     if (m<n and m<o):
#         print("Buy usb from Flipkart")   
#     elif (n<o):     
#         print("Buy usb from Amazon")  
#     else:
#         print("Buy usb from Snapdeal")

# a=[1,2,3,4,5,6]


# print(a[4])
# print(a[3+1])


# n=int(input())
# a=[]
# b=[]
# for i in range(n):
#     a.append(int(input()))
# for i in range(n):
#     b.append(int(input()))

# count=0
# for i in range(n):
#     for j in range(n-1,-1):
#         if a[i]==b[j]:
#             count+=1
#         else:
#             break

# print(count)            
# if(count==n):
#     print("in reverse")  
# else:
#      print("Not in reverse")                  
                               

# BEGIN

# DECLARE variables n, a[50], b[50], k, flag

# PRINT "Enter the value of n"
#     READ n

# PRINT "Numbers said by Pinky"
#     FOR i IN 0 to n-1 DO
#         READ a[i]
#     END FOR

# PRINT "Numbers said by Mary"    
#     FOR i IN 0 to n-1 DO
#         READ b[i]
#     END FOR  

# SET k=n-1, flag=0                 
         
# FOR j IN 0 to n-1 DO              
#     IF a[j]==b[k] THEN       
#         k=k-1                
#     ELSE                          
#         flag=1
#         BREAK
#     END IF   
# END FOR   

# IF flag==0 THEN
#     PRINT "Yes, it is in reverse order"
# ELSE
#     PRINT "No, it is not in reverse order"
# END IF

# END
    
                  










# BEGIN 
# DECLARE prices[15]

#     FOR I IN 0 to 14 THEN
#         READ prices[i]



# BEGIN
#     DECLARE products = ["mobile", "laptop", "speakers", "power bank", "USB"]
#     DECLARE sellers = ["Flipkart", "Amazon", "Snapdeal"]
    
#     FOR EACH product IN products
#         DECLARE min_price = INFINITY
#         DECLARE min_seller = ""
        
#         FOR EACH seller IN sellers
#             PRINT "Enter the price of " + product + " from " + seller + ":"
#             SET price = INPUT()
            
#             IF price < 0
#                 PRINT "Invalid Input"
#                 END
            
#             IF price < min_price
#                 SET min_price = price
#                 SET min_seller = seller
#             END IF
#         END FOR
        
#         PRINT "Buy " + product + " from " + min_seller
#     END FOR
# END

                
                    





