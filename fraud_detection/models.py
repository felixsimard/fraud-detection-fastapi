from pydantic import BaseModel


class FraudData(BaseModel):
    name_email_similarity: int
    current_address_months_count: int
    credit_risk_score: int
    housing_status: int
    velocity_6h: int
    bank_branch_count_8w: int
    employment_status: int
    prev_address_months_count: int
