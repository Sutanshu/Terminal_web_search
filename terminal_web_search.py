from googlesearch import search
import sys,webbrowser

inp = input("What do you want to search? ")
number_req=int(input("How many searches do you want to look up? "))
searches=[]
split_urls= []
def searching(number,input1):
    for asearch in search(query = inp,tld='com',lang='en',num=1,start = number,stop=1,pause=1):
        searches.append(asearch)
for i in range(number_req):
    searching(i,inp)
for i in searches:
    if 'www' not in i:
        split_urls.append(i.split('//')[1].split('.')[0])
    else:
        split_urls.append(i.split('.')[1])
print("You now have a choice of {} from this list: ".format(inp))
for i,j in enumerate(split_urls,1):
        print(i,j)
x= int(input("Enter your desired choice now: "))
webbrowser.open(searches[x-1])
