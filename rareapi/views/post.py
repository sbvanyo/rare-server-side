# """View module for handling requests about game types"""
# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers, status
# from rareapi.models import User


# class PostView(ViewSet):
#     """Post view"""

#     def retrieve(self, request, pk):
#         """Handle GET requests for single post

#         Returns:
#             Response -- JSON serialized post
#         """
#         game_type = GameType.objects.get(pk=pk)
#         serializer = GameTypeSerializer(game_type)
#         return Response(serializer.data)


#     def list(self, request):
#         """Handle GET requests to get all posts

#         Returns:
#             Response -- JSON serialized list of posts
#         """
