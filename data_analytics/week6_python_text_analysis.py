#!/usr/bin/env python
# coding: utf-8

# # Text Analysis of Two Alexandre Dumas Novels

# For this project I chose to compare "The Count of Monte Cristo" and "The Man in the Iron Mask" by Alexandre Dumas. I chose two books by the same autor because I was interested to see if there would be unusual words that were in both books. I expected that many common words would be the same and names would be different, but I hoped there would be a few more unusual words that were present in both books.

# First I set up the Python environment to be very similar to the exercises.

# In[2]:


import operator
import string
import re
from collections import defaultdict
from nltk.corpus import stopwords


# In[4]:


filepath = 'C:\\Users\\Meso\\Documents\\GitHub\\classwork\\data_analytics\\'
monte_cristo = open(filepath + 'cleaned_monte_cristo.txt', 'rb')


# I started first with "The Count of Monte Cristo" using the file handle 'monte_cristo'. I was not interested in stopwords, so I set it up to exclude them right away.

# In[5]:


monte_words = defaultdict(int)
punc = string.punctuation
stops = stopwords.words('english')
stops = set(stops)


# I found that some stopwords still got through because a quotation mark was left on the front end of the word. I used regular expressions to fix the few words I found.

# In[6]:


for line in monte_cristo:
    cln_line = re.sub('[' + punc + ']', '', line.decode('utf-8'))
    cln_line = cln_line.lower()
    spl_line = cln_line.strip().split()
    for word in spl_line:
        word = re.sub('\Wi', 'i', word)
        word = re.sub('\Wyou|you\W', 'you', word)
        word = re.sub('\Wand', 'and', word)
        word = re.sub('\Wwhat', 'what', word)
        word = re.sub('\Wthat', 'that', word)
        word = re.sub('\Wthe', 'the', word)
        word = re.sub('\Woh', 'oh', word)
        word = re.sub('\Wyes', 'yes', word)
        word = re.sub('me\W', 'me', word)
        word = re.sub('\Wbut', 'but', word)
        if word in stops: continue
        monte_words.setdefault(word, 0)
        monte_words[word] += 1
sorted_cristo = sorted(monte_words.items(), key = operator.itemgetter(1), reverse = True)
print('Number of distinct words: ', len(sorted_cristo))


# I then moved on to "The Man in the Iron Mask".

# In[7]:


iron_mask = open(filepath + 'cleaned_iron_mask.txt', 'rb')
iron_words = defaultdict(int)


# In[8]:


for line in iron_mask:
    cln_line = re.sub('[' + punc + ']', '', line.decode('utf-8'))
    cln_line = cln_line.lower()
    spl_line = cln_line.strip().split()
    for word in spl_line:
        word = re.sub('\Wi', 'i', word)
        word = re.sub('\Wyou|you\W', 'you', word)
        word = re.sub('\Wand', 'and', word)
        word = re.sub('\Wwhat', 'what', word)
        word = re.sub('\Wthat', 'that', word)
        word = re.sub('\Wthe', 'the', word)
        word = re.sub('\Woh', 'oh', word)
        word = re.sub('\Wyes', 'yes', word)
        word = re.sub('me\W', 'me', word)
        word = re.sub('\Wbut', 'but', word)
        if word in stops: continue
        iron_words.setdefault(word, 0)
        iron_words[word] += 1
sorted_iron = sorted(iron_words.items(), key = operator.itemgetter(1), reverse = True)
print('Number of distinct words: ', len(sorted_iron))


# To compare the top words in each book I wrote an input statement so I could easily change the number of top words I would look at.

# In[9]:


top_num = int(input('Enter the top number of words you would like to view: '))
print('Top %s words in The Man in the Iron Mask:' % top_num)
for pair in range(top_num):
    print(sorted_iron[pair])
print('Top %s words in The Count of Monte Cristo:' % top_num)
for pair in range(top_num):
    print(sorted_cristo[pair])


# To better compare the words, I looked at the top words in a book and filtered them based on if they were in the other book.

# In[10]:


print('Words in the top %s of The Man in the Iron Mask that are also anywhere in The Count of Monte Cristo:' % top_num)
for num in range(top_num):
    if sorted_iron[num][0] in monte_words.keys():
        print(sorted_iron[num][0])


# In[11]:


print('Words in the top %s of The Count of Monte Cristo that are also anywhere in The Man in the Iron Mask:' % top_num)
for num in range(top_num):
    if sorted_cristo[num][0] in iron_words.keys():
        print(sorted_cristo[num][0])


# To see more what the comarison of top words used was I created new dictionaries of the top 50 words of each book.

# In[12]:


iron_top_50 = {}
for num in range(50):
    iron_top_50[sorted_iron[num][0]] = sorted_iron[num][1]
cristo_top_50 = {}
for num in range(50):
    cristo_top_50[sorted_cristo[num][0]] = sorted_iron[num][1] 


# In[13]:


print('Top words of The Man in the Iron Mask that are also top words of The Count of Monte Cristo:')
for num in range(top_num):
    if sorted_iron[num][0] in cristo_top_50.keys():
        print(sorted_iron[num][0])
print('Top words of The Count of Monte Cristo that are also top words of The Man in the Iron Mask:')
for num in range(top_num):
    if sorted_cristo[num][0] in iron_top_50.keys():
        print(sorted_cristo[num][0])


# This showed that both books probably contain a lot of dialog with 'said' being the top word for each book. With 'one' and 'man' being on both lists it can be speculated that individual actors have a large presence in both books. It is interesting that by looking at the top words of both books, the words 'king' and 'count' are removed. This shows the difference in subjects of the two books. 
