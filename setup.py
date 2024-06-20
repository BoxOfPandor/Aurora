from setuptools import setup, find_packages

setup(
    name="aurora",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "speechrecognition",
        "pyaudio",
        "gtts",
        "pydub",
        "curses"
    ],
    entry_points={
        'console_scripts': [
            'aurora=main:main',
        ],
    },
)
