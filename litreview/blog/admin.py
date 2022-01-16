from django.contrib import admin

from . import models


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'user', 'time_created')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'headline', 'rating', 'user', 'time_created')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user',  'followed_user')


admin.site.register(models.Ticket, TicketAdmin)
admin.site.register(models.Review, ReviewAdmin)
admin.site.register(models.UserFollows, FollowAdmin)
