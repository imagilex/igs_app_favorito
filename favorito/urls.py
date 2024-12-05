from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.urls import include
from django.urls import path

from .vw import UsrAddFav
from .vw import UsrCreate
from .vw import UsrDelete
from .vw import UsrDeleteFav
from .vw import UsrDeleteMany
from .vw import UsrGetList
from .vw import UsrList
from .vw import UsrRead
from .vw import UsrUpdate
from .vw import views
from igs_app_base.utils.utils import create_view_urls

obj = 'favorito'
app_label = 'igs_app_favorito'

urlpatterns = views.create_urls(app_label) + [
    path('yo/', include(create_view_urls(
        app_label, "mine_fav",
        UsrList, UsrCreate, UsrUpdate, UsrRead,
        UsrDeleteMany, UsrDelete))),
] + [
    path(
        'get/',
        login_required(UsrGetList.as_view()),
        name=f"{obj}_get"),
    path(
        'add/',
        permission_required(f"{app_label}.add_ad_mine_fav", '/')(
            UsrAddFav.as_view()),
        name=f"{obj}_add"),
    path(
        'delete/',
        permission_required(f"{app_label}.delete_ad_mine_fav", '/')(
            UsrDeleteFav.as_view()),
        name=f"{obj}_delete"),
]
