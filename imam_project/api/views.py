from rest_framework.response import Response
from rest_framework.decorators import api_view
from chat.models import Message
from .serializers import MessageSerializer

# get All your messages
@api_view(['GET'])
def getMyData(request):
    msg         = Message.objects.all()
    serializer  = MessageSerializer(msg, many=True) 
    return Response(serializer.data)
# create a/some message
@api_view(['POST'])
def addData(request):
    serializer  = MessageSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)