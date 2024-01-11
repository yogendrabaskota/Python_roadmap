# string formatting in python
# f-string

# old approach
letter = "my name is {1} and i am from {0}"
country = "nepal"
name = "johns"
print(letter.format(country, name))
# f string approach
print(f"Hey! my name is {name} and i am from {country}")

txt = "its price is only {price:.2f} dollars"
print(txt.format(price = 89.9987789))

price = 667.343664
txt = f"For only {price:.2f} dollars"  # usinf f-string
print(txt)


#  About string formatting in Python using the format method and f-strings. 
# The format method allows for more precise control over the formatting, such as specifying the number of decimal places.
# F-strings, introduced in PEP 498, provide a convenient way to embed Python expressions directly inside string literals for formatting.
# By prefixing a string with 'f', it becomes an f-string, making it easier to interpolate variables and expressions.

