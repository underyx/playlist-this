import os
from . import app, USER_AGENT


@app.task
def gather_songs_for(permalink):
    R = praw.Reddit(USER_AGENT)
    R.login(os.environ['PT_REDDIT_USERNAME'], os.environ['PT_REDDIT_PASSWORD'])
    submission = R.get_submission(message.permalink)


    return


@app.task
def create_playlist(songs):
    return


@app.task
def generate_playlist_comment(playlist):
    return


@app.task
def post_comment(text, permalink):
    R = praw.Reddit(USER_AGENT)
    R.login(os.environ['PT_REDDIT_USERNAME'], os.environ['PT_REDDIT_PASSWORD'])
    return
