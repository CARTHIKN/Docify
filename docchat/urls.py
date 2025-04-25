from django.urls import path
from .views import RegisterView, LoginView, DocumentUploadView, DocChatView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('docchat/', DocChatView.as_view(), name='docchat'),
]
