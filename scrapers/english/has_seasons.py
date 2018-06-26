import os,sys
path = __file__
for i in range(3):
    path = os.path.dirname(path)
sys.path.insert(0,path)
import funcs
def parse(BS):
    return_dict = {}
    tables = funcs.table.table_sniffer('episode',BS)
    
    for table in tables:
        
        season_dict = {}
        season_name = funcs.table.find_season(table)
        
        if any(term in season_name.lower() for term in ('special','movie')):
            season_number = funcs.common.words.search(season_name).group(0)
            episode_column = 0
        else:
            season_number = funcs.common.seasons_digit.search(season_name).group(0)
            episode_column = 1
            
        header_row= funcs.table.get_headers(table)
        headers = funcs.parse.sep(header_row)
        
        for row_raw in table.find_all('tr',attrs = {'class':'vevent'}):
            row = funcs.parse.sep(row_raw,'~@~')
            episode_number = row[episode_column]
            
            #2fer
            if '~@~' in row[episode_column]: 
                multi = True
                episode_number = row[episode_column].replace('~@~','/')
                episode_dict = {}
                part_keys = row[episode_column].split('~@~')
                for i,column in enumerate(row):
                    
                    if isinstance(column,str):
                        parts = column.split('~@~')
                        
                    else:
                        parts = [column]
                        
                    if len(parts) == 1:
                        parts *= 2
                        
                    part_dict = dict(zip(part_keys,parts))
                    episode_dict[headers[i]] = part_dict
                
            #regular   
            else:
                multi = False
                row = funcs.parse.sep(row_raw)
                episode_dict = dict(zip(headers,row))
                
            del episode_dict[headers[episode_column]]
            episode_dict['multi'] = multi

            season_dict[episode_number] = episode_dict
            
        return_dict[season_number] = season_dict

    return return_dict
__all__ = ['parse']

