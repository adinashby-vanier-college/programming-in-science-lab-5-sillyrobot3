# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
#    result = ""
#    newline = "\n"
   x = "*"
   y = " "
   z = (n - 4) * y
   new = f"{x}{z}{x}"
   count = 3
   
   if n > 1:
    # result += t
    while count <= n:
        count += 1   
    # result += t
    return f"{x * n}\n{new}\n{x * n}"
   else:
        return x * n
#    return hollow_square(n)

   
print(hollow_square(1))
print(hollow_square(2))
print(hollow_square(5))


# def hollow_square(n):
#    x = "*"
#    return(x * n)
#    y = " "
#    count = 2
#    while count <= n - 1:
#     return(x, (n - 4) * y, x)
#     count += 1
#    return(x*n)
# 1
# 12
# 123
# 1234
# def number_pattern(n):
#     return ""

# # # Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
# def sum_of_natural_numbers(n):
#     return ""

# # Example for n = 4:
# #    *
# #   ***
# #  *****
# # *******
# def centered_star_pyramid(n):
#     return ""
