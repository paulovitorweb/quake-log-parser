from typing import Optional

from pydantic import BaseModel


def validate_response_body(data: dict | list, model: BaseModel) -> tuple[bool, Optional[Exception]]:
    try:
        model.model_validate(data)
        return True, None
    except ValueError as e:
        return False, e
