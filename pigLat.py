# Write your code here :-)
# English to Pig Latin.

print("Enter the Messae to Translate into Pig Latin:")
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []#A list of the words in Pig Latin.

for word in message.split():
    # Seperate teh non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    #Seperate teh non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]


   #Remeber if the word was in uppercase or lowercase
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()

    #Seperate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word)> 0 and not word[0] in VOWELS:
        prefixConsonants +=word[0]
        word = word[1:]

    #Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    #set teh word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    #Add the non letters back to the start of end of the word.Title
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

#Join all hte words back together into a single string:
print(' '.join(pigLatin))

