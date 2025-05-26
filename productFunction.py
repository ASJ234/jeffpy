#A function for multiplying 2 values

def product_function(x, y):
    result = (x * y)
    print("Result: " , result)
    
    
product_function(4,5) 

#A function using return
def get_vals(a, b):
    return a - b, a + b, a * b

sub,add,mul=get_vals(20,10)
print("Subtract: " ,sub)
print("Add: ", add)
print("Multiply: " ,mul)  


#Function to divide 2 values using return
def div_vals(c, r):
    if(r==0):
       print("Error cannot divide by a zero.")
       
    else:
        return (c/r)
    
print(div_vals(20,10))
    
        
# square of the list
list1=[1,2,3,4,5]
squared=list(map(lambda x : x * x,list1))
print(squared)

#Error handling
try:
    resul=5/2

except ZeroDivisionError:
    print("Cannot divide by a zer..")
    
else:
    print("Division successful", "Result: ",resul)        
    
finally:
    print("Execution completed")    
       
   
   
#raise a custom exception for checking for a positive number 

# Define a custom exception
class NegativeNumberError(Exception):
    pass

# Function to check for a positive number
def check_positive(number):
    if number <= 0:
        raise NegativeNumberError("Error: Number must be positive.")
    print(f"{number} is a positive number.")

# Example usage
try:
    check_positive(33)
except NegativeNumberError as e:
    print(e)   