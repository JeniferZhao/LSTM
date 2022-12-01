LSTM and Moving Average Based Trading Strategy

Introduction

In this project, a trading strategy that uses a Long Short-Term Memory (LSTM) model and a Moving Average (MA) model was implemented. This strategy can be used for both intraday trading and long-term trading. The LSTM model is a type of artificial neural network that is well-suited for time series data. It can learn to identify patterns in data and make predictions based on those patterns. The Moving Average model is a simple statistical model that predicts the future based on past data. The strategy discussed uses the LSTM model to predict the direction of the market (up or down) and the MA model to generate buy and sell signals. The LSTM and MA models are not perfect and will make mistakes, however, when used together, they can give an investor an edge in the market as they can utilize long-term and short-term patterns.

Methodology
Moving Average Based Trading
Moving average (MA) is a technical analysis indicator that helps smooth out price action by filtering out the “noise” from random price fluctuations. It is a lagging indicator that is based on past price data. Moving averages can be used to identify the direction of the trend, as well as support and resistance levels. For example, if the 10-day MA is greater than the 20-day MA, that is a buy signal. 
There are different types of moving averages, but the most common is the simple moving average (SMA) which is calculated by taking the average of a given number of past prices. There are disadvantages to using moving averages. Since it is a lagging indicator, it  will always be behind the price action. This can make it difficult for investors to time their trades. Additionally, moving averages can give false signals in a choppy market. Despite these disadvantages, moving averages can still be a useful tool for technical analysis. They can be used to identify the direction of the trend, as well as potential support and resistance levels.

LSTM
LSTM is a type of artificial neural network that is widely used in deep learning applications. It is well-suited for classifying, processing, and making predictions based on time series data. LSTM networks are composed of LSTM cells, which are similar to traditional artificial neural networks. However, LSTM cells have a memory unit that can remember information for long periods of time. This allows LSTM networks to learn from data that is in a temporal sequence.

LSTM networks have a number of advantages over traditional artificial neural networks. First, they can learn from data that is in a temporal sequence, which is important for many tasks such as speech recognition and language translation. Second, they can remember previous information in long-term memory, which allows them to make better predictions. Finally, LSTM networks are less likely to overfit training data, since they can learn from a larger amount of data. However, LSTM networks also have a number of disadvantages. For instance, they are more complex than traditional artificial neural networks and require more computational resources. Additionally, they are not well-suited to data that is not in a temporal sequence and can be difficult to train, since they require a large amount of data.

The Trading Strategy
The logic of basic strategy is as follows:
●	If the MA indicates a buy signal indicated by whether the 10-day moving average of close prices is greater than the 20-day moving average of close prices and the LSTM predicts an upward trend, a single stock is bought and any previously held stocks are sold provided there’s a profit.
●	If the MA indicates a buy signal and the LSTM predicts a downward trend, no new stock is bought on that day and any previously held stocks are solved provided there’s a profit.
●	If the MA indicates a sell signal, any previously held stocks are sold provided there’s a profit as a selling trend is foreseen by the algorithm.
 

Market Results
The six scenarios analyzed are the 2008 crisis, DotCom Bubble, Crypto, Losses after IPO, Metals ETFs and Stocks, and Meme stocks. The reason why we choose these scenarios is that the volatility of the stocks or portfolios during these periods are higher than normality, which is very similar to asset market during Covid-19 period thus will give possible practical suggestions. Besides, for some scenarios, arbitrage chances during these periods are huge due to misconceptions in the sense of behavioral finance. For each scenario, various stocks discussed below were analyzed over long-term periods. In most cases, the LSTM model coupled with the MA model provides a net gain.

The 2008 Crisis
In this case, the model analyzed the stock prices for Goldman Sachs, Morgan Stanley, JP Morgan, and the S&P 500 Index. In the table below, you can see that a net gain was produced for all except for Morgan Stanley, regardless, an overall net gain was produced at 0.73%. 

	GS	MS	JPM	SPY
MA	0.95%	-0.8%	-1.06%	0.27%
LSTM	1.39%	-1.71%	1.44%	0.62%
NET	1.37%	-1.63%	1.21%	0.60%

The DotCom Bubble
In this case, the model analyzed the stock prices for Amazon, Intel, Cisco, IBM, and eBay. A net portfolio gain of 1.48% was produced.

	AMZN	INTC	CSCO	IMB	EBAY
