import pandas as pd
from tkinter import *
from tkinter import messagebox
import re
import string
from sklearn.feature_extraction.text  import CountVectorizer
from sklearn.feature_extraction import stop_words
from sklearn.naive_bayes import MultinomialNB
def clean_text(test):
    #change to lower case
    test=test.lower()
    #remove punctuations
    punc=string.punctuation
    test=re.sub(f"[{punc}]",'',test)
    return test

def feature_vectors(clean_text_list):
    fv= cv.fit_transform(clean_text_list)
    return fv

def submit():
      test=entry_user.get()
      test=clean_text(test)
      test_vector=cv.transform([test])
      pred=gnb.predict(test_vector.todense())
      if(pred[0]==1):
            label=Label(root,text="THANK YOU \n LIKED",font=('Book Antiqua' ,25 ,'bold'),bg='teal',fg='white')
            label.place(x=400,y=450)
      else:
            label=Label(root,text="THANK YOU \n NOT LIKED",font=('Book Antiqua' ,25 ,'bold'),bg='teal',fg='white')
            label.place(x=400,y=450)
            


df=pd.read_csv('Restaurant_Reviews.txt',delimiter="\t")

df['Review']=df.Review.apply(clean_text)

sw=list(stop_words.ENGLISH_STOP_WORDS)
sw.remove('not')
sw.remove('cannot')
sw.remove("no")
sw.remove('cant')

cv=CountVectorizer(stop_words=sw,ngram_range=(2,3))
X=feature_vectors(df.Review)
y=df.Liked

gnb=MultinomialNB()
gnb.fit(X.todense(),y)

root=Tk()

root.state("zoomed")
root.configure(bg="white") 
root.resizable(width=False,height=False) 
root.title("MY PROJECT") 

lbl_title=Label(root,text="Review Analysis",font=('Book Antiqua' ,25 ,'bold'),bg='white',fg='dark olive green')
lbl_title.place(x=550,y=10)

lbl_user=Label(root,text="Enter Your Review",font=('cambria',20),bg='white', fg='dark olive green')
lbl_user.place(x=200,y=220)

entry_user=Entry(root,font=('',20), bg='white',bd=5) 
entry_user.place(x=450,y=220)

btn_rst=Button(root,command=submit,text="submit",font=('',20),bd=5)
btn_rst.place(x=450,y=350)

root.mainloop()
