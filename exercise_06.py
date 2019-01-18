# source: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
print('Type any word and I\'ll check whether this string is a palindrome or not')
word = input()
if word.lower() == word[::-1].lower():
    print('You typed \'{}\' and this word is a palindrome!'.format(word))
else:
    print('You typed \'{}\' and this word is not a palindrome!'.format(word))