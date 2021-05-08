'''
Simple Python script to convert raw Messenger JSON data to a text file containing only raw text from messages of a specific sender.
(Cleans out links, images, and non-text data for pre-processing)

Python 3.9
'''

import json
import re
import nltk
from nltk.corpus import stopwords

# In case of any corpus are missing
# download all-nltk
nltk.download()

stop_words = stopwords.words("english")

# Preproc function borrowed from: https://towardsdatascience.com/cleaning-text-data-with-python-b69b47b97b76
def text_preproc(x):
  #x = x.lower()
  #x = ' '.join([word for word in x.split(' ') if word not in stop_words])
  x = x.encode('ascii', 'ignore').decode()
  x = re.sub(r'https*\S+', ' ', x)
  x = re.sub(r'@\S+', ' ', x)
  #x = re.sub(r'#\S+', ' ', x)
  #x = re.sub(r'\'\w+', '', x)
  #x = re.sub('[%s]' % re.escape(string.punctuation), ' ', x)
  #x = re.sub(r'\w*\d+\w*', '', x)
  #x = re.sub(r'\s{2,}', ' ', x)
  return x

# Empty list to hold collected text to upload
collected_text = []

###### SPECIFY SENDER AND AMOUNT OF FILES TO COLLECT FROM HERE ######
Name = ''
file_amount = 8

# Do the collection and preprocessing for the JSON message files as per the username
for n in range(1,(file_amount+1)):
  with open('### enter path to JSON message files here ###/message_' + str(n) + '.json') as f:
    data = json.load(f)

  for messages in data['messages']:
    # For each message, save and preprocess text according to the name of sender
    if messages['sender_name'] == Name:
      try:
        text = messages['content']
        if text_preproc(text) != ' ' or text_preproc(text) != '':
          # Preprocess message text content
          print(text_preproc(text))
          collected_text.append(text_preproc(text) + '\n')
      # On the occasion that there is no text in the message throw KeyError exception
      except KeyError:
        print('###### CONTENT MISSING ######')

# Save data to a text file according to sender name
with open('### txt save path ###' + Name + '.txt', 'w') as f:
    f.writelines(collected_text)

'''with open('/Users/kurti/PycharmProjects/quoteGenerator/Data/' + Name + '.csv', 'w') as f:
  csv_writer = csv.writer(f)
  for val in collected_text:
    csv_writer.writerow([val])'''

'''# Purge empty rows in csv file
with open('/Users/kurti/PycharmProjects/quoteGenerator/Data/' + Name + '_raw.csv') as in_file:
  with open('/Users/kurti/PycharmProjects/quoteGenerator/Data/' + Name + '.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    for row in csv.reader(in_file):
      if row:
        writer.writerow(row)'''