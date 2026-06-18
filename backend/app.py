"""
Nothing Could Be Better — FastAPI Application

Thin entry point that wires together modular components.
"""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Nothing Could Be Better",
        description="A dating site for nihilists.",
        version="0.1.0",
    )

    # Wire up routes
    from backend.routes import landing, profiles, matching, forum
    app.include_router(landing.router)
    app.include_router(profiles.router)
    app.include_router(matching.router)
    app.include_router(forum.router)

    return app


# Module-level app instance for uvicorn
app = create_app()
