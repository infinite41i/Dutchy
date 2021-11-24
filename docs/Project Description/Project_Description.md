# Users - کاربران
کاربران در سامانه ثبت‌نام می‌کنند. کاربرهای متفاوتی نداریم بلکه همگی از یک نوع هستند. مثلا کاربر مدیر یا ادمین نداریم.

اطلاعات ذخیره شده از هر کاربر به شرح زیر است:
```json
{
  "id": 0,
  "first_name": "Ada",
  "last_name": "Lovelace",
  "email": "ada@example.com",
  "registration_status": "confirmed",
  "picture": "string"
}
```

# Groups - گروه‌ها
گروه‌ها نیز مدیر ندارند. بلکه صرفا یک نفر آن را ایجاد کرده است که اطلاعات آن را ذخیره می‌کنیم. پس از آن هم هرکس می‌تواند خرجی در گروه اضافه کند. ***برای ساده نگه داشتن برنامه نیازی به تایید دیگران نیست و فرض می‌کنیم افراد به یکدیگر اعتماد دارند.***

گروه دو لیست اصلی برای مخارج دارد:
1. لیست کل مخارج ثبت شده
1. لیست ساده شده؛‌یعنی جمع جبری بدهی و طلب هر شخص به هر شخص دیگر

این‌گونه و با نگه داشتن مقدار بدهی و طلب در ساختار داده، فهمیدن نحوه‌ی تسویه حساب راحت‌تر خواهد شد.

همچنین، همراه اطلاعات هر عضو گروه، بدهی یا طلب او را به صورت یک عدد صحیح مشخص می‌کنیم.

جزئیات در فایل زیر:
```json
{
  "groups": [
    {
      "id": 321,
      "name": "Housemates 2020",
      "updated_at": "2019-08-24T14:15:22Z",
      "avatar": "https://picsum.photos/200",
      "invite_link": "https://picsum.photos/200"
      "members": [
        {
          "id": 0,
          "first_name": "Ada",
          "last_name": "Lovelace",
          "email": "ada@example.com",
          "registration_status": "confirmed",
          "picture": {
            "small": "string",
            "medium": "string",
            "large": "string"
          },
          "balance": [
            {
              "amount": "-5.02"
            }
          ]
        }
      ],
      "original_debts": [
        {
          "from": 18523,
          "to": 90261,
          "amount": "414.5",
        }
      ],
      "simplified_debts": [
        {
          "from": 18523,
          "to": 90261,
          "amount": "414.5",
        }
      ]
    }
  ]
}
```

در پایگاه داده هر گروه با جداول مختلفی سروکار داریم که باید مشخص شوند؛‌ اما لازم به ذکر است که برای ثبت مخارج به دو جدول نیاز است. یک جدولی شامل تمام مخارج و جدولی دیگر شامل مخارج خلاصه شده
یعنی به کلیدهای زیر احتیاج خواهیم داشت:

`expense_id, simplified_expense_id`

# Friends - دوستان

***برای سادگی برنامه، فرض می‌کنیم افراد صرفاً از طریق لینک دعوت عضو گروه‌ها می‌شوند و کاری با بخش دوستان نداریم.***


# Expenses - مخارج

در هر گروه، هر کس می‌تواند خرج خودش را ثبت کند. هر کس هم می‌تواند ان را ویرایش کند. البته همه‌ی اینها به عنوان کامنت در همان خرج ثبت می‌شود. در هر خرج اطلاعاتی از قبیل
- عنوان
- مبلغ
- دسته بندی
- افراد سهیم
- توضیحات
- تاریخ و زمان
- تصویر رسید

وجود دارد که همه به جز توضیحات و تصویر رسید اختیاری اند.


```json
{
  "expense": {
    "title" : "Pizza",
    "cost": "25.0",
    "group_id": 391,
    "description": "Brunch",
    "details": "string",
    "date": "2012-05-02T13:00:00Z",
    "category_id": 15,
    "id": 51023,
    "created_at": "2012-07-27T06:17:09Z",
    "created_by": {
      "id": 0,
      "first_name": "Ada",
      "last_name": "Lovelace",
      "email": "ada@example.com",
      "registration_status": "confirmed",
      "picture": "string"
    },
    "updated_at": "2012-12-23T05:47:02Z",
    "updated_by": {
      "id": 0,
      "first_name": "Ada",
      "last_name": "Lovelace",
      "email": "ada@example.com",
      "registration_status": "confirmed",
      "picture": {
        "small": "string",
        "medium": "string",
        "large": "string"
      }
    },
    "deleted_at": "2012-12-23T05:47:02Z",
    "deleted_by": {
      "id": 0,
      "first_name": "Ada",
      "last_name": "Lovelace",
      "email": "ada@example.com",
      "registration_status": "confirmed",
      "picture": {
        "small": "string",
        "medium": "string",
        "large": "string"
      }
    },
    "category": {
      "id": 5,
      "name": "Electricity"
    },
    "receipt": {
      "large": "https://picsum.photos/200",
      "original": "https://picsum.photos/200"
    },
    "users": [
      {
        "user": {
          "id": 491923,
          "first_name": "Jane",
          "last_name": "Doe",
          "picture": {
            "medium": "image_url"
          }
        },
        "user_id": 491923,
        "paid_share": "8.99",
        "owed_share": "4.5",
        "net_balance": "4.49"
      }
    ],
    "comments": [
      {
        "id": 79800950,
        "content": "John D. updated this transaction: - The cost changed from $6.99 to $8.99",
        "comment_type": "System",
        "relation_type": "ExpenseComment",
        "relation_id": 855870953,
        "created_at": "2019-08-24T14:15:22Z",
        "deleted_at": "2019-08-24T14:15:22Z",
        "user": null
      }
    ]
  }
}
```

# Comments - نظرات
از آنجا که عهر کس می‌تواند مخارج را ثبت و ویرایش کند، نیاز است هر تغییری در هر خرج، به عنوان لاگ یا کامنت در انتهای آن ثبت شود. کاربران هم می‌توانند به صورت دستی کامنت بگذارند.

```json
{
  "comments": [
    {
      "id": 79800950,
      "content": "John D. updated this transaction: - The cost changed from $6.99 to $8.99",
      "comment_type": "System",
      "created_at": "2019-08-24T14:15:22Z",
      "deleted_at": "2019-08-24T14:15:22Z",
      "user": null
    }
  ]
}
```

