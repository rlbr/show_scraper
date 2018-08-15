from .common import *
__all__ = []
def search_it(movie):
    '''searches for movie'''
    results = w.search_raw(movie+"(movie)")['query']['search']
    return results
__all__.append(search_it)
def get_infobox(BS):
    return BS.find('table',attrs = {'class':'infobox'})
__all__.append(get_infobox)
def get_infobox_section(BS,section):
    section = section.lower()
    infobox = get_infobox(BS)
    return infobox.find(lambda tag: section in tag.text.lower()).find('td').text
__all__.append(get_infobox_section)
