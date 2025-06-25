import openai

class ProjectReporter:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_report(self, context):
        prompt = f"""
أنت مساعد تقني ذكي. إليك حالة مشروع GitHub:

📂 المستودع: {context['repo']}

🛠️ المهام المفتوحة:
{chr(10).join(context['issues']) or 'لا توجد مهام حالياً'}

📦 الطلبات المفتوحة (Pull Requests):
{chr(10).join(context['prs']) or 'لا توجد PRs مفتوحة'}

🌿 الفروع النشطة:
{', '.join(context['branches']) or 'فرع رئيسي فقط'}

📊 الرجاء توليد تقرير تنفيذي مختصر لحالة المشروع للمسؤول التقني.
"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
