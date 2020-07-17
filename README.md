# Messenger-Bulk-Message-Sender

## Installation
1. Install python3 in your machine.
2. Install `selenium`for python3 using pip. It is usually done from cmd or terminal. Command: `pip3 install selenium`
3. Download [chromedriver](https://chromedriver.chromium.org/downloads). Check your browser version and the chromedriver version. Extract the downloaded zip. Copy the file in the same directory of `main.py` file.
4. Now read from **Step 1** again and check in everything is done properly! 😉

## Usage
 1. Place you Facebook username and password in `authenticate.py` file and run the file once. This will save all cookies and other site data to perform like normal browser to Facebook next time.
 2. Place all the conversation links in `links.txt` file. To get links, go to [mbasic.facebook.com/messages](https://mbasic.facebook.com/messages), click on the friends name you want to send message, copy the browser link and then paste it in `links.txt`file.
 3. Place your message in `message.txt` file.
 4. Now run the `main.py` file, sit back and see the magic!
