"""ask - Pangram
Pangrams are sentences (i.e. strings) that contain all characters of the alphabet. Implement a method is_pangram that takes one argument as input and checks if the given string is a pangram and then returns the result as a boolean value.

Examples:
'Waltz, bad nymph, for quick jigs vex.'
'Glib jocks quiz nymph to vex dwarf.'
'Sphinx of black quartz, judge my vow.
'How vexingly quick daft zebras jump!'
'The five boxing wizards jump quickly.'
'Jackdaws love my big sphinx of quartz.'
'Pack my box with five dozen liquor jugs.'
Hint: A pangram is a sentence that includes every letter of the alphabet, A through Z
you can use sets for this task

Output:

pangram('Waltz, bad nymph, for quick jigs vex.') --> True
pangram('Not all characters.') --> False"""

# Solution 1

def is_pangram(sentence):
    # Convert the sentence to lowercase for case-insensitive comparison
    sentence_lower = sentence.lower()
    # Create a set of unique lowercase alphabets in the sentence
    alphabets = set(sentence_lower)
    # Remove non-alphabetic characters from the set
    alphabets.discard(' ')
    alphabets.discard(',')
    alphabets.discard('.')
    # Check if the set of alphabets contains all 26 lowercase letters
    return len(alphabets) == 26

sentence1 = 'Waltz, bad nymph, for quick jigs vex.'
sentence2 = 'Not all characters.'

print("pangram", "(",sentence1, ")", "-->", is_pangram(sentence1))  # Output: True
print("pangram", "(",sentence2, ")", "-->",is_pangram(sentence2))  # Output: False

print("________________________________________________")

# Solution 2

def is_pangram(sentence):
    # Convert the sentence to lowercase for case-insensitive comparison
    sentence_lower = sentence.lower()
    # Create a set of unique lowercase alphabets in the sentence
    alphabets = set(sentence_lower)
    # Remove non-alphabetic characters from the set
    alphabets = {ch for ch in alphabets if ch.isalpha()}
    # Check if the set of alphabets contains all 26 lowercase letters
    return len(alphabets) == 26

sentence1 = 'Waltz, bad nymph, for quick jigs vex.'
sentence2 = 'Not all characters.'


print("pangram", "(",sentence1, ")", "-->", is_pangram(sentence1))  # Output: True
print("pangram", "(",sentence2, ")", "-->",is_pangram(sentence2))  # Output: False