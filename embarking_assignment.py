# Even or Odd Solution
# URL https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# Convert a Number to a String Solution
# URL: https://www.codewars.com/kata/5265326f5fda8eb1160004c8
def number_to_string(num):
    return str(num)

# Vowel Count Solution
# URL: https://www.codewars.com/kata/54ff3102c1bad923760001f3
def get_count(sentence):
    count = 0
    for char in sentence:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    return count
