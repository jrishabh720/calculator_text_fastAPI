from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.tools import router as tools_router
from app.core.config import settings
from pathlib import Path
from fastapi.responses import FileResponse

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    description="A modular platform for tools and AI agents.",
)

app.include_router(health_router)
app.include_router(tools_router)


@app.get("/", include_in_schema=False)
def root():
    html_file = Path(__file__).parent / "static" / "index.html"
    return FileResponse(html_file)