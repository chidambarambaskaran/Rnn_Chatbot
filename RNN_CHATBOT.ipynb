!pip install tensorflow requests pyjokes ipywidgets beautifulsoup4 lxml pytz

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Embedding, Dense
import random
import requests
from datetime import datetime
from IPython.display import display, clear_output
import pyjokes
import ipywidgets as widgets
import pytz  # Import pytz for timezone handling

# Model configuration
vocab_size = 1000
embedding_dim = 16
rnn_units = 64

def create_model(vocab_size, embedding_dim, rnn_units):
    model = Sequential([
        Embedding(vocab_size, embedding_dim),
        SimpleRNN(rnn_units, return_sequences=True),
        SimpleRNN(rnn_units),
        Dense(64, activation='relu'),
        Dense(1)
    ])
    return model

model = create_model(vocab_size, embedding_dim, rnn_units)

# Fetch news
def get_news():
    try:
        response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=3ff646aa4dcd4294b3af45745f344bee')
        news_data = response.json()
        headlines = [article['title'] for article in news_data['articles'][:5]]
        return "Here are some news headlines:\n" + "\n".join(headlines)
    except Exception as e:
        return f"Sorry, I couldn't fetch the news right now. Error: {e}"

# Search Wikipedia
def start_search(query):
    try:
        response = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json')
        search_data = response.json()
        if search_data['query']['search']:
            snippet = search_data['query']['search'][0]['snippet']
            snippet = snippet.replace('<span class="searchmatch">', '').replace('</span>', '')
            return f"Result: {snippet}"
        else:
            return "No results found."
    except Exception as e:
        return f"Sorry, I encountered an error while searching. Error: {e}"

# Get current time in Indian Standard Time (IST)
def get_time():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    return f"Current time in India is {current_time}."

# Telling jokes
used_jokes = set()
def tell_joke():
    joke = pyjokes.get_joke()
    while joke in used_jokes:
        joke = pyjokes.get_joke()
    used_jokes.add(joke)
    return joke

# Play video by generating a YouTube search link
def play_video(search_term):
    search_url = f"https://www.youtube.com/results?search_query={search_term.replace(' ', '+')}"
    return f"You can watch videos related to '{search_term}' [here]({search_url})."

# Button click handlers
def on_news_button_click(b):
    clear_output(wait=True)
    display_buttons()
    print(get_news())

def on_time_button_click(b):
    clear_output(wait=True)
    display_buttons()
    print(get_time())

def on_joke_button_click(b):
    clear_output(wait=True)
    display_buttons()
    print(tell_joke())

def on_search_button_click(b):
    clear_output(wait=True)
    search_query = widgets.Text(placeholder="Enter search query")
    search_button = widgets.Button(description="Search")

    def execute_search(_):
        query = search_query.value
        result = start_search(query)
        clear_output(wait=True)
        display_buttons()
        print(result)

    search_button.on_click(execute_search)
    display(search_query)
    display(search_button)

def on_play_button_click(b):
    clear_output(wait=True)
    play_query = widgets.Text(placeholder="Enter video title")
    play_button = widgets.Button(description="Play")

    def execute_play(_):
        video_title = play_query.value
        video_link = play_video(video_title)
        clear_output(wait=True)
        display_buttons()
        print(video_link)

    play_button.on_click(execute_play)
    display(play_query)
    display(play_button)

# Display buttons
def display_buttons():
    news_button = widgets.Button(description="News")
    time_button = widgets.Button(description="Time")
    joke_button = widgets.Button(description="Joke")
    search_button = widgets.Button(description="Search")
    play_button = widgets.Button(description="Play")

    news_button.on_click(on_news_button_click)
    time_button.on_click(on_time_button_click)
    joke_button.on_click(on_joke_button_click)
    search_button.on_click(on_search_button_click)
    play_button.on_click(on_play_button_click)

    display(news_button)
    display(time_button)
    display(joke_button)
    display(search_button)
    display(play_button)

# Initial display
display_buttons()
print("Welcome to Jarvis! Use the buttons above to interact.")
