from django import forms
from .models import ItemModel,plat_choice,lang_choice,GenreList


select = forms.Select(attrs={'class':'ui selection dropdown'})
multiselect = forms.SelectMultiple(attrs={'class':'ui selection dropdown'})

class CreateForm(forms.ModelForm):
    genre = forms.ModelMultipleChoiceField(GenreList.objects,widget=multiselect)
    platform = forms.ChoiceField(widget=select, choices=plat_choice)
    language = forms.ChoiceField(widget=select, choices=lang_choice)
    class Meta:
        model = ItemModel
        exclude = ['rating','ratingcount']