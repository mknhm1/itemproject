from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'gadget'

# URLパターンを登録する変数
urlpatterns = [
    # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),
    
    # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreateGadgetView.as_view(), name='post'),
    
    # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    
    # カテゴリ一覧ページ
    # photos/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('gadgets/<int:category>',
         views.CategoryView.as_view(),
         name = 'gadget_cat'
         ),

    # ユーザーの投稿一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list'
         ),
    
    # 詳細ページ
    # photo-detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('gadget-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'gadget_detail'
         ),
    
    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    # 投稿写真の削除
    # photo/<Photo postsテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('gadget/<int:pk>/delete/',
         views.GadgetDeleteView.as_view(),
         name = 'gadget_delete'

         ),
    path(
        # 問い合わせページのURLは「contact/」
        'contact/',views.ContactView.as_view(),name='contact'
        # viewsモジュールのInquiryViewを実行

        # URLパターンの名前を'contact'にする

        ),
#     path('mypage/', views.MypageView.as_view(), name='mypage'),

#     path('gadget/<int:pk>/delete/' ,views.GadgetDeleteView.as_view(),
#          name='gadget_delate')
]
