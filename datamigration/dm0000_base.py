from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from igs_app_base.menu.models import MenuOpc
from igs_app_base.models import App
from igs_app_base.utils.utils import add_or_create_menuopc


def migration():
    app, created = App.objects.get_or_create(nombre="mis_favoritos")
    if created:
        app.posicion = 1002
        app.display_as_app = False
        app.save()

    adm = MenuOpc.objects.get(nombre="Administrar")

    add_or_create_menuopc(
        "Favoritos", 7, adm, "favorito")

    mine_perms = [
        Permission.objects.get(codename="view_mine_fav"),
        Permission.objects.get(codename="add_mine_fav"),
        Permission.objects.get(codename="change_mine_fav"),
        Permission.objects.get(codename="delete_mine_fav"),
        Permission.objects.get(codename="add_ad_mine_fav"),
        Permission.objects.get(codename="delete_ad_mine_fav"),
    ]

    gpo = Group.objects.get("Basico")
    gpo.permissions.add(mine_perms)
