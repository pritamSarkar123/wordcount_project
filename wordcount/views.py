from django.http import HttpResponse,request
from django.shortcuts import render
import operator

def home(request):
    return render(request,'homepage.html')
def about(request):
    return render(request,'aboutpage.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split(' ')
    worddictionary={}
    for word in wordlist:
        if word in worddictionary.keys():
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sortedWorddictionary=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'countpage.html',{'fulltext':fulltext,'sortedWorddictionary':sortedWorddictionary})