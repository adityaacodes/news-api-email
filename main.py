import requests
from send_email import send_mail

topic = "tesla"

api_key = "9be42617fb2e4709883447b481519c94"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-05-25&" \
      "sortBy=publishedAt&" \
      "apiKey=9be42617fb2e4709883447b481519c94&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the title and description
body = ""
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = "Subject: Today's news." + '\n' + body + article['title'] + '\n'\
               + article['description'] \
               + '\n' + article['url'] + 2*'\n'

body = body.encode("utf-8")
send_mail(message=body)
