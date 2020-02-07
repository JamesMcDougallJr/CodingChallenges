# Implement your function below.
def non_repeating(given_string):
    chars = [-1]*26
    for char in given_string:
        chars[ord(char)-ord('a')] += 1
# chr( i+ord('a') )
    print(chars)
    for char in given_string:
        print("Char {0}".format(char))
        if chars[ord(char)-ord('a')] == 0:
            print("Returning Char {0}".format(char))
            return char
    return None

if __name__ == '__main__':
    # NOTE: The following input values will be used for testing your solution.
    #non_repeating("abcab") # should return 'c'
    #non_repeating("abab") # should return None
    #non_repeating("aabbbc") # should return 'c'
    non_repeating("aabbdbc") # should return 'd'
