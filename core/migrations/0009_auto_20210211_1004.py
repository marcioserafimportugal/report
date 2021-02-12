# Generated by Django 3.1.5 on 2021-02-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210208_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='depto',
            field=models.CharField(choices=[('Executive Director', 'Executive Director'), ('Administrative Services', 'Administrative Services'), ('Project Management', 'Project Management'), ('Communication Manager', 'Communication Manager'), ('Department 01: Novos Biopesticidas', 'Department 01'), ('Department 02: Proteção de Culturas Específicas', 'Department 02'), ('Department 03: Gestão de Dados e Análise de Risco', 'Department 03'), ('Department 04: Monitorização e Diagnóstico', 'Department 04'), ('Department 05: Novas Formulações e Matrizes para a Aplicação de Biopesticida', 'Department 05'), ('Department 06: Gestão', 'Department 06')], default='Department 01: Novos Biopesticidas', max_length=100, verbose_name='Department:'),
        ),
    ]