from bs4 import BeautifulSoup as BS
if not  __name__ == "__main__":
    from .parsers import has_seasons,no_seasons,funcs
else:
    from parsers import has_seasons,no_seasons,funcs
import wikipedia as w
import urllib
import pprint
def parse_show(show):
    l = funcs.search_it(show)
    print(l)
    d = {}
    for hit in l:
        p = w.page(pageid=hit['pageid']).html()
        d.update(has_seasons.parse(BS(p,'lxml')))
    return d
