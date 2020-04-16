from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import JsonData
from .forms import JsonFormnew, AuthUserForm, RegisterUserForm
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages



class MainView(TemplateView):
    template_name = 'bboard/HomePage.html'

    def get(self, request):
       # if request.user.is_authenticated:
            #humans = Human.objects.all()
          #  ctx = {}
            #ctx['humans'] = humans
            return render(request, self.template_name)
       #else:
        #    return render(request, self.template_name, {})

class LoginFormView(LoginView):
    form_class = AuthUserForm
    success_url = '/bboard/'

    template_name = 'bboard/register.html'
    def get_success_url(self):
        return self.success_url


class LogoutView(LogoutView):
    next_page = '/bboard/'



class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    success_url = '/bboard/'
    success_msg = 'User succsesfully registered'
    model = User
    template_name = 'bboard/register.html'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username = username, password = password)
        login(self.request, auth_user)
        return form_valid



#def Homepage(request):
#    return render(request, 'bboard/HomePage.html')



def Checkingdict(dict):

    AttName = dict['AttributeName']

    AttId   = dict['AttributeID']
    data = JsonData.objects.filter(Q(AttributeID__iexact=AttId, AttributeName__iexact=AttName))
    p = len(data)
    if p > 0:
     JsonData.objects.get(AttributeID__iexact=AttId, AttributeName__iexact=AttName).delete()


def Creating_dict_for_database(StringJson):
    finaldict = dict.fromkeys(['AttributeName', 'AttributeID', 'AttributeContent'])  # create empty dictionary
    distros_dict = json.loads(StringJson)


    for distro in distros_dict:  # iterating list
        for key in distro:  # iterating dictionary
            finaldict['AttributeName'] = key  # add key in dict
            finaldict['AttributeID'] = distro[key]['id']  # add id in dict
            for key2 in distro[key]:  # iterating dict of content
                finaldict['AttributeContent'] = distro[key]  # add content in dict
            Checkingdict(finaldict)  # delete double keypair (att + attid)
            JsonData.objects.create(AttributeName=finaldict['AttributeName'],  # add data to database
                                        AttributeID=finaldict['AttributeID'],
                                        AttributeContent=finaldict['AttributeContent'])







class Post(LoginRequiredMixin, View):
        raise_exception = True
        def get(self, request):
            form = JsonFormnew()
            return render(request, 'bboard/post2.html', context={'form': form})

        def post(self, request):
            form = JsonFormnew(request.POST) # get data from form
            d = JsonData.objects.count()
            while d != 0:
                JsonData.objects.filter(id__icontains=d).delete()
                d = d - 1
            if form.is_valid():
                StringJson = form.cleaned_data['JsonDatoForread'] # Get the Json string
                Creating_dict_for_database(StringJson)
                messages.success(request, 'Your post is successfully saved')

            else:
                print(form.errors)

            return render(request, 'bboard/post2.html', context={'form': form})

def Playing(request):
    p = 'Ahoj Evzene!'
    return render(request, 'bboard/create.html')

def Searching(request):
    search_query = request.GET.get('textrequest1', '')
    datas = ''
    dataafterjson = ''
    if search_query:
        datas = JsonData.objects.filter(AttributeName__icontains=search_query).values()
        datotolist = list(datas)

        list22 = []
        for data in datotolist:
            list22.append(data['AttributeName'])
            list22.append(data['AttributeID'])


        d = JsonData.objects.count()
        print (d)
        if d != 0:
            dataafterjson = json.dumps(list22)
            print(dataafterjson)
        else:
            dataafterjson = ' '
    return render(request, 'bboard/postplay.html', context= {'datas': datas, 'search_query' : search_query, 'dataafterjson': dataafterjson})

def Searching_detail(request, AttributeName, id):
    data = JsonData.objects.get(AttributeID__iexact=id, AttributeName__iexact=AttributeName)
    return render(request, 'bboard/postid.html', context={'data': data})








