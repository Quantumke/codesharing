from django.db import models
from pygments import lexers

# Create your models here.

class language(models.Model):
	language_name=models.CharField(unique=False, max_length=100)
	language_code=models.CharField(unique=False, max_length=100)
	slug= models.SlugFiels(max_length=100)
	mime_type=models.CharFiels(max_length=100)
	date=models.DateFiels(default=DateTime.now,blank=False)
	

	class Meta:
		ordering=['-date']
	def __unicode__(self):
		return self.language_name
	def get_absolute_url(self):
		return('language_details', (), {'slug':self.slug})
	get_absolute_url = models.permalink(get_absolute_url)
	#now ill return appropriate lexer for a language

	def get_lexer(self):
		return lexers.get_lexer_by_name(self.language_code)

	
