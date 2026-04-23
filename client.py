from binance.client import Client

class BinanceClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(
            api_key=api_key,
            api_secret=api_secret,
            testnet=True
        )

    def get_client(self):
        return self.client