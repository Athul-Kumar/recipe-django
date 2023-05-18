from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

peoples = [

    {
        'first_name': 'Athul',
        'last_name':'Kumar',
        'age': 25,
        'Interest':'coding',
        'Goals':[
            'Become a financial independent',
            'Become a well known programmer',
            'Become a responsible man'
        ]
    },
    {

        'first_name': 'Amritha',
        'last_name':'Krishnan',
        'age': 26,
        'Interest':'Scientist',
        'Goals':[
            'Become a financial independent',
            'Become a well known Scientist',
            'Become a responsible woman'
        ]
    }
]


# for people in peoples:
#     print(people)

print(peoples[1]['first_name'])

def home(request):

    context = {'peoples':peoples,
               'pages': 'Home Page'}


    return render(request, "home/index.html", context)

def contact(request):

    context = {'pages':'Contact page'}

    return render(request, "home/contact.html", context)

def about(request):

    context = {'pages': 'About Page'}
    return render(request, "home/about.html",context)