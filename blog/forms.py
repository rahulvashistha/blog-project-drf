from django import forms
from django.forms import ModelForm, fields, widgets
from blog.models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

#create your forms here

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # using crispy forms helper to change form_method and layout
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'title',
            'content',
            'author',
            'views',
            'slug',
            Submit('submit', 'Submit', css_class='btn btn-sucess mt-3 p-2')
        )
