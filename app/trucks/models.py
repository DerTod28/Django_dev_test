from django.core.validators import MinValueValidator
from django.db import models

from utils.mixins import TimeStampedMixin


class TruckModel(TimeStampedMixin, models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование модели самосвала')
    max_load_capacity = models.IntegerField(validators=[MinValueValidator(0)],
                                            verbose_name='Максимальная грузоподъемность (в тоннах)')

    class Meta:
        verbose_name = 'Модель самосвала'
        verbose_name_plural = 'Модели самосвалов'

    def __str__(self):
        return self.name


class Truck(TimeStampedMixin, models.Model):
    board_number = models.CharField(max_length=100, unique=True, verbose_name='Бортовой номер')
    truck_model = models.ForeignKey('TruckModel', models.CASCADE,
                                    db_column='truck_model',
                                    verbose_name='Модель самосвала')

    class Meta:
        verbose_name = 'Самосвал'
        verbose_name_plural = 'Самосвалы'

    def __str__(self):
        return self.board_number


class CargoType(TimeStampedMixin, models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование груза')

    class Meta:
        verbose_name = 'Тип груза'
        verbose_name_plural = 'Типы грузов'

    def __str__(self):
        return self.name


class Cargo(TimeStampedMixin, models.Model):
    cargo_type = models.ForeignKey('CargoType', models.CASCADE, verbose_name='Вид груза')
    weight = models.IntegerField(validators=[MinValueValidator(0)],
                                 verbose_name='Вес груза (в тоннах)')
    truck = models.ForeignKey('Truck', models.CASCADE, verbose_name='Самосвал')

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

    def __str__(self):
        return self.cargo_type.name
