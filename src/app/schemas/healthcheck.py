from pydantic import BaseModel


class HealthCheckOut(BaseModel):
    status: str
