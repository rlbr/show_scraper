import sys,os
path = __file__
for i in range(2):
    path = os.path.dirname(path)
sys.path.append(path)
from funcs import page,common
from scrapers.english import *

show_test = r'test_html\shows'
show_test = os.path.join(path,show_test)
print(show_test)

if not os.path.exists(show_test):
    os.makedirs(show_test)
#{'ns': 0, 'title': 'List of showname episodes', 'pageid': 123456} = result format
def get_cache(query):
    query = query.lower()
    res = []
    for file in os.listdir(show_test):
        fullpath = os.path.join(show_test,file)
        if query in file.lower():
            with open(fullpath,'rb') as file:
                res.append(common.BS(file,'lxml'))
    if len(res) > 0:
        return res
    else:
        results = page.search_it(query)
        for result in results:
            p = page.open_result(result)
            page.save(p,os.path.join(show_test,result['title']+'.html'))
            p = common.BS(p.html(),'lxml')
            res.append(p)
        return res
def test(func,show):
    return list(map(func,get_cache(show)))
