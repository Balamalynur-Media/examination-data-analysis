from django.urls import path
from . import views as v

app_name = 'exam'

urlpatterns = [
    path('', v.index, name='index'),
    path('student/json/', v.student_json, name='student_json'),
    path('filter_list/', v.filter_list, name='filter_list'),
    path('filter_dropdown/', v.filter_dropdown, name='filter_dropdown'),
    path('filter_dropdown2/', v.filter_dropdown2, name='filter_dropdown2'),
    path('subjects/ajax/', v.subjects_ajax, name='subjects_ajax'),
    path(
        'subjects/choices/ajax/',
        v.subjects_choices_ajax,
        name='subjects_choices_ajax'
    ),
    path('testids/ajax/', v.testids_ajax, name='testids_ajax'),
    path(
        'testids/choices/ajax/',
        v.testids_choices_ajax,
        name='testids_choices_ajax'
    ),
]
