# Converting string value to Base Format Value

def string_to_base_format(n,base):

    if base == 16:
        convertString = "0123456789ABCDEF"

        print(convertString[n % base])
        if n < base:
            return convertString[n]
        else:
            return string_to_base_format(n//base,base) + convertString[n%base]
    else:
        if n < base:
            return n%2
        else:
            return str(string_to_base_format(n//2,base)) + str(n%2)

print('Converted value is ' + string_to_base_format(10,2))