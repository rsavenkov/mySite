from afrolov.models import Choice_afrolov, Question_afrolov

Question_afrolov.objects.all()

Question_afrolov.objects.filter(id=1)
Question_afrolov.objects.filter(Question_afrolov_text__startswith='What')

from django.utils import timezone

current_year = timezone.now().year
Question_afrolov.objects.get(pub_date__year=current_year)

Question_afrolov.objects.get(id=2)
Question_afrolov.objects.get(pk=1)

q = Question_afrolov.objects.get(pk=1)
q.was_published_recently()

q = Question_afrolov.objects.get(pk=1)
q.Choice_afrolov_set.all()

q.Choice_afrolov_set.create(Choice_afrolov_text='Not much', votes=0)
q.Choice_afrolov_set.create(Choice_afrolov_text='The sky', votes=0)
c = q.Choice_afrolov_set.create(Choice_afrolov_text='Just hacking again', votes=0)
c.Question_afrolov
q.Choice_afrolov_set.all()
q.Choice_afrolov_set.count()

Choice_afrolov.objects.filter(Question_afrolov__pub_date__year=current_year)
c = q.Choice_afrolov_set.filter(Choice_afrolov_text__startswith='Just hacking')
c.delete()
