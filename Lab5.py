
def hollow_square(n):

   x = "*"
   y = " "
   z = (n - 2) * y
   count = 3
   def new():
    return f"{x}{z}{x}\n"

   newer = new() * (n - 2)

   if n == 2:
    return f"{x * n}\n{x * n}"

   elif n > 1:
    while count <= n:
        count += 1
    return f"{x * n}\n{newer}{x * n}"

   else:
        return x * n

   return hollow_square(n)

   
# # print(hollow_square(5))
# # print(hollow_square(2))
# # print(hollow_square(1))


def number_pattern(n):
    result = ""
    for i in range(n):
        for j in range(i + 1):
            result += str(j + 1)
        result += "\n"
    return result.strip()

# print(number_pattern(4))
# print(number_pattern(1))
# print(number_pattern(3))


def sum_of_natural_numbers(n):
    result = 0
    count = 1

    for i in range(n):
        result += count + i

    return result


# print(sum_of_natural_numbers(5))
# print(sum_of_natural_numbers(0))
# print(sum_of_natural_numbers(1))
# print(sum_of_natural_numbers(10))
# print(sum_of_natural_numbers(3))


def centered_star_pyramid(n):
    result = ""
    
    for i in range(n):
        for j in range(n - i - 1):
            result += " "
        result += str(((i * 2) + 1) * "*")
        result += "\n"
    return result.rstrip()

# print(centered_star_pyramid(4))
