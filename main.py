import MetaTrader5 as mt5

mt5.initialize()

symbolsTotal = mt5.symbols_total()

if symbolsTotal > 0:
    print("Total de Simbolos:", symbolsTotal)
else:
    print("Simbolos não encontradops")

symbols = mt5.symbols_get()

count = 0

for s in symbols:
    count += 1
    print("{}. {}".format(count, s.name))
    if count == 100: break
print()

mt5.shutdown()

