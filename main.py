import requests

class BitcoinPrice(object):
    def __init__ (self, currency="USD"):
        self.currency = currency
        self.rate = None
        self.description = None
        self.updateTime = None

    def UpdatePrice(self):
        reply = requests.get("http://api.coindesk.com/v1/bpi/currentprice.json").json()
        self.rate = reply["bpi"][self.currency]["rate"]
        self.description = reply["bpi"][self.currency]["description"]
        self.updateTime = reply["time"]["updated"] #UTC Time
