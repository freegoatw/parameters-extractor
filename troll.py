#translate text using google translate
def translate(text, source, target):
    import requests
    url = 'https://translate.google.com/translate_a/single'
    params = {
        'client': 'gtx',
        'sl': source,
        'tl': target,
        'dt': 't',
        'q': text
    }
    response = requests.get(url, params=params)
    return response.json()[0][0][0]

q = translate("show me your boobs", "en", "fr")

print(q)