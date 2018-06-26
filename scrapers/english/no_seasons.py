import funcs
def parse(BS):
    return_dict = {}
    tables = funcs.table.table_sniffer('episode',BS)
    
    table = tables[0]
    header_row = funcs.table.get_headers(table)
    headers = funcs.parse.sep(header_row)
    episode_column = 0
    for row_raw in table.find_all('tr',attrs = {'class':'vevent'}):
        row = funcs.parse.sep(row_raw)
        episode_number = row[episode_column]
        episode_dict = dict(zip(headers,row))

        del episode_dict[headers[episode_column]]
        return_dict[episode_number] = episode_dict

    return return_dict
__all__ = ['parse']
if __name__ == "__main__":
    import time
    with open(r"test_html\List of band of brothers episodes.html",'rb') as file:
        p = funcs.common.BS(file,'lxml')
        print('start')
        start = time.time()
        d = parse(p)
        print(time.time()-start)
