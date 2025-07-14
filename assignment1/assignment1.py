# Task#1
def hello():
    return "Hello!"

#hello()

#Task#2
def greet(name):
     return(f"Hello, "+ name + "!")

#greet

#Task#3
def calc(arg1, arg2, operation="multiply"): 
    try:
        if operation =='add':
            return arg1+arg2
        elif operation == "subtract":
            return arg1-arg2
        elif operation == "multiply":
            return arg1*arg2
        elif operation == "divide":
            return arg1/arg2
        elif operation == "modulo":
            return arg1%arg2
        elif operation == "int_divide":
            return arg1//arg2
        elif operation == "power":
            return arg1**arg2
        else:
            return "Unexpected operator!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't " + operation + " those values!"

#Task#4
def data_type_conversion(value, type):
    try:
        if type =='int':
            return int(value)
        elif type =='float':
            return float(value)
        elif type =='str':
            return str(value)
        else:
            return "Unexpected type conversion!"
    except ValueError:
        return f"You can't convert " + value + " into a " + type + "."
    
#Task#5
def grade(*args):
    try:
        sum_of_arg = sum(args)
        qn = len(args)
        average = sum_of_arg//qn
        if average >= 90:
            return "A"
        else:
            if average >= 80:
                return "B"
            elif average >=70:
                return "C"
            else:
                return "F"
    except TypeError:
        return "Invalid data was provided."
    
#Task#6
def repeat(string, count):
    try:
        result = ""
        for c in range(count):
            result +=  string
            c =c + 1
        return result
    except TypeError:
        return "Unexpected parameter"

#Task#7
def student_scores(*args, **kwargs):
    score = 0
    if args[0] == "best":
        for key, value in kwargs.items():
            if value > score:
                score = value
                name = key
        return name
    elif args[0] == "mean":
        for value in kwargs.values():
            score += value
        return score//len(kwargs.values())
    else:
        return "Not suppported positional parameter"

#Task#8
def titleize(string):
    list_little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    result =[]
    words = string.split()

    if not words:
        return "The string is empty"

    for i, word in enumerate(words):
        if i==0 or i==len(words) - 1:
            result.append(word.capitalize())
        elif word in list_little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
          
    final_result = " ".join(result)
    return final_result

#Task#9
def hangman(secret, guess):
    secret = secret.lower()
    guess = guess.lower()
    result =""
    if not secret:
        return "Secret word is empty string. Input secret word"

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result+= "_"
    return result

#Task#10
def pig_latin(string):
    vowels = 'aeiou'
    words = string.split()
    result = []

    if not string:
        return "Empty string"
    
    words = string.split()

    for word in words:
        if word[0] in vowels:
            latin_word = word + "ay"
        elif word.startswith("qu"):
            latin_word = word[2:] + "qu" + "ay"
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i] == 'q' and i + 1 < len(word) and word[i + 1] == 'u':
                    i += 2
                    break
                i += 1
            latin_word = word[i:] + word[:i] + "ay"
        
        result.append(latin_word)
    latin_string = ' '.join(result)

    return latin_string

