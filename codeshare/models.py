from django.db import models
from pygments import lexers
from tagging.fields import TagField

# Create your models here.

class language(models.Model):
	language_name=models.CharField(unique=False, max_length=100)
	language_code=models.CharField(unique=False, max_length=100)
	slug= models.SlugFiels(max_length=100)
	mime_type=models.CharField(max_length=100)
	date=models.DateField(default=DateTime.now,blank=False)
	

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

class snippet(model.Model):
	title= model.CharField(max_length=100, unique=False)
	language=models.ForeignKey(language)
	author=models.ForeignKey(User)
	description=models.Textfield()
	description_html=models.TextField(editable=False)
	code=models.TextField()
	highlighted_code=models.TextField(editable=False)
	tags=TagField()
	pub_date=models.DateField(default=datetime.now)
	update_date=models.DateField(editable=False)

	class Meta():
		ordering=['-pub_date']

	def __unicode__(self):
		return self.title

	
