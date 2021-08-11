import math

sen=open("idf.txt", "r").read().split('\n')
N = len(sen)
u_words= set()

#Word count dictionary for each sentence
wc_list=[]
for s in sen:
    wc=dict()
    for word in s.split():
        u_words.add(word)
        if word in wc:
            wc[word]+=1
        else:
            wc[word]=1
    wc_list.append(wc)
print("unique words:")
print(u_words)
print("List of word count dictionaries")
print(wc_list)

#IDF Calculation
idf=dict()
for word in u_words:
    n=0
    for s in sen:
        if word in s:
            n+=1
    idf[word]= math.log(N/n)

#TF and TF-IDF calculation 
tf_list=[]
tfidf_list=[]
for wc in wc_list:
    tf={}
    tfidf={}
    for word in wc:
        tf[word]=wc[word]/sum(wc.values())
        tfidf[word]=tf[word]*idf[word]
    tf_list.append(tf)
    tfidf_list.append(tfidf)
print("List of Term Frequency Dictionaries:")
print(tf_list) 
print("List of TF-IDF Dictionaries")
print(tfidf_list)