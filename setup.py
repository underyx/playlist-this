import io
from playlist_this import __version__
from setuptools import setup

with io.open('README.md', encoding='utf-8') as f:
    README = f.read()

setup(
    name='playlist-this',
    version=__version__,
    url='https://github.com/underyx/playlist-this',
    author='Bence Nagy',
    author_email='bence@underyx.me',
    maintainer='Bence Nagy',
    maintainer_email='bence@underyx.me',
    download_url='https://github.com/underyx/playlist-this/releases',
    long_description=README,
    packages=['playlist_this'],
    package_data={'': ['LICENSE']},
    install_requires=[
        'praw<4',
        'celery<4',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
