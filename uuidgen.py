# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "hachitool",
#     "pydantic-settings",
# ]
# ///

import uuid
import typing as t

import hachitool
from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class UUIDGenerator(BaseSettings):
    namespace: uuid.UUID | t.Literal["dns", "oid", "url", "x500"] = Field(default_factory=uuid.uuid4)
    name: str = Field(default_factory=lambda: uuid.uuid4().hex)

    def generate(self):
        return uuid.uuid5(self.namespace, self.name)

    @field_validator("namespace")
    def validate_namespace(cls, v):
        return getattr(uuid, "NAMESPACE_{v.upper()}", v)

hachitool.set_output(uuid=UUIDGenerator().generate())
