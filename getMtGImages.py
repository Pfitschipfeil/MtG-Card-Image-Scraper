import json
import urllib.request
import os

baseURL = 'http://api.scryfall.com/cards/search?q=set:'

userTypedMTGSetShortName = input("Choose MtG Set Short Name (like grn for Guild of Ravnica): ")
userSetImageSize = input("What image size do you want?(small,large,png)")

mtgSetShortName = userTypedMTGSetShortName #Short name of your desired Magic the Gathering Sets from scryfall.com
imageSize = userSetImageSize #Set your desired image size. Values: small, normal, large, png, art_crop, border_crop

localImagePath = './pictures/' + mtgSetShortName  + '/' #Set image store

def checkLocalPath(): 
    if not os.path.isdir(localImagePath): #Check if image store exist. If not create a Magic Set short name folder within a "pictures" folder in the execution directory
        os.makedirs('pictures/' + mtgSetShortName)

def downloadJSONData(myURL): #Fetch JSON from scryfall.com and store the data in "jsonData" Variable
        with urllib.request.urlopen(myURL) as url:
                jsonData = json.loads(url.read().decode())
                return(jsonData)

        
def getCardImages(jsonData): #Searching and download card images
    card = jsonData['data']
    number = 0
    print('Downloading images...')

    for imageURL in card:
        imageURL = (jsonData['data'][number]['image_uris'][imageSize]) #Searching and define the picture URL
        cardNumber = (jsonData['data'][number]['collector_number']) #Searching and define the card number
        urllib.request.urlretrieve(imageURL, localImagePath + cardNumber + '.jpg')
        number = number + 1

def checkForMoreImages(jsonData): #If there are more JSON pages with cards in the set store the new "url"
    if jsonData['has_more'] is True:
        nextURL = jsonData['next_page']
        return(nextURL)
    else:
        print('No more data - DONE')
        return('')

url = baseURL + mtgSetShortName #Base URL will be created from the variables on top
while url != '': #As long as checkForMoreImages returns an url the loop is running
    jsonData = downloadJSONData(url)
    checkLocalPath()
    getCardImages(jsonData)
    url = checkForMoreImages(jsonData)