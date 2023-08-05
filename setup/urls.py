from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import AlunosViewSet, ApoliceListCreateView, ApoliceRetrieveUpdateDestroyView, CursosViewSet, ListaMatriculasAluno, ListaAlunosMatriculados, MatriculaViewSet, TipoApoliceListCreateView, TipoApoliceRetrieveUpdateDestroyView, TipoVendaApoliceListCreateView, TipoVendaApoliceRetrieveUpdateDestroyView, adicionar_aluno, EditarAlunoView, atualizar_aluno
from django.conf import settings
from django.conf.urls.static import static


# isso server para acessar as rotas pela api aquela que mostra no começo
router = DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')





urlpatterns = [
    path('Controle/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
    path('alunos/adicionar/', adicionar_aluno, name='adicionar_aluno'),
    path('alunos/<int:pk>/', atualizar_aluno, name='atualizar_aluno'),
    path('tipo-apolice/', TipoApoliceListCreateView.as_view(), name='tipo-apolice-list-create'),
    path('tipo-apolice/<int:pk>/', TipoApoliceRetrieveUpdateDestroyView.as_view(), name='tipo-apolice-retrieve-update-destroy'),

    # URLs para TipoVendaApolice
    path('tipo-venda-apolice/', TipoVendaApoliceListCreateView.as_view(), name='tipo-venda-apolice-list-create'),
    path('tipo-venda-apolice/<int:pk>/', TipoVendaApoliceRetrieveUpdateDestroyView.as_view(), name='tipo-venda-apolice-retrieve-update-destroy'),

    # URLs para Apolice
    path('apolice/', ApoliceListCreateView.as_view(), name='apolice-list-create'),
    path('apolice/<int:pk>/', ApoliceRetrieveUpdateDestroyView.as_view(), name='apolice-retrieve-update-destroy'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
