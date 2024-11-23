from ninja import NinjaAPI
from livros.api import livros_routers
api = NinjaAPI()
api.add_router('livros',livros_routers)