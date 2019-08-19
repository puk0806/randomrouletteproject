from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    return render(request,'home.html')

# 홈에서 체크박스 클릭 반응
def home(request):
    check_food = ''
    if request.method == 'POST':
        check_values = request.POST.getlist('menu')
        check_food = check_values
        #if koreanFood:
        #    food = 'Korean'
        return render(request,'home.html',{'food':check_food})
        #return redirect('home')
    else:
        return render(request,'home.html',{'food':check_food})    
