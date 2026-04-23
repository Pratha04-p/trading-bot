import argparse
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger

API_KEY = "demo_key"
API_SECRET = "demo_secret"


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Simple Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n Order Request Summary:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")

        client = BinanceClient(API_KEY, API_SECRET).get_client()

        order = place_order(client, symbol, side, order_type, quantity, price)

        print("\n Order Response:")
        print(order)

    except Exception as e:
        print(f"\n Error: {e}")


if __name__ == "__main__":
    main()