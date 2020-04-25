# Generated by Django 3.0.2 on 2020-04-25 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('synergy', '0013_customuser_info_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(choices=[(None, '- Select -'), ('CAN', 'Canada'), ('USA', 'United States'), ('OTH', 'Other')], max_length=3)),
                ('industry', models.CharField(choices=[(None, '- Select -'), ('AERO', 'Aerospace & Defense'), ('AGRI', 'Agriculture & Forestry'), ('AUTO', 'Automotive'), ('BUSI', 'Business'), ('CHEM', 'Chemicals'), ('CONS', 'Construction'), ('DIST', 'Distribution, Wholesale, Retail'), ('EDUC', 'Education'), ('ELCE', 'Electrical Equipment'), ('ELCT', 'Electronics'), ('ENGI', 'Engineering & Technical Services'), ('FOOD', 'Food, Beverage, Tobacco'), ('GOVE', 'Government & Military'), ('MACH', 'Machinery'), ('MANU', 'Manufacturing'), ('MEDI', 'Medical & Healthcare'), ('META', 'Metals - Raw, Formed, Fabricated'), ('MINI', 'Mining, Oil & Gas, Quarrying'), ('OTH', 'Other'), ('PAPE', 'Paper, Paper Products, Printing'), ('PLAS', 'Plastics & Rubber'), ('TEXT', 'Textiles, Apparel, Leather'), ('TRAN', 'Transportation & Logistics'), ('UTIL', 'Utilities & Telecommunications')], max_length=4)),
                ('postal_code', models.CharField(max_length=7, null=True)),
                ('website', models.URLField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='company_website',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='request',
            name='client',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='synergy.Business'),
        ),
    ]
