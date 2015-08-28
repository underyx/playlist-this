import os
import praw
import logging
from . import tasks
from celery import chain

__version__ = '0.0.1'

USER_AGENT = 'playlist-this v{0} (by /u/underyx)'.format(__version__)
CHECK_INTERVAL = os.getenv('PT_CHECK_INTERVAL', 60)


def main():
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(module)s.%(funcName)s - %(message)s')
    R = praw.Reddit(USER_AGENT)
    R.login(os.environ['PT_REDDIT_USERNAME'], os.environ['PT_REDDIT_PASSWORD'])
    logging.info('Starting check loop')
    while True:
        for message in R.get_unread():
            message.mark_as_read()
            if '/u/playlist-this!' not in message.body or not message.was_comment:
                continue

            if message.is_root:
                parent_permalink = message.submission.permalink
            else:
                parent_permalink = message.submission.permalink + message.parent_id[3:]

            chain(
                tasks.get_songs_from.s(parent_permalink),
                tasks.create_playlist.s(),
                tasks.generate_playlist_comment.s(),
                tasks.post_comment.s(message.permalink),
            ).apply_async()

        logging.info('Sleeping for %s seconds', CHECK_INTERVAL)
        time.sleep(CHECK_INTERVAL)


if __name__ == '__main__':
    main()
