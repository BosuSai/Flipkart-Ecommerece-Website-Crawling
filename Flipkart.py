import urllib3
from bs4 import BeautifulSoup as b

base_url = "https://www.flipkart.com/search?q="
url_connector = "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
user_request = "cot"

url = base_url + user_request + url_connector
http = urllib3.PoolManager()
r = http.request('GET', url)
soup = b(r.data, "html.parser")
Items_count= 0
Entry_check=0#if words like switerzland are typed then this takes
for s in soup.find_all("div", attrs={"class": "_3liAhj _1R0K0g"}):
    Entry_check=1
    try:  # ztitle
        k=s.find_all("a", attrs={"class": "_2cLu-l"})[0]
     #   k=s.find_all("a", attrs={"class": "_2cLu-duuhQJIAASADFSl"})[0]

        if(k.get('title')!=""):
            print(k.get('title'))
        elif(k.text!=""):
            print(k.text)
        else:
            print("No title found")

    except:
        print("No title found")
    try:  # cost
        price=s.select("[class~=_1vC4OE]")[0]
      #  price=s.select("[class~=_1vCdteuqijdrew4OE]")[0]

        if(price.text!=""):
            print(price.text)
        else:
            print("love")
            print("No price exsist for the product")
    except:
        print("No price exsist for the product")
    try:
        rating = s.select("[class~=hGSR34]")[0]  # Rating
        if(rating.text!=""):
            print(rating.text)
        else:
            print("No Rating exsists for the product")
    except:
            print("No Rating exsists for the product")
    Items_count=Items_count+1
print(Items_count)

if(Entry_check==0):
    print("Please Enter the Valid Product Name")
