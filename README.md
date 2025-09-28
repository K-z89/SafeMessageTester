<!DOCTYPE html><html lang="fa">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SafeMessageTester — ابزار تست پیام امن</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css">
<style>
body {font-family: Tahoma, sans-serif; background:#f4f4f4; color:#333; line-height:1.6; padding:20px;}
h1,h2,h3 {color:#2c3e50;}
a {color:#2980b9; text-decoration:none;}
a:hover {text-decoration:underline;}
code, pre {background:#ecf0f1; padding:2px 6px; border-radius:4px;}
pre {overflow-x:auto;}
section {background:#fff; padding:20px; margin-bottom:20px; border-radius:8px; box-shadow:0 2px 5px rgba(0,0,0,0.1);}
</style>
</head>
<body><section>
<h1>🚀 SafeMessageTester — ابزار تست پیام امن و حرفه‌ای</h1>
<p>⚡ یک ابزار <strong>امن، کنترل‌شده و حرفه‌ای</strong> برای تست ارسال پیام‌های مجاز و ایمن. مناسب برای توسعه‌دهنده‌ها و تیم‌هایی که می‌خواهند رفتار پیام‌رسانی را بررسی کنند بدون اینکه حساب واقعی آسیب ببینه.</p>
</section><section>
<h2>🌐 لینک پروژه GitHub</h2>
<p>کلون کردن مستقیم از مخزن GitHub:</p>
<pre><code>git clone https://github.com/K-z89/SafeMessageTester.git
cd SafeMessageTester</code></pre>
</section><section>
<h2>✨ معرفی پروژه</h2>
<p>SafeMessageTester اجازه می‌دهد پیام‌های <strong>کنترل‌شده و قانونی</strong> را به حساب‌های تستی، گروه‌ها یا کاربران با رضایت صریح ارسال کنید. ابزار با رعایت <strong>Rate Limit</strong> و مکانیزم <strong>Opt-in/Opt-out</strong> طراحی شده تا امنیت و مسئولیت‌پذیری تضمین شود.</p>
<p>⚠️ هشدار: استفاده غیرمجاز یا اسپم می‌تواند منجر به <strong>مسدود شدن اکانت تلگرام شما</strong> شود. سازنده هیچ مسئولیتی در قبال استفاده غیرقانونی ندارد.</p>
</section><section>
<h2>💡 قابلیت‌ها</h2>
<ul>
<li>ارسال پیام‌های تستی به یک یا چند حساب هدف با رضایت صریح.</li>
<li>صف‌بندی پیام‌ها و محدودیت سرعت (Rate Limit) قابل تنظیم.</li>
<li><strong>لاگینگ حرفه‌ای</strong>: ثبت زمان، فرستنده، گیرنده و وضعیت ارسال.</li>
<li>زمان‌بندی ارسال پیام‌ها (Scheduler).</li>
<li>پشتیبانی از Markdown برای قالب‌بندی حرفه‌ای پیام‌ها.</li>
<li>مکانیزم <strong>Opt-in / Opt-out</strong> برای تضمین رضایت دریافت‌کننده.</li>
</ul>
</section><section>
<h2>🚀 موارد استفاده مناسب</h2>
<ul>
<li>آزمایش پیام‌رسانی و بات‌ها در محیط‌های کنترل‌شده.</li>
<li>یادآوری‌ها و اعلان‌های داخلی تیمی یا سازمانی.</li>
<li>بررسی رفتار API تلگرام و Rate Limit بدون ریسک.</li>
</ul>
</section><section>
<h2>🔒 اصول استفاده امن</h2>
<ol>
<li><strong>رضایت الزامی</strong>: فقط به کسانی پیام بفرستید که صریحاً اجازه داده‌اند.</li>
<li><strong>آزمایش روی حساب تست</strong>: ابتدا در محیط تست اجرا شود.</li>
<li><strong>Rate Limit</strong>: تعداد پیام‌ها در دقیقه محدود شود.</li>
<li><strong>لاگینگ</strong>: تمام ارسال‌ها ثبت شود.</li>
<li><strong>Opt-out</strong>: در صورت درخواست کاربر، پیام‌ها متوقف شود.</li>
<li><strong>استفاده از API رسمی</strong>: از API رسمی تلگرام یا پلتفرم مربوطه استفاده شود.</li>
</ol>
</section><section>
<h2>🛠 نصب و راه‌اندازی سریع</h2>
<pre><code>git clone https://github.com/K-z89/SafeMessageTester.git
cd SafeMessageTester
pip install -r requirements.txt
python messagetester.py</code></pre>
<p>پس از اجرا، ابتدا از شما <strong>نام فرستنده (Sender Name)</strong> و <strong>Admin Secret</strong> خواسته می‌شود. حالت پیش‌فرض <strong>DRY_RUN</strong> فعال است تا هیچ پیامی بدون رضایت ارسال نشود.</p>
</section><section>
<h2>📦 فایل نصب کتابخانه‌ها</h2>
<p>یک فایل ساده <code>requirements.txt</code> برای نصب همه وابستگی‌ها:</p>
<pre><code>Flask==2.3.3
APScheduler==3.10.10
python-dotenv==1.0.0</code></pre>
<p>برای نصب سریع تمام کتابخانه‌ها:</p>
<pre><code>pip install -r requirements.txt</code></pre>
</section><section>
<h2>👤 توسعه‌دهنده</h2>
<p>GitHub: <a href="https://github.com/K-z89">K-z89</a><br>نسخه اولیه توسط <strong>K-z89</strong> طراحی و توسعه داده شده.</p>
</section></body>
</html>
