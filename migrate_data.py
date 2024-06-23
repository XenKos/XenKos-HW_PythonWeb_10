import mongoengine
from quotes_app.models import Author as MongoAuthor, Quote as MongoQuote
from quotes_app.models import DjangoAuthor, DjangoQuote
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_project.settings")
django.setup()

# Підключення до MongoDB
mongoengine.connect("mongodb+srv://XenKos:<kseni4ka78>@cluster0.02433gx.mongodb.net/XenKos?retryWrites=true&w=majority")

# Міграція авторів
mongo_authors = MongoAuthor.objects()
for mongo_author in mongo_authors:
    author = DjangoAuthor(
        fullname=mongo_author.fullname,
        born_date=mongo_author.born_date,
        born_location=mongo_author.born_location,
        description=mongo_author.description
    )
    author.save()

# Міграція цитат
mongo_quotes = MongoQuote.objects()
for mongo_quote in mongo_quotes:
    author = DjangoAuthor.objects.get(fullname=mongo_quote.author.fullname)
    quote = DjangoQuote(
        quote=mongo_quote.quote,
        author=author,
        tags=", ".join(mongo_quote.tags)
    )
    quote.save()

print("Міграція даних завершена")