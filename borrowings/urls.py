from django.urls import path, include
from rest_framework.routers import DefaultRouter

from borrowings.views import BorrowingViewSet, BorrowingCreateView

router = DefaultRouter()
router.register('borrowings', BorrowingViewSet, basename='borrowing')
urlpatterns = [
    path('', include(router.urls)),
    path('', BorrowingCreateView.as_view(), name='borrowing-create'),
]

app_name = 'borrowings'
