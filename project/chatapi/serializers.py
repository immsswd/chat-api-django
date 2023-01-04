from rest_framework import serializers
from . models import Chat

# create class Object for Chat Serializers
class ChatSerializer(serializers.ModelSerializer):
    
    # ReadOnlyField
    user    = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model   = Chat
        # which field do you want to serialize
        fields  = ['id', 'text', 'created', 'user', 'user_id']