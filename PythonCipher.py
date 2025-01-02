# بسم الله الرحمن الرحيم

انطر = lambda نطرات: print(نطرات)
حديث = str(input("ادخل النص اخى المسلم🙏🙏🙏: "))
عرف_مفتاح = "قضيبصناعي"
صفر = 0
واحد = 1

عملية = int(input("عايز ايه يك*#ك؟\n0: تشفير\n1: فكتشفير\n"))
if عملية < صفر or عملية > واحد :
    انطر("مش بقولك يك*مك اختار 1 او 0؟ اخترت %d ليه يعر*?" % عملية)
    exit(1)

def فيجينير(رسالة, مفتاح, اتجاه=واحد):
    فهرس_مفتاح = صفر
    الالفبائية = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
    رسالة_نهاية = ''

    for شار in رسالة.lower():
        # الحق اي غير حرف حرف للرسالة
        if not شار.isalpha(): # لو شار  == " ":
            رسالة_نهاية += شار
        else:
            # ابحث عن الحرف الصحيح للترميز/فك التشفير
            شار_مفتاح = مفتاح[فهرس_مفتاح % len(مفتاح)]
            فهرس_مفتاح += واحد

            # عرف الازاحة والمشفر/مفكوك الشفرة حرف
            ازاحة = الالفبائية.index(شار_مفتاح)
            فهرس = الالفبائية.find(شار)
            جديد_فهرس = (فهرس + ازاحة*اتجاه) % len(الالفبائية)
            رسالة_نهاية += الالفبائية[جديد_فهرس]

    return رسالة_نهاية

def تشفير(رسالة, مفتاح):
    return فيجينير(رسالة, مفتاح)
    # باصي

def فك_التشفير(رسالة, مفتاح):
    return فيجينير(رسالة, مفتاح, -واحد)

if عملية == 0:
    انطر("حديث: %s" % حديث)
    انطر("مفتاح: %s" % عرف_مفتاح)
    مشفر = تشفير(حديث, عرف_مفتاح)
    انطر("اضرب منوي: %s" % مشفر)
else:
    انطر("حديث مشفر: %s" % حديث)
    انطر("مفتاح: %s" % عرف_مفتاح)
    فكتشفير = فك_التشفير(حديث, عرف_مفتاح)
    انطر("انطر ابلكاش: %s" % فكتشفير)