import pyupbit
import pandas
import datetime
import time
access_key = "BDsiUgCPsKUvxfyn0DaVakOT9346k8xuUqSoSCFG"
secret_key = "z62A0ojKNOgUFn1F8cmtiGZzgTdu3LpWNDxSHkhj"
upbit = pyupbit.Upbit(access_key, secret_key)
def rsi(ohlc: pandas.DataFrame, period: int = 11):
    delta = ohlc["close"].diff()
    ups, downs = delta.copy(), delta.copy()
    ups[ups < 0] = 0
    downs[downs > 0] = 0
    AU = ups.ewm(com = period-1, min_periods = period).mean()
    AD = downs.abs().ewm(com = period-1, min_periods = period).mean()
    RS = AU/AD

    return pandas.Series(100 - (100/(1 + RS)), name = "RSI")

coinlist = ['KRW-ADA','KRW-XRP','KRW-BORA','KRW-SXP']
lower28 = []
higher70 = []

for i in range(len(coinlist)):
    lower28.append(False)
    higher70.append(False)

while(True):
    for i in range(len(coinlist)):
        data = pyupbit.get_ohlcv(ticker=coinlist[i], interval="minute15")
        now_rsi = rsi(data, 11).iloc[-1]       
        avg_buy_price = upbit.get_avg_buy_price(coinlist[i])
        avg_buy_price1 = upbit.get_avg_buy_price('KRW-ADA')
        avg_buy_price2 = upbit.get_avg_buy_price('KRW-XRP')
        avg_buy_price3 = upbit.get_avg_buy_price('KRW-BORA')
        avg_buy_price4 = upbit.get_avg_buy_price('KRW-SXP')
        now_price = pyupbit.get_current_price(coinlist[i])
        now_price1 = pyupbit.get_current_price('KRW-ADA')
        now_price2 = pyupbit.get_current_price('KRW-XRP')
        now_price3 = pyupbit.get_current_price('KRW-BORA')
        now_price4 = pyupbit.get_current_price('KRW-SXP')
        print("name: ", coinlist[i])
        print("nowtime: ", datetime.datetime.now())
        print("RSI :", now_rsi)
        print("buy_price:", avg_buy_price)
        print("now_price:", now_price)
        print()
        if now_rsi <= 28 :
            lower28[i] = True
        elif now_rsi >= 33 and lower28[i] == True :
            buy(coinlist[i])
            lower28[i] = False
        elif now_rsi >= 70 and higher70[i] == False :
            if avg_buy_price1 > 0 and ((now_price1 / avg_buy_price1 * 100 <= 97.0) or (now_price1 / avg_buy_price1 * 100 >= 101.62)) :
                amount1 = upbit.get_balance('KRW-ADA')
                cur_price1 = pyupbit.get_current_price('KRW-ADA')
                total1 = amount1 * cur_price1
                if total1 > 5000 :
                    print(upbit.sell_market_order('KRW-ADA', amount1))
                time.sleep(1)
            if avg_buy_price2 > 0 and ((now_price2 / avg_buy_price2 * 100 <= 97.0) or (now_price2 / avg_buy_price2 * 100 >= 101.62)) :
                amount2 = upbit.get_balance('KRW-XRP')
                cur_price2 = pyupbit.get_current_price('KRW-XRP')
                total2 = amount2 * cur_price2
                if total2 > 5000 :
                    print(upbit.sell_market_order('KRW-XRP', amount2))
                time.sleep(1)
            if avg_buy_price3 > 0 and ((now_price3 / avg_buy_price3 * 100 <= 97.0) or (now_price3 / avg_buy_price3 * 100 >= 101.62)) :
                amount3 = upbit.get_balance('KRW-BORA')
                cur_price3 = pyupbit.get_current_price('KRW-BORA')
                total3 = amount3 * cur_price3
                if total3 > 5000 :
                    print(upbit.sell_market_order('KRW-BORA', amount3))
                time.sleep(1)
            if avg_buy_price4 > 0 and ((now_price4 / avg_buy_price4 * 100 <= 97.0) or (now_price4 / avg_buy_price4 * 100 >= 101.62)) :
                amount4 = upbit.get_balance('KRW-SXP')
                cur_price4 = pyupbit.get_current_price('KRW-SXP')
                total4 = amount4 * cur_price4
                if total4 > 5000 :
                    print(upbit.sell_market_order('KRW-SXP', amount4))
                time.sleep(1)
            higher70[i] = True
        elif now_rsi <= 60 :
            if avg_buy_price1 > 0 and ((now_price1 / avg_buy_price1 * 100 <= 97.0) or (now_price1 / avg_buy_price1 * 100 >= 101.62)) :
                amount1 = upbit.get_balance('KRW-ADA')
                cur_price1 = pyupbit.get_current_price('KRW-ADA')
                total1 = amount1 * cur_price1
                if total1 > 5000 :
                    print(upbit.sell_market_order('KRW-ADA', amount1))
                time.sleep(1)
            if avg_buy_price2 > 0 and ((now_price2 / avg_buy_price2 * 100 <= 97.0) or (now_price2 / avg_buy_price2 * 100 >= 101.62)) :
                amount2 = upbit.get_balance('KRW-XRP')
                cur_price2 = pyupbit.get_current_price('KRW-XRP')
                total2 = amount2 * cur_price2
                if total2 > 5000 :
                    print(upbit.sell_market_order('KRW-XRP', amount2))
                time.sleep(1)
            if avg_buy_price3 > 0 and ((now_price3 / avg_buy_price3 * 100 <= 97.0) or (now_price3 / avg_buy_price3 * 100 >= 101.62)) :
                amount3 = upbit.get_balance('KRW-BORA')
                cur_price3 = pyupbit.get_current_price('KRW-BORA')
                total3 = amount3 * cur_price3
                if total3 > 5000 :
                    print(upbit.sell_market_order('KRW-BORA', amount3))
                time.sleep(1)
            if avg_buy_price4 > 0 and ((now_price4 / avg_buy_price4 * 100 <= 97.0) or (now_price4 / avg_buy_price4 * 100 >= 101.62)) :
                amount4 = upbit.get_balance('KRW-SXP')
                cur_price4 = pyupbit.get_current_price('KRW-SXP')
                total4 = amount4 * cur_price4
                if total4 > 5000 :
                    print(upbit.sell_market_order('KRW-SXP', amount4))
                time.sleep(1)
            #if (now_price + 15.0) <= avg_buy_price and avg_buy_price > 0 :
            #    amount = upbit.get_balance('KRW-ZRX') 
             #   cur_price = pyupbit.get_current_price('KRW-ZRX') 
            #    amount = upbit.get_balance('KRW-ZRX')
             #   cur_price = pyupbit.get_current_price('KRW-ZRX')
              #  total = amount * cur_price
               # if total > 5000 : 
               # if total > 5000 :
                #    print(upbit.sell_market_order('KRW-ZRX', amount))
              #  time.sleep(1)
            higher70[i] = False
    time.sleep(0.5)

    def buy(coinlist):
        avg_buy_price1 = upbit.get_avg_buy_price('KRW-ADA')
        avg_buy_price2 = upbit.get_avg_buy_price('KRW-XRP')
        avg_buy_price3 = upbit.get_avg_buy_price('KRW-BORA')
        avg_buy_price4 = upbit.get_avg_buy_price('KRW-SXP')
        krw_balance = upbit.get_balance("KRW")
        krw_price1 = 1000000
        krw_price2 = 100000
        if krw_balance > krw_price2 and avg_buy_price1 == 0:
            upbit.buy_market_order(ticker='KRW-ADA', price=krw_price1)
        if krw_balance > krw_price2 and avg_buy_price2 == 0:
            upbit.buy_market_order(ticker='KRW-XRP', price=krw_price1)
        if krw_balance > krw_price2 and avg_buy_price3 == 0:
            upbit.buy_market_order(ticker='KRW-BORA', price=krw_price1)
        if krw_balance > krw_price2 and avg_buy_price4 == 0:
            upbit.buy_market_order(ticker='KRW-SXP', price=krw_price1)
        if krw_balance > krw_price2 and avg_buy_price1 > 0:
            upbit.buy_market_order(ticker='KRW-ADA', price=krw_price2)
        if krw_balance > krw_price2 and avg_buy_price2 > 0:
            upbit.buy_market_order(ticker='KRW-XRP', price=krw_price2)
        if krw_balance > krw_price2 and avg_buy_price3 > 0:
            upbit.buy_market_order(ticker='KRW-BORA', price=krw_price2)
        if krw_balance > krw_price2 and avg_buy_price4 > 0:
            upbit.buy_market_order(ticker='KRW-SXP', price=krw_price2)
        #krw_price1 = 102980
        #krw_price2 = krw_balance / 4
        #if krw_balance > krw_price1 and avg_buy_price1 == 0:
            #upbit.buy_market_order(ticker=coinlist, price=krw_price2, )
        #if krw_balance > krw_price1 and avg_buy_price1 > 0:
            #upbit.buy_market_order(ticker=coinlist, price=krw_price1, )
        else:
            pass
        return
    def sell(coin):
        amount = upbit.get_balance(coin)
        cur_price = pyupbit.get_current_price(coin)
        total = amount * cur_price 
        if total > 5000 :
            print(upbit.sell_market_order(coin, amount))
        return
