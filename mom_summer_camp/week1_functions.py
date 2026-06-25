def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
#print(celsius_to_fahrenheit(100))

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9 
#print(fahrenheit_to_celsius(32))

def greet_student(name, subject="Mathematics", formal=False):
    if formal==False:
        return (f"Hi {name}, ready for {subject}?")
    elif formal==True:
        return (f"Good morning, {name}. Today we will be studying {subject}.")
#print(greet_student("Ada", "History", True))

def calculate_bmi(weight_kg, height_m):
    """calculate bmi
    Args:
        weight_kg(float):the weight
        height_m(float):height
    Returns:
        the bmi
    """
    return (weight_kg / (height_m*height_m))
#print(calculate_bmi(70, 1.75))
def bmi_category(bmi):
    """decide the bmi category
    Arg:
        bmi:bmi number
    returns:
        the bmi catagory
    """
    if bmi < 18.5:
        return ("underweight")
    elif bmi >= 18.5 and bmi<25:
        return ("normal")
    elif bmi >= 25 and bmi<30:
        return ("overweight")
    elif bmi>=30:
        return(obese)
#print(bmi_category(27.5))

def describe_triangle(a, b, c):
    """describe the triangle
    Arg:
        a:side
        b:side
        c:side
    Returns:
        what type of triangle it is
    """
    if a+b<=c or a+c<=b or c+b<=a:
        return("invalid")
    elif a==b==c:
        return("equilateral")
    elif a==b or b==c or a==c:
        return ("isosceles")
    else:
        return("scalene")
#print(describe_triangle(1, 2, 10))

def is_palindrome(text):
    """checks for palindromes
        Arg:
            text: what is typed into be checked
        Returns:
            whether it is a palindrome
    """
    cleaned = "".join(text.split()).lower()
    return cleaned == cleaned[::-1]
#print(is_palindrome('boat'))

