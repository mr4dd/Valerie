from flask import Flask, render_template
#import database_management_library

app = Flask(__name__)

def fetch_articles_without_content_from_database():
    pass

def get_audio_file():
    pass

@app.route('/')
def root():
    articles = fetch_articles_without_content_from_database()
    audio = get_audio_file()
    return render_template('index.html', articles=articles, audio=audio)


# user[UUID],date[double],headline[string],description[string],media[array],relevance[boolean]
# For database 'schema'
