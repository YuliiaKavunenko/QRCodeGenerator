# Генератор QR-кодів / QR code generator

## Навігація: / Navigation:
- [Головна / Home](#генератор-qr-кодів--qr-code-generator)
- [Мета проєкту / Project goal](#мета-проєкту--project-goal)
- [Команда розробників / Development team](#склад-команди-розробників--the-development-team-consists-of)
- [Технології / Technologies](#головні-технології-задіяні-в-проєкті)
- [Призначення застосунків / Application purpose](#призначення-кожного-застосунку--purpose-of-each-application)
  - [Contacts Page](#1-contacts_page)
  - [Generator Page](#2-generator_page)
  - [My QR Codes Page](#4-my_qrcodes_page)
  - [Subscription Page](#5-subscription_page)
  - [User Page](#6-user_page)
- [Підписки / Subscriptions](#принцип-роботи-підписок-та-їх-особливості--how-subscriptions-work-and-their-features)
- [Реалізація структури моделей / Model Structure Implementation](#реалізація-структури-моделей--model-structure-implementation)
- [Встановлення і запуск проєкту / Installation and Project Launch](#встановлення-і-запуск-проєкту--installation-and-project-launch)
- [Висновок / Conclusion](#висновок--conclusion)

### Мета проєкту: / Project goal:
- Поглиблення знань у Django та роботі з базою даних SQLite на практиці / Deepening knowledge in Django and working with the SQLite database in practice
- Поліпшення навичок командної роботи / Improving teamwork skills
- Розробка вебзастосунку для зручної генерація QR-кодів / Development of a web application for convenient generation of QR codes
### Наш вебзастосунок для генерації QR-кодів створений для того, щоб зробити процес обміну інформацією швидким, зручним і сучасним. / Our QR code generation web application is designed to make the process of information exchange fast, convenient, and modern.
- Простота у використанні й жодних складних налаштувань: введіть потрібні дані, і за мить отримаєте готовий QR-код; / Easy to use and no complicated settings: enter the required data and in a moment you will receive a ready-made QR code;
- Швидкий доступ до інформації: QR-код миттєво зчитується смартфоном, що дозволяє легко передавати посилання, контакти, Wi-Fi-дані тощо; / Quick access to information: The QR code is instantly read by a smartphone, allowing you to easily transfer links, contacts, Wi-Fi data, etc.;
- Зручне збереження та управління: можливість зберігати створені QR-коди для повторного використання; / Convenient storage and management: the ability to save created QR codes for reuse;
- Багатофункціональність і підтримка різних форматів: від тексту та URL до візитних карток та платіжних реквізитів. / Multifunctionality and support for various formats: from text and URL to business cards and payment details.
### Сервіс стане незамінним інструментом для бізнесу, навчання та повсякденного життя, дозволяючи швидко й ефективно передавати інформацію. / The service will become an indispensable tool for business, education, and everyday life, allowing for quick and efficient information transfer.

## Склад команди розробників: / The development team consists of:
>- [Юлія Кавуненко(Team Leader)](https://github.com/YuliiaKavunenko) / [Yuliia Kavunenko(Team Leader)](https://github.com/YuliiaKavunenko)
>- [Христина Литвиненко](https://github.com/LitvinenkoKristina1) / [Kristina Litvinenko](https://github.com/LitvinenkoKristina1)
>- 
### Figma-дизайн / Figma design : https://www.figma.com/design/Wa67sPMYUlACfpKII2mbxe/Untitled?node-id=0-1&t=9PpZEBSIA9E9Qcxy-1
## Головні технології, задіяні в проєкті

### Backend
- **Django** – основний фреймворк для створення веб-застосунку.
- **Django ORM** – робота з базою даних SQLite через об'єктно-реляційне моделювання.
- **qrcode** – генерація QR-кодів.
- **Pillow** – обробка зображень (зміна кольору QR-коду).
- **Django Authentication** – управління користувачами (реєстрація, вхід, валідація).

### Database
- **SQLite** – легка реляційна база даних для зберігання інформації про користувачів та QR-коди.

### Frontend
- **HTML/CSS** – розмітка та стилізація інтерфейсу.
- **JavaScript (Vanilla JS)** – базові інтерактивні елементи (вибір кольору, динамічні форми).

### DevOps та розгортання
- **Git & GitHub** – контроль версій та командна розробка.
- **Figma** – розробка UI/UX-дизайну.
- **Python venv** – створення віртуального середовища.

## Призначення кожного застосунку / Purpose of each application :

>- ## 1 `contacts_page`
**Призначення: / Appointment:**
- Надає користувачам можливість зв’язатися з технічною підтримкою через email або соціальні мережі. / Provides users with the ability to contact technical support via email or social media.

**Особливості: / Features:**
- Статична сторінка з контактною інформацією. / Static page with contact information.
- Можливість відправки запитів через форму зворотного зв’язку. / Ability to send requests via the feedback form.

**Приклад коду: / Code example:**
```python
from django.shortcuts import render

def contacts(request):
    return render(request, ""contacts_page/contacts_page.html"")
```
>- ## 2 `generator_page`
**Призначення: / Appointment:**
- Генерація QR-кодів за допомогою введеного посилання. / Generate QR codes using the entered link.
- Кастомізація QR-коду (розмір, колір, логотип тощо). 

**Особливості: / Features:**
- Використовує бібліотеку qrcode для створення QR-кодів. /Uses the qrcode library to create QR codes.
- Додає можливість кастомізації: / Adds customization options:
    + Вибір кольору. / Color selection.
    + Налаштування розміру. / Size settings.
    + Вставка логотипу всередину QR-коду. / Inserting a logo inside a QR code.

**Приклад коду: / Code example:**
```python
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import QRCodes
from PIL import Image, ImageDraw
from PIL import ImageFont
from subscription_page.models import Subscription
from django.utils.timezone import now
from datetime import timedelta

def render_generatorpage(request):
    qr_limit = 1
    if request.method == "GET" and "download" in request.GET:
        qr_id = request.GET.get("download")
        try:
            qr_code = QRCodes.objects.get(id=qr_id)
            response = HttpResponse(qr_code.picture, content_type="image/png")
            response['Content-Disposition'] = f'attachment; filename="{qr_code.name}.png"'
            return response
        except QRCodes.DoesNotExist:
            return HttpResponse("QR code not found!", status=404)

    qr_instance = None
    download_link = None
    subscription = Subscription.objects.filter(user=request.user).first()
    if subscription:
        print('subscription.subscription_type:', subscription.subscription_type)
        if subscription.subscription_type == "free":
            qr_limit = 1
        elif subscription.subscription_type == "standart":
            qr_limit = 10
        elif subscription.subscription_type == "pro":
            qr_limit = 100
        else:
            qr_limit = 1
    else:
        print('subscription is None')
        qr_limit = 1
    user_qr_count = QRCodes.objects.filter(user=request.user).count()

    if request.method == "POST" and request.user.is_authenticated:
        action = request.POST.get("action")
        if action == "generate":
            
            if user_qr_count >= qr_limit:
                return render(request, 'generator_page/generator_page.html', {
                    'message': 'You have reached the limit of QR codes for your subscription. Upgrade to create more.'
                })
            
            qr_name = request.POST.get("QR-code-name")
            qr_link = request.POST.get("your-link")
            color = request.POST.get("color", "#000000")
            size = request.POST.get("size", "300")
            shape = request.POST.get("shape", "standard")
            text_to_frame = request.POST.get("text-to-frame", "")

            if qr_name and qr_link:
                try:
                    size = int(size)
                except ValueError:
                    size = 300

                qr_instance = QRCodes(name=qr_name, user=request.user, link=qr_link)

                qr = qrcode.QRCode(
                    version = 1,
                    error_correction = qrcode.constants.ERROR_CORRECT_L,
                    box_size = 10,
                    border = 4,
                )
                qr.add_data(qr_link)
                qr.make(fit = True)

                qr_matrix = qr.modules

                img_size = size + 60
                img = Image.new("RGB", (img_size, img_size), "white")
                draw = ImageDraw.Draw(img)
                box_size = size // len(qr_matrix)

                offset_x = (img_size - len(qr_matrix) * box_size) // 2
                offset_y = (img_size - len(qr_matrix) * box_size) // 2

                for y in range(len(qr_matrix)):
                    for x in range(len(qr_matrix[y])):
                        if qr_matrix[y][x]:
                            x_pos = x * box_size + offset_x
                            y_pos = y * box_size + offset_y

                            if shape == "shape1":
                                draw.ellipse([(x_pos, y_pos), (x_pos + box_size, y_pos + box_size)], fill=color)
                            elif shape == "shape2":
                                draw.regular_polygon(
                                    (x_pos + box_size // 2, y_pos + box_size // 2, box_size // 2), 
                                    n_sides=5, 
                                    fill=color
                                )
                            elif shape == "shape3":
                                draw.ellipse([(x_pos, y_pos), (x_pos + box_size, y_pos + box_size)], fill=color)
                            elif shape == "shape4":
                                draw.polygon(
                                    [
                                        (x_pos + box_size // 2, y_pos),
                                        (x_pos + box_size, y_pos + box_size // 2),
                                        (x_pos + box_size // 2, y_pos + box_size),
                                        (x_pos, y_pos + box_size // 2),
                                    ],
                                    fill=color,
                                )
                            else:
                                draw.rectangle([(x_pos, y_pos), (x_pos + box_size, y_pos + box_size)], fill=color)

                if text_to_frame:
                    try:
                        font = ImageFont.truetype("JosefinSans-Bold.ttf", size // 2)
                    except IOError:
                        font = ImageFont.load_default()


                    bbox = draw.textbbox((0, 0), text_to_frame, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    text_x = (img_size - text_width) // 2
                    text_y = img_size - text_height - 15

                    draw.text((text_x, text_y), text_to_frame, font=font, fill=color)

                buffer = BytesIO()
                img.save(buffer, format="PNG")
                filename = f'qr_{qr_name}.png'

                qr_instance.picture.save(filename, ContentFile(buffer.getvalue()), save=False)
                qr_instance.save()

                download_link = f"?download={qr_instance.id}"

            else:
                return HttpResponse("Not all fields are filled in")
    
    return render(
        request=request,
        template_name='generator_page/generator_page.html',
        context={
        'qr_instance': qr_instance,
        'download_link': download_link,
        'qr_limit': qr_limit,
        'user_qr_count': user_qr_count,
    }
    )

```
## 4 `my_qrcodes_page`
**Призначення: / Appointment:**
- Відображення всіх QR-кодів, створених користувачем. / Display all QR codes created by the user.
- Можливість фільтрації за датою створення та назвою. / Ability to filter by creation date and name.

**Особливості: / Features:**
- Додає можливість скачати QR-коди. / Adds the ability to download QR codes.
- Впроваджена фільтрація за параметрами. / Filtering by parameters has been implemented.

**Приклад коду: / Code example:**
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from generator_page.models import QRCodes

def render_myqrcodespage(request):
    if not request.user.is_authenticated:
        
        return render(
            request,
            "my_qrcodes_page/my_qrcodes_page.html",
        )

    if request.method == "POST":
        qr_id = request.POST.get("qr_id")
        action = request.POST.get("action")

        try:
            qr_code = QRCodes.objects.get(id=qr_id, user=request.user)

            if action == "download":
                response = HttpResponse(qr_code.picture, content_type="image/png")
                response["Content-Disposition"] = f'attachment; filename="{qr_code.name}.png"'
                return response

            elif action == "delete":
                qr_code.delete()
                return redirect("myqrcodes")

        except QRCodes.DoesNotExist:
            return HttpResponse("QR code not found!", status=404)

    user_qrcodes = QRCodes.objects.filter(user = request.user)
    
    sort_order = request.GET.get("sort", "default")  

    if sort_order == "asc":
        user_qrcodes = QRCodes.objects.filter(user=request.user).order_by("date")
    else:
        user_qrcodes = QRCodes.objects.filter(user=request.user).order_by("-date")

    return render(
        request,
        "my_qrcodes_page/my_qrcodes_page.html",
        {
            "user_qrcodes": user_qrcodes,
            'is_authorizated': request.user.is_authenticated,
        },
    )

```
## 5 `subscription_page`
**Призначення: / Appointment:**
- Керування підписками користувача / Manage user subscriptions (Free, Standart, Pro).

**Особливості: / Features:**
- Визначає ліміт QR-кодів, які можна створити. / Specifies the limit of QR codes that can be created.
- Додає можливість зміни підписки. / Adds the ability to change subscriptions.

**Приклад коду: / Code example:**
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Subscription

def render_subscription_page(request):
    if not request.user.is_authenticated:
        return redirect("authorization")  # Якщо користувач не авторизований

    if request.method == "POST":
        new_plan = request.POST.get("plan")

        if new_plan in ["standart", "pro"]:
            request.session["new_subscription"] = new_plan
            return redirect("payment")

        elif new_plan == "free":
            # Переконуємося, що підписка існує або створюємо її
            subscription, _ = Subscription.objects.get_or_create(user=request.user)
            subscription.subscription_type = "free"
            subscription.qr_limit = 1
            subscription.save()
            return redirect("subscription")

    return render(request, "subscription_page/subscription_page.html", {
        "is_authorizated": request.user.is_authenticated
    })


def render_payment_page(request):
    if not request.user.is_authenticated:
        return redirect("authorization")  

    new_plan = request.session.get("new_subscription")
    error_message = None  

    if request.method == "POST" and new_plan:
        password = request.POST.get("password")

        # Перевіряємо правильність пароля
        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            # Оновлення підписки
            subscription, _ = Subscription.objects.get_or_create(user=request.user)
            subscription.subscription_type = new_plan
            subscription.qr_limit = 10 if new_plan == "standart" else 100
            subscription.save()

            # Видаляємо дані сесії та переходимо назад
            del request.session["new_subscription"]
            return redirect("subscription")
        else:
            error_message = "Incorrect password. Please try again."

    return render(request, "subscription_page/payment_page.html", {
        "new_subscription": new_plan,
        "error_message": error_message
    })


```
## 6 `user_page`
**Призначення: / Appointment:**
- Відображення профілю користувача. / Displaying the user profile.
- Налаштування акаунта. / Account settings.

**Особливості: / Features:**
- Містить інформацію про користувача./ Contains information about the user.
- Додає можливість виходу з акаунта. / Adds the ability to log out of the account.

**Приклад коду: / Code example:**
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from subscription_page.models import Subscription
# Create your views here.
def render_user_page(request):
    if request.user.is_authenticated:
        username = request.user.username
        is_authenticated = True
    else:
        username = None
        is_authenticated = False

    return render(
        request=request,
        template_name="user_page/user_page.html",
        context={
            'is_authenticated': is_authenticated,
            'username': username,
        }
    )


def render_registration_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            user = User.objects.create_user(username = username, email = email, password = password)
            Subscription.objects.create(user = user)
            return redirect("authorization")
        else:
            return render(request = request, template_name = "registration/registration.html", context = {"current_page": "registration"})

    return render(
        request = request,
        template_name = "registration/registration.html",
        context = {"current_page": "registration"}
    )

def render_authorization_page(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request = request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error_message = "ERROR. CHECK YOUR DATA AND TRY AGAIN LATER"

    return render(
        request=request,
        template_name="authorization/authorization.html",
        context={
            "current_page": "authorization",
            "error_message": error_message,
        }
    )

def logout_user(request):
    if request.method == "POST":
        logout(request)
    return redirect("home")

```
## Принцип роботи підписок та їх особливості / How subscriptions work and their features

>- 1. Free – 1 QR-код на 6 місяців.
>- 2. Standart – 10 QR-кодів за 2$/місяць.
>- 3. Pro – 100 QR-кодів за 10$/місяць.
### Логіка у моделі Subscription: / The logic in the Subscription model:
```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length = 20, default = "free")
    purchase_date = models.DateTimeField(auto_now_add=True)
    qr_limit = models.IntegerField(default = 1)
```
## Реалізація структури моделей / Implementing the model structure
```python
from django.db import models
from django.contrib.auth.models import User
# Create your models here
class QRCodes(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    link = models.TextField()
    picture = models.ImageField(upload_to = 'images/')
    date = models.DateTimeField(auto_now_add = True)
```
## Встановлення і запуск проєкту: / Installing and launching the project:
### Встановлення: / Installation:
Зробіть копію проєкту / Make a copy of the project
```bash
  git clone https://github.com/YuliiaKavunenko/QRCodeGenerator.git
```
Перейдіть до папки з проєктом / Go to the project folder
```bash
  cd QRcodeMaker
```
Завантажте необхідні залежності / Download the required dependencies
```bash
  pip install -r requirements.txt
```

### Для запуску: / To start:
Перейдіть до головної папки / Go to the main folder
```bash
  cd GeneratorQrCode
```
Запустіть проєкт через manage.py / Launch the project via manage.py
```bash
  python manage.py runserver
```
# **Висновок / Conclusion**

У межах цього проєкту було створено веб-додаток для генерації та керування QR-кодами з різними підписками. Система дозволяє користувачам створювати, кастомізувати та зберігати QR-коди відповідно до обраного тарифного плану. / As part of this project, a web application was created to generate and manage QR codes with different subscriptions. The system allows users to create, customize, and save QR codes according to the selected tariff plan.

Основні досягнення проєкту: / Main achievements of the project:
- **Гнучка система підписок / Flexible subscription system** (Free, Standart, Pro) з відповідними обмеженнями на кількість QR-кодів та можливостями кастомізації; / with appropriate restrictions on the number of QR codes and customization options;
- **Зручний інтерфейс / User-friendly interface** для генерації QR-кодів із можливістю налаштування кольору, розміру, форми та додавання тексту; / for generating QR codes with the ability to customize color, size, shape and add text;
- **Гостьовий режим / Guest mode** для тестування сервісу без реєстрації; / for testing the service without registration;
- **Фільтрація та управління QR-кодами / QR code filtering and management** на сторінці "Мої QR-коди"; / on the "My QR codes" page;
- **Захист даних / Data protection** та безпечна аутентифікація користувачів із підтвердженням email; / and secure user authentication with email confirmation;

Проєкт у майбутньому буде легко масштабувати та розширювати, завдяки зручній структурі проєкту. / The project will be easy to scale and expand in the future, thanks to the convenient project structure.
<<<<<<< HEAD
=======

>>>>>>> e884f8ad4cff77e9ee7100d610b2076c8852d9d4
