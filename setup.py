import sys
import setuptools

setuptools.setup(
    license="MIT",
    name="TwitchHQ",
    version='1.1.0',
    keywords=["twitchtv","twitch","api","client","justintv","justin"],
    description="Python Library for Twitch.tv",
    long_description=open("README.md").read(),

    author="Mark McGuire",
    author_email="???",
    url="https://github.com/TronPaul/TwitchHQ",
    download_url="https://github.com/TronPaul/TwitchHQ/archive/master.zip",

    platforms=["any"],

    classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries",
            "Topic :: Utilities",
        ],

    entry_points={
        'console_scripts': [
            'twitch = twitchapi.cli:main',
        ]
    },

    install_requires=['httplib2'],
    packages=setuptools.find_packages(),
    zip_safe=True
)
