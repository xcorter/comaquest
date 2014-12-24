from django.shortcuts import render
from django.views import generic
from main.models import About, Slider, Quest, QuestImage, Contact


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["about"] = About.objects.first()
        context["contact"] = Contact.objects.first()
        context['slider'] = Slider.objects.all()
        quests = Quest.objects.all()
        questImages = QuestImage.objects.all()
        questsArr = []
        for i in range(len(quests)):
            questsArr.append({"quest": quests[i]})
            images = []
            for image in questImages:
                if image.quest == quests[i]:
                    images.append(image)
            questsArr[i]["images"] = images
        context["quests"] = questsArr
        return context