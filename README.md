Trading Bot (Binance Futures Testnet)

Overview:

CLI-based trading bot to place MARKET and LIMIT orders.

Setup:

pip install -r requirements.txt

Run:

MARKET:
py cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

LIMIT:
py cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 30000

Logs:

Logs are stored in trading_bot.log