from asgiref.sync import async_to_sync
from channels.generic.websocket import SyncConsumer, WebsocketConsumer
import json

from channels.db import database_sync_to_async


class BroadcastConsumer(WebsocketConsumer):

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def connect(self):
        # get user's subscribed segments here
        # for each segment, check if a group exists
        # if group exists, add the channel name to group
        # else create new group for each segment and add channel name to it

        self.accept()
        message = {
            "type":"connect",
            "data":"connection succeeded"
        }
        self.send(json.dumps(message))

    def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['id']
        schema = data['schema']


    def broadcast(self, message):

        self.send(json.dumps(message))






