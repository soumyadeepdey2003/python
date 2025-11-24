
"""
Given a list of strings:
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
Write code that:
Create a new list with words that have more than 5 characters (using list comprehension)
Create another list with the length of each word (using list comprehension)
Create a list of tuples: (word, length, first_char, last_char) for words starting with vowels (a, e, i, o, u)
Count total characters in all words combined
Print the longest word and its length

"""

# ans:

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
new=[]
for i in words:
    if(len(i)>5):
        new.append(i)

print(new)

lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)

vowels = 'aeiouAEIOU'
vowel_words =[]
for word in words:
   if word[0] in vowels:
       vowel_words.append((word, len(word), word[0], word[-1])) 

print(vowel_words)


total_chars =0
for word in words:
    total_chars=total_chars+len(word)

print(total_chars)



maxcar=max(words,key=len)

print(maxcar,len(maxcar))