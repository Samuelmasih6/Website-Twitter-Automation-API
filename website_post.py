from pydantic import BaseModel
from typing import List, Optional

class WebsitePost(BaseModel):
    post_id: str
    title: str
    body: str
    author: Optional[str] = None
    tags: List[str] = []
    url: Optional[str] = None
