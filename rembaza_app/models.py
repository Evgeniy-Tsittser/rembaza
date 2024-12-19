from django.db import models
from datetime import datetime

"""Генератор списка отчетных годов"""
YEAR_CHOICES = [(y, y) for y in range(2024, datetime.now().year + 2)]

"""Модель для фиксации выполненных работ за каждый месяц
 - заполняется в админ-панели,
 - перед внесением данных нужно выбрать в выпадающем списке год,
  месяц и соответствующий вид работ"""


class MonthWorks(models.Model):
    TYPE_CHOICES = (
        (1, 'Вода'),
        (2, 'Канализация')
    )

    MONTH_CHOICES = (
        (1, 'Январь'),
        (2, 'Февраль'),
        (3, 'Март'),
        (4, 'Апрель'),
        (5, 'Май'),
        (6, 'Июнь'),
        (7, 'Июль'),
        (8, 'Август'),
        (9, 'Сентябрь'),
        (10, 'Октябрь'),
        (11, 'Ноябрь'),
        (12, 'Декабрь')
    )

    type_work = models.IntegerField(choices=TYPE_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    month = models.IntegerField(choices=MONTH_CHOICES)
    completed_works = models.CharField(max_length=255)
    description = models.TextField()
    volume = models.FloatField(default=0.0)
    summ = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return self.completed_works


"""Модель для агрегации данных по воде за весь год
 - заполняется автоматически при внесении данных в таблицу MonthWorks 
  в зависимости от установленного отчетного года"""


class WaterTable(models.Model):
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    completed_works = models.CharField(max_length=255)
    january_vol = models.FloatField(null=True, blank=True, default=0.0)
    january_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    february_vol = models.FloatField(null=True, blank=True, default=0.0)
    february_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    march_vol = models.FloatField(null=True, blank=True, default=0.0)
    march_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    first_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    april_vol = models.FloatField(null=True, blank=True, default=0.0)
    april_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    may_vol = models.FloatField(null=True, blank=True, default=0.0)
    may_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    june_vol = models.FloatField(null=True, blank=True, default=0.0)
    june_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    second_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    july_vol = models.FloatField(null=True, blank=True, default=0.0)
    july_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    august_vol = models.FloatField(null=True, blank=True, default=0.0)
    august_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    september_vol = models.FloatField(null=True, blank=True, default=0.0)
    september_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    third_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    october_vol = models.FloatField(null=True, blank=True, default=0.0)
    october_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    november_vol = models.FloatField(null=True, blank=True, default=0.0)
    november_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    december_vol = models.FloatField(null=True, blank=True, default=0.0)
    december_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    fourth_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    year_total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)

    def __str__(self):
        return self.completed_works


"""Модель для агрегации данных по водоотведению за весь год
 - заполняется автоматически при внесении данных в таблицу MonthWorks
 в зависимости от установленного отчетного года"""


class SeverageTable(models.Model):
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    completed_works = models.CharField(max_length=255)
    january_vol = models.FloatField(null=True, blank=True, default=0.0)
    january_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    february_vol = models.FloatField(null=True, blank=True, default=0.0)
    february_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    march_vol = models.FloatField(null=True, blank=True, default=0.0)
    march_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    first_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    april_vol = models.FloatField(null=True, blank=True, default=0.0)
    april_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    may_vol = models.FloatField(null=True, blank=True, default=0.0)
    may_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    june_vol = models.FloatField(null=True, blank=True, default=0.0)
    june_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    second_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    july_vol = models.FloatField(null=True, blank=True, default=0.0)
    july_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    august_vol = models.FloatField(null=True, blank=True, default=0.0)
    august_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    september_vol = models.FloatField(null=True, blank=True, default=0.0)
    september_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    third_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    october_vol = models.FloatField(null=True, blank=True, default=0.0)
    october_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    november_vol = models.FloatField(null=True, blank=True, default=0.0)
    november_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    december_vol = models.FloatField(null=True, blank=True, default=0.0)
    december_summ = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    fourth_quarter = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)
    year_total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, default=0.00)

    def __str__(self):
        return self.completed_works
