import os
import re
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, RegexpTokenizer

def case_names(year):
    file_names = []
    for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/' + str(year)):
        file_names.append(file)

    file_paths = []
    for text in file_names[1:-1]:
        file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/" + str(year) + "/" + str(year) + "_txt/" + str(text) + ".txt")
    # return file_paths

    file_names_transformed = []
    for file in file_names[1:]:
        try:
            info = re.findall(r'\w*', file)
            new_name = info[0] + '-' + info[2]
            file_names_transformed.append(new_name)
        except:
            pass
    
    final_names = []
    for file in file_names_transformed:
    	try:
    		new_name = re.sub(r'[_][a-zA-z0-9][a-zA-z0-9][a-zA-z0-9][a-zA-z0-9]','', file)
    		final_names.append(new_name)
    	except:
    		pass
    return final_names

def text(year, stemmed):  
    # gets the file names in a folder on the desktop; please note that it has been hard coded and should be changed to match your system
    file_names = []
    for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/' + str(year)):
        file_names.append(file)

    # gets the file path names; please note that it has been hard coded and should be changed to match your system
    file_paths = []
    for text in file_names[1:]:
        file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/" + str(year) + "/" + str(year) + "_txt/" + str(text) + ".txt")

    # transforms the file names 
    file_names_transformed = []
    for file in file_names[1:]:
        try:
            info = re.findall(r'\w*', file)
            new_name = info[0] + '-' + info[2]
            file_names_transformed.append(new_name)
        except:
            pass

    # gets the text for each file by opening in read mode
    for item in range(len(file_paths)):
        try:
            with open(file_paths[item], "r") as text:
                file_names_transformed[item] = text.read()
        except:
            pass
    
    kennedy_speech = []
    for file in file_names_transformed:
        new_text = re.sub(r'\n+\d{1,2}','', file)
        new_text_1 = re.sub(r'\b(cid:173)\b','', new_text)
        # deletes all matching substrings of \n\n
        new_text_2 = re.sub(r'\n+\n','', new_text_1)
        # deletes the miscellaneous 'x0c' marker 
        new_text_3 = re.sub(r'\x0c','', new_text_2)
        # deletes the substrings from the text
        new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
        new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
        new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)
        new_text_7 = re.sub(r'\d{2}\s\d{2}[a-z][a-z]\s\bStreet[,]\s[N][.][W][.][,]\s\bSuite\s\d{3}\s\bAlderson\s\bReporting\s\bCompany\s[-]\d{3}[-]\bFOR[-]\bDEPO\s\bWashington[,]\s\bDC\s\d{5}\sPage\s\d{0,4}', '', new_text_6)
        new_text_8 = re.sub(r'\d{2}\s\d{2}[a-z][a-z]\s\bStreet[,]\s[N][W]\s\bSuite\s\d{3}\s\bAlderson\s\bReporting\s\bCompany\s[-]\d{3}[-]\bFOR[-]\bDEPO\s\bWashington[,]\s\bDC\s\d{5}\s', '', new_text_7)
        new_text_9 = re.sub(r'\d{2}\s\d{2}[a-z][a-z]\s\bStreet\s[N][W][,]\s\bSuite\s\d{3}\s\bPage\s\d{0,3}\s\bAlderson\s\bReporting\s\bCompany\s\bWashington[,]\s\bDC\s\d{5}\s\d{0,3}', '', new_text_8)
        new_text_10 = re.sub(r'\d{2}\s\d{2}[a-z][a-z]\s\bStreet\s[N][W][,]\s\bSuite\s\d{3}\s\s\bAlderson\s\bReporting\s\bCompany\s\bWashington[,]\s\bDC\s\d{5}','', new_text_9)
        new_text_11 = re.sub(r'\d{2}\s\d{2}[a-z][a-z]\s\bStreet\s[N][W][,]\s\bSuite\s\d{3}\s\s\bAlderson\s\bReporting\s\bCompany\s\bWashington[,]\s\bDC\s\d{5}\s\d{4}','', new_text_10)
        new_text_12 = re.sub(r'\d{2}\s\d{2}[a-z][a-z]\s\bStreet[,]\s[N][W][,]\s\bSuite\s\d{3}\s\bAlderson\s\bReporting\s\bCompany\s[-]\d{3}[-]\bFOR[-]\bDEPO\s\bWashington[,]\s\bDC\s\d{5}\s\d{0,5}','', new_text_11)
        new_text_13 = re.sub(r'\d{2}\s\d{2}[a-z][a-z]\s\bStreet[,]\s[N][W][,]\s\bSuite\s\d{3}\s\bAlderson\s\bReporting\s\bCompany[,]\s\bInc[.][-]\d{3}[-]\bFOR[-]\bDEPO\s\bWashington[,]\s\bDC\s\d{6}','', new_text_12)
        new_text_14 = re.sub(r'\d{2}\s\d{2}[a-z][a-z]\s\bStreet[,]\s[N][W]\s\bSuite\s\d{3}\s\bAlderson\s\bReporting\s\bCompany\s\d{1}[-]\bFOR[-]\bDEPO\s\bWashington[,]\s\bDC\s\d{5}\s\d{0,4}','', new_text_13)
        new_text_15 = re.sub(r'\d{2}\s\d{2}[a-z][a-z]\s\bStreet[,]\s[N][W]\s\bSuite\s\d{3}\s\bPage\s\d{0,3}\s\bAlderson\s\bReporting\s\bCompany\s\bWashington[,]\s\bDC\s\d{5}\s\ba34bda65-a6f1-42d8-83ec-09cfb6aa8dc6\s\d{1}','', new_text_14)
        new_text_16 = re.sub(r'Alderson Reporting CompanyOfficial', '', new_text_15)
        new_text_17 = re.sub(r'\bAldersonReportingCompany\s\bOfficial\s\s', '', new_text_16)
        new_text_18 = re.sub(r'\bAldersonReportingCompany\s\d{0,10}\s*\bOfficial', '', new_text_17)

        # gets kennedy's actual speech; 'JUSTICE' has been omitted for ease of parsing 
        kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_18)
        kennedy_speech.append(kennedy)
	
    # open stopwords and add "KENNEDY:" to them
    stop_words = set(stopwords.words('english'))
    stop_words.add('KENNEDY')
    stop_words.add(':')

    filtered_sentences = []
    for case in kennedy_speech:
    	cases = []
    	for x in case:
    		# removes punctuation from the text 
    		tokenizer = RegexpTokenizer(r'\w+')
    		words = tokenizer.tokenize(x)
    		cases.append([w for w in words if not w in stop_words])
    	filtered_sentences.append(cases)

    flat_case_speech = []
    for case in filtered_sentences:
    	flat_case_speech.append([item for sublist in case for item in sublist])

	
    if stemmed == 'stemmed':
	    # stem the words using snowball stemmer
        ss = SnowballStemmer('english')
        stemmed_all = []
        for item in flat_case_speech:
            stemmed_some = []
            for word in item:
                stemmed_some.append(ss.stem(word))
            stemmed_all.append(stemmed_some)
        return stemmed_all
    else:
    	return flat_case_speech


