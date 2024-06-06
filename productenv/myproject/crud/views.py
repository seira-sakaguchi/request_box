from django.shortcuts import render
from django.views import generic
from .models import Product
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ProductCreateForm

class ProductListView(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 5

    #検索機能を作る
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:  #検索ワードがgetされたら一致するものだけをproduct_listとして表示
            product_list = Product.objects.filter(
                name__icontains=query)    #__icontainsは小文字大文字の区別がない。部分一致で可。
        else:  #何も検索されていなければ通常通り全てのリストを表示
            product_list = Product.objects.all()
        return product_list

class ProductCreateView(generic.CreateView):
    model = Product
    template_name = 'new_product.html'
    success_url = reverse_lazy('crud:list')
    form_class = ProductCreateForm

    # バリデーション
    def form_valid(self,form):
        product = form.save(commit=False) #DBにフォームの内容を保存せずに該当のモデルオブジェクト(Product)を取得
        product.user = self.request.user
        product.save() #実際にDBに保存
        messages.success(self.request,'商品を登録しました。') #メッセージのフレームワークを作っている。
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'商品の登録に失敗しました。')
        return super().form_invalid(form)


class ProductUpdateView(generic.UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('crud:list')
   
    def form_valid(self,form):
        messages.success(self.request,'商品情報を更新しました。')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'商品情報の更新に失敗しました。')
        return super().form_invalid()
        

class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('crud:list')

    def form_valid(self,form):
        messages.success(self.request,'商品情報を削除しました。')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'商品削除に失敗しました。')
        return super().form_invalid()

