from slacker import Slacker
from Searchbot import config

token = config.BOT_USER_OAUTH_ACCESS_TOKEN['token']
slack = Slacker(token)

slack.chat.post_message('#bots_test', 'Hello!')
