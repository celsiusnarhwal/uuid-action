# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "hachitool",
#     "pydantic-settings",
# ]
# ///

import typing as t
import uuid

import hachitool
from pydantic import Field, TypeAdapter, field_validator
from pydantic_settings import BaseSettings


class UUIDGenerator(BaseSettings):
    namespace: uuid.UUID | t.Literal["dns", "oid", "url", "x500"] = Field(
        default_factory=uuid.uuid4
    )
    name: str = Field(default_factory=lambda: uuid.uuid4().hex)

    def generate(self) -> uuid.UUID:
        return uuid.uuid5(self.namespace, self.name)

    @field_validator("namespace")
    def validate_namespace(cls, v):
        return getattr(uuid, "NAMESPACE_{v.upper()}", v)


generator = UUIDGenerator()
identifier = generator.generate()

output = {
    "uuid": identifier,
    "hex": identifier.hex,
    "int": identifier.int,
    "urn": identifier.urn,
    "namespace": generator.namespace,
    "name": generator.name,
}

hachitool.set_output(**output, json=TypeAdapter(dict).dump_json(output).decode())
