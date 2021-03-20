from django.db import models

JOURNAL_TYPE_BULLET = 1
JOURNAL_TYPE_FOOD = 2
JOURNAL_TYPE_TRAVEL = 3
JOURNAL_TYPE_SPORT = 4
JOURNAL_TYPES = (
    (JOURNAL_TYPE_BULLET, 'bullet'),
    (JOURNAL_TYPE_FOOD, 'food'),
    (JOURNAL_TYPE_TRAVEL, 'travel'),
    (JOURNAL_TYPE_SPORT, 'sport'),
)


class BookJournalBase(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    description = models.TextField(max_length=500, blank=True, verbose_name="Описание")
    created_at = models.DateField(auto_now_add=True, verbose_name="Когда создан?")

    class Meta:
        abstract = True
        ordering = ['-created_at']
        verbose_name = "Базовый класс для книг и журналов"
        verbose_name_plural = "Базовые классы для книг и журналов"


class Book(BookJournalBase):
    num_pages = models.IntegerField(verbose_name="Сколько страниц?", blank=True)
    genre = models.CharField(max_length=100, verbose_name="Жанр книги")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        res = '%s %s' % (self.name, self.genre)
        return res.strip()


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=JOURNAL_TYPES,
                                    default=JOURNAL_TYPE_BULLET,
                                    verbose_name="Вид журнала")
    publisher = models.CharField(max_length=100, verbose_name="Автор")

    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журналы"

    def __str__(self):
        res = '%s %s' % (self.name, self.publisher)
        return res.strip()
