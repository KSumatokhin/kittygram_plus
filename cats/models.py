from django.db import models as m


class Achievement(m.Model):
    name = m.CharField(max_length=64)

    def __str__(self):
        return self.name


class Owner(m.Model):
    first_name = m.CharField(
        max_length=128)
    last_name = m.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Cat(m.Model):
    name = m.CharField(max_length=16)
    color = m.CharField(max_length=16)
    birth_year = m.IntegerField()
    # Новое поле в модели:
    owner = m.ForeignKey(
        Owner, related_name='cats', on_delete=m.CASCADE)
    # Связь будет описана через вспомогательную модель AchievementCat
    achievements = m.ManyToManyField(
        Achievement,
        through='AchievementCat')

    def __str__(self):
        return self.name


# В этой модели будут связаны id котика и id его достижения
class AchievementCat(m.Model):
    achievement = m.ForeignKey(
        Achievement,
        on_delete=m.CASCADE)
    cat = m.ForeignKey(
        Cat, on_delete=m.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.cat}'
