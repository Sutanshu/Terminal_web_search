from googlesearch import search
import sys,webbrowser

inp = input("What do you want to search? ")
while True:
    try:
        number_req=int(input("How many searches do you want to look up? "))
        break
    except ValueError:
        print ("Please enter a number")
        continue
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
while True:
    try:
        choice = int(input("Enter your desired choice now: "))
        if choice > number_req:
            print("Please make sure the number is within the range requested")
            continue
        break
    except ValueError:
        print("Please enter a number, and ensure it is less than or equal to the number of searches you require")
        continue
webbrowser.open(searches[choice-1])
