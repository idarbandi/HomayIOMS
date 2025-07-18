# Generated by Django 5.2.1 on 2025-07-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_customer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('Active', '✅ فعال'), ('Inactive', '⏸️ غیرفعال'), ('Suspended', '🚫 معلق'), ('Blocked', '🔒 مسدود'), ('Requested', '📝 در انتظار تایید')], default='Active', help_text='وضعیت فعلی مشتری در سیستم', max_length=255, verbose_name='📊 وضعیت مشتری'),
        ),
    ]
