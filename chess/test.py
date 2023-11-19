print(ord('a'))

def validateMove(move):
    #move should be in format: A1 B2
    #check input format and convert to coordinates
    if not(len(move) == 5): return False
    a,b,c,d = [None]*4
    if move[0].isalpha(): b=(ord(move[0].lower())-97) 
    if move[1].isnumeric(): a=int(move[1])-1
    if move[3].isalpha(): d=(ord(move[3].lower())-97) 
    if move[4].isnumeric(): c=int(move[4])-1
    print(a,b,c,d)
    print([(x == None or x not in range(8)) for x in [a,b,c,d]])
    if any([ (x == None or x not in range(8)) for x in [a,b,c,d]]): return False

    return True

print(validateMove('f1 B3'))