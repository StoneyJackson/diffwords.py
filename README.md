# diffwords.py

Finds differences between words in two files by comparing words in the same
position in two files. Suppose you are comparing file1 and file2, then
diffwords.py prints the kth word in file1 and file2 if they are different for
all k. It also prints the line number and starting character in each file.

The operating assumption of this tool is that you have two files that are
almost the same, but differ in that some words are misspelled in one of them.
In such cases, this tool will report each time the two files disagree about
a word.
