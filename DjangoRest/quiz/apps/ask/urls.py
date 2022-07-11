from rest_framework.routers import DefaultRouter
from ask.views import QuestionViewSet



router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='user')

urlpatterns = router.urls