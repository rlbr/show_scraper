import bs4
from bs4 import BeautifulSoup as BS
import wikipedia as w
import re
from dateutil.parser import parse as parse_date

#pattern to replace the refences in wikipedia
repl = re.compile(r'([\"]|\[\d+\]| {2,})')
#pattern to find the English words (useful for anime)
words = re.compile(r'[\w ]+\w')
#episode regex
episode = re.compile(r'([a-zA-z]+ {0,1})+ \(\w+ ?\d{1,2}\)')
#pattern to find the digits
seasons_digit = re.compile(r'\d{1,3}')
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
