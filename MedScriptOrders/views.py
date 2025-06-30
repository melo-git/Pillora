from django.shortcuts import render

# Create your views here.
# function to insert any prescription, whether text or file, uploaded by user to the database
#table Prescription table and then notify staff
def upload_prescription(request):
    if request.method =='POST':