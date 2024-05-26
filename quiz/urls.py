from django.urls import path 
from .views import *


app_name = "quiz"


urlpatterns = [
    path('f0aebd04a8e6d9970573a520f084a8c3dfa7b93aa89818abe631be0839cc1b67' , QuestionAPIView.as_view() , name="question" ),
    path('8f35863e12d598583ee09c31bb260d0ac7db3d870f7002644938d14c04142b4f' , RegisterAPIView.as_view() , name="register"),
    path('e12bf89d64422d555b4ad855591036093e3afaac1d867cc351464fad8b6b49a1' , ResultAPIView.as_view() , name="result"),
    path('e8270ebb4d78d5528fc8ef01228f3e2301bfd946d3703f95d7fad86f1172d192' , CheckAnswerAPIView.as_view() , name = 'check_answer')
]