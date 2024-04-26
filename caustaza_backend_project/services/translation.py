from modeltranslation.translator import TranslationOptions, translator

from .models import Service, ServiceIndex


class ServiceTranslationOptions(TranslationOptions):
    fields = ("title", "short_content")


class ServiceIndexTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "description")


translator.register(Service, ServiceTranslationOptions)
translator.register(ServiceIndex, ServiceIndexTranslationOptions)
