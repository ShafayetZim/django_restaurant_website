# Generated by Django 4.0.2 on 2022-05-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('biryani', 'biryani'), ('curry_combo', 'curry_combo'), ('vegetable_combo', 'vegetable_combo'), ('appetizers', 'appetizers'), ('extra_order', 'extra_order'), ('drinks', 'drinks')], default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='food/images')),
            ],
        ),
    ]
