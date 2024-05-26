from django.shortcuts import render ,redirect
from .models import *
from django.views import View   
from .tools import *
from django.contrib import messages
import telebot





token = "7241155398:AAFXcoUeaSpCxftOhqanm90GL6EQ-G4GCzU"
bot = telebot.TeleBot(token)

class HomePageView(View):
    def get(self , request):
        workers = Worker.objects.order_by('-reg_date')[:8]
        faq = FAQ.objects.all()
        video_choice_we = VideoChoice.objects.order_by("-reg_date")[:4]
        sponsor =  Sponsor.objects.order_by()[:8]
        ourvideo = OurVideo.objects.latest("-id")
        context = {
            'workers': workers,
            'faq':faq,
            "video":video_choice_we,
            "sponsor":sponsor,
            "ourvideo":ourvideo
        }
        return render(request , "index.html" , context)


class CreateStudentView(View):  
  
   def post(self, request):
        
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        course = request.POST.get('course') 
        print(request.POST)
        if validate_phone_number(phone):
            if validate_student(phone):
                age_str = int(age)
                if 9 <= age_str <= 30:
                    RegisterStudent.objects.create(field_of_study=course, name=name, phone_number=phone, age=age)
                    user_id = '--4271050685'
                    message_text = (
    f"""
#kurs: {course}\n
    
Ismi: {name}\n
    
Yoshi: {age}\n
    
Telefon raqami: +{phone}\n"""
            )

                    bot.send_message(user_id, message_text )   
                    messages.success(request, 'Arizangiz qabul qilindi tez orada administratorlarimiz siz bilan boglanishadi.')
                else:
                    messages.error(request , "Sizning yoshingiz tog'ri kelmaydi yosh chegarasi 9-30 ")
            else:
                messages.error(request , 'Bunday raqam dan ariza berilgan. Arizangiz qabul qilingan.')
                
        else:
            messages.error(request, 'Telefon raqami noto‘g‘ri. Raqamni toʻgʻri formatda kiriting: 998XXXXXXXXX .')
        

        return redirect("main:home")
    
    
class ConsultingView(View):
    def post(self,request):
        name = request.POST.get('name')
        phone = request.POST.get('number')
        age = request.POST.get('age')
        if validate_phone_number(phone):
                age_str = int(age)
                if 9 <= age_str <= 30:
                    student = Consulting.objects.create(name=name, phone=phone, age=age)
                    user_id = '-1002119623085'
                    #'5786792768'
                    message_text = (
    f"""
#konsultatsiya\n
    
Ismi: {name}\n
    
Yoshi: {age}\n
    
Telefon raqami: +{phone}\n"""
            )

                    bot.send_message(user_id, message_text )    
                    messages.success(request, 'Arizangiz qabul qilindi tez orada administratorlarimiz siz bilan boglanishadi.')
                    
                else:
                    messages.error(request , "Sizning yoshingiz tog'ri kelmaydi yosh chegarasi 9-30 ")
           
                
        else:
            messages.error(request, 'Telefon raqami noto‘g‘ri. Raqamni toʻgʻri formatda kiriting: 998XXXXXXXXX .')
        return redirect('main:home')
    
    









'''

'''



'''
<div class="notification-bar" id="notificationBar">
        {% if messages %}
          <ul class="messages">
            {% for message in messages %}
              <li class="{{ message.tags }}"><b>{{ message }}</b></li>
            {% endfor %}
          </ul>
          <script>
            var messagesContainer = document.querySelector('.notification-bar');
            messagesContainer.style.display = 'block';
      
            setTimeout(function() {
              messagesContainer.style.display = 'none';
            }, 4000); 
          </script>
        {% endif %}
      </div>
'''


'''
 <form class="modal-body__from" id="myForm" action="{% url 'main:create_student' %}" method="get">
                                    {% csrf_token %}
                                    <div class="modal-body__from__div">
                                        <button class="active">Bepul maslahat uchun ariza qoldirish</button>
                                                <button><span>Fron-tend</span> kursi uchun ariza</button>
                                                <button><span>Back-end</span> kursi uchun ariza</button>
                                                <button><span>Dizayn</span> kursi uchun ariza</button>
                                                <button><span>Foundation</span> kursi uchun ariza</button>
                                                <button><span>Marketing</span> kursi uchun ariza</button>

                                    </div>
                                    <b>Formani to'ldiring</b>
                                    <input type="text" name="name" placeholder="Ism: " required>
                                    <input type="tel" id="phone" name="phone" placeholder="Telefon raqam" pattern="^998[0-9]{9}$" required value="998" title="Telefon raqamni kiriting, masalan: 9989XXXXXXXX">
                                    <input type="text" id="age" name="age" placeholder="Yosh:" required pattern="[0-9]{1,2}" title="Yoshingizni raqam bilan kiriting, masalan: 25">
                                    <button class="btn" type="button" onclick="submitForm()">Отправить запрос</button>
                                    <p>Tugmani bosish orqali men ma'lumotlarimni qonunga muvofiq qayta ishlashga roziman.</p>
                                </form>                              
                               
                                
'''


'''


  <script>
        function submitForm() {
            var formData = {
                name: $("input[name='name']").val(),
                phone: $("input[name='phone']").val(),
                age: $("input[name='age']").val(),
                course: $(".modal-body__from__div button.active").text() 
            };
    
            var queryString = $.param(formData);
    
            window.location.href = $("#myForm").attr("action") + "?" + queryString;
        }
    
        $(".modal-body__from__div button").click(function () {
            $(this).addClass("active").siblings().removeClass("active");
        });

    </script>
'''