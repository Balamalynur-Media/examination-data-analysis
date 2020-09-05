from import_export import resources
from .models import *

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

class GradeResource(resources.ModelResource):
    class Meta:
        model = Grade

class StudentmarkResource(resources.ModelResource):
    class Meta:
        model = Studentmark
    
class BranchResource(resources.ModelResource):
    class Meta:
        model = Branch