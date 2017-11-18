import bs4 as bs
import urllib.request  
import requests
import re
import os
from urllib.parse import urljoin
import pandas as pd


def get_codes_df(input_list):
	# dfs = []
	for item in input_list:
		url_get = ('http://scdb.wustl.edu/documentation.php?var=' + str(item))
		sauce = urllib.request.urlopen(str(url_get)).read()
		soup = bs.BeautifulSoup(sauce, 'lxml')

		things = []
		for a in soup.find_all('td'):
	 		x = a.string
	 		y = str(x).strip()
	 		things.append(y)
		
		stop = (len(things)-15)
		things = things[23:stop]
		new_keys = dict(zip(things[::2], things[1::2]))
		df_name = (str(item) + 'df')
		df_name = pd.DataFrame.from_dict(list(new_keys.items()))
		print(df_name)
		# df = pd.DataFrame.from_dict(list(new_keys.items()))
		# dfs.append(df)

get_codes_df(['issueArea', 'petitionerState', 'petitioner', 'decisionDirection', 
	'decisionDirectionDissent', 'authorityDecision2', 'caseOrigin', 'chief', 'lawType', 
	'lawSupp', 'declarationUncon', 'caseDisposition', 'caseDispositionUnusual', 'partyWinning', 
	'precedentAlteration', 'justice', 'justiceName', 'vote', 'opinion', 'direction', 'majority'])

def get_codes_csv(input_list):
	for item in input_list:
		url_get = ('http://scdb.wustl.edu/documentation.php?var=' + str(item))
		sauce = urllib.request.urlopen(str(url_get)).read()
		soup = bs.BeautifulSoup(sauce, 'lxml')

		things = []
		for a in soup.find_all('td'):
	 		x = a.string
	 		y = str(x).strip()
	 		things.append(y)
		
		stop = (len(things)-15)
		things = things[23:stop]
		new_keys = dict(zip(things[::2], things[1::2]))
		df = pd.DataFrame.from_dict(list(new_keys.items()))
		df.to_csv((str(item)+'.csv'))

# get_codes_csv(['issueArea', 'petitionerState', 'petitioner', 'decisionDirection', 
	# 'decisionDirectionDissent', 'authorityDecision2', 'caseOrigin', 'chief', 'lawType', 
	# 'lawSupp', 'declarationUncon', 'caseDisposition', 'caseDispositionUnusual', 'partyWinning', 
	# 'precedentAlteration', 'justice', 'justiceName', 'vote', 'opinion', 'direction', 'majority'])

