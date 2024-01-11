import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    quote_data = response.json()[0]
    return f"Your Quote goes like:\n {quote_data['q']} - {quote_data['a']}"

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()
    return f"your joke goes like:\n {joke_data['setup']} - {joke_data['punchline']}"

if __name__ == "__main__":
    quote = get_quote()
    print(quote)
    joke = get_joke()
    print(joke)