# simple hash function that shifts the previous value by 5 steps, and adds the ascii value of the current character 
def hash1(input_string):
    hash_value = 0

    for char in input_string:
        hash_value = (hash_value << 5) + ord(char)

    return hash_value % 10000

# hash function that multiplies the previous hash_value by 31 and adds the ascii value of the current character
def hash2(input_string):
    hash_value = 0

    for char in input_string:
        hash_value = (hash_value * 31) + ord(char)

    return hash_value % 10000

