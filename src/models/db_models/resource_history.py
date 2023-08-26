'''File for resource_history DB table'''

import logging
from datetime import datetime

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

logger = logging.getLogger('pyhir.models.db_models.resource_history')

class ResourceHistory(Base):
    __tablename__ = "resource_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    version: Mapped[int] = mapped_column(primary_key=True)
    create_time: Mapped[datetime]
    resource: Mapped[dict] = mapped_column(JSONB)

    def __repr__(self) -> dict:
        return self.resource
