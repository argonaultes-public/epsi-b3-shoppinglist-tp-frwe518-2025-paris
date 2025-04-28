from django import forms

class ItemForm(forms.Form):
    item_name_field = forms.CharField(label='Item Name')
    item_serial_field = forms.IntegerField(label='Item Serial')