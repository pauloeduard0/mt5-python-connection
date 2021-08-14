import MetaTrader5 as mt5

mt5.initialize()

symbol = "EURUSD"

mt5.symbol_select(symbol, True)

lot = 1
price = mt5.symbol_info_tick(symbol).ask
deviation = 2

request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": float(lot),
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": price - 0.05,
    "tp": price + 0.05,
    "deviation": deviation,
    "magic": 123456,
    "comment": "my first robot",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN
}

result = mt5.order_send(request)

print(result)

print(price)

