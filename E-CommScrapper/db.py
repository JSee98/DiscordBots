import requests


def queryDB(channel_id, url):
    endpoint = url

    queryPath = "https://api.notion.com/v1/databases/DATA-BASE-ID/query"
    payload = {"page_size": 100,
               "filter": {"and": [
                   {

                       "property": "Channel_ID",

                       "title": {"equals": channel_id}
                   },
                   {
                       "property": "URL",

                       "title": {"equals": endpoint}
                   }
               ]

               }
               }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer <SECRET-HERE>"
    }

    response = requests.request(
        "POST", queryPath, json=payload, headers=headers)

    responseJSON = response.json()
    res = responseJSON['results'][0]
    entry_id = res['id']
    properties = res['properties']
    product_id = properties['Product']['rich_text'][0]['plain_text']

    return product_id, entry_id


def insertDB(channel_id, url, product_id, domain):
    endpoint = url

    updatePath = "https://api.notion.com/v1/pages"

    payload = {
        "parent": {
            "database_id": "DATA-BASE-ID"
        },
        "properties": {
            "Channel_ID": {
                "title": [
                    {
                        "text": {
                            "content": channel_id
                        }
                    }
                ]
            },
            "Product": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": product_id
                        }
                    }
                ]
            },
            "URL": {
                "url": endpoint
            },
            "Domain": {
                "url": domain
            }
        }
    }

    headers = {

        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer API-SECRET-HERE"
    }

    response = requests.request(
        "POST", updatePath, json=payload, headers=headers)


def deleteEntry(channel_id, url):

    queryResponse = queryDB(channel_id, url)

    deletePath = "https://api.notion.com/v1/blocks/"+queryResponse[1]
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Authorization": "Bearer API-SECRET-HERE"
    }
    response = requests.request("DELETE", deletePath, headers=headers)


def queryAll():
    queryPath = "https://api.notion.com/v1/databases/DATA-BASE-ID/query"
    payload = {"page_size": 500}
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer API-SECRET-HERE"
    }

    response = requests.request(
        "POST", queryPath, json=payload, headers=headers)

    responseJSON = response.json()
    uuid_lis = []
    channel_lis = []
    endpoint_lis = []
    prod_id_lis = []
    domain_lis = []

    for res in responseJSON['results']:

        entry_id = res['id']
        uuid_lis.append(entry_id)

        properties = res['properties']

        product_id = properties['Product']['rich_text'][0]['plain_text']

        prod_id_lis.append(product_id)

        endpoint = properties['URL']['url']
        endpoint_lis.append(endpoint)

        channel_id = properties['Channel_ID']['title'][0]['plain_text']
        channel_lis.append(channel_id)

        domain = properties['Domain']['url']
        domain_lis.append(domain)

    return uuid_lis, channel_lis, endpoint_lis, prod_id_lis, domain_lis


def updateEntry(page_id, product_id):

    updatePath = 'https://api.notion.com/v1/pages/'+page_id

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer API-SECRET-HERE"
    }

    payload = {
        "properties": {
            "Product": {"rich_text": [{"text": {"content": product_id}}]}
        }
    }

    response = requests.request(
        "PATCH", updatePath, headers=headers, json=payload)
