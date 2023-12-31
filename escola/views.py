from rest_framework import viewsets, generics
from rest_framework import status
from escola.models import Aluno, Apolice, Curso, Matricula, TipoApolice, TipoVendaApolice
from escola.serializer import AlunoSerializer, AlunoSerializerV2, ApoliceSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer, TipoApoliceSerializer, TipoVendaApoliceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView
from rest_framework import filters


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer


class EditarAlunoView(UpdateAPIView):
    """View para editar um aluno"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def get_object(self):
        # Obtém o aluno com base no parâmetro pk da URL
        pk = self.kwargs['pk']
        return Aluno.objects.get(pk=pk)

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('nome'):
            return ['nome']
        return super().get_search_fields(view, request)



class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put', 'path']


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer


class TipoApoliceListCreateView(generics.ListCreateAPIView):
    queryset = TipoApolice.objects.all()
    serializer_class = TipoApoliceSerializer

class TipoApoliceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoApolice.objects.all()
    serializer_class = TipoApoliceSerializer

# Views para TipoVendaApolice
class TipoVendaApoliceListCreateView(generics.ListCreateAPIView):
    queryset = TipoVendaApolice.objects.all()
    serializer_class = TipoVendaApoliceSerializer

class TipoVendaApoliceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoVendaApolice.objects.all()
    serializer_class = TipoVendaApoliceSerializer

# Views para Apolice
class ApoliceListCreateView(generics.ListCreateAPIView):
    queryset = Apolice.objects.all()
    serializer_class = ApoliceSerializer

class ApoliceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apolice.objects.all()
    serializer_class = ApoliceSerializer







@api_view(['POST'])
def adicionar_aluno(request):
    if request.method == 'POST':
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT'])
def atualizar_aluno(request, pk):
    try:
        aluno = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
        return Response({"error": "Aluno não encontrado."}, status=404)

    if request.method == 'PUT':
        # Remove o campo 'foto' do dicionário request.data
        request.data.pop('foto', None)

        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
