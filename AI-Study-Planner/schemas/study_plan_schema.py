from pydantic import BaseModel, Field
from typing import List

class DayPlan(BaseModel):
    day: int = Field(..., description="Day number starting from 1")
    difficulty: str = Field(..., description="Beginner, Intermediate, or Advanced")
    topics: List[str] = Field(..., description="List of topics for the day")

class StudyPlan(BaseModel):
    goal: str = Field(..., description="Learning goal")
    duration: str = Field(..., description="Total duration (e.g., '7 days')")
    plan: List[DayPlan] = Field(..., description="Day-wise study plan")
