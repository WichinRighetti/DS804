
# we start by asking the user both numerator and denominator 
def get_fraction():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    return numerator, denominator

# Get input for first fraction
print("Enter the values for the first fraction:")
fraction1 = get_fraction()

# Get input for second fraction
print("\nEnter the values for the second fraction:")
fraction2 = get_fraction()

# we now make the fraction out of the user input values and we will need to have the same denominator
# after we find the common denominator we can do the sum of the two numerators
def calculate_sum(fraction1, fraction2):
    num1, den1 = fraction1
    num2, den2 = fraction2
    numerator = (num1 * den2) + (num2 * den1)
    denominator = den1 * den2
    return numerator, denominator

#we simplify our sum finding the greated commun divisor python has a method already for this
def simplify_fraction(fraction):
    numerator, denominator = fraction
    gcd = find_gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return numerator, denominator

# we loop our ,method until we have the simplest fraction 
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Calculate the sum of the fractions
result = calculate_sum(fraction1, fraction2)

# Simplify the result
result = simplify_fraction(result)

# Print the simplified result
print("\nThe sum of the fractions is: {}/{}".format(result[0], result[1]))
