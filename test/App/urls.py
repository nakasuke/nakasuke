from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
    path('', views.CompanyList.as_view(), name='list'),                         #一覧画面
    path('detail/<int:pk>/',views.CompanyDetail.as_view(),name='detail'),       #詳細画面
    path('create/',views.CompanyCreateView.as_view(),name='create'),            #新規登録画面(会社)
    path('create2/',views.CompanyCreateView2.as_view(),name='create2'),         #新規登録画面(従業員)
    path('update/<int:pk>/',views.CompanyUpdateView.as_view(),name='update'),   #更新画面(会社)
    path('update2/<int:pk>/',views.CompanyUpdateView2.as_view(),name='update2'),#更新画面(従業員)
    path('delete/<int:pk>/',views.CompanyDeleteView.as_view(),name='delete'),   #削除画面(会社)
]
