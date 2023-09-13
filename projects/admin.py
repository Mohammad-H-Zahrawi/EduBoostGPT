from django.contrib import admin
from projects.models import TrackTeacherModel, ExamGPTModel, Donate, ContactUs, LessonPlanGPTModel, ExamGPTWhisperModel, LessonGPTWhisperModel

# Register your models here.
admin.site.register(TrackTeacherModel)
admin.site.register(ExamGPTModel)
admin.site.register(Donate)
admin.site.register(ContactUs)
admin.site.register(LessonPlanGPTModel)
admin.site.register(ExamGPTWhisperModel)

admin.site.register(LessonGPTWhisperModel)






