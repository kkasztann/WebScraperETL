import requests
from .models import Product 
from bs4 import BeautifulSoup  
import re

#global product id variable
productID = ''

def productRunETL(productID):
    print ("Starting ETL")
    loadProduct(transformProduct(extractProduct(productID)))

#return string with pure extracted opinions html
def productRunE(prodID):
    global productID
    productID = prodID
    return extractProduct(productID)  

#return transformed list of arrays
def productRunT(extractedData):
    return transformProduct(extractedData)

#inject data into the database
def productRunL(transformedData):
    loadProduct(transformedData)   


#---------------------CORE---------------------
#return array with 2 fields containing important data
def extractProduct(productID):
    print('Extracting Product')
    baseLink = 'https://www.ceneo.pl/' + productID + '#tab=spec'
    htmlToParse = requests.get(baseLink).text
    soup = BeautifulSoup(htmlToParse, 'html.parser')  
    productName = soup.find('h1', attrs={'class':'product-name'}).text
    productData = soup.findAll('div', attrs={'class':'specs-group'})
    return ((productName,productData))

def transformProduct(scrapedProductHTML):
    print('Transforming Product')
    productName = scrapedProductHTML[0]
    productData = scrapedProductHTML[1]
    productParameters = []  

    for data in productData:  
        allTableRows = data.findAll('tr')
        for tr in allTableRows:
            parameter = tr.find('th').get_text(strip=True)
            value = tr.find('li').get_text(strip=True)
            if len(parameter) < 80 and len(value) <80:
                productParameters.append((productName,productID,parameter,value))
    return productParameters

def loadProduct(productParameters):
    print('Loading Product data')
    for parameter in productParameters:  
        print(parameter[0], parameter[1], parameter[2], parameter[3], 'loaded')
        p = Product(productName=parameter[0], productID=parameter[1], parameter=parameter[2], value=parameter[3])
        p.save()