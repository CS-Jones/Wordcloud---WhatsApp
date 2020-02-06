import numpy as np
import pandas as pd
import os
from pandas import DataFrame
import re 
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

currdir = os.path.dirname(__file__)


def startsWithDateTime(s):
    pattern = '^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)(\d{2}|\d{4}), ([0-9][0-9]):([0-9][0-9]) -'
    result = re.match(pattern, s)
    if result:
        return True
    return False
	
def startsWithAuthor(s):
    patterns = [
        '([\w]+):',                        # First Name
        '([\w]+[\s]+[\w]+):',              # First Name + Last Name

    ]
    pattern = '^' + '|'.join(patterns)
    result = re.match(pattern, s)
    if result:
        return True
    return False
	
def getDataPoint(line):
    # line = 18/06/17, 22:47 - ['Name', 'Message']
    
    splitLine = line.split(' - ') # splitLine = ['18/06/17, 22:47']
    
    dateTime = splitLine[0] # dateTime = '18/06/17, 22:47'
    
    date, time = dateTime.split(', ') # date = '18/06/17'; time = '22:47'
    
    message = ' '.join(splitLine[1:]) # message = 'Message?'
    
    if startsWithAuthor(message): # True
        splitMessage = message.split(': ') # splitMessage = ['Name', 'Message']
        author = splitMessage[0] # author = 'Name'
        message = ' '.join(splitMessage[1:]) # message = 'Message?'
    else:
        author = None
    return date, time, author, message
	
parsedData = [] # List to keep track of data so it can be used by a Pandas dataframe
conversationPath = '' #Path to exported Whatsapp messages
with open(conversationPath, encoding="utf-8") as fp:
    fp.readline() # Skipping first line of the file (usually contains information about end-to-end encryption)
        
    messageBuffer = [] # Buffer to capture intermediate output for multi-line messages
    date, time, author = None, None, None # Intermediate variables to keep track of the current message being processed
    
    while True:
        line = fp.readline() 
        if not line: # Stop reading further if end of file has been reached
            break
        line = line.strip() # Guarding against erroneous leading and trailing whitespaces
        if startsWithDateTime(line): # If a line starts with a Date Time pattern, then this indicates the beginning of a new message
            if len(messageBuffer) > 0: # Check if the message buffer contains characters from previous iterations
                parsedData.append([date, time, author, ' '.join(messageBuffer)]) # Save the tokens from the previous message in parsedData
            messageBuffer.clear() # Clear the message buffer so that it can be used for the next message
            date, time, author, message = getDataPoint(line) # Identify and extract tokens from the line
            messageBuffer.append(message) # Append message to buffer
        else:
            messageBuffer.append(line) # If a line doesn't start with a Date Time pattern, then it is part of a multi-line message. So, just append to buffer
			
df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Author', 'Message'])
df.head()
df.describe()	

text = " ".join(Message for Message in df.Message) 

stopwords = ["image omitted", "sorry", "image", "omitted", "deleted message", "hate" ] + list(STOPWORDS)




image_coloring = np.array(Image.open(path.join(currdir, "tor.png"))) #image you want to use to base wordcloud off 


wc = WordCloud(background_color="white", max_words=6000, mask=image_coloring,
               stopwords=stopwords, max_font_size=50)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(image_coloring)

# show
fig, axes = plt.subplots(1, 3)
axes[0].imshow(wc, interpolation="bilinear")
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
axes[2].imshow(image_coloring, cmap=plt.cm.gray, interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()
plt.show()





# store to file
wc.to_file(path.join(currdir, "torcloud.png"))