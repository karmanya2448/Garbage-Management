from django.db import models


class user_details(models.Model):
	userProfilePicture = models.ImageField(upload_to = r'', default = r'')
	userName= models.CharField(max_length=25)
	userDay= models.IntegerField()
	userMonth= models.IntegerField()
	userYear= models.IntegerField()
	userAddress= models.TextField()
	userEmail=models.CharField(max_length=50)
	userPhno=models.BigIntegerField()
	userUname=models.CharField(max_length=25)
	userPwrd=models.CharField(max_length=25)
	userType = models.IntegerField()
	isLoggedIn = models.BooleanField()
	device_id = models.CharField(max_length = 50, blank = True, null = True)
	notifications =  models.IntegerField(default=0)

	def __str__(self):
		return self.userName

	class Meta:
		verbose_name_plural = "User Info"

class driver_info(models.Model):
	driver_id = models.ForeignKey('user_details', on_delete=models.CASCADE)
	driverLicPicture = models.ImageField(upload_to = '', default = '')
	driverDayLIC=models.IntegerField()
	driverMonthLIC=models.IntegerField()
	driverYearLIC=models.IntegerField()
	driverLino=models.CharField(max_length=15)
	driverVeno=models.CharField(max_length=10)
	approved = models.BooleanField(null=True, blank=True)
	driverArea=models.CharField(max_length=20, blank= True, null=True)

from django.db import models
from django.contrib.auth.models import User

# Model to store extra information for drivers
class DriverDetails(models.Model):
    # This links the driver details to a specific user in Django's built-in User model.
    # If a User is deleted, their associated DriverDetails will also be deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    phone_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=20, unique=True)
    vehicle_number = models.CharField(max_length=20, unique=True)
    address = models.TextField()

    # This defines how the object will be displayed (e.g., in the admin panel)
    def __str__(self):
        return self.user.username

# Model to store information about a scheduled garbage pickup
class PickupSchedule(models.Model):
    # Defines the choices for the status field
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Assigned', 'Assigned'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    # A regular user who requested the pickup. A user can have many pickups.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The driver assigned to the pickup. This can be blank initially.
    # If a driver is deleted, this field becomes null (the pickup is unassigned).
    driver = models.ForeignKey(DriverDetails, on_delete=models.SET_NULL, null=True, blank=True)
    
    pickup_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    
    # Automatically records the date and time when a request is created.
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pickup for {self.user.username} on {self.pickup_date} ({self.status})"

class garbageDetails(models.Model):
	garbagePicture = models.ImageField(upload_to = '', default = '')
	#garbagePicture = models.TextField()
	#garbagePictureVerification = models.TextField(blank=True, null=True)
	garbagePictureVerification = models.ImageField(upload_to = '', default = '', blank=True, null=True)
	geotag = models.CharField(max_length=255, blank=True, null=True)
	user_id = models.IntegerField(max_length=255, blank=True, null=True)
	time = models.CharField(max_length=25, blank=True, null=True)
	driver_id = models.IntegerField(blank=True, null=True)
	date = models.CharField(max_length=25, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Garbage Details"

class schedule(models.Model):
	user_id = models.IntegerField()
	address = models.TextField(blank=True, null=True)
	days = models.IntegerField()
	community = models.BooleanField()
	noOfHouses = models.IntegerField(blank=True, null=True)
	specialInst = models.TextField(blank=True, null=True)
	driver_id = models.IntegerField(blank=True, null=True)
	landmark = models.CharField(max_length=30, blank=True, null=True)
	driver_completion = models.IntegerField(blank=True, null=True)
	user_approval = models.IntegerField(blank=True, null=True)

	class Meta:
		verbose_name_plural = "Schedule"