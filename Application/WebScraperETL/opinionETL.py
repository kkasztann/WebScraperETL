import requests
from .models import Opinion 
from bs4 import BeautifulSoup  
import re

#global product id variable
productID = ''

def opinionRunETL(productID):
    print ("Starting ETL")
    loadOpinions(transformOpinions(extractOpinions(generateOpinionLinkList(productID))))

#return string with pure extracted opinions html
def opinionRunE(prodID):
    global productID
    productID = prodID
    return extractOpinions(generateOpinionLinkList(productID))   

#return transformed list of arrays
def opinionRunT(extractedData):
    return transformOpinions(extractedData) 

#inject data into the database
def opinionRunL(transformedData):
    loadOpinions(transformedData)   


#---------------------CORE---------------------
#Ceneo can show only 10 opinions per site, this function returl list containing all url's
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
    return listOfOpinionLinks            

def extractOpinions(listOfOpinionLinks):
    print('Extracting Opinions')
    htmlToParse = ''
    for link in listOfOpinionLinks:
        print(link, ' scrapped')
        htmlToParse += requests.get(link).text
        
    soup = BeautifulSoup(htmlToParse, 'html.parser')  
    scrapedHTML = soup.find_all('li', attrs={'class':'review-box js_product-review'})
    return scrapedHTML

def transformOpinions(scrapedHTML):
    print('Transforming data')
    opinions = []

    for result in scrapedHTML:  
        username = result.find('div', attrs={'class':'reviewer-name-line'}).text.lstrip()
        productRating = result.find('span', attrs={'class':'review-score-count'}).text
        productReview = result.find('p', attrs={'class':'product-review-body'}).text
        opinions.append((productID, username, productRating, productReview))
    return opinions

def loadOpinions(opinions):
    print('Loading data')
    for opinion in opinions:  
        print(opinion[0], ' loaded')
        o = Opinion(productID=opinion[0], username=opinion[1], productRating=opinion[2], productReview=opinion[3])
        o.save()