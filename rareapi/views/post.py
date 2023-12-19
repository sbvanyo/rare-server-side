"""View module for handling requests about posts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, User
import base64



class PostView(ViewSet):
    """Post view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized post
        """
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all posts

        Returns:
            Response -- JSON serialized list of posts
        """
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized post instance
        """
        user = User.objects.get(uid=request.data["rareUserId"])
        
        # Decode the Base64 string to bytes
        approved_bytes = base64.b64decode(request.data["approved"])

        post = Post.objects.create(
            title=request.data["title"],
            publication_date=request.data["publicationDate"],
            image_url=request.data["imageUrl"],
            content=request.data["content"],
            approved=approved_bytes,
            rare_user_id=user,
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    
    def update(self, request, pk):
        """Handle PUT requests for a post

        Returns:
            Response -- Empty body with 204 status code
        """
        approved_bytes = base64.b64decode(request.data["approved"])
        
        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.publication_date = request.data["publicationDate"]
        post.image_url = request.data["imageUrl"]
        post.content = request.data["content"]
        post.approved = approved_bytes

        rare_user_id = User.objects.get(pk=request.data["rareUserId"])
        post.rare_user_id = rare_user_id
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    """JSON serializer for posts"""
    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'rare_user_id', 'tags')
        depth = 1
        
    def get_tags(self, obj):
        post_tags = obj.tag_posts.all()
        return [{'id': tag.tag.id, 'label': tag.tag.label} for tag in post_tags]
