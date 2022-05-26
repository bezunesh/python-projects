from rest_framework import routers
from .views import WordOfTheDayView

router = routers.SimpleRouter()
router.register(r'wordoftheday', WordOfTheDayView, basename='resource')
urlpatterns = router.urls
