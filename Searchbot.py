from slacker import Slacker
import config
token=config.BOT_USER_OAUTH_ACCESS_TOKEN['token']
slack = Slacker('<your-slack-api-token-goes-here>')

# Send a message to #general channel
slack.chat.post_message('#general', 'Hello fellow slackers!')
