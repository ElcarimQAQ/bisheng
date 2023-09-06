from datetime import datetime, timezone
from typing import Dict, Optional
from uuid import UUID

from bisheng.database.models.base import SQLModelSerializable
from pydantic import BaseModel, validator
from sqlalchemy import JSON, TIMESTAMP, Column, DateTime, text
from sqlmodel import Field


class ModelDeployBase(SQLModelSerializable):
    endpoint: str = Field(index= False, unique=False)
    server: str = Field(index= True)
    model: str = Field(index=False)
    config: Optional[str] = Field(index=False)
    status: Optional[str] = Field(index=False)
    remark: Optional[str] = Field(index= False)

    create_time: Optional[datetime] = Field(sa_column=Column(DateTime, nullable=False, index=True,
                                                   server_default=text('CURRENT_TIMESTAMP')))
    update_time: Optional[datetime] = Field(sa_column=Column(DateTime, nullable=False,
                                                   server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP')))

class ModelDeploy(ModelDeployBase, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ModelDeployRead(ModelDeployBase):
    id: Optional[int]

class ModelDeployQuery(SQLModelSerializable):
    id: Optional[int]
    server: Optional[str]

class ModelDeployCreate(ModelDeployBase):
    pass

class ModelDeployUpdate(SQLModelSerializable):
    id: int
    config: Optional[str] = None