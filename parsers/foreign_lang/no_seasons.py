if __name__ == '__main__':
    from funcs import table_sniffer,get_headers,sep,words
else:
    from parsers.funcs import table_sniffer,get_headers,sep,words
def parse(BS):
    page = BS
    table = table_sniffer('episode',page)[0]
    show_dict = {}
    headers = sep(get_headers(table))
        
    episodes = table.find_all('tr',attrs = {'class':'vevent'})
    for episode in episodes:
        episode = sep(episode)
        ep_no = episode[0]
        episode_dict = dict(zip(headers,episode))
        show_dict[ep_no] = episode_dict
            
    return show_dict
