import ex28
import requests
import json

def imageParams(imageFileName):
    params = {}
    params["action"] = "query"
    params["titles"] = "File:" + imageFileName
    params["format"] = "json"
    params["prop"] = "imageinfo"
    params["iiprop"] = "url"
    return params

if __name__ == "__main__":
    apiUrl = "https://www.mediawiki.org/w/api.php"

    baseInfo = ex28.getResult()
    params = imageParams(baseInfo["国旗画像"])

    res = requests.get(apiUrl, params=params)
    response = json.loads(res.text)
#    print(response)

    imageUrl = response["query"]["pages"]["-1"]["imageinfo"][0]["url"]
    print(imageUrl)
