import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("agricultores", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cultivo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=100)),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("hortaliza", "Hortaliza"),
                            ("fruta", "Fruta"),
                            ("aromatica", "Aromática"),
                            ("grano", "Grano"),
                            ("semilla", "Semilla"),
                        ],
                        default="hortaliza",
                        max_length=20,
                    ),
                ),
                ("cantidad_kg", models.DecimalField(decimal_places=2, max_digits=7)),
                ("disponible_intercambio", models.BooleanField(default=True)),
                ("creado", models.DateTimeField(auto_now_add=True)),
                (
                    "agricultor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cultivos",
                        to="agricultores.agricultor",
                    ),
                ),
            ],
            options={
                "ordering": ["-creado"],
            },
        ),
    ]
