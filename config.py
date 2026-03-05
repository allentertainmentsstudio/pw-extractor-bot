#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8763570217:AAE6k4YqYeEExkw6BwQzGzI9pv2bdm91zfc")
    API_ID = int(os.environ.get("API_ID", "34724970"))
    API_HASH = os.environ.get("API_HASH", "f240eae7c60e8e30c17203ab0e052f7e")
    AUTH_USERS = "7521421400"


