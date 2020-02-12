from django.contrib import admin
from lotto.models import GuessNumbers
#from .models import GuessNumbers 같은 폴더라 lotto 생략가능

# Register your models here.
admin.site.register(GuessNumbers)
