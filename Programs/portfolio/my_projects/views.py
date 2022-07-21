from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projects=[
    {"id":'1',
    "name":"ScreenSaver",
    "Language":["C++"],
    "Additional Libraries":[],
    "Description":"Displays random balls and  terrain in 3D which can collide",
    "url":"some_random url1"
    },
    {
    "id":'2',
    "name":"AC Circuit Solver",
    "Language":["C++","js"],
    "Additional Libraries":["Matrix Computation Library","SVG Rendering"],
    "Description":"Given a circuit text file input , render it on html page and also show the current and voltage values.",
    "url":"some_random url2"
    }
]

def index(request):
    return HttpResponse('<h1> Hello World!</h1>')
def home(request):
    return render(request,'my_projects/home.html',context={"all_my_projects": projects,})

def project(request,id):
    project_det=None
    name=None
    for prj in projects:
        if(id==prj["id"]):
            project_det=prj
            name=prj['name']
    return render(request,'my_Projects/project.html',context={"project_name": name , "project_details": project_det,})