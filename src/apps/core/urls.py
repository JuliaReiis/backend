from django.urls import path
from .views.user import UserView
# from .views.views import views

urlpatterns = [
    path('user/', UserView),
    # path('doc/', DocView),
    # path('company/', CompanyView),









    # path('user/', views.list_users, name='user-list'),
    # path('users/<int:user_id>/', views.listar_company_por_usuario, name='user-detail'),
    # path('listar-doc/<int:company_id>/<int:user_id>/', views.listar_doc_por_company_e_usuario, name='listar_doc_por_company_e_usuario'),
    # path('criar-company/', views.criar_company, name='criar_company'),
    # path('criar-usuario/', views.criar_usuario, name='criar_usuario'),
    # path('criar-doc/', views.criar_doc, name='criar_doc'),
    # path('atualizar-company/<int:company_id>/', views.atualizar_company, name='atualizar_company'),
    # path('atualizar-usuario/<int:user_id>/', views.atualizar_usuario, name='atualizar_usuario'),
    # path('atualizar-doc/<int:doc_id>/', views.atualizar_doc, name='atualizar_doc'),
    # path('deletar-company/<int:company_id>/', views.deletar_company, name='deletar_company'),
    # path('deletar-usuario/<int:user_id>/', views.deletar_usuario, name='deletar_usuario'),
    # path('deletar-doc/<int:doc_id>/', views.deletar_doc, name='deletar_doc'),
]
