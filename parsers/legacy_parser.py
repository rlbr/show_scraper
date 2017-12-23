from bs4 import BeautifulSoup as _bs
import re

def parse(html):
    #output container
    show_dict = {}

    #create BeautifulSoup object
    bs = _bs(html,'lxml')

    #find all listings of seasons in wikipedia table
    seasons = list(
        map(
            lambda x: re.search(r'[Ss]eason (\d+)',x.text).group(1)
            ,bs.find_all(lambda tag: 'season' in tag.text.lower(),{'class':'mw-headline'})
            )
        )

    #finds all tables with specific class, this is common in my experience but not enough so to trust it. Why did I make it an iterator??
    tables = iter(bs.find_all('table',{'class':'wikiepisodetable'}))
    
    #main iteration
    for season,table in zip(seasons,tables):
        #this is like the season
        show_dict[season] = {}

        #finds the header to the table
        _headers = table.find('tr').find_all('th')
        #forms them into a python list. This will serve
        headers = list(map(lambda x: repl.sub('',replace_with_char(x,' ')),_headers))

        #iterates over everything besides the headers to the table
        for row in table.find_all('tr',{'class':'vevent'}):
            _row = row
            row = list(map(lambda x: repl.sub('',replace_with_char(x)),row.find_all(['th','td'])))
            row = dict(zip(headers,row))

            #this was a special case thing for nested episode listing? Like two in one row
            if any('\n' in v for v in row.values()):
                for row in spec_ops(row):
                    show_dict[season][row['No. in season']] = row
                    
            else:
                show_dict[season][row['No. in season']] = row

    return show_dict

#thing for the special case
def spec_ops(row):
    row = dict(map(lambda t: (t[0],re.split(r'\n+',t[1])),row.items()))
    for pos in range(len(row['No. in season'])):
        temp = {}
        for key,v in row.items():
            if len(v) > 1:
                temp[key] = v[pos]
            else:
                temp[key] = v[0]
        yield temp
