from django.urls import path
from . import views




app_name = 'projects'


#domain.com/projects/track_teacher_performance
urlpatterns = [ 
               
    path('track_teacher_performance/', views.track_teacher, name='track_teacher'),
    path('generatingExamUsingGPT/', views.examGPT, name = 'examGPT'), 
    # path('generatingExamUsingGPT/whisper/', views.examGPT_voice, name = 'examGPT_voice'),
    # path('generatingExamUsingGPT/whisper/record/', views.record, name = 'record'), 
 

    path('generatingExamUsingGPT/download_exam', views.download_exam, name='download_exam'), #project
    path('generatingExamUsingGPT/download_exam_arabic', views.download_exam_arabic, name='download_exam_arabic'), #project

    
    path('generatingExamUsingGPT/download_exam_answers', views.download_exam_answers, name = 'download_answers'), 
    # path('generatingExamUsingGPT/download_exam_whisper', views.download_exam_whisper, name='download_exam_whisper'), #project
    # path('generatingExamUsingGPT/download_exam_answers_whisper', views.download_exam_answers_whisper, name='download_exam_answers_whisper'), #project

    path('signup/', views.signup, name='signup'), 
    path('track_teacher_performance/sendReport', views.send_trackTeachers, name='send_trackTeachers'),
    path('track_teacher_performance/download_teachers_report', views.download_teachers_report, name='download_teachers_report'),

    
    
    path('generatingLessonPlanUsingGPT/', views.LessonPlanGPT, name = 'LessonPlanGPT'), 
    path('generatingLessonPlanUsingGPT/download_lessonPlan', views.download_lessonPlan, name = 'download_lessonPlan'), 



    
    
    # path('thankyou/', views.thank, name='thank'), 
    

 
    
]
