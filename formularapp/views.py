from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import MultiStepFormModel

def multistepform(request):
    return render(request,"multistepform.html")

def multistepform_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("multistepform"))
    else:

        privat_oder_gewerbe = request.POST.get("privat_oder_gewerbe")
        strom_oder_gas = request.POST.get("strom_oder_gas","-")
        personen_im_haushalt = request.POST.get("personen_im_haushalt","-")
        wohnflaeche = request.POST.get("wohnflaeche","-")
        gewerbeflaeche = request.POST.get("gewerbeflaeche","-")
        grundversorger = request.POST.get("grundversorger")
        oekotarif = request.POST.get("oekotarif")
        plz=request.POST.get("plz")
        ort=request.POST.get("ort")
        rueckruftermin = request.POST.get("rueckruftermin")
        nachricht=request.POST.get("nachricht")

        try:
            multistepform = MultiStepFormModel(privat_oder_gewerbe = privat_oder_gewerbe,
                                                strom_oder_gas = strom_oder_gas,
                                                personen_im_haushalt = personen_im_haushalt,
                                                wohnflaeche = wohnflaeche,
                                                gewerbeflaeche = gewerbeflaeche,
                                                grundversorger = grundversorger,
                                                oekotarif = oekotarif,
                                                plz=plz,
                                                ort=ort,
                                                rueckruftermin = rueckruftermin,
                                                nachricht=nachricht)
            multistepform.save()
            messages.success(request,"Data Save Successfully")
            return HttpResponseRedirect(reverse('multistepform'))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('multistepform'))
