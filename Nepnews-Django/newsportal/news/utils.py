# newsportal/news/utils.py
import requests

API_KEY = 'your-api-key-here'

def fetch_news_data():
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&country=np&language=en"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []
