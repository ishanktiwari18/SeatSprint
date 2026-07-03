import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SeatStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.show_id = self.scope['url_route']['kwargs']['show_id']
        self.group_name = f"show_{self.show_id}"
        user = self.scope.get('user')
        if not user or not user.is_authenticated:
            await self.close()
            return
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({"type": "connection_established", "message": "Connected to seat updates"}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def seat_status_update(self, event):
        await self.send(text_data=json.dumps({
            "type": "seat_status_update",
            "seat_ids": event['seat_ids'],
            "status": event['status'],
        }))
