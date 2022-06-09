from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Group, Comment, Follow, User


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
    user = serializers.SlugRelatedField(
            many=False, 
            read_only=True, 
            slug_field='username', 
            default=serializers.CurrentUserDefault())
    # передаем по умолчанию текущего юзера, чтобы работал
    # UniqueTogetherValidator(проверяет отсутствие повторных подписок)
    following=serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    # указываем queryset c объектами связанной модели, чтобы сериалайзер
    # взял оттуда нужный объект по полю username при Post запросе
    # запись идет через метод to_internal_value поля
    
    class Meta:
        fields = ('user', 'following')
        model = Follow
        read_only_fields = ('user',)
        # это поле подгружается автоматически из self.request.user
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        if self.context.get('request').user == data['following']:
        # Проверяем, чтобы подписчик не совпадал с автором
            raise serializers.ValidationError(
                'You cannot follow yourself')
        return data 


   
