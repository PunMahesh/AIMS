from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
=======
from .models import User, addcrop

#Register your models here.
admin.site.register(User)
admin.site.register(addcrop)
>>>>>>> Master
