from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostTag, Tag, Post

class PostTagView(ViewSet):
    def retrieve(self, request, pk):
      try: 
        post_tag = PostTag.objects.get(pk=pk)
        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data)
      except PostTag.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
      post_tags = PostTag.objects.all()
      serializer = PostTagSerializer(post_tags, many=True)
      return Response(serializer.data)
    
class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
      model = PostTag
      fields = ('id', 'post', 'tag')
