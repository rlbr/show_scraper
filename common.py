import wikipedia as w
import re

#patern to replace the refences in wikipedia
repl = re.compile(r'(["]|\[\d+\])')

#replaces line breaks with a space or other character
def replace_with_char(element,char='\n'):
    text = ''
    for elem in element.recursiveChildGenerator():
        if isinstance(elem, str):
            text += elem.replace('\n',char)
        elif elem.name in ('br','hr'):
            text += char
    return text

#gets html of a show based off of it's name, but is super slow so perhaps
#implement a cache system?
def search_it(show,debug = False):
    article = w.search('list of {} episodes'.format(show),results = 1)
    if debug:
        print('Found article')
    html = w.page(article).html()
    if debug:
        print('Got html')
    return html
