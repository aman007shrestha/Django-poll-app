from django.urls import path
from . import views

app_name = "vote4change"



urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>', views.detail, name='detail'),
	path('<int:pk>/result', views.result, name='result'),
	# vote handler
	path('<int:pk>/vote', views.vote, name='vote'),
	path('<str:object_id>/resultsdata/', views.result_data, name="result_data"),
]



