from langchain_core.output_parsers import PydanticOutputParser
from schemas.study_plan_schema import StudyPlan

def get_study_plan_parser():
    return PydanticOutputParser(pydantic_object=StudyPlan)