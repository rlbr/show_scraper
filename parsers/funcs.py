import bs4
from bs4 import BeautifulSoup as BS
import wikipedia as w
import re
from dateutil.parser import parse as parse_date

#pattern to replace the refences in wikipedia
repl = re.compile(r'([\"]|\[\d+\]| {2,})')
#pattern to find the English words (useful for anime)
words = re.compile(r'[\w ]+\w')
#episode regex
episode = re.compile(r'([a-zA-z]+ {0,1})+ \(\w+ ?\d{1,2}\)')
#pattern to find the digits
seasons_digit = re.compile(r'\d{1,3}')
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

def search_it(show):
    '''finds show based off of it's name, and returns episodes if article is split up'''
    regex = re.compile(
        r'list of {show} (\(.+\) )?episodes( \(seasons 1-20\))?'.format(show=show),
        re.IGNORECASE
        )
    results = w.search_raw('list of {show} episodes'.format(show = show))['query']['search']
    return list(filter(
        lambda result: regex.match(result['title']),results
        ))

def table_sniffer(section,page):
    '''finds tables under a given section'''
    tables = []
    section = section.lower()
    start = page.find(lambda tag: tag.name == 'h2' and section in tag.text.lower())
    for tag in filter(lambda thing: isinstance(thing,bs4.element.Tag),start.next_elements):
            if tag.name == 'h2':
                    break
            if tag.name == 'table':
                    tables.append(tag)
    return tables

def find_season(table):
    '''finds season above a given table'''
    for tag in filter(lambda thing: isinstance(thing,bs4.element.Tag),table.previous_elements):
        if tag.name == 'h3' and any(thing in tag.text.lower() for thing in ('season','series','special','movie')):
            return tag.text

def get_headers(table):
    '''gets the first row of a table, most likely to be the headers'''
    headers = table.find('tr')
    return headers

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
def sanitize(string):
    string = replace_with_char(string,' ')
    string = re.sub('\xa0|\u200a',' ',string)
    string = re.sub(' +$','',repl.sub('',string))
    match = re.search(r"\d{4}\D+\d{2}\D+\d{2}",string)
    if match and any(month in string.lower() for month in months):
        return parse_date(match.group(0))
    else:
        return string
def sep(row):
    '''splits the row into columns and maps replace_with_char on each column'''
    return list(map(sanitize,row.find_all(('th','td'))))
