import os
import re
import pandas as pd

def case_names(year):
    file_names = []
    for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/' + str(year)):
        file_names.append(file)

    file_paths = []
    for text in file_names[1:]:
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


def text(year):  
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
        # gets kennedy's actual speech; 'JUSTICE' has been omitted for ease of parsing 
        kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_17)
        kennedy_speech.append(kennedy)

    return kennedy_speech


def get_df(year):
    df = pd.DataFrame(text(year))
    df.insert(0, "case_name", case_names(year))
    return df