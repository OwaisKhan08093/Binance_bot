import logging
import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Price required for LIMIT orders")

    args = parser.parse_args()

    # Normalize input
    args.symbol = args.symbol.upper()
    args.side = args.side.upper()
    args.type = args.type.upper()

    try:
        # Validate input
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        # Log CLI input
        logging.info(f"CLI Input: {args}")

        # Create client
        client = get_client()

        # Place order
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            float(args.quantity),
            float(args.price) if args.price else None,
        )

        # Print output
        print("\n📊 ORDER SUMMARY")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")

        print("\n✅ ORDER RESPONSE")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))

    except Exception as e:
        logging.error(f"CLI Error: {str(e)}")
        print("\n❌ ERROR:", str(e))


if __name__ == "__main__":
    main()
