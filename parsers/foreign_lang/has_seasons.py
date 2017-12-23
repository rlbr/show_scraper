if __name__ == '__main__':
    from funcs import table_sniffer,get_headers,find_season,seasons_digit,sep,words
else:
    from parsers.funcs import table_sniffer,get_headers,find_season,seasons_digit,sep,words
def parse(BS):
    page = BS
    tables = list(
        map(
            lambda table: (find_season(table),table),table_sniffer('episode',page)
            )
        )
    show_dict = {}
    for season,table in tables:
        if 'special' in season.lower():
            seas_no = words.search(season).group(0)
        else:
            seas_no = seasons_digit.search(season).group(0)
        headers = sep(get_headers(table))
        
        episodes = table.find_all('tr',attrs = {'class':'vevent'})
        show_dict[seas_no] = {}
        for episode in episodes:
            episode = sep(episode)
            ep_no = episode[1]
            episode_dict = dict(zip(headers,episode))
            show_dict[seas_no][ep_no] = episode_dict
            
    return show_dict