# function to calculate if justice voted for petitioner or respondent
# 0 = vote for petitioner 
# 1 = vote for respondent 
def pet_v_resp(row):
    if row['majority'] == float(2): 
        if row['partyWinning'] == float(1):
            return 0
        else:
            return 1 
    if row['majority'] == float(1):
        if row['partyWinning'] == float(1):
            return 1 
        else:
            return 0 

def get_df(year, stemmed):
    # create the dataframe
    speech = pd.Series(text(year, stemmed))
    df = pd.DataFrame({'docket':case_names(year), 'speech':speech})
    # takes speech column and removes the list element 
    df['speech'] = df['speech'].apply(lambda x: ', '.join(x))

    word_count = []
    for row in range(len(df)):
    	word_count.append(len(df.speech.iloc[row]))

    wc = pd.Series(word_count)
    df = pd.concat((df, wc.rename('word_count')), axis=1)

    os.chdir('/Users/collinlyou/Downloads/')
    df_1 = pd.read_csv('SCDB_2017_01_justiceCentered_Docket.csv', encoding = "ISO-8859-1")
    df_1 = df_1[(df_1['term'] >= 2004) & (df_1['justiceName'] == 'AMKennedy')]
    df = df.merge(df_1, on=['docket', 'docket'], how='left')

    # add a new column for who won Kennedy's vote 
    df['winner'] = df.apply(pet_v_resp, axis=1)
    
    return df
    
def total_word_count(year):
	all_text = []
	for x in range(len(get_df(year))):
		for word_list in get_df(year).iloc[x]:
			all_text.append(word_list)

	flat_list = []
	for sublist in all_text:
		if sublist is None:
			pass
		else:
			for item in sublist:
				flat_list.append(item)			
	cnt = Counter()
	for word in flat_list:
		cnt[word] +=1
	return cnt

def get_all_df(stemmed):
    if stemmed == 'stemmed': 
        all_df = pd.concat([get_df(2004, stemmed='stemmed'), get_df(2005, stemmed='stemmed'), get_df(2006, stemmed='stemmed'), get_df(2007, stemmed='stemmed'), get_df(2008, stemmed='stemmed'), get_df(2009, stemmed='stemmed'), get_df(2010, stemmed='stemmed'), get_df(2011, stemmed='stemmed'), get_df(2012, stemmed='stemmed'), get_df(2015, stemmed='stemmed'), get_df(2016, stemmed='stemmed')])
        return all_df
    if stemmed != 'stemmed':
        all_df = pd.concat([get_df(2004, stemmed='notstemmed'), get_df(2005, stemmed='notstemmed'), get_df(2006, stemmed='notstemmed'), get_df(2007, stemmed='notstemmed'), get_df(2008, stemmed='notstemmed'), get_df(2009, stemmed='notstemmed'), get_df(2010, stemmed='notstemmed'), get_df(2011, stemmed='notstemmed'), get_df(2012, stemmed='notstemmed'), get_df(2015, stemmed='notstemmed'), get_df(2016, stemmed='notstemmed')])
        return all_df
