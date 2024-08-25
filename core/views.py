from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer


@csrf_exempt
@api_view(["GET", "POST"])
def livro_list_create(request):
    if request.method == "GET":
        print("GET em livros")
        livros = Livro.objects.all()
        print(f"livros: {livros}")
        serializer = LivroSerializer(livros, many=True)
        print(f"serializer: {serializer.data}")
        return Response(serializer.data)

    if request.method == "POST":
        serializer = LivroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def livro_detail(request, pk):
    livro = Livro.objects.get(pk=pk)

    if request.method == "GET":
        serializer = LivroSerializer(livro)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
