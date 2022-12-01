
from cmath import isnan
import csv
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np
from LSTM import LSTM_Predict
class Stock():
   def __init__(self, ticker, close, date):
       self.ticker = ticker
       self.close  = close
       self.date   = date
       self.tenDayAverage, self.twentyDayAverage = self.dayAverages()
       self.up, self.down = self.averageChanges()

   def dayAverages(self):
       tenList = []
       twyList = []

       if len(self.close) < 20: return None, None
       for i in range(10): tenList.append(self.close[i])
       for i in range(10, 20): tenList.append(mean(self.close[i-10:i]))
       for i in range(20): twyList.append(self.close[i])

       for i in range(20, len(self.close)):
           tenList.append(mean(self.close[i-10:i]))
           twyList.append(mean(self.close[i-20:i]))

       self.close = self.close[20:]
       self.date = self.date[20:]
       tenList = tenList[20:]
       twyList = twyList[20:]
       return tenList, twyList

   def averageChanges(self):
       aChanges = []
       for i in range(len(self.tenDayAverage)):
           if self.tenDayAverage[i] >= self.twentyDayAverage[i]:
               aChanges.append(1)
           else:
               aChanges.append(-1)
       i = 0
       upSignal = []
       downSignal = []
       while i < len(aChanges):
           if aChanges[i] == 1:
               upSignal.append(self.close[i])
               downSignal.append(np.NAN)
           else:
               upSignal.append(np.NAN)
               downSignal.append(self.close[i])
           j = i + 1
           while j < len(aChanges) and aChanges[i] == aChanges[j]:
               upSignal.append(np.NAN)
               downSignal.append(np.NAN)
               j += 1
           i = j
       return upSignal, downSignal
  
   def movingAvgProfit(self):
       b, s = [], []
       stIndex = 0
       for i in range(len(self.up)):
           if not isnan(self.up[i]): break
           stIndex += 1
       for i in range(stIndex, len(self.up)):
           if not isnan(self.up[i]):
               b.append(self.up[i])
           if not isnan(self.down[i]):
               s.append(self.down[i])
       profit = 0
       bs, ss = 0, 0
       numTrades = 0
       if len(s) < len(b):
           profit += (self.close[-1] - b[-1])
           bs += b[-1]
           ss += self.close[-1]
       lossNum = 0
       for i in range(len(s)):
           profit += (s[i] - b[i])
           print(s[i])
           print(b[i])
           numTrades += 1
           bs += b[i]
           ss += s[i]
           if s[i] - b[i] < 0:
               lossNum += 1
       pp = 0
       if bs != 0:
           pp = ((ss - bs) / bs) * 100
       # print('MA loss num = ', lossNum)
       return profit, pp, numTrades, bs, ss, lossNum
  
   def lstmMovingAverageProfit(self, days = None):
       buys = []
       sumb = 0
       sums = 0
       profit = 0
       count = 0
       countYear = 0
       if not days: days = len(self.tenDayAverage)
       bYear, sYear, yProfit = 0, 0, []
       numTrades = 0
       lossNum = 0
       for i in range(days):
           countYear += 1
           print('iteration ', i)
           while len(buys) > 0 and buys[0] < self.close[i]:
               profit += (self.close[i] - buys[0])
               numTrades += 1
               sums += self.close[i]
               sYear += self.close[i]
               buys.pop(0)
           if self.tenDayAverage[i] > self.twentyDayAverage[i] and i - 30 >= 0:
               count += 1
           if self.tenDayAverage[i] > self.twentyDayAverage[i] and i - 30 >= 0 and count % 7 == 0:
               lstm_res = LSTM_Predict(self.close[i-30:i], 7)
               val = np.mean(lstm_res)
               del lstm_res
               if self.close[i] < val:
                   for _ in range(7): buys.append(self.close[i])
                   sumb += self.close[i] * 7
                   bYear += self.close[i] * 7
                   numTrades += 1
                   buys.sort()
           # Year has passed check profit %
           if countYear % 255 == 0:
               yp = 0
               if bYear != 0: yp = ((sYear - bYear)/ bYear) * 100
               yProfit.append(yp)
       # sell it all at last close if there are more buys even at a loss :(
       if len(buys) > 0:
           for b in buys:
               profit += (self.close[days - 1] - b)
               sums += self.close[days - 1]
               numTrades += 1
               lossNum += 1
       pp = 0
       if sumb != 0: pp = ((sums - sumb)/ sumb) * 100
       # print('LSTM loss num = ', lossNum)
       return profit, numTrades, pp, yProfit, sumb, sums, lossNum

def readData(filename):
   with open(filename, 'r') as f:
       inp = csv.reader(f, delimiter=',', quotechar='|')
       date, close = [], []
       count = 0
       for r in inp:
           if count == 0:
               count = 1
               continue
           date.append(r[0])
           close.append(float(r[4]))
      
       ticker = filename.split('.csv')[0].split('./' + folder + '/')[1]
       return Stock(ticker, close, date)
