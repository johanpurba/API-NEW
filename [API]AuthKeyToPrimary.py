import requests, json

def AuthKey2Primary():
    apiKey = input("Your API key: ")
    authKey = input("Your AuthKey: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/authkey2primary?authkey="+authKey,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


AuthKey2Primary()
