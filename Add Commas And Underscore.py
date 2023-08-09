def add_commas_and_underscore(n):
    formatted_number = f"{n:,}"
    if len(formatted_number) > 3:

        parts = formatted_number.split(",")
        integer_part = parts[:-1]
        integer_part_joined = "".join(integer_part)
        integer_part_int = int(integer_part_joined)
        formatted_integer = f"{integer_part_int:,}"
        return f"{formatted_integer}_{parts[-1]}"
    else:
        return formatted_number

number = 123456789

print(add_commas_and_underscore(number))
