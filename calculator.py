def add( first, second):
    return first + second #This will add the first number with the second number
   

def subtract( first, second):
    
    return first - second #This will subtract the first number with the second number
   
def multiply( first, second):
    
    return first * second #This will multiply the first number with the second number
    

def divide( first, second):

    if second == 0: #This will check to see is 0 was entered for the second number
        raise Exception("I'm sorry, I can't divide by zero") #If the second number is 0, then it will give the Exception
    else: 
        return first / second #If the number is not 0, it will calculate the division

