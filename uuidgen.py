# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "hachitool",
#     "pydantic-settings",
# ]
# ///

import uuid

import hachitool
from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class UUIDGenerator(BaseSettings):
    name: str = Field(default_factory=uuid.uuid4)
    namespace: UUID = Field(default_factory=uuid.uuid4)

    def generate(self):
        return uuid.uuid5(self.namespace, self.name)

    @field_validator("namespace")
    def validate_namespace(cls, v):
        if v.startswith("spec::"):
            try:
                return getattr(uuid, "NAMESPACE_" + v.split("::")[1].upper())
            except AttributeError:
                pass

        try:
            return uuid.UUID(v)
        except ValueError:
            hachitool.fail(f"Invalid namespace: {v}")


hachitool.set_output(uuid=UUIDGenerator().generate())
