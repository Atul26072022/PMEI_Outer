from django.urls import path,include
# from .views import PDIView,SetUpDataModelViewset
from rest_framework.routers import SimpleRouter
from .views import PDIView, ScheduleCancellationView

router = SimpleRouter()
# router.register('data',SetUpDataModelViewset)   

urlpatterns = [
    path("", PDIView.as_view()),
    path("schedulecanceel/",ScheduleCancellationView.as_view())
    # path("setup/", SetupDataView.as_view()),
    # path("setup/",include(router.urls))
]
