from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class FactCheckInput(BaseModel):
    """Input schema for FactCheckTool."""

    claim: str = Field(
        ...,
        description="The claim that needs to be fact-checked."
    )


class FactCheckTool(BaseTool):
    name: str = "Fact Checker"

    description: str = (
        "Checks a claim and provides information that can help determine "
        "whether the claim is supported by reliable evidence."
    )

    args_schema: Type[BaseModel] = FactCheckInput

    def _run(self, claim: str) -> str:
        # Fact-checking implementation goes here
        return f"Fact-checking claim: {claim}"