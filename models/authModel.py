from typing import Optional
from pydantic import BaseModel, Field
import secrets

class Auth(BaseModel):
    name: Optional[str] = None
    email: str
    password: str
    password_reset_token: str = Field(default_factory=lambda: secrets.token_hex(16))
    role: str = Field(default="USER")