MA	1.76%	3.12%	1.81%	4.89%	6.22%
LSTM	1.98%	0.01%	2.23%	1.31%	0.96%
NET	1.96%	0.205	2.21%	1.54%	1.33%


Crypto
In this case, the model analyzed the crypto prices for Bitcoin, Ethereum, Ripple, Shiba, and Solana. In the table below, you can see that a net gain was produced for all except for Solana, with an overall net gain produced of 2.48%. 

	BTC	ETH	XRP	SHIB	SOL
MA	2.24%	8.00%	4.23%	27%	9.88%
LSTM	2.42%	3.50%	2.97%	9.7%	-5.14%
NET	2.40%	3.90%	3.10%	12.55%	-3.55%

Losses after IPO
In this case, the model analyzed the stock prices for Robinhood, GitLab, Kind, Rivian Automotive Inc, and Root Inc after their IPO. In the table below, you can see that a net gain was produced for only Robinhood and Root Inc, and an overall net loss was produced at -25.85%. This loss was mostly attributed to Rivian Automotive Inc. Additionally, the LSTM model produced significantly better results in terms of positive returns and magnitude.
	HOOD	GTLB	KIND	RIVN	ROOT
MA	-8.56%	-18.82%	-16.54%	-25.2%	-7.76%
LSTM	6.33%	1.47%	-3.84%	-24.78%	1.81%
NET	3.12%	-4.28%	-5.0%	-24.84%	0.74%

Metals ETFs & Stocks
In this case, the model analyzed the Metals ETFs & Stocks prices for Cobalt Blue Holdings Ltd, Gold, Silver, S&P Metals and Mining ETF and ArcelorMittal SA. In the table below, you can see that a net gain was produced only for CBBHF and MT, however, an overall net gain was produced at 1.78%. 
	CBBHF	GOLD	SLV	XME	MT
MA	-4.81%	-1.35%	-1.57%	-4%	0.18%
LSTM	5.09%	1.90%	-0.32%	-2.41%	1.90%
NET	5.05%	-1.87%	-0.42%	-2.52%	1.76%

Meme Stocks
In this case, the model analyzed the stock prices for five meme stocks: Nio, GameStop, Bed Bath & Beyond Inc, Virgin Galactic Holdings Inc and Palantir Technologies Inc. In the table below, you can see that a net gain was produced for all except Palantir Technologies Inc. Additionally, an overall net gain was produced at 4.14%, the highest of all scenarios.
	NIO	GME	BBBY	SPCE	PLTR
MA	4.07%	3.19%	1.10%	5.08%	0.07%
LSTM	2.00%	7.97%	4.38%	0.06%	-1.74%
NET	2.18%	7.51%	4.06%	0.5%	-1.59%

Improvements and Conclusion
Although the Long Short-Term Memory (LSTM) model and a Moving Average (MA) model worked fairly well in the six cases presented above, there are various improvements that can be implemented to potentially improve the results. These improvements include but are not limited to:

●	The trading strategy can be modified to utilize the slope of the LSTM prediction to gauge the number of stocks to be bought. This would drastically increase the profit margin as compared to buying a single stock in case of an upward trend.
●	Past events can be analyzed with methods like dynamic time warping to figure out the historical trends. Using this, downtrends can be capitalized if there is an expected uptrend in the near future which might be very profitable.
●	Sentiment analysis methods can be used to understand the public market sentiment from news sources and social media sites to add another dimension to the trading algorithm. In general, this can allow investors to understand the sentiment around a particular stock before the news drives the behavior of stock prices. Additionally, it can help investors determine when forces in the market are being driven by rational or irrational decision-making.
●	Per second market data can be obtained to transform this algorithm into a day-trading algorithm for highly volatile stocks or even for highly volatile currencies.
●	Short-term options trades can be placed if the LSTM predicts a high upward trend which would drastically improve the profits of the algorithm, albeit risky in case of failure.
●	Other machine learning models such as GRUs or transformers can be used in synchrony and boosting methods can be incorporated to fine-tune the results.
In summary, the LSTM model, coupled with the MA model provided the intended investor with an edge in the market. The advantages of the artificial neural network suited for the time series of the LSTM model and the statistical MA model based on historical data were able to combine to produce net positive returns in a majority of historical cases, including cases of high volatility.

