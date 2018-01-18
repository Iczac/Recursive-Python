# Converting string value to Base Format Value

def string_conversion(n,base):

    if base == 16:
        convertString = "0123456789ABCDEF"

        print(convertString[n % base])
        if n < base:
            return convertString[n]
        else:
            return string_conversion(n//base,base) + convertString[n%base]
    else:
        if n < base:
            return n%2
        else:
            return str(string_conversion(n//2,base)) + str(n%2)

print('Converted value is ' + string_conversion(10,2))