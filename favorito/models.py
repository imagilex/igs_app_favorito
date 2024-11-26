from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe


class Favorito(models.Model):
    user = models.ForeignKey(
        User, models.CASCADE, related_name="mis_favoritos")
    etiqueta = models.CharField(max_length=300)
    url = models.URLField(max_length=500)

    class Meta:
        ordering = ['user', 'etiqueta', 'url']
        permissions = [
            ('view_mine_fav', 'Ver Mis Favoritos'),
            ('add_mine_fav', 'Agregar Mis Favoritos'),
            ('change_mine_fav', 'Actualizar Mis Favoritos'),
            ('delete_mine_fav', 'Eliminar Mis Favoritos'),
            ('add_ad_mine_fav', 'Agregar Mis Favoritos (Acceso Directo)'),
            ('delete_ad_mine_fav', 'Eliminar Mis Favoritos (Acceso Directo)'),
        ]

    def __str__(self):
        return self.etiqueta

    @property
    def a_internal(self) -> str:
        return self.a()

    @property
    def a_external(self) -> str:
        return self.a(True)

    def a(self, external: bool = False) -> str:
        target = ' target="_blank"' if external else ""
        title = f'title="{self.etiqueta}"'
        href = f'href="{self.url}"'
        return mark_safe(
            f'<a {href} class="fav-lnk" {target} {title}>'
            f'{truncatechars(self.etiqueta, 20)}</a>')
