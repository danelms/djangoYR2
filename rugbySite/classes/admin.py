from django.contrib import admin
from .models import Player, Position

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
