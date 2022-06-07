from attr import field
from rest_framework import serializers

from posts.models import Post, Group, Comment, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')

    class Meta:
        fields = ('__all__')
        model = Post
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')

    class Meta:
        fields = ('__all__')
        model = Comment
        read_only_fields = ('author', 'post')

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(many=False, read_only=True,
                                          slug_field='username')
    # following = serializers.SlugRelatedField(slug_field='username', queryset=Follow.objects.all())
    class Meta:
        fields = ('__all__')
        model = Follow
        read_only_fields = ('user',)
        # это поле подгружается автоматически из self.request.user
    
    # def validate_following(self, value):
    #     if value == 'user':
    #         raise serializers.ValidationError('Author is not specified')
    #     return value 
