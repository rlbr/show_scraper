import wikipedia as w
from bs4 import BeautifulSoup as BS
from dateutil.parser import parse
import re
def get_release_date(bs):
    info_box = bs.find('table',attrs = {'class':'infobox'})
    release_date = info_box.find(lambda tag: 'release date' in tag.text.lower()).find('td').text
    return list(map(parse,re.findall(r'\d{4}-\d{2}-\d{2}',release_date)))
