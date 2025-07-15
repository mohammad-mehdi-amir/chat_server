import json
import time
from channels.generic.websocket import AsyncWebsocketConsumer
online_users = set()


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add("chat_global", self.channel_name)
        await self.accept()
        await self.channel_layer.group_send(
            "chat_global",
            {
                'type': 'chat_message',
                'message': 'یک کاربر جدید وارد گروه شد!',
                'username': 'سیستم',
            }
        )
        await self.get_logs('add')
        await self.update_user_list()
        print('someone connected...')

    async def disconnect(self, close_code):
        if hasattr(self, "username") and self.username in online_users:
            online_users.discard(self.username)
            await self.update_user_list()

            await self.channel_layer.group_send(
                "chat_global",
                {
                    'type': 'chat_message',
                    'message': f'{self.username} از گروه خارج شد!',
                    'username': 'سیستم',
                }

            )
            await self.get_logs('remove')

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        self.username = username
        self.message = message
        if username not in online_users:
            online_users.add(username)
            await self.update_user_list()
        await self.channel_layer.group_send(
            "chat_global",
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )
        await self.get_logs('sending message')
        print('send to all...')

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': event['message'],
            'username': event['username'],
        }))

    async def update_user_list(self):
        await self.channel_layer.group_send(
            "chat_global",
            {
                'type': 'user_list',
                'users': list(online_users),
            }
        )

    async def user_list(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_list_update',
            'users': event['users'], }))

    async def get_logs(self, state):
        try:
            with open('chat_log.txt', 'r') as file:
                logs = file.readlines()

        except FileNotFoundError:
            with open('chat_log.txt', 'w') as file:
                file.write('')
        if state == 'add':
            with open('chat_log.txt', 'a') as file:
                file.write(f"[{time.ctime()}]: new user connected\n")
        elif state == 'remove':
            with open('chat_log.txt', 'a') as file:
                file.write(f"[{time.ctime()}]: {self.username} disconnected\n")
        elif state == 'sending message':
            with open('chat_log.txt', 'a') as file:
                file.write(
                    f"[{time.ctime()}]: {self.username} sent a message : ({self.message})\n")
