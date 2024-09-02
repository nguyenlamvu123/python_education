from telethon import TelegramClient
#site: https://stackoverflow.com/questions/50975793/telegram-get-chat-messages-posts-python-telethon

# Use your own values from my.telegram.org
name = 'herrculessss'
api_id = 26001757
api_hash = 'something'
chat = 'https://t.me/+x9445bBh-LljZjM9'


with TelegramClient(name, api_id, api_hash) as client:
    for message in client.iter_messages(chat):
        print(message.sender_id, ':', message.text)
