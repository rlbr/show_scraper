if __name__ == '__main__':
    from funcs import table_sniffer,get_headers,find_season,seasons_digit,sep,words
else:
    import funcs
    from .funcs import table_sniffer,get_headers,find_season,seasons_digit,sep,words
def parse(BS):
    page = BS
    tables = list(
        map(
            lambda table: (find_season(table),table),table_sniffer('episode',page)
            )
        )
    show_dict = {}
    for season,table in tables:
        if any(thing in season.lower() for thing in ('special','movie')):
            seas_no = words.search(season).group(0)
            i = 0
        else:
            seas_no = seasons_digit.search(season).group(0)
            i = 1
##        print(get_headers(table))
        headers = sep(get_headers(table))
##        print(headers)
        
        episodes = table.find_all('tr',attrs = {'class':'vevent'})
        show_dict[seas_no] = {}
        for episode in episodes:
            episode = sep(episode,skip = [i,headers.index('Title')])
            ep_no = ','.join(map(funcs.sanitize,funcs.split_br(episode[i])))
            t = episode[headers.index('Title')]
            t = list(map(funcs.sanitize,t))
##            input(repr(episode))
            episode_dict = dict(zip(headers,episode))
            episode_dict['Title'] = funcs.replace_with_char(episode_dict['Title'],'^').split('^')
            show_dict[seas_no][ep_no] = episode_dict
            
    return show_dict
