import requests

api_key = "9be42617fb2e4709883447b481519c94"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2023-05-25&sortBy=publishedAt" \
      "&apiKey=9be42617fb2e4709883447b481519c94"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the title and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
print(content)
