import os,sys
path = __file__
for i in range(2):
    path = os.path.dirname(path)
sys.path.insert(0,path)
import re
import funcs
def get_release_date(bs):
    release_date = funcs.movie_funcs.get_infobox_section(bs,'release date')
    return list(map(
        funcs.common.parse_date,re.findall(r'\d{4}-\d{2}-\d{2}',release_date)
        ))
if __name__ == "__main__":
    r = funcs.movie_funcs.search_it('return of the jedi')[0]
    p = funcs.page.open_result(r)
    funcs.page.save(p,os.path.join(path,'test_html',r['title']+'.html'))
    bs = funcs.common.BS(p.html(),'lxml')
    t = get_release_date(bs)
