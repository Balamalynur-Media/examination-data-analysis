from django.http import JsonResponse
from django.shortcuts import render
#from localflavor.br.br_states import STATE_CHOICES
from .forms import TestForm
from .models import *
from tablib import Dataset
from .resources import StudentResource,GradeResource,StudentmarkResource,BranchResource

def index(request):
    context = {}
    student_list = Student.objects.all()
    context['student_list'] = student_list
    return render(request, 'index.html', context)


def student_json(request):
    students = Studentmark.objects.all()
    data = [student.to_dict_json() for student in students]
    response = {'data': data}
    return JsonResponse(response)


def filter_list(request):
    context = {}
    subjects = Subject.objects.all()
    testids = Testid.objects.all()
    context['subjects'] = subjects
    context['testids'] = testids
    return render(request, 'filter_list.html', context)


def filter_dropdown(request):
    context = {}
    context['form'] = TestForm
    # Filtro
    q = request.GET.get('testid')
    if q:
        q = q.replace('.', '')
        students = Studentmark.objects.filter(test=str(q))
        count = len(students)
        sum = 0
        for stu in students:
            sum += stu.mark
        marks = (sum/count)
        context['stuednts'] = students
        context['marks'] = marks
    
    return render(request, 'filter_dropdown.html', context)


def filter_dropdown2(request):
    context = {}
    test = request.GET.get('test')
    subject = request.GET.get('subject')
    context['form'] = TestForm(test, subject)
    # Filtro
    q = request.GET.get('testid')
    up=[]
    mk=[]
    na=[]
    bper=[]
    if q:
        q = q.replace('.', '')
        students = Studentmark.objects.filter(test=str(q))
        count = len(students)
        sum = 0
        for stu in students:
            sum += stu.mark
            marks = round((sum/count),2)
            context['marks'] = marks
            context['students'] = students
            x = stu.student.grade_id.branch_id      
            if x not in up:
                up.append(x)
                context['up']= up
                sts = Studentmark.objects.filter(student__grade_id__branch_id=x,test=str(q))
                s=0
                cot =len(sts)
                for st in sts:
                    s +=st.mark
                m = round((s/cot),2)   
                mk.append(m)
                students = Studentmark.objects.filter(test=str(q))
                co = len(students)
                su = 0
                for stu in students:
                    su += stu.mark
                    mar = round((su/co),2)
                for i in mk:
                    na = round((i/mar)*100,2)
                bper.append(na)
        context['mk']=mk
        context['na']=na   
        context['bper']=bper 
        ziplist = zip(up,mk,bper)
        context['ziplist'] = ziplist
    return render(request, 'filter_dropdown2.html', context)


def subjects_ajax(request):
    tname = request.GET.get('tname')
    subjects = Subject.objects.filter(tname=tname)
    context = {'subjects': subjects}
    return render(request, 'includes/_subjects.html', context)


def subjects_choices_ajax(request):
    tname = request.GET.get('tname')
    subjects = Subject.objects.filter(tname=tname)
    context = {'subjects': subjects}
    return render(request, 'includes/_subjects_choices.html', context)

def testids_ajax(request):
    subject = request.GET.get('subject')
    testids = Testid.objects.filter(sub=subject)
    context = {'testids': testids}
    return render(request, 'includes/_testids.html', context)


def testids_choices_ajax(request):
    subject = request.GET.get('subject')
    testids = Testid.objects.filter(sub=subject)
    context = {'testids': testids}
    return render(request, 'includes/_testids_choices.html', context)

def simple_upload(request):
    if request.method == 'POST':
        student_resource = StudentResource()
        dataset = Dataset()
        new_students = request.FILES['myfile']

        imported_data = dataset.load(new_students.read())
        result = student_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            student_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

def simple_upload(request):
    if request.method == 'POST':
        grade_resource = GradeResource()
        dataset = Dataset()
        new_grades = request.FILES['myfile']

        imported_data = dataset.load(new_grades.read())
        result = grade_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            grade_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

def simple_upload(request):
    if request.method == 'POST':
        sm_resource = StudentmarkResource()
        dataset = Dataset()
        new_sm = request.FILES['myfile']

        imported_data = dataset.load(new_sm.read())
        result = sm_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            sm_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

def simple_upload(request):
    if request.method == 'POST':
        branch_resource = BranchResource()
        dataset = Dataset()
        new_branch = request.FILES['myfile']

        imported_data = dataset.load(new_branch.read())
        result = branch_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            branch_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

