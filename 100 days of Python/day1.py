 #reverse the string passed into it.
def solution(string):
    reversed_string = string[::-1]
    return reversed_string


##alternative method
def solution(string):
    # Pythonic way :)
    return string[::-1]
    
    # For beginners it's good practise 
    # to know how reverse() or [::-1]
    # works on the surface
    #for char in range(len(string)-1,-1,-1):
        #return string[char]