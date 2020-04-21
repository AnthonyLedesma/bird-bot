# Updates from spacelord
Given that BestBuy checkout doesn't work - I edited the BestBuy code to instead continually send a text message when stock is found. The SMS text includes a URL link to the item in stock so you can react quickly. I was able to cop a BestBuy switch with this functionality.

I also added the same functionality for Target. So you can add a Target link and it will text you once it finds stock. I have seen some wonky behavior with Target, so it's not guaranteed to work.

You will need to create a Twilio free account to obtain a random number to send texts from. Once you've done that go into send_sms.py.dummy,  edit the information to add your ID, token, and to/from phone numbers, then remove the .dummy extension.

# Bird Bot
[Support Discord](https://discord.gg/8UVSkpP)<br/><br/>
Bird Bot is an auto-checkout bot that currently supports Walmart and Best buy. It is intended to be used to purchase Nintendo Switch consoles. More sites will be added in the future.

* Easy to use interface built on PyQt5
* Waits for items to restock if they are out of stock
* Optional price checker
* Lighting fast auto-checkout

<p align="center">
  <img src="https://i.imgur.com/E105F74.png" alt="Bird Bot UI" width="738">
</p>

## Installation
[View The Docs Here](https://nateskicks13.gitbook.io/bird-bot/)
