from rest_framework import viewsets, permissions, mixins, filters
from rest_framework.pagination import LimitOffsetPagination


from posts.models import Post, Group, Comment, Follow
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from .permissions import IsAuthorOrReadOnlyPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    # Только автор вправе изменять посты
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)
        # меняем queryset с которым будет работать класс
        # Нам нужны не все комментарии, а только к определенному посту
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        # получаем значение post_id из адреса
        post = Post.objects.get(id=post_id)
        # получаем пост, к которому нужно сделать комментарии
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)

class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    # Наследуем от миксинов с нужными методами 
    # и дженерика, поскольку роутер с миксинами не работает
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(user=self.request.user)
        # меняем queryset с которым будет работать класс
        # Нам нужны не все комментарии, а только к определенному посту
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        