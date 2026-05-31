from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def unidad1(request):
    return render(request, 'unidad1.html')

def unidad2(request):
    return render(request, 'unidad2.html')

def unidad3(request):
    return render(request, 'unidad3.html')

def unidad4(request):
    return render(request, 'unidad4.html')

def unidad5(request):
    return render(request, 'unidad5.html')

def arduino(request):
    return render(request, 'arduino.html')

def rp2040(request):
    return render(request, 'rp2040.html')

def emu(request):
    return render(request,'Emu.html')