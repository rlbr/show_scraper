from .common import *
__all__ = []
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
__all__.append('search_it')
def open_result(result):
    return w.page(pageid = result['pageid'])
__all__.append('open_result')
def save(page,filename):
    if not isinstance(page,str):
        page = page.html()
    encodings = ['ascii','utf-8','utf-16']
    for encoding in encodings:
        try:
            ret = page.encode(encoding)
        except Exception as e:
            pass
    with open(filename,'wb') as file:
        file.write(ret)
__all__.append('save')
