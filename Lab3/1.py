n = int(input())

def is_valid_number(n):
    str_n = str(abs(n))
    
    for digit in str_n:
        if int(digit) % 2 != 0:
            return "Not valid"
            
    return "Valid"
print(is_valid_number(n))