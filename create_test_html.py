from funcs import page
import os
if not os.path.exists('test_html'):
    os.makedirs('test_html')
os.chdir('test_html')
test_shows = ['band of brothers',
 'better call saul',
 'black mirror',
 'case closed',
 'darker than black',
 'king of the hill',
 'seinfeld',
 'west world',
 'the wire',
 'the simpsons',
 'futurama',
 'rick and morty']
results = list(map(page.search_it,test_shows))
for result in results:
    print(result)
    for sub_result in result:
        p = page.open_result(sub_result)
        page.save(p,sub_result['title']+'.html')
