class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input('Поиск(input#search','Input#text')
print(search.loc,text)

class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

text_button = Button('text#Button', 'loc#Button')
print(text_button)



class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

text_title = Title('text#Title', 'loc#Title')
print(text_title)



class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

text_link = Link('text#Link', 'loc#Link')
print(text_link)