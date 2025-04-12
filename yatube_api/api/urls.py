from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path(
        "api/v1/posts/<int:post_id>/comments/",
        CommentViewSet.as_view({"get": "list", "post": "create"}),
        name="post-comments",
    ),
    path(
        "api/v1/posts/<int:post_id>/comments/<int:pk>/",
        CommentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="post-comment-detail",
    ),
]
