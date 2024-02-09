# استخراج سوالات آیین نامه رانندگی 
این یک پروژه وب اسکرپر بسیار ساده برای استخراج سوالات آیین نامه رانندگی از سایت `test-drive.ir` است شما با استفاده از این پروژه میتوانید همه دیتا های سوالات را از سایت مورد نظر استخراج و استفاده کنید


 استفاده های مختلفی که از دیتای این پروژه میتوان کرد به عنوان مثال ساخت یک وبسایت کامل برای یادگیری سوالات آیین نامه با فیچر های مختلف مثل علامت گزاری سوالات اشتباه و نمره دهی بر اساس نحوه پاسخگویی کاربر و گزارش دهی بر اساس نحوه پاسخگویی و ...

## راه اندازی 
```
pip install requests bs4
```
نصب دو کتابخانه bs4 و reqeusts و اجرا کردن فایل main
```
python main.py
```

 ## ساختار دیتای پروژه 
 بعد از اجرای پروژه یک فایل json کنار فایل ها ساخته میشود که دیتای به این شکل دارد

 ```json
{
    "1": [
        {
            "text": "#1. در هنگام مشاهده چراغ زرد چشمک زن چه اقدامی باید انجام داد؟ ",
            "img": "https://test-drive.ir/wp-content/uploads/2022/03/435766.jpg",
            "options": [
                {
                    "lable": "1- با مشاهده چنین چراغی ایست کامل می کنیم.",
                    "is_correct": false,
                    "order": 1
                },
                {
                    "lable": "2- عبور می کنیم و احتیاط لازم نیست.",
                    "is_correct": false,
                    "order": 2
                },
                {
                    "lable": "3- قبل از خط ایست ویا گذرگاه عابر پیاده توقف کامل می کنیم.",
                    "is_correct": false,
                    "order": 3
                },
                {
                    "lable": "4- از سرعت خود کم کرده و با احتیاط عبور کرده ودر ضرورت توقف می کنیم.",
                    "is_correct": true,
                    "order": 4
                }
            ]
        },
        {
            "text": "#2. هنرجوی گرامی در تقاطع شکل بالا حق تقدم عبور را مشخص کنید. ( آمبولانس در حال ماموریت است) ",
            "img": "https://test-drive.ir/wp-content/uploads/2023/10/657889564.jpg",
            "options": [
                {
                    "lable": "1- آمبولانس - زرد - سبز - بنفش",
                    "is_correct": false,
                    "order": 1
                },
                {
                    "lable": "2- آمبولانس - سبز - بنفش - زرد",
                    "is_correct": false,
                    "order": 2
                },
                {
                    "lable": "3- آمبولانس - بنفش - زرد - سبز",
                    "is_correct": false,
                    "order": 3
                },
                {
                    "lable": "4- آمبولانس - زرد و بنفش همزمان - سبز",
                    "is_correct": true,
                    "order": 4
                }
            ]
        },

```

در json کلی که key ها به صورت عدد هستند هر عدد نشان دهنده یک ازمون هست و value ان هم یک لیست از سوالات ان ازمون هست 
