from .common import *
__all__ = []
def replace_with_char(element,char='\n'):
    '''replaces "br" and "hr" tags, as well as newlines, to a specified character'''
    text = element
    if not isinstance(element,str):
        text = ''
        for elem in element.recursiveChildGenerator():
            if isinstance(elem, str):
                text += elem.replace('\n',char)
            elif elem.name in ('br','hr'):
                text += char
    return text
__all__.append('replace_with_char')
def sanitize(string):
    string = replace_with_char(string,' ')
    string = re.sub('\xa0|\u200a',' ',string)
    string = re.sub(' +$','',repl.sub('',string))
    match = re.search(r"\d{4}\D+\d{2}\D+\d{2}",string)
    if match and any(month in string.lower() for month in months):
        return parse_date(match.group(0))
    else:
        return string
__all__.append('sanitize')
def sep(row):
    '''splits the row into columns and maps replace_with_char on each column'''
    return list(map(sanitize,row.find_all(('th','td'))))
__all__.append('sep')
