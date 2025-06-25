# github-mcp-bot


##  بوت GitHub الذكي باستخدام Model Context Protocol (MCP)

يعمل هذا المشروع كخادم ذكي يتفاعل مع مستودعات GitHub من خلال Webhooks. يقوم بتحليل المهام والفروع وطلبات الدمج (Pull Requests)، ويُنشئ تقارير تنفيذية باستخدام GPT.

---

###  الميزات

* رد تلقائي على قضايا (Issues) جديدة باستخدام GPT-4.
* توليد تقارير تنفيذية لحالة المشروع (المهام، PRs، الفروع).
* هيكل سياقي يعتمد على نموذج MCP.
* متكامل  مع OpenAI  API.

---

###  المتطلبات

* Python 3.9+
* حساب على GitHub + Personal Access Token
* حساب OpenAI API + مفتاح

---

###  التثبيت

1. انسخ المستودع:

```bash
git clone https://github.com/MKQH1999/github-mcp-bot.git
cd github-mcp-bot
```

2. أنشئ ملف `.env` بناءً على `env.template` وأدخل المفاتيح المطلوبة.

3. ثبّت التبعيات:

```bash
pip install -r requirements.txt
```

4. شغّل الخادم:

```bash
uvicorn main:app --reload --port 8000
```

---

###  ربط GitHub Webhook

* في إعدادات مستودع GitHub الخاص بك:

  * Webhook URL: `http://yourserver.com/webhook`
  * Content type: `application/json`
  * Events: `Issues`

---

###  توليد تقرير حالة المشروع

زر الرابط التالي:

```
GET /project-report/<username>/<repository>
```

مثال:

```
http://localhost:8000/project-report/MKQH1999/github-mcp-bot
```

سيتم توليد تقرير ذكي من GPT يعرض:

* المهام المفتوحة
* PRs النشطة
* الفروع
* تحليل تنفيذي للحالة الحالية

---

###  هيكل المشروع

```
main.py            - نقطة التشغيل
context.py         - إعداد السياق (MCP)
gpt_agent.py       - التفاعل مع GPT
github_api.py      - GitHub API
tracker.py         - تتبع المشروع
reports.py         - توليد التقارير
.env.template      - قالب المفاتيح البيئية
requirements.txt   - التبعيات
README.md          - هذا الملف
```

---

###  ملاحظات

* يمكن نشر هذا المشروع على Render أو Railway بسهولة.
* يدعم التوسعة لإضافة Slack/Discord Bots.
* يمكنك ربطه بجداول زمنية (CRON) لتقارير يومية.

---


