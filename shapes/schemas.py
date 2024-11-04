from ninja import Schema
from typing import Optional
from datetime import datetime
from enum import Enum


class ShapeType(str, Enum):
    RECTANGLE = "rectangle"
    CIRCLE = "circle"
    LINE = "line"
    TEXT = "text"


class ShapeProperties(Schema):
    width: Optional[float] = None
    height: Optional[float] = None
    radius: Optional[float] = None
    endX: Optional[float] = None
    endY: Optional[float] = None
    text: Optional[str] = None
    fontSize: Optional[float] = None
    points: Optional[list[float]] = None


class ShapeStyle(Schema):
    fill: Optional[str] = None
    stroke: Optional[str] = None
    padding: Optional[float] = None


class ShapeCreate(Schema):
    shape_type: ShapeType
    x: float
    y: float
    properties: ShapeProperties
    style: ShapeStyle
    order: Optional[int] = 0


class ShapeUpdate(Schema):
    id: int
    shape_type: Optional[ShapeType] = None
    x: Optional[float] = None
    y: Optional[float] = None
    properties: Optional[ShapeProperties] = None
    style: Optional[ShapeStyle] = None
    order: Optional[int] = None


class ShapeOut(Schema):
    id: int
    shape_type: ShapeType
    x: float
    y: float
    properties: ShapeProperties
    style: ShapeStyle
    created_at: datetime
    updated_at: datetime
    created_by_id: int
    order: int
    project_id: int
