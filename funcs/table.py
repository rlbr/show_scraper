from .common import *
__all__ = []
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
__all__.append('table_sniffer')
def find_season(table):
    '''finds season above a given table'''
    for tag in filter(lambda thing: isinstance(thing,bs4.element.Tag),table.previous_elements):
        if tag.name == 'h3' and any(thing in tag.text.lower() for thing in ('season','series','special','movie')):
            return tag.text
__all__.append('find_season')
def get_headers(table):
    '''gets the first row of a table, most likely to be the headers'''
    headers = table.find('tr')
    return headers
__all__.append('get_headers')
