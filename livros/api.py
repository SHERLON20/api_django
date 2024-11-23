from ninja import Router,Query
from .schemas import livrosschema,avaliacaoschemas,filtrossortear
from .models import livros,categoria



livros_routers=Router()

@livros_routers.post('/')
def create_livro(request,livro_schema: livrosschema):
    nome = livro_schema.dict()['nome']
    streaming = livro_schema.dict()['streaming']
    categorias = livro_schema.dict()['categorias']
    if streaming not in ['F','AK']:
        return 400,{'status':'erro: streaming deve ser f ou AK'}
    livro = livros(
        nome = nome,
        streaming = streaming,
    )
    livro.save()
    for categori in categorias:
        categoria_temp = categoria.objects.get(id=categori)
        livro.categorias.add(categoria_temp)
    return {'status':'ok'}

@livros_routers.put('/{livro_id}',response={200:dict,404:dict})
def avaliar_livro(request,livro_id:int,avaliacao_schemas:avaliacaoschemas):
    comentarios = avaliacao_schemas.dict()['comentarios']
    nota = avaliacao_schemas.dict()['nota']
    if nota <0 or nota>10:
        return 404,{'error 404':'nota deve ser um numero entre 0 e 10'}
    try:
        livro= livros.objects.get(id= livro_id)
        livro.comentarios = comentarios
        livro.nota = nota
        livro.save()
        return 200,{'status':'avaliação realizada com sucesso!'}
    except:
        return {'ERROR 500':'erro interno do servidor!'}
    
@livros_routers.delete('/{livro_id}')
def deletar_livro(request,livro_id:int):
    livro = livros.objects.get(id=livro_id)
    livro.delete()
    return {'livro deletado':livro.nome}

@livros_routers.get('/sortear/',response={200:dict,404:dict})
def sortear_livros(request,filtros:Query[filtrossortear]):
    nota_minima = filtros.dict()['nota_minima']
    categoria = filtros.dict()['categorias']
    reler = filtros.dict()['reler']
    livro = livros.objects.all()
    if not reler:
        livro = livro.filter(nota = None)
    if nota_minima:
        livro = livro.filter(nota_gte = nota_minima)
    if categoria:
        livro = livro.filter(categorias_id = categoria)
    
    livro1 = livro.order_by('?').first()
    
    if livro.count()>0:
        return 200,{'livro selecionado':livro1.nome}
    else:
        return 404,{'status':'livro não encontrado'}