from rest_framework import routers
from views import WordOfTheDayView

router = routers.SimpleRouter()
router.register(r'api/wordoftheday', WordOfTheDayView, basename='resource')
urlpatterns = router.urls