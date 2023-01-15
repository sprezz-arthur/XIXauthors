# Generated by Django 4.1.4 on 2023-01-15 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bibliotheque", "0003_personne_remove_livre_auteur_delete_auteur"),
    ]

    operations = [
        migrations.CreateModel(
            name="Auteur",
            fields=[
                (
                    "personne_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="bibliotheque.personne",
                    ),
                ),
            ],
            bases=("bibliotheque.personne",),
        ),
        migrations.AddField(
            model_name="livre",
            name="auteur",
            field=models.ManyToManyField(blank=True, to="bibliotheque.auteur"),
        ),
    ]
