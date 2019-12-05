from django import forms

class TweetForm(forms.Form):
    tweet_url = forms.CharField(label='Tweet URL', max_length=300,
            widget=forms.TextInput(attrs={'class':'form-control form-control-lg' ,'placeholder':'Enter Tweet URL to check!'}))