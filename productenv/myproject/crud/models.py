from django.db import models


class Product(models.Model):

    # purchase_codeはプルダウン式のため、選択肢を記載
    purchase_code_choices = [
        ('','選択してください'),
        ('1', 'T1111'),
        ('2', 'T08754395'),
        ('3', 'T768594444'),
    ]

    code = models.PositiveBigIntegerField(verbose_name='商品コード')
    name = models.CharField(verbose_name='商品名', max_length=100)
    price = models.PositiveBigIntegerField(verbose_name='単価')
    stock = models.PositiveBigIntegerField(verbose_name='在庫数')
    purchase_code = models.CharField(verbose_name='仕入れ先コード', choices=purchase_code_choices, max_length=100)

    def __str__(self):
        return self.name

