if __name__ == '__main__':
    from funcs import table_sniffer,get_headers,find_season,seasons_digit,sep
else:
    from parsers.funcs import table_sniffer,get_headers,find_season,seasons_digit,sep
def parse(BS):
    page = BS
    tables = list(
        map(
            lambda table: (find_season(table),table),table_sniffer('episode',page)
            )
        )
    show_dict = {}
    for season,table in tables:
        
        season = seasons_digit.search(season).group(0)
        headers = sep(get_headers(table))
        
        episodes = table.find_all('tr',attrs = {'class':'vevent'})
        
        for episode in episodes:
            episode = sep(episode)
            episode_dict = dict(zip(headers,episode))
            print(episode_dict)
            return
