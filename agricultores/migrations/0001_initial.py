from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agricultor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=100)),
                ("barrio", models.CharField(max_length=100)),
                ("telefono", models.CharField(blank=True, max_length=20)),
                ("creado", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "agricultor",
                "verbose_name_plural": "agricultores",
                "ordering": ["nombre"],
            },
        ),
    ]
