"""Pure, testable business logic using entirely synthetic inquiry data."""
from enum import Enum
from pydantic import BaseModel, Field

class Category(str, Enum):
    POLICY = "policy"
    TRANSACTION = "transaction"
    GENERAL = "general"

class Inquiry(BaseModel):
    inquiry_id: str = Field(min_length=3, max_length=80)
    question: str = Field(min_length=3, max_length=2000)

class InquiryResult(BaseModel):
    inquiry_id: str
    category: Category
    message: str
    source: str = "synthetic-training-data"

class InquiryService:
    """Deliberately deterministic rule-based baseline, not an LLM or banking tool."""
    def classify(self, question: str) -> Category:
        q = question.lower()
        if "policy" in q or "procedure" in q:
            return Category.POLICY
        if "transaction" in q or "payment" in q:
            return Category.TRANSACTION
        return Category.GENERAL

    def process(self, inquiry: Inquiry) -> InquiryResult:
        category = self.classify(inquiry.question)
        return InquiryResult(
            inquiry_id=inquiry.inquiry_id,
            category=category,
            message=f"Training result: route to the {category.value} workflow; human review required.",
        )
