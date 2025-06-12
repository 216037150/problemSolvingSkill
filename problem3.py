# A string is a palindrome if it reads the same backward.

def my_Palidrom(sentence):
    # Remove spaces and convert to lowercase
    sentence = sentence.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    if sentence == sentence[::-1]:
        return True
    return False 
print(my_Palidrom('Madam')) 