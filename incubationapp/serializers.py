from rest_framework import serializers
from incubationapp.models import Company, CompanyBank, Medicine, MedicalDetails, Employee, Customer, Bill,CustomerRequest, CompanyAccount, EmployeeBank, EmployeeSalary
    

class CompanySerliazer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=["name","license_no","address","contact_no","email","description"]