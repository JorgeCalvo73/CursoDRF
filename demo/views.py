from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer, BookMiniSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
"""
Book.objects tiene varios métodos:
    all() que devuelve todos los registros
    filter() que permite pasar parámetros dentro del método para filtrar
    get() que devuelve sólo un registro, podemos pasar parámetros dentro del get


class Another(View):

    book = Book.objects.get(id = 1)

    output = f"We have {book.title} book with ID {book.id}"

    #for book in books:
        #output += f"We have {book.title} book with ID {book.id}"

    def get(self, request):
        return HttpResponse(self.output)


#render acepta un tercer parámetro, el cual es un objeto que podemos usar en el template que estamos pasando en el render
def first(request):

    books = Book.objects.all()

    return render(request, 'first_temp.html', {'books': books})

"""

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    #Con este método, sacado directamente de .ModelViewSet, retornamos un único registro, y en ese caso usamos el BookSerializer
    # para que nos saque la info completa del libro
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)