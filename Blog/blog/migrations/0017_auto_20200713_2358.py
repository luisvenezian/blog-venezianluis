# Generated by Django 3.0.8 on 2020-07-13 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200708_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='email',
            field=models.TextField(default='email@email.com', max_length=200),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='autor',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_email_autor'),
        ),
        migrations.AddConstraint(
            model_name='autor',
            constraint=models.UniqueConstraint(fields=('usuario',), name='unique_usuario_autor'),
        ),
    ]