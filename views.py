from django.shortcuts import render

# Create your views here.
context = {
	'title':'About|lab TI',
	'judul':'About Us',
	'copyright':'2021 lab TI UMS',
}

def daftar(request):
	return render(request,'about/daftar.html',context)

def anggota(request):
	return render(request,'about/anggota.html',context)