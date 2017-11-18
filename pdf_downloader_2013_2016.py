import bs4 as bs
import urllib.request  
import requests
import re
import os
from urllib.parse import urljoin

def get_pdfs():
	url_get = 'https://www.supremecourt.gov/oral_arguments/argument_transcript/2012'
	sauce = urllib.request.urlopen(str(url_get)).read()
	soup = bs.BeautifulSoup(sauce, 'lxml')

	pdf_link = soup.find_all('span', style='display:block;width:80px;float:left;')
	pdf_urljoins = []
	for link in pdf_link:
	 	pdf_urljoin = re.findall(r'\bargument_transcripts[/]\d{0,10}[/]\d{0,10}[-]\d{0,10}[_]\w*[.]\bpdf', str(link))
	 	pdf_urljoins.append(pdf_urljoin)
	print(len(pdf_urljoins))
	
	# Finds the name of the specific PDFs (without the 'base' link; this is provided later )
	pdf_names = []
	for link in pdf_link:
	 	pdf_name = re.findall(r'\d{0,10}[-]\d{0,10}[_]\w\w\w\w[.]\bpdf', str(link))
	 	pdf_names.append(pdf_name)

	# flattens pdf_urljoins list 
	flat_pdf_urljoins = [item for url in pdf_urljoins for item in url]

	# flattens pdf_names list 
	flat_pdf_names =  [item for url in pdf_names for item in url]
	print(flat_pdf_names)
	# provides the base for the URLs in urljoin
	base = re.findall(r'\bhttps://www[.]\bsupremecourt[.]\bgov/oral_arguments/', url_get)
	
	# Creates a download 
	links = []
	for url in flat_pdf_urljoins:
		x = urljoin(str(base[0]), str(url))
		links.append(x)

	# Executes the download 
	counter = 0
	for link in links:
		r = requests.get(link, allow_redirects=False)
		#skips the first 70 characters and then writes the files to the current directory 
		open(str(link[70:]), 'wb').write(r.content)
		counter += 1
		print(counter, link)
		
	return(None)

		
	
get_pdfs()