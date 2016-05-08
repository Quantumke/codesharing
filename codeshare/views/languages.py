# from django.shortcuts import get_object_or_404
# from django.views.generic.list_detail import object_list
# from codeshare.models import language
#
# def language_detail(request, slug):
#     language = get_object_or_404(language, slug=slug)
#     return object_list(request,
#                        query=language.snippet_set.all()),
#                         paginate_by=20,
#                         template_name="language_detail.html",
#                         extra_context ={'language': language}