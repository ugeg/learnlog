from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('topic/',views.topics,name = 'topics'),
    path('topic/<topic_id>/',views.topic,name='topic'),
    path('new_topic',views.new_topic,name='new_topic'),
    path('edit_entry/<entry_id>/',views.edit_entry,name = 'edit_entry'),
    path('new_entry/<topic_id>/',views.new_entry,name = 'new_entry')
]
app_name = 'learnlogs'