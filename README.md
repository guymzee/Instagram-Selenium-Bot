<div align="center">
  <img src="./img/logo-icon.svg" alt="alt text" width="200px">
  <h1>Instagram Selenium Bot</h1>
</div>

# 🔥 Version 0.1.1 🔥

This is the first version of this Instagram bot. Much more is to come in future and this is just a working beta. It's easy to use and very simple for now. I am planning on adding much more features in the future and automate a lot more processes. My goal is to create a Instagram script which is able to run 24/7 without beeing detected by Instagram.

Find more of my Selenium Bots here: http://selenium-bots.000webhostapp.com/

# Instagram Selenium Bot

🚀 Automate your Instagram Account 🚀

📌 Ver. 0.1.1 📌

⚠ No Proxy Support yet ⚠️

## Features

* Watch all Stories from feed
* Like recent posts from a certain hashtag
    * Detects if post already got liked by user
* Comment on recent posts from a certain hashtag
    * Detects if post already got commented by user

### Support 👨‍💻

Any problems with running the script and any questions please cantact me via Twitter [@hendrik_bgr](https://twitter.com/Hendrik_bgr)

### Prerequisites

You need python 3 installed on your System.
As well as Selenium and the Firefox Webdriver

Get a copy of the Project. Open your Terminal and enter:

```
git clone https://github.com/hendrikbgr/Instagram-Selenium-Bot
```

To install all needed requirements run the following command in the project directory:
(coming soon...)

```
pip install -r requirements.txt
```

After that you can proceed to edit the Script.

### Edit Script

Open /utils/secret.py with any TextEditor.

Change all needed values such as username and password.

Also open bot.py and change the max rate limits.

## Running 🏃🏽‍♂️

To run this script open your Terminal in the project directory.

To start the script enter:

```
python bot.py
```

## Authors

* **Hendrik Bgr** - *Initial work* - [HendrikBgr](https://github.com/hendrikbgr)
    * **Twitter** - *Initial work* - [HendrikBgr](https://twitter.com/hendrik_bgr)


## Acknowledgments

* Hat tip to anyone whose code was used

## To Do List 📝

* Add follow script
* Add unfollow script
* Store information in database so the same media wont get targeted twice
* Add inputs for rate limits on startup & optional create config file.

## Known Bugs 🐛

* Still watches stories even tho they already got watched.


