from django.db import models
from pygments import formatters, highlight, lexers
from tagging.fields import TagField
from markdown import markdown
import datetime
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

	def save(self, force_insert=False,force_update=False):
		if not self.id:
			self.pub_date=deatetime.datetime.now()
		self.update_date=datetime.datetime.now()
		self.description_html =markdown(self.description)
		self.highlighted_code = self.highlight()
		super(Snippet, self). save(force_insert, force_update)
	def get_absolute_url(self):
		return('snippet_detail',(), {'object_id',self.id})
	get_absolute_url= models.permalink(get_absolute_url)
	

	def highlight(self):
		return highlight(self.code, self.language.get_lexer(),formatters.HtmlFormatter(linenos=True))
		#linenon = True ->show line numbers
