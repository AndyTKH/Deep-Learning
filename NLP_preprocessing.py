import json
import os
import os.path
import utils

text = []
path_to_json = '/Users/AndyTan/data/'

# search folder names from the "/Users/AndyTan/data/" directory
# multiple target folder names that begin with '2018'
for folder_name in [folder for folder in os.listdir(path_to_json) if folder.startswith('2018')]:
    # search for json file names from each folder
    for file_name in [file for file in os.listdir(path_to_json + folder_name) if file.endswith('.json')]:
        # open each json file and only append the "text" data
        with open(path_to_json + folder_name + '/' + file_name) as access_json:
            read_content = json.load(access_json)
            # append all json 'text' data into text list
            text.append(read_content['text'])

# save the text list as fin_news in local directory
save_path = '/Users/AndyTan/Desktop'
completeName = os.path.join(save_path, "fin_news" +".txt")
new_file = open(completeName, "w")
new_file.write(text)
new_file.close()

# read in the text file
with open('/Users/AndyTan/Desktop/fin_news.txt') as f:
    text = f.read()

# preprocess and get list of words
words = utils.preprocess(text)
print("Raw words:", words[0:200])

# remove punctuation words
punctuation = ['<PERIOD>','<COMMA>','<QUOTATION_MARK>','<COLON>','\\n','\\na',"'",'|','<SEMICOLON>','<RIGHT_PAREN>',
              '<LEFT_PAREN>','-','/','<EXCLAMATION_MARK>','<QUESTION_MARK>', '"','<HYPHENS>']

cleaned_words = []

# only append words that are not in the punctuation list 
for char in words:
    if char not in punctuation:
        cleaned_words.append(char)

words = cleaned_words
print("Cleaned words:", words[0:200])

# print some stats about this word data
print("Total words in text: {}".format(len(words)))

# length of non-duplicated words
print("Unique words: {}".format(len(set(words))))

# create two dictionaries to convert words to integers, and integers to words
# most frequent words will be given integer 0, and the next most frequent is 1, and so on
vocab_to_int, int_to_vocab = utils.create_lookup_tables(words)
