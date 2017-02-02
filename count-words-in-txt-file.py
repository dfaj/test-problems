#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This is a quick and dirty program written in Python 2.7.10 to produce a count of all
    the different "words" in a text file.

    The definition of a "word" is not that easy to programmatically construct without some use of NLP.
    Here, I have defined a word loosely as:
     1) any tab-space delimited word without any punctuation string
     2) any tab-space delimited word made up of simple well-known emoticons e.g, :)
     3) any tab-space delimited made up of special characters that may be meaningful, e.g. \o/
     4) any tab-space delimited word with well-known separators, e.g., home/user becomes home, user

     The text to be analyzed is assume to be English Language wiht ASCII encoding.
     
     The run the script, call it from the terminal prompt and pass the .txt file to be processed as an argument. For example:
     
     ```
     $ python count-words-in-txt-file.py example.txt
     ```


     __version__ = '1.0'
     __author__ = 'Deji Fajebe'

"""

import collections
import sys
import os.path


#variable used for reading input file
inFile = sys.argv[1]


#python Counter from Collections is used for the counting. Tracks how many times equivalents values are added.
wordcount = collections.Counter()

#the punctuation strings to be used for matching and scrubbing the input file
punctuationString = "!\"#%&'()*+,-./:;<=>?[\]^_`{|}~"
specialPunctuationString = "!\"#%'()$¥*+,-./:;<=>?[\]^_`{|}~"
specialString = '$¥#@+-'

stopWords = "\"'(),:;=?[\]^`{|}~."
emoticonWords = "\"'():;=[\]^`{|}~"
bracketWords = "():;=[\]^`{|}~<>\""
dividerWords = "!\"#%'*+/:;<=>?[\]^_`{}|~"

subWords = ['/', '<', '>']


# do a quick sanity check that input file exists and is a txt file
if not os.path.isfile(inFile):
    print '\nThe input file name you have given cannot be found in same path as this script. ' \
          'Check that both files are in the same path or folder.\n'

    exit(0)

# check to see that file is a txt file
if '.txt' not in inFile:
    print '\nThe input file you have used is not a .txt file.\n'
    exit(0)


with open(inFile, 'rU') as file:
    for line in file:

        #variables to used for storing the data at different stages of processing

        #split the line of text
        line_of_words = line.split()

        #line with single words scrubbed
        line_with_single_words_scrubbed = []

        #line with single words scrubbed
        line_with_stop_words_scrubbed = []

        #line with special words (i.e., characters in words & punctuations) scrubbed
        line_with_special_words_scrubbed = []

        #line with brackets at beginning and end of words scrubbed
        line_with_brackets_words_scrubbed = []

        #line with divider characters in the middle of words scrubbed
        line_with_middle_words_scrubbed = []

        #temp_words_splitted on special characters
        temp_words_splitted = []

        #scrub single words first
        for word in line_of_words:
            if len(word) == 1 and (word in punctuationString):
                if word == '':
                    line_with_single_words_scrubbed.append('')

            else:
                line_with_single_words_scrubbed.append(word)


        #scrub punctuations at the end of words
        for word in line_with_single_words_scrubbed:
            if len(word) == 1:
                line_with_stop_words_scrubbed.append(word)

            elif (word[len(word)- 1] in stopWords and word[len(word)- 2] not in emoticonWords):
                line_with_stop_words_scrubbed.append(word[:-1])

            else:
                line_with_stop_words_scrubbed.append(word)


        #scrub brackets at the end and beginning of words
        for word in line_with_stop_words_scrubbed:
            if len(word) == 1:
                line_with_brackets_words_scrubbed.append(word)

            elif word[0] in bracketWords and word[1] in emoticonWords:
                line_with_brackets_words_scrubbed.append(word)

            elif word[0] in bracketWords and word[1] not in emoticonWords:
                # print '\nword[0] in bracketWords and word[1] not in emoticonWords: ' + word[1:]
                line_with_brackets_words_scrubbed.append(word[1:])

            elif word[len(word) - 1] in bracketWords and word[len(word) - 2] not in emoticonWords:
                line_with_brackets_words_scrubbed.append(word[:-1])

            else:
                line_with_brackets_words_scrubbed.append(word)

        #srub special characters in the middle of words
        for word in line_with_brackets_words_scrubbed:
            # print '\n\nType of WORD IS ' + str(type(word)) + '\n\n\n'
            if len(word) == 1:
                line_with_middle_words_scrubbed.append(word)

            elif len(word) == 2:
                line_with_middle_words_scrubbed.append(word)

            else: # len(word) > 2
                #ignore the first and last
                new_word = word[1:]
                new_word = new_word[:-1]
                initial_word = list(word)

                index = 0

                for c in new_word:
                    index = index + 1
                    if c in dividerWords:
                        if initial_word[index + 1] not in dividerWords:
                            initial_word[index] = ' '

                        elif initial_word[index + 1] in dividerWords and 0 < index + 2 < len(initial_word):
                            if initial_word[index + 2] in emoticonWords:
                                initial_word[index] = c
                            elif initial_word[index + 2] in dividerWords:
                                initial_word[index] = ' '
                        else:
                            initial_word[index] = c

                replaced_word = "".join(initial_word)
                temp_words_splitted = replaced_word.split()

                for item in temp_words_splitted:
                    line_with_middle_words_scrubbed.append(item)

        # cleaned word stored in the Container
        wordcount.update(line_with_middle_words_scrubbed)


# get the result from the counter and sort it in descending order
sorted_result = [(k,v) for (k,v) in wordcount.items()]
sorted_result.sort(key=lambda x:x[1],reverse=True)


print '\nThe Count of all the different words in the file: ' + inFile + ' is:\n'

# print result to screen
print 'Word', 'Count'
for k, v in sorted_result:
    print "{}\t{}".format(k, v)

