from scrapers.english import *
import pprint
import funcs
def get_info(show):
    results = funcs.page.search_it(show)
    d = {}
    print(show,pprint.pformat(results))
    for result in results:

        page_raw = funcs.page.open_result(result).html()
        try:
            page = funcs.common.BS(page_raw,'lxml')
            eps = funcs.table.table_sniffer('episode',page)
            season = funcs.table.find_season(eps[0])
            if season:
                parser = has_seasons
            else:
                parser = no_seasons
            d.update(parser.parse(page))
        except Exception as e:
            print(show,e)
            return page
        
    return d

if __name__ == "__main__":
    test_shows = [
        'band of brothers',
        'family guy',
        'the simpsons',
        'survivor',
        'better call saul',
        'king of the hill',
        'westworld',
        'black mirror'
        ]
    ret = dict(zip(test_shows,map(get_info,test_shows)))
    
