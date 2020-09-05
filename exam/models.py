from django.db import models
import math
# Create your models here.
class Branch(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.branch

class Section(models.Model):
    id = models.CharField(max_length=50, primary_key =True)
    section = models.CharField(max_length=2)

    def __str__(self):
        return self.section

class Subject(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    Test = (
        ('--','--'),
        ('WT','WEEKLY-TEST'),
        ('ST','SPECIAL-TEST'),
    )
    tname = models.CharField(max_length=4, choices = Test)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.subject

class Testid(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    sub = models.ForeignKey(Subject, on_delete=models.CASCADE)
    testid = models.CharField(max_length=10)

    def __str__(self):
        return self.testid

class Grade(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    grade = models.CharField(max_length=50)
    branch_id = models.ForeignKey(Branch, on_delete= models.CASCADE)
    section_id = models.ForeignKey(Section, on_delete= models.CASCADE)
    subject_id = models.ManyToManyField(Subject)

    def __str__(self):
        b = Branch.objects.get(branch = self.branch_id)
        sec = Section.objects.get(section = self.section_id)
        return '%s %s %s' %(b.branch,sec.section,self.grade)

class Student(models.Model):
    id = models.CharField(max_length=500)
    erp = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=100)
    grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.erp
          
class Studentmark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Testid, on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self):
        stu = Student.objects.get(erp=self.student)
        tt = Testid.objects.get(testid=self.test)
        return '%s %s' %(stu.erp,tt.testid)
    
    def get_cie(self):
        marks_list = self.marks_set.all()
        m = []
        for mk in marks_list:
            m.append(mk.marks1)
        cie = math.ceil(sum(m[:5])/2)
        return cie

    def to_dict_json(self):
        return {
            'erp': self.student,
            'name': self.test,
            'grade_id': self.mark,}




