from django.shortcuts import render
from .forms import UserForm
from django.views import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


# Create your views here.

### FBV

def user_form_fbv(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return render(request, 'result.html',{'data': form.cleaned_data})
    else:
        form = UserForm()

    return render (request,'form.html',{'form': form, 'method': 'FBV'})


### CBV 


class UserFormCBV(View):
    def get(self, request):
        form = UserForm()
        return render(request,'form.html',{'form': form, 'method':'CBV'})
    
    def post(self,request):
        form = UserForm(request.POST)
        if form.is_valid():
            return render(request,'result.html', {'data': form.cleaned_data})
        return render(request,'form.html',{'form': form,'method': 'CBV'})
    


### GenericV


class UserFormGenericView(FormView):
    #tempalte_name = 'form.html'
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('form_generic')


    def form_valid(self,form):
        return render(self.request,'result.html',{'data': form.cleaned_data})
    
        

