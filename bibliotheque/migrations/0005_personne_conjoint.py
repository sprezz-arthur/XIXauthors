# Generated by Django 4.1.4 on 2023-01-15 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bibliotheque", "0004_auteur_livre_auteur"),
    ]

    operations = [
        migrations.AddField(
            model_name="personne",
            name="conjoint",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="bibliotheque.personne",
            ),
        ),
    ]