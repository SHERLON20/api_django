from ninja import ModelSchema,Schema
from .models import livros

class livrosschema(ModelSchema):
    class Meta:
        model = livros
        fields = ['nome','streaming','categorias']

class avaliacaoschemas(ModelSchema):
    class Meta:
        model = livros
        fields = ['nota','comentarios']

class filtrossortear(Schema):
    nota_minima : int=None
    categorias : int = None
    reler : bool = False