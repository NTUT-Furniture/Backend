import inspect
from typing import Type, Optional, get_origin, Union, get_args
from fastapi import HTTPException
from pydantic import BaseModel

def is_optional(field):
    return not (get_origin(field) is Union or type(None) in get_args(field))

def as_form(cls: Type[BaseModel]):
    async def as_form_func(**data):
        # Validate the form data using the Pydantic model
        try:
            instance = cls(**data)
        except ValueError as e:
            raise HTTPException(status_code=422, detail=str(e))
        
        return instance

    # Update the function signature
    sig = inspect.signature(as_form_func)
    
    # Update the parameters in the signature based on the model's annotations
    new_parameters = []
    for field_name, field_type in cls.__annotations__.items():
        # Check if the field is required
        is_required = is_optional(field_type)

        parameter = inspect.Parameter(
            name=field_name,
            kind=inspect.Parameter.POSITIONAL_OR_KEYWORD,
            default=inspect.Parameter.empty if is_required else None
        )
        new_parameters.append(parameter)
    
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig
    
    # Attach the as_form method to the Pydantic model
    setattr(cls, 'as_form', as_form_func)
    
    return cls