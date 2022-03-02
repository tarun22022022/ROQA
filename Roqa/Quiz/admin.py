from django.contrib import admin
from .models import Quiz, Questions, Options, CorrectOptions, UsersGivingTest, RecordedResponses, TestLogs,TeacherCourse,Classroom

admin.site.register(
    [Quiz, Questions, Options, CorrectOptions,
        UsersGivingTest, RecordedResponses, TestLogs,TeacherCourse,Classroom]
)
# Register your models here.
