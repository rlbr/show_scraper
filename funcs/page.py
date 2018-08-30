from .common import *
from wikipedia.util import cache
from wikipedia.wikipedia import _wiki_request
__all__ = []
@cache
def search_raw(query, results=10, suggestion=False):
    '''
    Do a Wikipedia search for `query`.

    Keyword arguments:

    * results - the maxmimum number of results returned
    * suggestion - if True, return results and suggestion (if any) in a tuple
    '''

    search_params = {
        'list': 'search',
        'srprop': '',
        'srlimit': results,
        'limit': results,
        'srsearch': query
    }
    if suggestion:
        search_params['srinfo'] = 'suggestion'

    raw_results = _wiki_request(search_params)

    if 'error' in raw_results:
        if raw_results['error']['info'] in ('HTTP request timed out.', 'Pool queue is full'):
            raise HTTPTimeoutError(query)
        else:
            raise WikipediaException(raw_results['error']['info'])

    return raw_results

def search_it(show):
    '''finds show based off of it's name, and returns episodes if article is split up'''
    regex = re.compile(
        r'list of {show} (\(.+\) )?episodes( \(seasons 1-20\))?'.format(show=show),
        re.IGNORECASE
        )
    results = search_raw('list of {show} episodes'.format(show = show))['query']['search']
    ret = list(filter(
        lambda result: regex.match(result['title']),results
        ))
    if not ret:
        ret = [search_raw('{show} tv'.format(show=show))['query']['search'][0]]
    return ret
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
