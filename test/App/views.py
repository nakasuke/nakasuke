from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)
from . import models

#一覧画面
class CompanyList(ListView):
    #Companyテーブル連携
    model = models.Company
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "company_list"
    #テンプレートファイル連携
    template_name = "Company_list.html"

#詳細画面
class CompanyDetail(DetailView):
    #Companyテーブル連携
    model = models.Company
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "company_detail"
    #テンプレートファイル連携
    template_name = "Company_detail.html"

#Create(会社)画面
class CompanyCreateView(CreateView):
    #Companyテーブル連携
    model = models.Company
    #入力項目定義
    fields = ("name","industory","location")
    #テンプレートファイル連携
    template_name = "Company_form.html"
    #更新後のリダイレクト先
    def get_success_url(self):
        return reverse('App:detail', kwargs={'pk': self.object.pk})

#Create(従業員)画面
class CompanyCreateView2(CreateView):
    #Companyテーブル連携
    model = models.Employee
    #入力項目定義
    fields = ("name","age","company")
    #テンプレートファイル連携
    template_name = "Company_form.html"
    #作成後のリダイレクト先
    success_url = reverse_lazy("App:list")

#Upadate画面(会社情報)
class CompanyUpdateView(UpdateView):
    #入力項目定義
    fields = ("name","industory","location")
    #Companyテーブル連携
    model = models.Company
    #テンプレートファイル連携
    template_name = "Company_form.html"
    #更新後のリダイレクト先
    def get_success_url(self):
        return reverse('App:detail', kwargs={'pk': self.object.pk})

#更新画面(従業員情報)
class CompanyUpdateView2(UpdateView):
    #入力項目定義
    fields = ("name","age")
    #Employeeテーブル連携
    model = models.Employee
    #テンプレートファイル連携
    template_name = "Company_form.html"
    #更新後のリダイレクト先
    success_url = reverse_lazy("App:list")

#削除画面
class CompanyDeleteView(DeleteView):
    #Companyテーブル連携
    model = models.Company
    #テンプレートファイル連携
    template_name = "Company_delete.html"
    #削除後のリダイレクト先
    success_url = reverse_lazy("App:list")