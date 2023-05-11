# define the function to converto into hex values 
def rgb_to_hex(r, g, b):
    hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_code

# Here I'll ask the user for input of values r,g & b 
red_value = int(input("Enter the red value (0-255): "))
green_value = int(input("Enter the green value (0-255): "))
blue_value = int(input("Enter the blue value (0-255): "))

# hex_color will receive the converted value of RGB and then will printout the result 
hex_color = rgb_to_hex(red_value, green_value, blue_value)
print("Hexadecimal color code:", hex_color)