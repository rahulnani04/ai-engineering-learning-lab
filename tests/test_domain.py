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
