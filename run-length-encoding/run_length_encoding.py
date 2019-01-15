from re import sub

def decode(string):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), string)

##def encode(old_string):

    #segment = lambda c, n:(str(n)if n >1 else '') + c
    #previous_char = ''
    #occurences = 0
    #result = ''
    #for c in string:
        #if c == previous_char:
         #occurences += 1
        #else:
            #result += segment(previous_char, occurences)
            #previous_char: c
            #occurences = 1
        #result += segment(previous_char, occurences)
        #return result
           
def encode(string):
     return sub(r'([A-Z])/1 +' , lambda m: str(len(m.group(0)))+ m.group(1),string)