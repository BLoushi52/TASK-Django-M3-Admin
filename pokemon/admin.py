from django.contrib import admin

from pokemon.models import Pokemon
from .models import Pokemon
# Register your models here.

admin.site.register(Pokemon)