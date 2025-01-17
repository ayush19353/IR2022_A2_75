# -*- coding: utf-8 -*-
"""IR_Assignment2_Q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BqVwiXdUQZCV4KxbmkuccRqD5Jmve9zZ

Question 1 - [40 Points] Scoring and Term-Weighting
"""

from google.colab.patches import cv2_imshow
import csv
import cv2
from google.colab import files
!pip install nltk
!pip install pandas
!pip install numpy
!pip install ipython-autotime
from natsort import natsorted
import string
import matplotlib.pyplot as plt
import numpy as np
from google.colab.patches import cv2_imshow
import pandas as pd
from google.colab import files
import numpy as np
import os
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
import nltk
from nltk.tokenize import RegexpTokenizer
from collections import defaultdict
import string
import re#import re
from collections import defaultdict
import operator
import numpy as np
import pandas as pd
from collections import Counter
import math

# import these modules
from nltk.stem import WordNetLemmatizer
 


import nltk
nltk.download('stopwords')
nltk.download('punkt')
import nltk
nltk.download('wordnet')

nltk.download('stopwords')



# function to read the files
def read_file(filename):
    with open(filename,encoding= 'utf-8',errors='ignore') as f:
        stuff = f.read()
    f.close
   # stuff = remove_header_footer(stuff) 
    return stuff
    
# function to convert numbers to strings
def convert_Numbers(final_string):
    final_string=re.sub(r'0',' zero ',final_string)
    final_string=re.sub(r'1',' one ',final_string)    
    final_string=re.sub(r'2',' two ',final_string)
    final_string=re.sub(r'3',' three ',final_string)
    final_string=re.sub(r'4',' four ',final_string)
    final_string=re.sub(r'5',' five ',final_string)
    final_string=re.sub(r'6',' six ',final_string)
    final_string=re.sub(r'7',' seven ',final_string)
    final_string=re.sub(r'8',' eight ',final_string)
    final_string=re.sub(r'9',' nine ',final_string)

    return final_string

# To remove apostrophe
def apost(final_string):
    final_string=re.sub(r"'","",final_string)
    return final_string
# function to remove punctuation
def remove_punc(final_token):
    trans_tab= str.maketrans('', '', '\t')# Removing punctuations. # Q2 part a part iv)
    final_token = [word1.translate(trans_tab) for word1 in final_token]
    name_punc = (string.punctuation).replace("'", "")
    trans_table = str.maketrans('', '', name_punc)
    wordss= [word.translate(trans_table) for word in final_token]
    final_token = [str for str in wordss if str]
    return final_token

# function to remove header and footer from the input sentence
def remove_header_footer(final_string):
    new_final_string = ""
    tokens = final_string.split('\n\n')
 
    # Remove tokens[0] and tokens[-1]
    for token in tokens[0: ]:
        new_final_string += token+" "
    return new_final_string.lower()  # first convert to lower


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

# defining the path and then storing the names of all the files in a list named as names_file
path = "/content/drive/MyDrive/Humor,Hist,Media,Food"
os.chdir(path)
names_file = natsorted(os.listdir(path))

# Function to perform complete preprocessing
def preprocessing(final_string):
    final_string=final_string.lower();
  #  lemmatizer = WordNetLemmatizer() # lemmatization

#    final_string = convert_Numbers(final_string) # converting numbers
  #  final_string= apost(final_string)
  #  final_string = remove_single_characters(final_string)
    #stemmer= PorterStemmer()     

 
    #final_string=re.sub(r'\d+','',final_string)#removing numbers
    tokenizer = TweetTokenizer()      # tokenisation
    token_l = tokenizer.tokenize(final_string)

    token_lz=[]
    for w in token_l:
   #     w=lemmatizer.lemmatize(w)
        token_lz.append(w)
    stop_words = set(stopwords.words("english")) # stop words 
    token_lz = [word for word in token_lz if word not in stop_words]# removing stop words
   # token_l= [np.char.replace(word, "'", "") for word in token_l]
                                                          # Remove punctuation marks
    token_lz =remove_punc(token_lz)
   # tab= str.maketrans('', '', '\t')
    #token_lz = [word.translate(tab) for word in token_lz]
   # pu = (string.punctuation).replace("'", "")
    #trable = str.maketrans('', '', pu)
    #stripped_words = [word.translate(trable) for word in token_lz]
    #token_lz = [str for str in stripped_words if str]
 
    # Change to low\ercase.
   # token_lz=[word.lower() for word in token_lz]
    while("" in token_lz) :# removing blank spaces
      token_lz.remove("")
    while(" " in token_lz) :
      token_lz.remove(" ")
  #  for i in token_list:
   #   i= remove_apostrophe(i)

 

    return token_lz, set(token_lz)

z1,z2=preprocessing('LION STOOD THOUGHTFULLY FOR A MOMENT')
print(z1)
print(z2)

from collections import defaultdict
import nltk
from nltk.tokenize import RegexpTokenizer

import string
import re
    # list containing all the doc ids
