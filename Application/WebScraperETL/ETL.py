import requests
from .models import Opinion 
from bs4 import BeautifulSoup  
import re

def runETL(productID):
    print ("Starting ETL")
    load(transform(extract(generateOpinionLinkList(productID))))

def runE(productID):
    return extract(generateOpinionLinkList(productID))   

def runT(extractedData):
    return transform(extractedData) 

def runL(transformedData):
    return load(transformedData)   

def generateOpinionLinkList(prodID):
    baseLink = 'https://www.ceneo.pl/' + prodID
    htmlToParse = requests.get(baseLink).text
    soup = BeautifulSoup(htmlToParse, 'html.parser')  
    opinionsTag = soup.find('span', attrs={'itemprop':'reviewCount'})
    listOfOpinionLinks = []

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
    #Ceneo can show only 10 opinions per site, this list store all url's
    return listOfOpinionLinks            

def extract(listOfOpinionLinks):
    print('Extracting data')
    htmlToParse = ''
    for link in listOfOpinionLinks:
        print(link, ' scrapped')
        htmlToParse += requests.get(link).text

    soup = BeautifulSoup(htmlToParse, 'html.parser')  
    scrapedHTML = soup.find_all('li', attrs={'class':'review-box js_product-review'})

    print('Number of results scrapped: ' , len(scrapedHTML))
    #pure html of scraped opinions
    return scrapedHTML

def transform(scrapedHTML):
    print('Transforming data')
    opinions = []

    for result in scrapedHTML:  
        username = result.find('div', attrs={'class':'reviewer-name-line'}).text.lstrip()
        print('Username: ', username)
        productRating = result.find('span', attrs={'class':'review-score-count'}).text
        print('Rate: ', productRating)
        productReview = result.find('p', attrs={'class':'product-review-body'}).text
        print('Review: ', productReview)
        opinions.append((username, productRating, productReview))
        print('----------------------------------------------------------------')
    #transformed html to opinions list
    return opinions

def load(opinions):
    print('Loading data')
    for opinion in opinions:  
        print(opinion[0], ' loaded')
        o = Opinion(username=opinion[0], productRating=opinion[1], productReview=opinion[2])
        o.save()