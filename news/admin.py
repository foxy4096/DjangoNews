from django.contrib import admin


from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.reporter = request.user
        return super().save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(reporter=request.user)

    list_display = ('headline', 'reporter', 'pub_on')
    exclude = ('reporter',)

admin.site.register(Article ,ArticleAdmin)