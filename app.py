from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.nota_routes import nota_route
from routes.tipo_nota_routes import tipo_nota_route
from routes.usuario_routes import usuario_route

app = FastAPI(
    title="NOTAS API",
    description="REST API DE NOTAS",
    version="0.0.1",
    # openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(nota_route)
app.include_router(tipo_nota_route)
app.include_router(usuario_route)
