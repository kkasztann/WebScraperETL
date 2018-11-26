import requests
from .models import Opinion 
from bs4 import BeautifulSoup  
import re

#Ceneo can show only 10 opinions per site, this list store all url's
listOfOpinionLinks = []
#pure html of scraped opinions
scrapedHTML = ''
#transformed html to opinion objects list
opinions = []

def runETL(productID):
    print ("Starting ETL")
    generateOpinionList(productID)
    extract()
    transform()
    load()


def generateOpinionList(prodID):
    baseLink = 'https://www.ceneo.pl/' + prodID
    htmlToParse = requests.get(baseLink).text
    soup = BeautifulSoup(htmlToParse, 'html.parser')  
    opinionsTag = soup.find('span', attrs={'itemprop':'reviewCount'})

    if not opinionsTag:
        print("List is empty, there are no opinions")
    else:
        numberOfOpinions = int(opinionsTag.text)
        numberOfSites = (numberOfOpinions // 10) + 1
        print ('There are:', numberOfOpinions, ' opinions and ', numberOfSites, ' sites')

        for iterate in range(numberOfSites):
            if iterate == 0:
                listOfOpinionLinks.append((baseLink + '#tab=reviews'))
            else:
                listOfOpinionLinks.append((baseLink + '/opinie-' + str(iterate+1)))

def extract():
    print('Extracting data')
    htmlToParse = ''
    for link in listOfOpinionLinks:
        print(link, ' scrapped')
        htmlToParse += requests.get(link).text

    soup = BeautifulSoup(htmlToParse, 'html.parser')  
    global scrapedHTML
    scrapedHTML = soup.find_all('li', attrs={'class':'review-box js_product-review'})

    print('Number of results scrapped: ' , len(scrapedHTML))

def transform():
    print('Transforming data')

    for result in scrapedHTML:  
        username = result.find('div', attrs={'class':'reviewer-name-line'}).text.lstrip()
        print('Username: ', username)
        productRating = result.find('span', attrs={'class':'review-score-count'}).text
        print('Rate: ', productRating)
        productReview = result.find('p', attrs={'class':'product-review-body'}).text
        print('Review: ', productReview)
        opinions.append((username, productRating, productReview))
        print('----------------------------------------------------------------')

def load():
    print('Loading data')
    for opinion in opinions:  
        print(opinion[0], ' loaded')
        o = Opinion(username=opinion[0], productRating=opinion[1], productReview=opinion[2])
        o.save()