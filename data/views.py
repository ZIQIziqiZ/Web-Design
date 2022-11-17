from django.shortcuts import render
from data.models import PassRate,Distribution

# Create your views here.
def Finance(request):
    level1 = PassRate.objects.filter(title="CFA考试").filter(subject="Level I")
    level2 = PassRate.objects.filter(title="CFA考试").filter(subject="Level II")
    level3 = PassRate.objects.filter(title="CFA考试").filter(subject="Level III")
    return render(request,'Eva-Finance.html',context={'level1':level1,'level2':level2,'level3':level3}) 

def Accounting(request):
    phase1 = PassRate.objects.filter(title="CPA考试").filter(subject="专业阶段")
    phase2 = PassRate.objects.filter(title="CPA考试").filter(subject="综合阶段")
    AB = PassRate.objects.filter(title="ACCA考试").filter(subject="AB")
    MA = PassRate.objects.filter(title="ACCA考试").filter(subject="MA")
    FA = PassRate.objects.filter(title="ACCA考试").filter(subject="FA")
    LW = PassRate.objects.filter(title="ACCA考试").filter(subject="LW")
    PM = PassRate.objects.filter(title="ACCA考试").filter(subject="PM")
    TX = PassRate.objects.filter(title="ACCA考试").filter(subject="TX")
    FR = PassRate.objects.filter(title="ACCA考试").filter(subject="FR")
    AA = PassRate.objects.filter(title="ACCA考试").filter(subject="AA")
    FM = PassRate.objects.filter(title="ACCA考试").filter(subject="FM")
    AFM = PassRate.objects.filter(title="ACCA考试").filter(subject="AFM")
    APM = PassRate.objects.filter(title="ACCA考试").filter(subject="APM")
    ATX = PassRate.objects.filter(title="ACCA考试").filter(subject="ATX")
    AAA = PassRate.objects.filter(title="ACCA考试").filter(subject="AAA")
    y18 = PassRate.objects.filter(title="CPA考试").filter(date="2018-01-01").exclude(subject="专业阶段").exclude(subject="综合阶段")
    y19 = PassRate.objects.filter(title="CPA考试").filter(date="2019-01-01").exclude(subject="专业阶段").exclude(subject="综合阶段")
    y20 = PassRate.objects.filter(title="CPA考试").filter(date="2020-01-01").exclude(subject="专业阶段").exclude(subject="综合阶段")
    y21 = PassRate.objects.filter(title="CPA考试").filter(date="2021-01-01").exclude(subject="专业阶段").exclude(subject="综合阶段")
    return render(request,'Eva-Accounting.html',context={'phase1':phase1,'phase2':phase2,
                                                         'AB':AB,'MA':MA,'FA':FA,'LW':LW,'PM':PM,'TX':TX,
                                                         'FR':FR,'AA':AA,'FM':FM,'AFM':AFM,'APM':APM,'ATX':ATX,'AAA':AAA,
                                                         'y18':y18,'y19':y19,'y20':y20,'y21':y21})

def Language(request):
    Eng = PassRate.objects.filter(title="英语").filter(subject="四六级")
    CET4 = Distribution.objects.filter(title="英语四级")
    CET6 = Distribution.objects.filter(title="英语六级")
    return render(request,'Eva-Language.html',context={'Eng':Eng,'CET4':CET4,'CET6':CET6})
