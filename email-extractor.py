## extracts emails 

samplefile = "email-sample.lst"

def extract_emails(st):
    # extracts emails from a line
    print ("hello",st)

extract_emails("m@mail.ru")





with open(samplefile) as f:
        for line in f:
            extract_emails(line)
f.closed

