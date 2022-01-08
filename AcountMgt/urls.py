from django.urls import path
from . import views

app_name = "AccountMgt"

urlpatterns = [
    # for Personal account
    path('account', views.AcountList.as_view(), name='list'),                   		#一覧画面(Account)
    path('account/detail/<int:pk>/',views.AccountDetail.as_view(),name='account.detail'),       #詳細画面(Account)
    path('account/create',views.AccountCreateView.as_view(),name='account.create'),         	#新規登録画面(Account)
    path('account/update/<int:pk>/',views.AccountUpdateView.as_view(),name='account.update'),   #更新画面(Account)
    path('account/delete/<int:pk>/',views.CompanyDeleteView.as_view(),name='account.delete'),   #削除画面(Account)
    # for Company account
    path('company', views.CompanyList.as_view(), name='list'),                 			#一覧画面(Company)
    path('company/detail/<int:pk>/',views.CompanyDetail.as_view(),name='company.detail'),       #詳細画面(Company)
    path('company/create/',views.CompanyCreateView.as_view(),name='company.create'),            #新規登録画面(Company)
    path('company/update/<int:pk>/',views.CompanyUpdateView.as_view(),name='company.update'),  	#更新画面(Company)
    path('company/delete/<int:pk>/',views.AccountDeleteView.as_view(),name='company.delete2'), 	#削除画面(Company)
]
