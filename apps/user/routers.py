from rest_framework import routers

from apps.user.views.playlist import PlaylistView
from apps.user.views.user import UserView

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('playlist', PlaylistView)
