from bs4 import BeautifulSoup
import requests
import json
import re


def getLatest(url):
    endpoint = url.split('?')
    endpoint = endpoint[0].split('/')
    URL = 'https://www.funko.com/api/craft/pages/'+endpoint[-1]
    postPath = 'https://www.funko.com/api/search/template'
    page = requests.get(URL)

    headDict = page.json()

    collectionId = headDict['blades'][2]['content'][0]['content']['id']

    payload = json.dumps({
        "type": "shop",
        "sort": {
            "createdAt": "desc"
        },
        "collection": str(collectionId),
        "pageCount": 24,
        "page": "1"
    })
    headers = {
        'Content-Type': 'application/json',
    }

    postResponse = requests.request(
        "POST", postPath, headers=headers, data=payload)
    postResponse = postResponse.json()
    newest = postResponse['hits'][0]

    rawDescription = newest['description']
    processedDescription = re.sub('<.*?>', '', rawDescription)

    details_url = "https://www.funko.com/shop/details/"+newest["handle"]

    return (newest['title'], newest["price"], newest["media"][0]['src'], processedDescription, details_url, newest['uid'])


def getLatestTarget():

    URL = 'https://www.target.com/b/funko/-/N-4ynjc?lnk=snav_rd_funko_pop'

    page = requests.get(URL)

    cookies = page.cookies

    visitor_id = None

    for c in cookies:
        if c.name == 'visitorId':
            visitor_id = c.value

    headers = {
        "Accept": "application/json",
    }

    soup = BeautifulSoup(page.text, "html.parser")

    scripts = soup.find_all("script")

    apiKey = None

    for data in scripts:

        match = re.search(r"apiKey.*?}", data.getText())
        if (match != None):
            unprocessed = match.group()
            processed = unprocessed.split(',')[0].split(':')[
                1].replace('\\', '')
            apiKey = processed[1:-1]
            break

    if (apiKey != None and visitor_id != None):
        postPath = ('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key='
                    + apiKey
                    + '&brand_id=4ynjc&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&offset=0&page=/b/4ynjc&platform=desktop&pricing_store_id=1002&sort_by=newest&store_ids=1002,1871,1043,1001,1970&useragent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0&visitor_id='
                    + visitor_id)
        postResponse = requests.request("GET", postPath, headers=headers)
        postResponse = postResponse.json()

        latest = postResponse["data"]["search"]["products"][0]

        image = latest['item']['enrichment']['images']['primary_image_url']

        title = latest['item']['product_description']['title']

        price = latest['price']['current_retail']
        url = latest['item']['enrichment']["buy_url"]
        return (title, price, image, url)


def get_latest_hot(url):
    url = url
    rule = "/?srule=sortingNewArrival&start=0&sz=60"
    if(url.count(rule) > 0):
        pass
    else:
        url = url+rule
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    re = requests.get(url, headers=headers)

    soup = BeautifulSoup(re.content, "html.parser")

    li = soup.find_all("li", class_="grid-tile")
    print(li[0])
    latest_item = li[0]
    title = latest_item.find(
        "div", class_="product-tile").find("a", class_="name-link").contents[0].strip()
    img = latest_item.find("div", class_="product-tile").find("div",
                                                              class_="product-image").find("a", class_="thumb-link").find("source")["srcset"].split(",")[0].split(" ")[0]
    price = latest_item.find(
        "div", class_="product-tile").find("span", {"title": "Sale Price"}).contents[0]
    url = latest_item.find(
        "div", class_="product-tile")["data-monetate-producturl"]

    return(title, img, price, url)
