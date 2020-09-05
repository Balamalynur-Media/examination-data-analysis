from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Branch,Grade,Section,Testid,Student,Studentmark,Subject
# Register your models here.

admin.site.register(Section)
admin.site.register(Testid)
admin.site.register(Subject)

@admin.register(Student)
class studentAdmin(ImportExportModelAdmin):
    pass

@admin.register(Grade)
class gradeAdmin(ImportExportModelAdmin):
    pass

@admin.register(Studentmark)
class studentmarkAdmin(ImportExportModelAdmin):
    pass

@admin.register(Branch)
class branchAdmin(ImportExportModelAdmin):
    pass