"""CI test: must be rejected by the cross-import check."""

from core_api.main import app

__all__ = ["app"]
