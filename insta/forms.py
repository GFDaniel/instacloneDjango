from django import forms
from .models import Post, User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import ( PrependedText, PrependedAppendedText, FormActions )


class PostForm(forms.ModelForm):
	helper = FormHelper()
	helper.from_method = "POST"
	helper.add_input(Submit('Post', 'Post', css_class='btn-primary'))

	class Meta:
		model = Post
		fields = [
			'image',
			'caption'
		]