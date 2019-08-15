# -*- coding: utf-8 -*-

'''
Script:
    constants.py
Description:
    Constants values for join_captcha_bot.py.
Author:
    Jose Rios Rubio
Creation date:
    09/09/2018
Last modified date:
    15/08/2019
Version:
    1.5.2
'''

####################################################################################################

### Imported modules ###

from os import path

####################################################################################################

### Constants ###

# Actual constants.py full path directory name
SCRIPT_PATH = path.dirname(path.realpath(__file__))


# General Bots Parameters
CONST = {

    # Bot Token (get it from @BotFather)
    "TOKEN" : "XXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",

    # Languages texts files directory path
    "LANG_DIR" : SCRIPT_PATH + "/language",

    # Chats directory path
    "CHATS_DIR" : SCRIPT_PATH + "/data/chats",

    # Directory where create/generate temporary captchas
    "CAPTCHAS_DIR" : SCRIPT_PATH + "/data/captchas",

    # Chat configurations JSON files
    "F_CONF" : "configs.json",

    # Initial chat title at Bot start
    "INIT_TITLE" : "Unknown Chat",

    # Initial chat link at Bot start
    "INIT_LINK" : "Unknown",

    # Initial language at Bot start
    "INIT_LANG" : "EN",

    # Initial enable/disable status at Bot start
    "INIT_ENABLE" : True,

    # Initial captcha solve time (in minutes)
    "INIT_CAPTCHA_TIME_MIN" : 5,

    # Initial captcha difficult level
    "INIT_CAPTCHA_DIFFICULTY_LEVEL" : 2,

    # Initial captcha characters mode (nums, hex or ascci)
    "INIT_CAPTCHA_CHARS_MODE" : "nums",

    # Default time (in mins) to remove self-destruct sent messages from the Bot
    "T_DEL_MSG" : 5,

    # IANA Top-Level-Domain List (https://data.iana.org/TLD/tlds-alpha-by-domain.txt)
    "F_TLDS" : "tlds-alpha-by-domain.txt",

    # Regular expression to detect URLs in a string based in TLD domains
    "REGEX_URLS" : r"((?<=[^a-zA-Z0-9])*(?:https\:\/\/|[a-zA-Z0-9]{{1,}}\.{{1}}|\b)" \
                   r"(?:\w{{1,}}\.{{1}}){{1,5}}(?:{})\b/?(?!@))",

    # Bot developer
    "DEVELOPER" : "@JoseTLG",

    # Bot code repository
    "REPOSITORY" : "https://github.com/J-Rios/TLG_JoinCaptchaBot",

    # Developer Paypal address
    "DEV_PAYPAL" : "https://www.paypal.me/josrios",

    # Developer Bitcoin address
    "DEV_BTC" : "3N9wf3FunR6YNXonquBeWammaBZVzTXTyR",

    # Bot version
    "VERSION" : "1.5.2 (15/08/2019)"
}


# Supported languages list
TEXT = {
    "EN" : None, # English
    "ES" : None, # Spanish
    "CA" : None, # Catalan
    "GL" : None, # Galician
    "PT_BR" : None, # Portuguese (Brasil)
    "ZH_CN" : None # Chinese (Mainland)
}
