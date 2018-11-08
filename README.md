
# journotools

All tools journalistic

# Welcome to journotools

This is a collection of tools that may prove useful to journalists. It will grow eventually into a big toolkit.

## email-extractor

This simple script gets all emails from a text file and outputs them in orderly manner

Current version only gets emails that positioned on different strings.

## paragraph-check

Checks paragraphs in your text:

- does a paragraph fits on mobile screen
- does it consists of too long sentences
- does it contains exclamation marks or other punctuation marks that make text sound biased or too emotional
- checks homogenity of sentences
- too long paragraphs that consist of one-sentence are not needed here

## header-checks

Checks if

- a header is too long. Takes into account mobile and search platforms
- a keyword stands first in the header

## text-checks

Checks if

- subheaders placed too sparse
- words are double-spaced
- double empty lines are used
- punctuation marks placed erroneously
- too many words from Odgen's lists 
- too many words repeated

## picture-checks

Takes URL as an argument. Checks if

- picture file size is too big for a mobile connection. Recommends to convert big PNGs to JPGs.
- picture itself is too small to be optimally represented in social networks

## lede-generator

Tool that generates lede by taking the first sentence from each paragraph. 

## Some constants

Average length of a Russian oral sentence: 10 words. Average written Russian sentence consists of 14 words. 

Average length of an English written sentence: 20 words. The Wall Street Journal uses sentences with average length of 23 words. The same metric of The New York Times is 28 words.
