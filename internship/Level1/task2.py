#Temperature conversion

def temp_convert(t, u):
    if u == 'c':
        fh = (t * 9/5)+32
        return fh, "F"
    elif u == 'f':
        cel = (t * 5/9)+32
        return cel, "C"
    else:
        return None, None

temp = float(input("Enter a temperature to convert: "))
unit = input("Enter the unit (C/F): ").lower()

new_temp, new_unit = temp_convert(temp, unit)
if new_temp is not None:
    print(f'Converted Temperature: {round(new_temp,2)} °{new_unit}')
else:
    print("Invalid Unit Entered!")