document_names=[]
document_content=[]
document_content1=[]
# iterating over every file
for fileName in names_file:
  # print(fileName)
  stuff=read_file(fileName)
  try:
  #  stuff=stuff.lower() # convering the text to lower cases 
 #   tokenizer=RegexpTokenizer(r'\w+')
    # print(stuff)
    temping1,temp2=preprocessing(stuff) # processing the text
    document_names.append(fileName)
    document_content.append(temping1)
    document_content1.append(temp2)
    # print(temping1)
  except:
    a = 0
#     print(fileName)
# print(len(token_file))
#pri

"""Jaccard Coefficient [20 points]"""

def jacc_coeff(a,b,c11,d_name,e): # using & for intersection of the set of words in a file with the set of words in query
# using | for union of the set of words in a file with the set of words in query

    cc=0
    jac_values1={} # stores the jac coefficient of each file 
    print(type(e))
    for k in a:
      jac_values1[d_name[cc]] = len(set(k) & set(b))/len(set(k) | set(b))
      cc=cc+1  
    
    for i in Counter(jac_values1).most_common(5): # top 5 documents
      print("document name,  jac_value-----",i[1],i[0])





query=input("Enter the query")
if (len(query)==0):
    print("Empty")
else:
    query=query.lower()
    query,query1=preprocessing(query)
    #print(query)
    #query=remove_stopwords(query)query=lemmatization_func(query)
    print(query)
    jacc_coeff(document_content,query,query1,document_names,document_content1)



"""**TF-IDF Matrix [20 points]**

1. Use the same data given in assignment 1 and carry out the same preprocessing steps as mentioned
before.
"""

import math
def calcuate_idf(doc_names,doc_content):

    df_vals={}

    for i in range(0,len(doc_names)):
     token_list=doc_content[i] 
     for j in token_list:
      if j not in df_vals.keys():
        #print(type(j))
        #
        df_vals[j]={1}
      else:
        df_vals[j].add(i)
    for k in df_vals:
      df_vals[k]=len(df_vals[k]) # df values for each word contains the number of documents containng the word
    
 #   print(df_vals)
    print(df_vals)
    idf_vals= {}

    for i in df_vals:
      idf_vals[i]= math.log(len(doc_names)/(df_vals[i]+1)) # by formula caclulating the idf for each word
    return idf_vals



def count_tot(ans): # counting each word frequency in the doc, and returning the document
   dictt={}
   for zz in ans:
       if not zz in dictt:       
          dictt[zz] = ans.count(zz)
   return dictt

"""6. Use all 5 weighting schemes for term frequency calculation and report the TF-IDF score and
results for each scheme separately
"""



from collections import Counter
def calculate_tf(doc_names,doc_content):

  tf_mat={} # log normalization
  tf_mat_term_freq={} # term frequency
  tf_mat_bin={} # binary
  tf_mat_norm={} #double normalization
  tf_mat_raw={} # raw  count
  for i in range(0,len(doc_names)):
    tf_cont=[]
    tf_max=[]
    token_list=doc_content[i] 
    ff=len(token_list)
    az=count_tot(token_list) # counting each word frequency in the doc, and returning the document
    leng=len(token_list)
    for j in token_list:
        tf_cont.append(az[j])
    max1=float(max(tf_cont))
    
    for j in token_list:
      if j not in tf_mat.keys():
        tf_mat[i,j]=math.log(az[j]+1) # log normalization
        tf_mat_term_freq[i,j]=(float)(az[j])/(float)(ff) # term frequncey
        tf_mat_bin[i,j]= (1 if az[j]>0 else 0) # binary
        tf_mat_norm[i,j]= 0.5*((float)(az[j])/(float)(max1))+0.5  # dobule normalization
        tf_mat_raw[i,j]= az[j] # raw
      else:
        tf_mat[i,j].append(math.log(az[j]+1))
        tf_mat_term_freq[i,j].append(az[j]/ff)
        tf_mat_bin[i,j].append(1 if az[j]>0 else 0)
        tf_mat_norm[i,j].append(0.5*(az[j]/max1)+0.5)  # dobule normalization
        tf_mat_raw[i,j].append(az[j])
  return tf_mat,tf_mat_term_freq,tf_mat_bin,tf_mat_norm,tf_mat_raw
    #print(len(az))

"""2. Build the matrix of size no. of document x vocab size.
3. Fill the tf idf values in the matrix of each word of the vocab.
"""

# part 2 Q1


def tf_idf(doc_names,doc_content, query,k=5):

  leng= len(doc_names)
  print(leng)
  print(len(doc_content))
  idf_vals=calcuate_idf(doc_names,doc_content) # idf-values of every word
 # print(idf_vals)
  #print(len(idf_vals))
  #print(leng)
  #print(len(doc_content))
  tf_val_log_norm,tf_val_term_freq,tf_val_bin, tf_val_norm_double,tfVal_raw=calculate_tf(doc_names,doc_content) # tf values- matrix form 

    
  return tf_val_log_norm,tf_val_term_freq,tf_val_bin, tf_val_norm_double,tfVal_raw,idf_vals

