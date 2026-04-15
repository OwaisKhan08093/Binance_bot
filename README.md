# 🚀 Binance Futures Testnet Trading Bot

A Python-based CLI application to place **MARKET** and **LIMIT** orders on Binance Futures Testnet (USDT-M).
This project demonstrates API integration, input validation, structured code design, logging, and error handling.

---

## 📌 Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* CLI-based input using argparse
* Input validation and error handling
* Logging of API requests, responses, and errors
* Clean and modular project structure

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py        # Binance client setup
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input validation
│   └── logging_config.py
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clonehttps://github.com/OwaisKhan08093/Binance_bot
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Configure API Keys

Create a `.env` file in the root directory:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret
```

> ⚠️ Use **Binance Futures Testnet API keys** from
> https://testnet.binancefuture.com

---

## ▶️ Usage

### ✅ MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### ✅ LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 71000
```

> 💡 Note:
> SELL LIMIT → price must be above market
> BUY LIMIT → price must be below market

---

## 📊 Sample Output

```
📊 ORDER SUMMARY
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001
Price: None

✅ ORDER RESPONSE
Order ID: 12345678
Status: FILLED
Executed Qty: 0.001
Avg Price: 64000
```

---

## 📝 Logging

Logs are stored in:

```
trading.log
```

Includes:

* API request details
* API responses
* Errors and exceptions

---

## ⚠️ Assumptions

* Uses Binance Futures Testnet (demo environment)
* Only USDT-M futures supported
* Valid quantity and price inputs
* Market conditions affect LIMIT order execution

---

## ❌ Common Errors & Fixes

* **Invalid API Key (-2015)**
  → Use Futures Testnet API keys

* **Timestamp error (-1021)**
  → Sync system time or use timestamp offset

* **Limit price error (-4024)**
  → Follow correct BUY/SELL limit rules

---

## ⭐ Bonus (Optional Feature)

* Support for STOP MARKET order *(if implemented)*

---

## 👨‍💻 Author

Owais Khan

---

## 📬 Notes

* Successfully tested with MARKET and LIMIT orders
* Includes logging and validation
* Designed with modular architecture
* Ready for evaluation

---
