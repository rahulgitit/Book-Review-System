from django import forms
from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description','genre','isbn','publication_date','average_rating')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholer':'Enter Book Title'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'genre':forms.Select(attrs={'class':'form-select'}),
            'isbn':forms.TextInput(attrs={'class':'form-control'}),
            'publication_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'average_rating':forms.NumberInput(attrs={'class':'form-control'})
        }