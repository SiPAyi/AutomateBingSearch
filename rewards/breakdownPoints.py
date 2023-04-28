import requests
from bs4 import BeautifulSoup

# Send GET request to the Bing Rewards Points Breakdown page
response = requests.get('https://rewards.bing.com/pointsbreakdown')

# Create a BeautifulSoup object to parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# # Find the first element with class "pointsDetail c-subheading-3 ng-binding"
# points_detail = soup.find(class_='pointsDetail c-subheading-3 ng-binding')

# # Check if the element was found
# if points_detail is not None:
#     # Print the text content of the element
#     print(points_detail.text.strip())
# else:
#     print('Element not found')

print(soup)