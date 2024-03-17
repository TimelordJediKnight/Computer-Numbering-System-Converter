#This program will convert between decimal, decimal, hexadecimal and octal
           
def bin_dec(binary : str):
    """Enter a binary number and return the decimal representation"""
    
    decimal = 0
    binary = binary[::-1]
    
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2**i
        
    return decimal

def bin_oct(binary : str):
    """Convert binary string to octal"""
    decimal = bin_dec(binary)
    return dec_oct(decimal)

def bin_hex(binary : str):
    decimal = bin_dec(binary)
    return dec_hex(decimal)

def dec_bin(decimal : str):

    binary = ""
    decimal = int(decimal)
    
    if decimal != 0:
        while decimal > 0:
        
            if decimal%2 == 1:
                binary += "1"
                decimal //= 2
             
            elif decimal%2 == 0:
                binary += "0"
                decimal //= 2
            
    elif decimal == 0:
        binary = 0
            
    return binary[::-1]

def oct_dec(octal : str):
    #Enter an octal number and return the decimal equivalent
    decimal = 0

    octal = octal[::-1]
    octal_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8')
    
    for i in range(len(octal)):
        if octal[i] in octal_chars:
            decimal += octal_chars.index(octal[i])*8**i
    
    return decimal

def oct_bin(binary : str):
    decimal = oct_dec(binary)
    return dec_bin(decimal)

def oct_hex(binary : str):#failed
    decimal = oct_dec(binary)
    return dec_hex(decimal)

def dec_oct(decimal : str):

    oct = ""
    decimal = int(decimal)
    
    if decimal != 0:
        while decimal > 0:
        
            if decimal%8 != 0:
                oct += str(decimal%8)
                decimal //= 8
             
            elif decimal%8 == 0:
                oct += "0"
                decimal //= 8
            
    elif decimal == 0:
        oct = 0
            
    return oct[::-1]

def hex_dec(hexadecimal : str):
    #Enter a hexadecimal value and return the decimal equivalent
    decimal = 0
    hexadecimal = hexadecimal[::-1]
    
    hex_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    
    for i in range(len(hexadecimal)):

        if hexadecimal[i] in hex_chars:
            decimal += hex_chars.index(hexadecimal[i])*16**i
            
    return decimal

def hex_bin(binary : str):
    decimal = hex_dec(binary)
    return dec_bin(decimal)

def hex_oct(binary : str):
    decimal = hex_dec(binary)
    return dec_oct(decimal)

def dec_hex(decimal : str):

    hexVal = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 
              10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

    hex = ""
    decimal = int(decimal)
    
    if decimal != 0:
        
        while decimal > 0:
        
            if decimal%16 >= 0:
                hex += hexVal[decimal%16]
                decimal //= 16
            
    elif decimal == 0:
        hex = '0'
            
    return hex[::-1]

def convertLoop(): # binary:% octal:0 hexadecimal:$
    """%11 decimal -> 3; "11 binary decimal" return decimal value 3"""
    
    prompt = input("> ").lower().split()
    
    if prompt[0][0] == "%" and prompt[1] in ("dec", "decimal"):
        print(bin_dec(prompt[0]))
        
    elif prompt[0][0] == "%" and prompt[1] in ("oct", "octal"):
        print(bin_oct(prompt[0]))
        
    elif prompt[0][0] == "%" and prompt[1] in ("hex", "hexadecimal"):
        print(bin_hex(prompt[0]))
        
    elif prompt[0][0] == "0" and prompt[1] in ("dec", "decimal"):
        print(oct_dec(prompt[0]))
        
    elif prompt[0][0] == "0" and prompt[1] in ("bin", "binary"):
        print(oct_bin(prompt[0]))
        
    elif prompt[0][0] == "0" and prompt[1] in ("hex", "hexadecimal"):
        print(oct_hex(prompt[0]))
        
    elif prompt[0][0] == "$" and prompt[1] in ("dec", "decimal"):
        print(hex_dec(prompt[0]))
        
    elif prompt[0][0] == "$" and prompt[1] in ("bin", "binary"):
        print(hex_bin(prompt[0]))
        
    elif prompt[0][0] == "$" and prompt[1] in ("oct", "octal"):
        print(hex_oct(prompt[0]))
        
    elif int(prompt[0][0]) > 0 and prompt[1] in ("bin", "binary"):
        print(dec_bin(prompt[0]))
        
    elif int(prompt[0][0]) > 0 and prompt[1] in ("oct", "octal"):
        print(dec_oct(prompt[0]))
        
    elif int(prompt[0][0]) > 0 and prompt[1] in ("hex", "hexadecimal"):
        print(dec_hex(prompt[0]))
    
    else:
        prompt
        
def main():
    print("Enter a number, a numbering system, and the numbering system that you want to convert to:")
    while True:
        convertLoop()


print(chr(bin_dec('111111010011')))
print(bin_dec('1111110100114'))