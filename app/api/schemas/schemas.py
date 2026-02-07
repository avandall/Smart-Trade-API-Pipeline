from pydantic import BaseModel, Field
from typing import Any, Dict, Optional


class Transaction(BaseModel):
    timestamp: str = Field(..., description="Thời gian giao dịch")
    category: str = Field(..., description="Danh mục giao dịch")
    amount: float = Field(..., description="Số tiền giao dịch")
    currency: str = Field(..., description="Loại tiền tệ")
    flow_type: str = Field(..., description="Loại dòng tiền (inflow hoặc outflow)")
    description: Optional[str] = Field(None, description="Mô tả giao dịch")
    metadata : Optional[Dict[str, Any]] = Field(None, description="Thông tin bổ sung customize")

class FinancialDashboard(BaseModel):
    total_inflow: float = Field(..., description="Tổng số tiền vào")
    total_outflow: float = Field(..., description="Tổng số tiền ra")
    net_flow: float = Field(..., description="Dòng tiền ròng (total_inflow - total_outflow)")
    top_categories: Dict[str, float] = Field(..., description="Danh mục hàng đầu theo số tiền")
    efficiency_ratio: float = Field(..., description="Tỷ lệ hiệu quả (total_outflow / total_inflow)")

class DataProcessingConfig(BaseModel):
    normalize: bool = Field(False, description="Có chuẩn hóa dữ liệu không")
    target_currency: Optional[str] = Field(None, description="Loại tiền tệ mục tiêu để chuyển đổi")
    exchange_rates: Optional[Dict[str, float]] = Field(None, description="Tỷ giá hối đoái để sử dụng trong chuyển đổi")
    fill_missing: Optional[float] = Field(None, description="Giá trị để điền vào các ô trống, nếu có")
    date_format: Optional[str] = Field(None, description="Định dạng ngày tháng nếu cần chuyển đổi")