vowels = 0
consonants = 0
sentence = input('Enter your sentence: ' )
for letter in sentence:
    if letter in 'aeiou':
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Vowels: ", vowels, "Consonants: ", consonants)