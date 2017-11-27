import glob
import os 

os.chdir('/Users/collinlyou/Desktop/Supreme_Court_Cases/2016_txt')

files = []
for file in glob.glob('*.txt'):
	files.append(file)

new_text_file = open('combined.txt', 'w')

with new_text_file as outfile:
	for fname in files:
		with open(fname) as infile:
			for line in infile:
				outfile.write(line) 

new_text_file.close()

# with open("2010_Cases_All.txt", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())