query="american dream"
query,query1=preprocessing(query)  # preprocessinng the query

 
tf_val_log_norm,tf_val_term_freq,tf_val_bin, tf_val_norm_double,tfVal_raw,rr1=tf_idf(document_names,document_content,query,5)





"""4. Make the query vector of size vocab

5. Compute the TF-IDF score for the query using the TF-IDF matrix. Report the top 5 relevant
documents based on the score.
"""

print("LOG NORMALIZATION")
print(query) # log_normalization
scores_final={}
ss={}
for i in range(0,len(document_names)):
    l=0
    for j in query:
      if (i,j) in tf_val_log_norm.keys():
       
       l=l+(rr1.get(j,"0")*(tf_val_log_norm.get((i,j),"0"))) # by formula to calculate tf-idf, i.e, tf*idf
       ss[i]=(i,j)
      # print(l)

    scores_final[i]=(l)
print(ss)
print(scores_final) # matrix of size no. of document x vocab size.
print("Retrieved docs")
temp=sorted(scores_final.items(), key=operator.itemgetter(1),reverse=True)
temp1=(temp[:5])
    #print(temp1)
    #print((temp1[0]))
retrieved_doc_name=[]
tt=[]
for i in range(len(temp1)):
        docid=temp1[i][0]
        retrieved_doc_name.append(document_names[docid])
        tt.append(temp1[i][1])
print(retrieved_doc_name) # retreived document names
print(tt)

print("TERM FREQUENCY")
print(query) # term frequency
scores_final={}
ss={}
for i in range(0,len(document_names)):
    l=0
    for j in query:
      if (i,j) in tf_val_term_freq.keys():
       
       l=l+(rr1.get(j,"0")*(tf_val_term_freq.get((i,j),"0")))
       ss[i]=(i,j)
      # print(l)

    scores_final[i]=(l)
print(ss)
print(scores_final)
print("retrieved documents")
temp=sorted(scores_final.items(), key=operator.itemgetter(1),reverse=True)
temp1=(temp[:5])
    #print(temp1)
    #print((temp1[0]))
retrieved_doc_name=[]
tt=[]
for i in range(len(temp1)):
        docid=temp1[i][0]
        retrieved_doc_name.append(document_names[docid])
        tt.append(temp1[i][1])
print(retrieved_doc_name)
print(tt)

print("BINARY")
print(query) # binary
scores_final={}
ss={}
for i in range(0,len(document_names)):
    l=0
    for j in query:
      if (i,j) in tf_val_bin.keys():
       
       l=l+(rr1.get(j,"0")*(tf_val_bin.get((i,j),"0")))
       ss[i]=(i,j)
      # print(l)

    scores_final[i]=(l)
print(ss)
print(scores_final)
print("RETRIEVED DOCUMENt")
temp=sorted(scores_final.items(), key=operator.itemgetter(1),reverse=True)
temp1=(temp[:5])
    #print(temp1)
    #print((temp1[0]))
retrieved_doc_name=[]
tt=[]
for i in range(len(temp1)):
        docid=temp1[i][0]
        retrieved_doc_name.append(document_names[docid])
        tt.append(temp1[i][1])
print(retrieved_doc_name)
print(tt)

print("DOUBLE NORMALIZATION")
print(query) # dobule normalziaton
scores_final={}
ss={}
for i in range(0,len(document_names)):
    l=0
    for j in query:
      if (i,j) in tf_val_norm_double.keys():
       
       l=l+(rr1.get(j,"0")*(tf_val_norm_double.get((i,j),"0")))
       ss[i]=(i,j)
      # print(l)

    scores_final[i]=(l)
print(ss)
print(scores_final)
print("RETRIEVED DOCUMENTS")
temp=sorted(scores_final.items(), key=operator.itemgetter(1),reverse=True)
temp1=(temp[:5])
    #print(temp1)
    #print((temp1[0]))
retrieved_doc_name=[]
tt=[]
for i in range(len(temp1)):
        docid=temp1[i][0]
        retrieved_doc_name.append(document_names[docid])
        tt.append(temp1[i][1])
print(retrieved_doc_name)
print(tt)

print("RAW COUNT")

print(query) # raw
scores_final={}
ss={}
for i in range(0,len(document_names)):
    l=0
    for j in query:
      if (i,j) in tfVal_raw.keys():
       
       l=l+(rr1.get(j,"0")*(tfVal_raw.get((i,j),"0")))
       ss[i]=(i,j)
      # print(l)

    scores_final[i]=(l)
print(ss)
print(scores_final)
print("RETRIEVED DOCUMENTs")
temp=sorted(scores_final.items(), key=operator.itemgetter(1),reverse=True)
temp1=(temp[:5])
    #print(temp1)
    #print((temp1[0]))
tt=[]
retrieved_doc_name=[]
for i in range(len(temp1)):
        docid=temp1[i][0]
        retrieved_doc_name.append(document_names[docid])
        tt.append(temp1[i][1])
print(retrieved_doc_name)
print(tt)

from google.colab import drive
drive.mount('/content/drive')





