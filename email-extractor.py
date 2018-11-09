# -*- coding: utf-8 -*-
# 
# extracts emails from a file
# uses email-sample.lst if arguments not provided
import re


samplefile = "email-sample.lst"

def extract_emails(st):
    # extracts emails from a line
    regexemail = r"[A-Za-z0-9\-\.\+]+\@[A-Za-z0-9\-\.\+]+\.[A-Za-z0-9]+"
    matches = re.findall (regexemail, st)
    for match in matches:
        print (match)


with open(samplefile,encoding="utf8") as f: # open file
    content = f.readlines()                 # read lines

content = [x.strip() for x in content]      # strip a line of spaces

for line in content:
    extract_emails (line)                        # line by line
    # print (line, "→", extract_emails(line)) # extract emails
f.closed                                    # close the file
