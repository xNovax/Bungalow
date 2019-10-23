# Generated by Django 2.2.6 on 2019-10-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area_unit', models.TextField(blank=True, verbose_name='Area Unit')),
                ('bathrooms', models.FloatField(blank=True, null=True, verbose_name='Number of Bathrooms')),
                ('bedrooms', models.IntegerField(blank=True, null=True, verbose_name='Number of Bedrooms')),
                ('home_size', models.IntegerField(blank=True, null=True, verbose_name='House Size')),
                ('home_type', models.CharField(blank=True, choices=[('SingleFamily', 'Single Family'), ('VacantResidentialLand', 'Vacant Residential Land'), ('Miscellaneous', 'Miscellaneous'), ('MultiFamily2To4', 'Multi Family 2 to 4'), ('Condominium', 'Condominium'), ('Apartment', 'Apartment'), ('Duplex', 'Duplex')], max_length=50, null=True, verbose_name='Home Type')),
                ('last_sold_date', models.DateField(blank=True, null=True, verbose_name='Last Sold Date')),
                ('last_sold_price', models.IntegerField(blank=True, null=True, verbose_name='Last Sold Price')),
                ('link', models.URLField(blank=True, verbose_name='Link')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Price $')),
                ('property_size', models.IntegerField(blank=True, null=True, verbose_name='Property Size')),
                ('rent_price', models.IntegerField(blank=True, null=True, verbose_name='Rent Price')),
                ('rentzestimate_amount', models.IntegerField(blank=True, null=True)),
                ('rentzestimate_last_updated', models.DateField(blank=True, null=True)),
                ('tax_value', models.FloatField(blank=True, null=True, verbose_name='Tax Value')),
                ('tax_year', models.IntegerField(blank=True, null=True, verbose_name='Tax Year')),
                ('year_built', models.IntegerField(blank=True, null=True, verbose_name='Year Built')),
                ('zestimate_amount', models.IntegerField(blank=True, null=True)),
                ('zestimate_last_updated', models.DateField(blank=True, null=True)),
                ('zillow_id', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Zillow ID')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('city', models.TextField(blank=True, verbose_name='City')),
                ('state', models.TextField(blank=True, verbose_name='State')),
                ('zipcode', models.CharField(blank=True, max_length=5, verbose_name='Zip Code')),
            ],
        ),
    ]
