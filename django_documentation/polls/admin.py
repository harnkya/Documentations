# admin sayfasında göstereceğin uygulamaları burada import ediyorsun

from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2  # 2 extra boş form bırakıyor
    


# TabularInline kısmı yatay göstermeye yarayan ayrı bir class. Yani choice'ları dikey göstersin diyorsun.
# dikey göstermek istersen de StackedInline kullanacaksın.

# ana model question, ilişkili model choice. choiceları question altında göstermek için choice'ları ayrı bir classta tanımlayıp sonrasında o class'ı question'ın inline attribute'una kaydediyor.


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    # asıl olay burada, choice'ları question'lara dahil ediyor.

    list_display = ["question_text", "pub_date", "was_published_recently"]

    list_filter = ["pub_date"]
    search_fields = ["question_text"]  # buna göre filtreleyerek arayabilirsin



admin.site.register(Question, QuestionAdmin)


"""
class QuestionAdmin(admin.ModelAdmin):
Django'nun ModelAdmin sınıfından türeyen bir sınıf tanımlıyorsunuz.
Bu sınıf, admin panelinde modelin nasıl görüneceğini, düzenleneceğini veya filtreleneceğini kontrol eder.
Burada, fields özelliği kullanılarak, düzenleme formunda hangi alanların (fields) görüneceği ve sıralamaları belirleniyor.
"""
