def convert(number):
    # function return raindrop sounds if the input was divisible by 3,5 or 7
    result = ""
    if number % 3 == 0 :
        result += "Pling"
    if number % 5 == 0 :
        result += "Plang"
    if number % 7 == 0 :
        result += "Plong"
    if result == "" : 
        return str(number)
    return result
