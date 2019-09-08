# -*- coding: utf-8 -*-

# Contains a Firefly, the journalistic linter

# text model


class LinterMessage:
    def __init__(self, type="warning",message="Unknown warning: you're not supposed to see it"):
        self.type = type
        self.message = message
    def print(self):
        print(self.type, self.message)



class Header:
    def __init__(self, title="В научном центре \"Роскосмоса\" поймали группу вандалов"):
        self.lang = "ru"
        self.title = title
        self.length = len(self.title)
        print ("header initialized")
        self.showtitle()
        self.checklength()
    def showtitle(self):
        print ("title is", self.title)

    def checklength(self):
        print("title length is", self.length)
        if self.length > 35:
            temp = LinterMessage("warning","Zen will diminish font size").print()
    
    def checkup(self):
        checklength()


# myheader = Header()

class Body:
    def __init__(self):
        self.body = "TK"


class Text:
    def __init__(self):
        print("initializing text")
        self.header = Header()
        self.body = Body()
        print("text created")

class Paragraph:
    def __init__(self):
        print("initializing paragraph")
        self.sentences=[]

class Sentence:
    def __init__(self):
        print("initializing sentence")

class Image:
    def __init__(self):
        self.size_x=0
        self.size_y=0
        self.url="https://example.com"

t = Text()

# Blocks are stacked in the next order:
# Header -> SubHeader -> Lede -> Body -> Additional blocks
# 
# There are additional fields and blocks that don't have perfect placement in the model.
# For instance, open graph fields and basic image are lintering too.
# Right now model gets down to sentence level, but it should use word level too.

# The Linter's Scope

# The linter can be configured to understand in what scope it works. For example a news agency would want to keep its headers in one piece but Buzzfeed can use more options.

# On the other hand, listicle author would want to insert numbers to her headers.

        

l = LinterMessage(message="hi there!")

l.print()



# Checkup 

# ZEN

    # Header

# Google Discover

# Yandex News

# Social Media

# Twitter

