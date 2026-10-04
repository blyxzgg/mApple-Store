from django.db import models

class BannerImage(models.Model):
    image = models.ImageField(
        upload_to='banners/',
        verbose_name="Изображение для баннера"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Картинка баннера"
        verbose_name_plural = "Картинка баннера"

    def __str__(self):
        return "Изображение баннера"

