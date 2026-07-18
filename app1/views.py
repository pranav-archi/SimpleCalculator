from django.shortcuts import render
list1=[]
# Create your views here.
def home(request):
    res=calc(8,4)
    return render(request,'app1/index.html',{'param1':res}) 
def calc(n1,n2):
    sum1=n1+n2
    diff1=n1-n2
    prod1=n1*n2
    div1=n1/n2
    div2=n1//n2
    rem1=n1%n2
    exp1=n1**n2
    list1.append(sum1)
    list1.append(diff1)
    list1.append(prod1)
    list1.append(div1)
    list1.append(div2)
    list1.append(rem1)
    list1.append(exp1)
    return list1