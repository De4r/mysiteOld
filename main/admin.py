from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [("Title/date", {'fields': ["tutorialTitle", "tutorialPublished"]}),
                 ("URL", {'fields': ["tutorial_slug"]}),
                 ("Series", {'fields': ["tutorial_series"]}),
                 ("Content", {'fields': ["tutorialContent"]})]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},

    }

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)
