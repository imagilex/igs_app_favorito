from igs_app_base.hiperforms import BaseHiperModelForm

from .models import Favorito


class MainForm(BaseHiperModelForm):
    class Meta:
        model = Favorito
        fields = "__all__"


class UsrMainForm(BaseHiperModelForm):
    class Meta:
        model = Favorito
        fields = ["etiqueta", "url"]
