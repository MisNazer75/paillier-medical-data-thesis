# راهنمای انتشار پروژه در گیت‌هاب

۱. فایل ZIP را روی رایانه استخراج کنید. محتویات پوشه paillier_thesis باید فایل‌های پروژه باشد.
۲. وارد https://github.com شوید و سپس https://github.com/new را باز کنید.
۳. نام مخزن را paillier-medical-data-thesis انتخاب کنید؛ برای دسترسی عمومی داور، Public را انتخاب کنید.
۴. Add a README file را فعال کنید و Create repository را بزنید.
۵. در صفحه مخزن Add file و سپس Upload files را انتخاب کنید. فایل ZIP را بارگذاری نکنید؛ فایل‌ها و پوشه‌های استخراج‌شده را بارگذاری کنید. README موجود در بسته را جایگزین README اولیه کنید.
۶. اگر مرورگر پوشه‌ها را درست بارگذاری نکرد، GitHub Desktop را از https://desktop.github.com نصب کنید، وارد حساب شوید، مخزن را Clone کنید و فایل‌ها را داخل پوشه محلی مخزن کپی کنید. در GitHub Desktop با پیام Add reproducible thesis experiment، Commit to main و سپس Push origin را بزنید.
۷. پوشه local_run، محیط .venv و هیچ کلید خصوصی را منتشر نکنید. فایل .gitignore بسته برای جلوگیری از انتشار این موارد در روش Git تنظیم شده است؛ هنگام آپلود دستی نیز آن‌ها را انتخاب نکنید.
۸. صفحه مخزن و فایل data/synthetic_patients.csv را در یک پنجره بدون ورود به حساب باز کنید تا دسترسی عمومی بررسی شود.
۹. لینک واقعی مخزن را در محل «نشانی مخزن کد» فصل سوم و لینک واقعی فایل داده را در محل «نشانی داده‌ها» قرار دهید. نشانی نمونه را در پایان‌نامه نگذارید.
۱۰. بعد از انتشار، فایل داده را باز کنید و دکمه y روی صفحه‌کلید را بزنید تا نشانی فایل به نسخه همان commit اشاره کند. برای ثبت نسخه کد، SHA همان commit را در پایان‌نامه ذکر کنید.
۱۱. اگر دانشکده اجرای محلی پژوهشگر را می‌خواهد، دستورهای README را روی رایانه خود اجرا و نتایج/مشخصات محیط را جایگزین نسخه مرجع کنید؛ نتایج مرجع را به رایانه خود نسبت ندهید.

الگوی نشانی‌ها (فقط راهنما؛ باید نام کاربری واقعی جایگزین شود):
- کد: https://github.com/YOUR_USERNAME/paillier-medical-data-thesis
- داده: https://github.com/YOUR_USERNAME/paillier-medical-data-thesis/blob/main/data/synthetic_patients.csv

راهنمای رسمی:
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
