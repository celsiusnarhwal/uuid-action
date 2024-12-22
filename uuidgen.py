# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "hachitool",
#     "pydantic-settings",
# ]
# ///

import uuid

import hachitool
from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class UUIDGenerator(BaseSettings):
    model_config = SettingsConfigDict(validate_default=False)

    name: str = None
    namespace: str = None

    def generate(self):
        if self.name and self.namespace:
            return uuid.uuid5(self.namespace, self.name)

        return uuid.uuid4()

    @model_validator(mode="after")
    def validate_model(self):
        if (self.name or self.namespace) and not (self.name and self.namespace):
            hachitool.fail(
                "You must either provide both a name and a namesapce or neither."
            )

        return self

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
            hachitool.fail(f"Malformed UUID: {v}")


hachitool.set_output(uuid=UUIDGenerator().generate())
