number = 123456789876123
"""
def add_commas_and_underscore(n):
    
   # foramatNum = "{:,}".format(n)
    foramatNum = f"{n:,}"
    if len(foramatNum)>3:
        lst = foramatNum.split(",")
        first = lst[:-1] 
        firstJoin = "".join(first)
        firstInt = int(firstJoin)
        firstFormat = f"{firstInt:,}"
        finalResult = f"{firstFormat}_{lst[-1]}"
        return finalResult
    else:
        return foramatNum
print(add_commas_and_underscore(number)) # 120
"""

"""
#اضافة جزء عشري ف النهاية
def add_commas_and_underscore(n):
    formatted_number = f"{n:,}"
    if len(formatted_number) > 3:

        parts = formatted_number.split(",")
        integer_part = parts[:-1]
        joined_integer = "".join(integer_part)
        joined_integer_to_int = int(joined_integer)
        formatted_integer = f"{joined_integer_to_int:,}"
        return f"{formatted_integer},{parts[-1]}"  # إضافة الجزء العشري مرة أخرى
    else:
        return formatted_number

#number = 100000012345  # يمكنك استبداله بالعدد الذي تريد

print(add_commas_and_underscore(number))
"""

def add_commas_as_underscores(n):
    formatted_number = f"{n:,}"
    return formatted_number.replace(",", "_")

number = 1000000  # يمكنك استبداله بالعدد الذي تريد

print(add_commas_as_underscores(number))
