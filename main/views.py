from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from main.models import *
from django.utils import timezone
from django.core import serializers
from django.http import JsonResponse
import datetime, time as ftime
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


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


def error_json_response(message):
    return JsonResponse({"success": False, "message": message}, status=400)


def json_response(message):
    return JsonResponse({"success": True, "message": message}, status=200)


class OrderView(CreateView):
    template_name = 'main/order.html'

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(date__gte=timezone.now())
        times = Time.objects.all()
        order_json = serializers.serialize("json", orders)
        quests = Quest.objects.all()
        form = {
            'times': times,
            'order_json': order_json,
            'quests': quests
        }
        return render(request, self.template_name, form)

    def post(self, request, *args, **kwargs):
        try:
            time = int(request.POST['time'])
            time_obj = Time.objects.get(pk=time)
            if not time_obj:
                raise Exception("Время не найдено")
            date = request.POST['date']
            timestamp = int(ftime.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()))
            current_time = int(ftime.time()) - 86400
            if timestamp < current_time:
                raise Exception("Попытка забронировать на прошедшие даты")
            quest = int(request.POST['quest'])
            quest = Quest.objects.get(pk=quest)
            if not quest:
                return error_json_response("Wrong request")
            wrong_time = True
            for available_time in quest.schedule.all():
                if available_time == time_obj:
                    wrong_time = False
            if wrong_time:
                raise Exception("Попытка забронировать на несуществующее время")
            first_name = request.POST['firstName'].strip()
            last_name = request.POST['lastName'].strip()
            phone = request.POST['phone'].strip()
            email = request.POST['email'].strip()
            comment = request.POST['comment'].strip()
            participant_amount = int(request.POST['participantAmount'])
            if first_name == "" or phone == "" or email == "" or last_name == "":
                return error_json_response("Заполните все поля")
            try:
                Order.objects.get(time=time_obj, quest=quest, date=date)
            except Order.DoesNotExist:
                quest_order = Order(
                    quest=quest,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    time=time_obj,
                    date=date,
                    comment=comment,
                    participant_amount=participant_amount
                )
                quest_order.save()
                try:
                    from django.core.mail import send_mail
                    text = "На " + time_obj.time + ", " + date + " был забронирован квест " + quest.title + ".\n" + \
                           "Имя: " + first_name + ".\n" + \
                           "Фамилия: " + last_name + ".\n" + \
                           "Телефон: " + phone + ".\n" + \
                           "Email: " + email + ".\n" + \
                           "Комментарий: " + comment + ".\n" + \
                           "Количество человек: " + str(participant_amount)
                    send_mail(
                        "Бронирование comaquest",
                        text,
                        "comaquest@mailer.ru",
                        ["comaquest@gmail.com"],
                        fail_silently=False
                    )
                except Exception as e:
                    logger.error("Exception when send email: " + str(e))
                return json_response("Ваша заявка принята")
            else:
                return error_json_response("Данное время уже забранировано")
        except Exception as e:
            logger.error(str(e))
            return error_json_response("Неизвестная ошибка")