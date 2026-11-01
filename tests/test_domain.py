import pytest
from pydantic import ValidationError
from banking_lab.domain import Category, Inquiry, InquiryService

def test_policy_routing():
    result = InquiryService().process(Inquiry(inquiry_id="SYN-01", question="Show policy information"))
    assert result.category == Category.POLICY
    assert result.source == "synthetic-training-data"

def test_empty_question_rejected():
    with pytest.raises(ValidationError):
        Inquiry(inquiry_id="SYN-01", question="")

def test_transaction_routing():
    assert InquiryService().classify("Review a transaction alert") == Category.TRANSACTION

def test_whitespace_only_question_rejected():
    with pytest.raises(ValidationError):
        Inquiry(
            inquiry_id="SYN-101",
            question="   "
        )


def test_question_is_trimmed():
    inquiry = Inquiry(
        inquiry_id="SYN-102",
        question="  Review a payment  "
    )

    assert inquiry.question == "Review a payment"


def test_short_question_after_trim_rejected():
    with pytest.raises(ValidationError):
        Inquiry(
            inquiry_id="SYN-103",
            question="  Hi  "
        )
