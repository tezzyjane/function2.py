def add_numbers(a,b):
     return a+b
print(add_numbers(10,5))
def subtraction(a,b):
 return  a-b  
print(subtraction(20,8))   
def multiply(a,b):
   return a*b
print(multiply(10,6))
def divide(a,b):           
   if b==0:
      return "division by zero not allowed"
   return a/b
print(divide(15,3))
def area_rect(length,width):
   return length*width
print(area_rect(20,4))
def area_circle(radius):
   pi=3.1142
   return pi*radius*radius
print(area_circle(6))
def simple_interest(principal,rate,time):
   return principal*rate*time*0.01
print(simple_interest(10000,5,2))
def average(a,b,c):
   return (a+b+c)/3
print(average(12,6,8))
def even_odd(number):
 if number % 2==0:
  return "even" 
 else:
      return "odd"
print(even_odd(6))
def power_number(base,exponent):
   return base**exponent
print(power_number(2,4))
def commission(sales,rate):
 if sales>=100000:
      print("Excellent sales")
      return sales*10/100
 elif sales>=50000 and sales<=99999:
       print("Good sales")
       return sales*7/100
 else:
       print("Needs improvement")
       return sales*5/100
 
print(commission(150000,10))
print(commission(75000,7))
print(commission(30000,5))



def salary(PAYE,NHIF,NSSF,NET_SALARY):
   if NET_SALARY >=80000:
         print("high income earner")
         return NET_SALARY-(PAYE+NHIF+NSSF)
   elif 40000>= NET_SALARY <=79999:
         print("middle income earner")
         return NET_SALARY-(PAYE+NHIF+NSSF) 
   else:
         print("low income earner")
         return NET_SALARY-(PAYE+NHIF+NSSF) 
print(salary(8000,1500,1000,80000))  
print(salary(3000,1500,1000,30000))
print(salary(2000,1500,1000,20000))

def grade(marks,Grade):
    if marks>=70:
        print("excellent")
        return "A"
    elif marks>=60:
        print("good")
        return "B"
    elif marks>=50:
        print("average")
        return "C"
    elif marks>=40:
        print("below average")
        return  "D"
    else:
        print("fail")
        return "F"
print(grade(72,"A"))
print(grade(62,"B"))
print(grade(50,"C"))
print(grade(45,"D"))
print(grade(30,"F"))    
    #electricity bill calculator
def electricity_bill(units,rate,bill):
        if bill>=10000:
         print("high usage")
        else:
         print("normal usage")
        if units==50:
            return units*rate
        elif units==100:
            return units*rate
        elif units>=150:
            return units*rate
        else:
            return units*rate
        
print(electricity_bill(65,20))
print(electricity_bill(120,25))
print(electricity_bill(200,30))

    #employee overtime pay
def overtime_pay(hours,payrule,remark):
        if hours>40:
            print("overtime applied")
            return hours*1.5*payrule
        else:
            print("no overtime")
            return hours*1.0*payrule
print(overtime_pay(45,200, "overtime applied"))
print(overtime_pay(35,200, "no overtime"))  
    #body mass index(BMI) calculator
def bmi_calculator(weight,height,bmi,category):
        bmi=weight/(height*height)
        if bmi<18.5:
            print("underweight")
            return weight/height
        elif bmi>=18.5 and bmi<=24.9:
            print("Normal")
            return weight/height
        elif bmi>=25 and bmi<=29.9:
            print("overweight")
            return weight/height
        else:
            print("obese")
        return bmi_calculator
print(bmi_calculator(30,3,"bmi","underweight"))
print(bmi_calculator(18.5,2,"bmi","Normal"))
print(bmi_calculator(27,2,"bmi","overweight"))
print(bmi_calculator(35,4,"bmi","obese"))

#examination pass eligibility
def results(subject,marks,average_mark,result):
        average_mark=marks/subject
        if average_mark>=50:
            print("pass")
            return marks/subject
        else:
            print("fail")
            return marks/subject
print(results(3,240))
print(results(3,120))        