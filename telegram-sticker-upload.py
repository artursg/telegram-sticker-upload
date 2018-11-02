#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import configparser
import time
from pytg import Telegram

# load configuration
home_dir= os.getenv("HOME")
config = configparser.ConfigParser()
config.read_file(open('defaults.cfg'))

# get telegram
tg = Telegram(
    telegram=home_dir + '/' + config['TELEGRAM']['APP'],
    pubkey_file=home_dir + '/' + config['TELEGRAM']['PUBKEY_FILE']
    )

# load images
stickers = []
try: 
    for root, dirnames, filenames in os.walk(config['STICKERS']['PATH']):
        for filename in filenames:
            if filename.endswith(config['STICKERS']['EXTENSION']):
                stickers.append(os.path.join(root, filename))
except IOError: 
    sys.exit("IO error. Aborting.") 
if len(stickers) == 0:
    sys.exit("No sticker images. Aborting.") 

# upload to telegram bot
bot_name = config['BOT']['NAME']
tg.sender.send_msg(bot_name, '/' + config['BOT']['NEWPACK'])
tg.sender.send_msg(bot_name, config['STICKERS']['PACK_FULL_NAME'])

for sticker in stickers:    
    tg.sender.send_document(bot_name, sticker)
    tg.sender.send_msg(bot_name, config['STICKERS']['DEFAULT_EMOJI'])

# wait a while for image upload to be complete
time.sleep(5)

# publish stickers
tg.sender.send_msg(bot_name, '/' + config['BOT']['PUBLISH'])
tg.sender.send_msg(bot_name, config['STICKERS']['PACK_NAME'])
