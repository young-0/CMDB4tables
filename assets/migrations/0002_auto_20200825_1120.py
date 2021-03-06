# Generated by Django 2.2 on 2020-08-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'verbose_name': '服务器', 'verbose_name_plural': '服务器'},
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[('server', '服务器'), ('networkdevice', '网络设备'), ('storagedevice', '存储设备'), ('securitydevice', '安全设备'), ('software', '软件资产')], default='server', max_length=64, verbose_name='资产类型'),
        ),
        migrations.AlterField(
            model_name='newassetapprovalzone',
            name='asset_type',
            field=models.CharField(blank=True, choices=[('server', '服务器'), ('networkdevice', '网络设备'), ('storagedevice', '存储设备'), ('securitydevice', '安全设备'), ('software', '软件资产')], default='server', max_length=64, null=True, verbose_name='资产类型'),
        ),
        migrations.AlterField(
            model_name='server',
            name='model',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='服务器型号'),
        ),
        migrations.AlterField(
            model_name='server',
            name='sub_asset_type',
            field=models.SmallIntegerField(choices=[(0, 'PC服务器'), (1, '刀片机'), (2, '小型机')], default=0, verbose_name='服务器类型'),
        ),
    ]
