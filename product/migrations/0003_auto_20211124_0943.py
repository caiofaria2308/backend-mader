# Generated by Django 3.2.9 on 2021-11-24 12:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211124_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icms_csosn',
            field=models.SmallIntegerField(choices=[(101, 'Tributada pelo Simples Nacional com permissão de crédito'), (102, 'Tributada pelo Simples Nacional sem permissão de crédito '), (103, 'Isenção do ICMS no Simples Nacional para faixa de receita bruta'), (201, 'Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por substituição tributária'), (202, 'Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por substituição tributária'), (203, 'Isenção do ICMS no Simples Nacional para faixa de receita bruta e com cobrança do ICMS por substituição tributária '), (300, 'Imune'), (400, 'Não tributada pelo Simples Nacional'), (500, 'ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação '), (900, 'Outros')], null=True, verbose_name='icms csosn'),
        ),
        migrations.AlterField(
            model_name='product',
            name='icms_origin',
            field=models.SmallIntegerField(choices=[(0, 'Nacional, exceto as indicadas nos códigos 3 a 5 '), (1, 'Estrangeira - Importação direta, exceto a indicada no código 6 '), (2, 'Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7 '), (3, 'Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40%'), (4, 'Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam o Decreto-Lei nº 288/67 e as Leis nºs 8.248/91,8.387/91, 10.176/01 e 11.484/07'), (5, 'Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%'), (6, 'Estrangeira - Importação direta, sem similar nacional, constante em lista de Resolução CAMEX'), (7, 'Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista de Resolução CAMEX')], null=True, verbose_name='origem icms'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='type',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
