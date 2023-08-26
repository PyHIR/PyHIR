'''File for resource DB table'''

import logging
from datetime import datetime

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

logger = logging.getLogger('pyhir.models.db_models.resource')

class Resource(Base):
    __tablename__ = "resource"

    id: Mapped[int] = mapped_column(primary_key=True)
    version: Mapped[int]
    create_time: Mapped[datetime]
    resource: Mapped[dict] = mapped_column(JSONB)

    def __repr__(self) -> dict:
        return self.resource
