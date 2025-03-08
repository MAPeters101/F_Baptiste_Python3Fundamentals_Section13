'''
Question 4
Write a function that receives a string as an argument (defaults to an empty
string) and returns a dictionary with the unique words and their frequency.

For example, for a string such as:

This is the first sentence. This is the scecond sentence. This is not the
fourth sentence, it is the third sentence.
the result of the function should be:

result = {
    'This': 3,
    'is': 4,
    'the': 4,
    'first': 1,
    'sentence': 4,
    'scecond': 1,
    'not': 1,
    'fourth': 1,
    'it': 1,
    'third': 1
}
You may assume that word separators are limited to spaces, commas, and periods
(no newline characters).

Hint: You will want to split based on some character. Problem is that we
really need to split based on three different characters: spaces, commas and
periods. One approach would be to replace all commas and periods with spaces
and then split on spaces.
'''