from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import AlunosViewSet, CursosViewSet, ListaMatriculasAluno, ListaAlunosMatriculados, MatriculaViewSet, adicionar_aluno, EditarAlunoView, atualizar_aluno
from django.conf import settings
from django.conf.urls.static import static

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
