from django.urls import path
from .views import *

urlpatterns=[
        path('login',Log.as_view(),name='login'),
        path('add',Add.as_view(),name="add"),
        path('count',Count.as_view(),name="count"),
        path('cal',Cal.as_view(),name="cal"),
        path('form',Regview.as_view(),name="forms"),
        path('vemp',employeelist.as_view(),name='vemp1'),
        path('demp\<int:eid>',Deletemp.as_view(),name='demp1'),
        path('upemp\<int:eid>',Update.as_view(),name='upemp'),
        path('man',Addman.as_view(),name='man'),
        path('vman',managerLIst.as_view(),name='vman'),
        path('delman\<int:eid>',delman.as_view(),name='dman'),
        path('upman\<int:eid>',updateMan.as_view(),name='uman'),

]