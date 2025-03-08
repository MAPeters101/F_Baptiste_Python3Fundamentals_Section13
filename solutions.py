'''
Question 1
Write a function that takes a variable number of arguments (with a minimum of
one), and returns the average of these numbers.

Solution
We could write the function this way:

def average(*args):
    sum_values = 0
    for value in args:
        sum_values += value
    return sum_values / len(args)
average(1, 2, 3)
2.0
First thing is that we can use the built-in Python function sum() to sum up
the values:

def average(*args):
    return sum(args) / len(args)
average(1, 2, 3)
2.0
The problem though is that we could call this function without any arguments,
and this will lead to a ZeroDivisionError exception:

average()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-5-c4feed39dc61> in <module>
----> 1 average()

<ipython-input-3-2a0882cc9d56> in average(*args)
      1 def average(*args):
----> 2     return sum(args) / len(args)

ZeroDivisionError: division by zero
We could decide that this is perfectly fine and that the exception should
occur - that's perfectly valid.

The problem with just letting that exception happen is that it is not very
informative in terms of why that exception occurred - person using our
function may not understand that this was caused by passing zero arguments.

So, at the very least, we shoudl provide a better error message:

We could use the LBYL approach, and test for the number of arguments passed in,
and raise an exception if none were passed:

def average(*args):
    if len(args) == 0:
        raise ValueError('At least one argument must be passed to function.')
    return sum(args) / len(args)
average()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-7-c4feed39dc61> in <module>
----> 1 average()

<ipython-input-6-992157a124cf> in average(*args)
      1 def average(*args):
      2     if len(args) == 0:
----> 3         raise ValueError('At least one argument must be passed to
function.')
      4     return sum(args) / len(args)

ValueError: At least one argument must be passed to function.
Another approach (EAFP) could be:

def average(*args):
    try:
        return sum(args) / len(args)
    except ZeroDivisionError:
        raise ValueError('At least one argument must be passed to function.')
average()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-8-78429c1e52b8> in average(*args)
      2     try:
----> 3         return sum(args) / len(args)
      4     except ZeroDivisionError:

ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

ValueError                                Traceback (most recent call last)
<ipython-input-9-c4feed39dc61> in <module>
----> 1 average()

<ipython-input-8-78429c1e52b8> in average(*args)
      3         return sum(args) / len(args)
      4     except ZeroDivisionError:
----> 5         raise ValueError('At least one argument must be passed to
function.')

ValueError: At least one argument must be passed to function.
But we can actually enforce that at least one argument must be passed by
changing how we specify our arguments - we can specify a single positional,
followed by a *args - this way the function must be called with at least one
argument:

def average(arg, *args):
    sum_values = arg + sum(args)
    return sum_values / (len(args) + 1)
average(1, 2, 3)
2.0
average()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-8-78429c1e52b8> in average(*args)
      2     try:
----> 3         return sum(args) / len(args)
      4     except ZeroDivisionError:

ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

ValueError                                Traceback (most recent call last)
<ipython-input-11-c4feed39dc61> in <module>
----> 1 average()

<ipython-input-8-78429c1e52b8> in average(*args)
      3         return sum(args) / len(args)
      4     except ZeroDivisionError:
----> 5         raise ValueError('At least one argument must be passed to
function.')

ValueError: At least one argument must be passed to function.
Question 2
Write a function that returns a string based on two input arguments:

a character or string to be repeated
the number of times the string should be repeated
The function should be such that the number of repetitions defaults to 10 if
it is not passed by the caller, and the default character to be repeated
should be a negative sign (-).

Call your function separator.

Use a keyword-only argument for the string argument.

Solution
Here we'll want to use default values for the value and the string, as well
as make the string a keyword-only argument:

def separator(number=10, *, char='-'):
    return char * number
separator()
'----------'
separator(5)
'-----'
separator(char='*')
'**********'
separator(5, char='*')
'*****'
Question 3
Write a lambda function that returns the number of unique elements in an
iterable. This could be the number of unique characters in a string, or the
number of unique elements in a list, tuple, etc.

If the iterable received by the lambda function is empty, then it should
return 0.

Solution
Let's first write this using a regular function.

We're going to use sets to obtain the unique elements of an iterable, and
then return the length of the set:

def count_unique(iterable):
    unique_elements = set(iterable)
    return len(unique_elements)
count_unique('abcdabcd')
4
count_unique([1, 1, 2, 2, 3])
3
And this even works for empty iterables:

count_unique([])
0
We can then make a lambda function with the same functionality:

f = lambda iterable: len(set(iterable))
f('aabbcc')
3
f([1, 1, 2, 2, 3, 4])
4
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

Solution
The first thing our function will need to do is split all the words on the
space, comma and prediod characters.

But the split function cannot handle multiple separators, so we need a way
around this.

One approach would be to iterate over every character in the string and
maintain the splits ourselves by checking the current character value as a
separator value or not a separator value - but this is not as easy to do as it
sounds.

Another approach, beyond the scope of this course, would be to use regular
expression.

The approach I'm going to take here is to replace all the separator characters
with spaces - and then just split on spaces.

s = "word1, word2. word3 word4 word4"
s = s.replace(',', ' ')
s
'word1  word2. word3 word4 word4'
s = s.replace('.', ' ')
s
'word1  word2  word3 word4 word4'
Now we can split on spaces, but you'll notice that we sometimes have repeated
spaces in our string:

s.split(' ')
['word1', '', 'word2', '', 'word3', 'word4', 'word4']
But remember that with no argument, split will split based on any whitespace
characters - and this works much better for us, since it will treat ' '
(single space) in the same way as '  ' (two spaces).

s.split()
['word1', 'word2', 'word3', 'word4', 'word4']
Once we have that, we can build up a dictionary containing the unique words
and their frequency:

freq = {}
for word in s.split():
    freq[word] = freq.get(word, 0) + 1

freq
{'word1': 1, 'word2': 1, 'word3': 1, 'word4': 2}
Or we could use the Counter object we saw earlier:

from collections import Counter

freq = Counter(s.split())
freq.dict()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-32-3143d6d02a85> in <module>
      2
      3 freq = Counter(s.split())
----> 4 freq.dict()

AttributeError: 'Counter' object has no attribute 'dict'
If we truly want a dictionary, we can convert that Counter object to a dict
type:

dict(freq)
{'word1': 1, 'word2': 1, 'word3': 1, 'word4': 2}
Now we are ready to build a function that does all these steps:

def word_frequencies(s = ''):
    s = s.replace(',', ' ')
    s = s.replace('.', ' ')
    words = s.split()
    return dict(Counter(words))
Let's try this function out with some arguments (including no arguments):

word_frequencies()
{}
word_frequencies('word1, word2, word1. word1 word1... word3')
{'word1': 4, 'word2': 1, 'word3': 1}
And finally let's try it out with the sample text and make sure we get the
same results:

s = """
This is the first sentence. This is the scecond sentence. This is not the
fourth sentence, it is the third sentence.
"""
computed = word_frequencies(s)
computed
{'This': 3,
 'is': 4,
 'the': 4,
 'first': 1,
 'sentence': 4,
 'scecond': 1,
 'not': 1,
 'fourth': 1,
 'it': 1,
 'third': 1}
We could visually check the results against the sample result, but we can also
just compre the dictionaries using ==:

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
computed == result
True
'''