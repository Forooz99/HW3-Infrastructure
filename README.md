## مقدمه

در این تمرین با توزیع بار با استفاده از nginx و docker-compose و تست بار با استفاده از locust آشنا می‌شویم. هدف شما تکمیل فایل ‌های داده شده و ارائه یک گزارش است که در ادامه توضیح هر قسمت آورده شده است.

## محتوای پوشه‌های django و go

در پوشه‌ای که در اختیارتان قرار گرفته است دو پروژه django و gin-go قرار دارد که هر کدام یک api دارد که خروجی یک عدد بر می‌گرداند. هر برنامه دو عدد به صورت query param دریافت می‌کند یکی n و دیگر k و سپس شروع به ایجاد اعداد رندوم n رقمی می‌کند. اولین عددی که به تعداد k صفر در ابتدایش داشته باشد را برمی‌گرداند. یکی با زبان go و فریمورک gin-go و دیگری با زبان Python و فریمورک Django نوشته شده است (نیازی به تغییر کد در این پوشه‌ها نیست).

## بخش اول

لازم است که docker-compose.yml و nginx/conf.d/default.conf را به گونه‌ای تغییر دهید که موارد زیر برقرار باشد:
- بتوان تعداد دلخواه از کدام django_server و یا go_server با دستور docker-compose up به اجرا در آورد. (با تغییر یک عدد در .env تعداد نمونه های این سرویس ها تغییر کند)
- بتوان میزان منابع مصرفی مانند memory و cpu را برای django_server و go_server تعیین کرد.
- تمام ترافیک از طریق nginx بین django_server و go_server توزیع شود. (روش توزیع مهم نیست)
- در نهایت تنها پورت ارتباطی با django_server و go_server پورت nginx باشد.

## بخش دوم

پس از بالا آمدن سرویس‌ها و عملکرد صحیح آنها با استفاده از locust (یا ابزارهای تست بار معروف دیگر) اندپوینت های مربوط به سرور django و go را ارزیابی کنید و در مورد موارد زیر گزارشی با استفاده از آمار (response time و تعداد ریکوئست بر ثانیه زده شده و وضعیت cpu و ram هنگام تست بار و ...) بنویسید:

- این docker-compose را با یک نمونه از هر server بالا بیاورید و منابع مصرفی و میزان تحمل بار سرورها را مقایسه کنید.
- اینبار از هر server چند نمونه ایجاد کنید و نتایج را با حالت قبل مقایسه کنید.
