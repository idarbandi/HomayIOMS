# Generated by Django 5.2.3 on 2025-06-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_add_logs_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='logs',
            field=models.TextField(blank=True, default='', verbose_name='📝 لاگ‌ها', help_text='لاگ‌های تحلیلی برای تیم آنالیتیکس (append only)'),
        ),
    ]
