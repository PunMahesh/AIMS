
#creating table for farmer kyc that extends User table where user id is in one to one relation
class farmerKYC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=225)
    MiddleName = models.CharField(max_length=225)
    Last_name = models.CharField(max_length=225)
    Gender = models.CharField(max_length=50)
    MaritualStatus = models.CharField(max_length=50)
    Dob = models.DateField(default=date.today)
    Nationality = models.CharField(max_length=225)
    Citizenship = models.IntegerField(default=0)
    Passport = models.IntegerField(default=0)
    Residential = models.CharField(max_length=50)
    FatherName = models.CharField(max_length=225)
    MotherName = models.CharField(max_length=225)
    GrandfatherName = models.CharField(max_length=225)
    GrandMotherName = models.CharField(max_length=225)
    SpouseName = models.CharField(max_length=225)
    SonName = models.CharField(max_length=225)
    DaughterName = models.CharField(max_length=225)
    Country = models.CharField(max_length=225)
    District = models.CharField(max_length=225)
    Province = models.CharField(max_length=225)
    Municipality = models.CharField(max_length=225)
    WardNo = models.CharField(max_length=225)
    Street = models.CharField(max_length=225)
    PassportPhoto = models.ImageField(upload_to="images/docs")
    CitizenProof = models.CharField(max_length=50)
    FrontPic = models.ImageField(upload_to="images/docs")
    BackPic = models.ImageField(upload_to="images/docs")
    Verify = models.BooleanField(default=False)