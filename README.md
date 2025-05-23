# PIS_API

Сценарій використання зовнішнього API на прикладі WEB-сервісу NASA Astronomy Picture of the Day (APOD):

Спочатку необхідно отримати API-ключ на офіційному сайті NASA https://api.nasa.gov/.
Після реєстрації стає доступним персональний ключ доступу до NASA API (у моєму випадку - JmyD8ON7eMjDevqsv3YoTuIpikMPbm2PmxbcoggQ).

Сервіс APOD (Astronomy Picture of the Day) дозволяє отримувати інформацію про зображення дня з поясненням.
Запит має вигляд https://api.nasa.gov/planetary/apod?api_key=ВАШ_КЛЮЧ&date=РРРР-ММ-ДД, наприклад
https://api.nasa.gov/planetary/apod?api_key=JmyD8ON7eMjDevqsv3YoTuIpikMPbm2PmxbcoggQ&date=2023-05-20

В HTML-файлі реалізовано JavaScript-код, який надсилає запит до API, отримує JSON-відповідь, зчитує такі дані:

- назва зображення (title)
- дата (date)
- посилання на зображення (url)
- пояснення (explanation)
  та виводить їх на сторінку.

Окрім цього, було реалізовано власний HTTP-сервер (server.py) мовою Python.
Після запуску сервер приймає запити за адресою http://localhost:7000/?login=is-34fiot-23-173
Якщо логін правильний, повертається HTML-сторінка з персональними даними:

Прізвище: Романюк
Ім’я: Діана
Курс: 2
Група: ІС-34
