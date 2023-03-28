from django.contrib import admin

from .models import todo


from .models import Review
from .models import Contact

admin.site.register(todo)
admin.site.register(Review)
admin.site.register(Contact)

