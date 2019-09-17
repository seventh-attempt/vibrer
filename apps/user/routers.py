from rest_framework import routers

from apps.user.views.user import UserView
from apps.user.views.playlist import PlaylistView


router = routers.DefaultRouter()
router.register('user', UserView)
router.register('playlist', PlaylistView)
