

import re

from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Word, Description, WordVersion, WordLocation, Tag
from .forms import WordForm
from language.models import Language
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



class WordView(DetailView):
    template_name = 'word/display.html'
    http_method_names = ['get']
    model = Word

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'descriptions': self.object.desc.all(),
            'synonyms': self.object.synonyms.all(),
            'locations': self.object.locations.all(),
        })
        return context


@method_decorator(login_required, name='dispatch')
class SuggestView(TemplateView):
    """
    User story:
      Word: Kusko
      WordVersion: Quechua Ayacuchano where the word they use is Kusko
      Language: Quechua
    """
    template_name = 'word/suggest.html'
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'versions': WordVersion.objects.all(),
        })
        return context

    def post(self, request, *args, **kwargs):
        word_obj = None
        if request.method == "POST" and "file" in request.FILES:
            form = WordForm(request.POST, request.FILES)
            if form.is_valid():
                print("$"*10, "form is valid")
                word_obj = form.save(commit=False)
                word_obj.submitter = request.user.profile
                word_obj.audio = request.FILES["file"]
                word_obj.save()
            else:
                print("$" * 10, form.errors)

        word = request.POST.get('word')
        tags = request.POST.getlist('tags')
        ipa = request.POST.get('ipa')
        default_variant_str = request.POST.get('language')
        location = request.POST.get('location')
        synonyms = request.POST.getlist('synonyms')
        wiktionary_link = request.POST.get('wiktionary_link')

        desc_list = self.create_descriptions(request)

        language_object = Language.objects.get(default_variant=default_variant_str)

        # TODO: so far all word versions of a language can be associated with
        # TODO: only one variant (the language's own default variant)
        word_version = WordVersion.objects.filter(language=language_object)[0]

        if word_obj:
            word_obj.word = word
            word_obj.ipa = ipa
            word_obj.status = 'SUG'
            word_obj.version = word_version
            word_obj.wiktionary_link = wiktionary_link
            word_obj.save()
        else:
            word_obj = Word.objects.create(
                word=word,
                ipa=ipa,
                status='SUG',
                version=word_version,
                submitter=request.user.profile,
                wiktionary_link=wiktionary_link,
            )

        for desc in desc_list:
            word_obj.desc.add(desc)

        for tag in tags:
            tag_object, _ = Tag.objects.get_or_create(name=tag.lower())
            word_obj.tags.add(tag_object)

        for syn in synonyms:
            syn_object, _ = Word.objects.get_or_create(
                submitter=request.user.profile,
                word=syn.lower(),
            )
            word_obj.synonyms.add(syn_object)
        if location:
            location = WordLocation.objects.create(
                word=word_obj,
                place=location,
                submitter=request.user.profile,
            )

        query = word
        choices = list(Word.objects.all().values_list("word", flat=True))
        # Get a list of matches ordered by score, the top 3
        results = process.extract(query, choices)[0:3]
        results = [x[0] for x in results]
        print("################results", results)

        url = reverse_lazy('word:word_view', kwargs={'pk': word_obj.id})
        return HttpResponseRedirect(url)

    def create_descriptions(self, request):
        """Generate list of description objects for one word,
        each description object is in a different language and contains both
        short and long description strings

        {
            'english': {'desc_short': 'short mouse', 'desc_long': 'long mouse'},
            'spanish': {'desc_short': 'raton corto', 'desc_long': 'raton largo'}
        }
        :param request: original django request
        :return: list of Description objects
        """
        descriptions = {}
        for key, value in request.POST.items():
            if not value:
                continue
            if key.startswith("desc_long") or key.startswith("desc_short"):
                key, language = key.rsplit("_", 1)
                try:
                    desc = descriptions[language]
                except KeyError:
                    language_obj = Language.objects.get(name=language)
                    desc = Description(language=language_obj)
                    descriptions[language] = desc
                setattr(desc, key, value)
        descriptions = list(descriptions.values())
        Description.objects.bulk_create(descriptions)
        return descriptions


class EditView(UpdateView):
    model = Word
    fields = [
        'word', 'ipa', 'desc', 'tags', 'audio', 'wiktionary_link', 'synonyms'
    ]
    template_name_suffix = '_update_form'


class WordListView(ListView):
    http_method_names = ['get']
    paginate_by = 10
    template_name = 'word/word_list.html'

    def get_queryset(self):
        words = Word.objects.all()
        words = words.order_by('creation_date')

        return words


class BareWordView(DetailView):
    template_name = 'word/word_detail.html'
    http_method_names = ['get']
    model = Word

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'descriptions': self.object.desc.all(),
            'translations': self.object.translations.all(),
        })
        return context
