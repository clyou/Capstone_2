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




# def case_names_2004():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2004'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2004/2004_txt/" + str(text) + ".txt")

#     file_names_transformed_2004 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2004.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2004

# def text_2004():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2004'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2004/2004_txt/" + str(text) + ".txt")

#     file_names_transformed_2004 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2004.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2004[item] = text.read()
#         except:
#             pass

#     kennedy_speech = []
#     for x in file_names_transformed_2004:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech


# def case_names_2005():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2005'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2005/2005_txt/" + str(text) + ".txt")

#     file_names_transformed_2005 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2005.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2005

# def text_2005():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2005'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2005/2005_txt/" + str(text) + ".txt")

#     file_names_transformed_2005 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2005.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2005[item] = text.read()
#         except:
#             pass

#     kennedy_speech = []
#     for x in file_names_transformed_2005:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech

# def case_names_2006():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2006'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2006/2006_txt/" + str(text) + ".txt")

#     file_names_transformed_2006 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2006.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2006

# def text_2006():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2006'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2006/2006_txt/" + str(text) + ".txt")

#     file_names_transformed_2006 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2006.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2006[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2006:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech


# def case_names_2007():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2007'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2007/2007_txt/" + str(text) + ".txt")

#     file_names_transformed_2007 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2007.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2007

# def text_2007():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2007'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2007/2007_txt/" + str(text) + ".txt")

#     file_names_transformed_2007 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2007.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2007[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2007:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech

# def case_names_2008():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2008'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2008/2008_txt/" + str(text) + ".txt")

#     file_names_transformed_2008 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2008.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2008

# def text_2008():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2008'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2008/2008_txt/" + str(text) + ".txt")

#     file_names_transformed_2008 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2008.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2008[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2008:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech


# def case_names_2009():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2009'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2009/2009_txt/" + str(text) + ".txt")

#     file_names_transformed_2009 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2009.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2009

# def text_2009():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2009'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2009/2009_txt/" + str(text) + ".txt")

#     file_names_transformed_2009 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2009.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2009[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2009:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech


# def case_names_2010():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2010'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2010/2010_txt/" + str(text) + ".txt")

#     file_names_transformed_2010 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2010.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2010

# def text_2010():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2010'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2010/2010_txt/" + str(text) + ".txt")

#     file_names_transformed_2010 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2010.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2010[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2010:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech


# def case_names_2011():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2011'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2011/2011_txt/" + str(text) + ".txt")

#     file_names_transformed_2011 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2011.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2011

# def text_2011():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2011'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2011/2011_txt/" + str(text) + ".txt")

#     file_names_transformed_2011 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2011.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2011[item] = text.read()
#         except:
#             pass

#     kennedy_speech = []
#     for x in file_names_transformed_2011:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech



# def case_names_2012():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2012'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2012/2012_txt/" + str(text) + ".txt")

#     file_names_transformed_2012 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2012.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2012

# def text_2012():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2012'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2012/2012_txt/" + str(text) + ".txt")

#     file_names_transformed_2012 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2012.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2012[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2012:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech



# def case_names_2013():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2013'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2013/2013_txt/" + str(text) + ".txt")

#     file_names_transformed_2013 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2013.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2013

# def text_2013():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2013'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2013/2013_txt/" + str(text) + ".txt")

#     file_names_transformed_2013 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2013.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2013[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2013:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech



# def case_names_2014():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2014'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2014/2014_txt/" + str(text) + ".txt")

#     file_names_transformed_2014 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2014.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2014

# def text_2014():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2014'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2014/2014_txt/" + str(text) + ".txt")

#     file_names_transformed_2014 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2014.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2014[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2014:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech



# def case_names_2015():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2015'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2015/2015_txt/" + str(text) + ".txt")

#     file_names_transformed_2015 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2015.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2015


# def text_2015():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2015'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2015/2015_txt/" + str(text) + ".txt")

#     file_names_transformed_2015 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2015.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2015[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2015:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech



# def case_names_2016():
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2016'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2016/2016_txt/" + str(text) + ".txt")

#     file_names_transformed_2016 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + '-' + info[2]
#             file_names_transformed_2016.append(new_name)
#         except:
#             pass
#     return file_names_transformed_2016


# def text_2016():  
#     file_names = []
#     for file in os.listdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2016'):
#         file_names.append(file)

#     file_paths = []
#     for text in file_names[1:]:
#         file_paths.append("/Users/collinlyou/Desktop/Supreme_Court_Cases/2016/2016_txt/" + str(text) + ".txt")

#     file_names_transformed_2016 = []
#     for file in file_names[1:]:
#         try:
#             info = re.findall(r'\w*', file)
#             new_name = info[0] + info[2]
#             file_names_transformed_2016.append(new_name)
#         except:
#             pass

#     for item in range(len(file_paths)):
#         try:
#             with open(file_paths[item], "r") as text:
#                 file_names_transformed_2016[item] = text.read()
#         except:
#             pass
    
#     kennedy_speech = []
#     for x in file_names_transformed_2016:
#         new_text = re.sub(r'\n+\d{1,2}','', x)
#         new_text_0 = re.sub(r'11 14th Street NW, Suite 400  Alderson Reporting Company Washington, DC 20005','', new_text)

#         # deletes all '\' 
#         new_text_1 = re.sub(r'\b(cid:173)\b','', new_text_0)
#         # deletes all matching substrings of \n\n
#         new_text_2 = re.sub(r'\n+\n','', new_text_1)
#         # deletes the miscellaneous 'x0c' marker 
#         new_text_3 = re.sub(r'\x0c','', new_text_2)
#         # deletes the substrings from the 
#         new_text_4 = re.sub(r'Alderson Reporting Company 1Official - Subject to Final Review', '', new_text_3)
#         new_text_5 = re.sub(r'Alderson Reporting Company Official - Subject to Final Review', '', new_text_4)
#         new_text_6 = re.sub(r'Alderson Reporting CompanyOfficial - Subject to Final Review', '', new_text_5)

#         # eases the nomenclature of the wording by removing 'Chief' from Chief Justice Roberts' Title for parsing 
#         new_text_7 = re.sub(r'CHIEF', '', new_text_6)
#         kennedy = re.findall(r'KENNEDY\b.*?(?=[A-Z]{2,3}[.]|[A-Z]{7}|\n [A-Z]{2,3}[.]|\n [A-Z]{7})', new_text_7)
#         kennedy_speech.append(kennedy)

#     return kennedy_speech