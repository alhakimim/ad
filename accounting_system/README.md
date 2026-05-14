# Accounting System Desktop App (Python + PyQt5)

مشروع نظام محاسبي مكتبي (سطح المكتب) بلغة بايثون باستخدام PyQt5 لواجهة المستخدم وSQLite كقاعدة بيانات.

## هيكلية المجلدات

```
accounting_system/
├── main.py
├── settings.py
├── requirements.txt
├── README.md
│
├── database/
│   ├── db_manager.py
│   └── init_db.sql
│
├── models/
│   ├── accounts.py
│   ├── transactions.py
│   ├── customers.py
│   └── suppliers.py
│
├── controllers/
│   ├── auth_controller.py
│   ├── accounts_controller.py
│   ├── transactions_controller.py
│   └── reports_controller.py
│
├── views/
│   ├── main_window.py
│   ├── login_window.py
│   ├── dashboard.py
│   ├── accounts_window.py
│   ├── customers_window.py
│   └── reports_window.py
│
├── ui/
│   ├── main_window.ui
│   ├── login_window.ui
│   ├── accounts_window.ui
│   ├── customers_window.ui
│   └── reports_window.ui
│
├── reports/
│   ├── balance_sheet.py
│   ├── income_statement.py
│   └── trial_balance.py
│
└── utils/
    ├── helpers.py
    └── validators.py
```

## لتشغيل النظام:

1. تأكد من وجود بايثون وpip
2. نفّذ:
    ```
    pip install -r requirements.txt
    python main.py
    ```

## ملاحظات
- كل مجلد يحتوي ملفات منطقية منظمة حسب دورها.
- قاعدة بيانات SQLite تسهّل التشغيل بدون إعدادات خارجية.
- يمكن تطوير الواجهات بـ Qt Designer ثم تحويل ملفات ui إلى py.
