from django.db import models

class Candidates(models.Model):
    event_details = models.CharField(max_length=50, blank=True, null=True)
    job_position = models.CharField(max_length=50, blank=True, null=True)
    recruiter_alert = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    education_qualification = models.CharField(max_length=50, blank=True, null=True)
    contact_no_primary = models.CharField(max_length=15, blank=True, null=True)  # Adjust the max_length accordingly
    contact_no_alternate = models.CharField(max_length=15, blank=True, null=True)  # Adjust the max_length accordingly
    address_line = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)  # Adjust the max_length accordingly
    education_specialization_other = models.TextField(blank=True, null=True)
    education_institution_other = models.TextField(blank=True, null=True)
    years_of_experience = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    current_employer = models.CharField(max_length=100, blank=True, null=True)
    current_designation = models.TextField(blank=True, null=True)
    current_monthly_salary = models.IntegerField(blank=True, null=True)
    expected_monthly_salary = models.IntegerField(blank=True, null=True)
    notice_period = models.CharField(max_length=50, blank=True, null=True)
    photo_path = models.ImageField(upload_to='photos/', blank=True, null=True)  # Adjust the upload_to path accordingly
    resume_path = models.FileField(upload_to='resumes/', blank=True, null=True)  # Adjust the upload_to path accordingly
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    geo_location = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField( max_length=50,blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.CharField( max_length=50,blank=True, null=True)


    
