import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "5MAB2Z2J9DG043C7"
NEWS_API_KEY = "e5e464c3bcda45c59932cd9ffc3b01e5"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=parameters_stock)
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"Yesterday closing price : {yesterday_closing_price}")
print(f"Day before yesterday closing price : {day_before_yesterday_closing_price}")
print(yesterday_data)

# Find the positive difference between yesterday and the day before prices
price_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

up_down = None
if price_difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

# Work out the percentage difference from yesterday price
diff_percent = round((price_difference / float(yesterday_closing_price)) * 100)

# Use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 3:
    parameters_news = {
        "qinTitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=parameters_news)
    articles = news_response.json()["articles"]

    # Use Python slice operator to create a list that contains the first 3 article
    first_threes_articles = articles[:3]

    # Create a new list of the first 5 articles headline and description
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline : {article['title']}.\nBrief: {article['description']} " for article in first_threes_articles]
    for art in formatted_articles:
        print(f"\n{art}\n")