from django.contrib import admin

from . import models


class TicketAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image', 'user', 'time_created')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'headline', 'rating', 'user', 'time_created')


admin.site.register(models.Ticket, TicketAdmin)
admin.site.register(models.Review, ReviewAdmin)
