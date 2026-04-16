"""
Simulated CRM/ERP tool definitions for OpenAI function-calling.
"""
from typing import Optional

CUSTOMERS = [
    {"id": "C001", "name": "Acme Corp", "revenue": 450000, "industry": "Manufacturing"},
    {"id": "C002", "name": "TechStart Inc", "revenue": 320000, "industry": "Technology"},
    {"id": "C003", "name": "Global Retail", "revenue": 580000, "industry": "Retail"},
    {"id": "C004", "name": "HealthPlus", "revenue": 210000, "industry": "Healthcare"},
    {"id": "C005", "name": "EduLearn", "revenue": 150000, "industry": "Education"},
]

INVENTORY = [
    {"sku": "P001", "product": "Widget A", "stock": 1200, "warehouse": "East"},
    {"sku": "P002", "product": "Gadget B", "stock": 340, "warehouse": "West"},
    {"sku": "P003", "product": "Device C", "stock": 890, "warehouse": "Central"},
]


def query_crm_revenue(quarter: Optional[str] = None, top_n: int = 5) -> dict:
    sorted_customers = sorted(CUSTOMERS, key=lambda x: x["revenue"], reverse=True)
    return {"query": f"Top {top_n} by revenue", "quarter": quarter or "All", "results": sorted_customers[:top_n]}


def query_erp_inventory(warehouse: Optional[str] = None) -> dict:
    results = INVENTORY
    if warehouse:
        results = [i for i in INVENTORY if i["warehouse"].lower() == warehouse.lower()]
    return {"inventory": results, "warehouse_filter": warehouse or "All"}


def get_customer_profile(customer_id: str) -> dict:
    for c in CUSTOMERS:
        if c["id"] == customer_id:
            return {"customer": c, "status": "found"}
    return {"customer": None, "status": "not_found"}


def get_crm_tools() -> list:
    return [
        {
            "name": "query_crm_revenue",
            "description": "Query CRM to get top customers sorted by revenue for a given quarter",
            "parameters": {
                "type": "object",
                "properties": {
                    "quarter": {"type": "string", "description": "Quarter e.g. Q1 2024"},
                    "top_n": {"type": "integer", "description": "Number of top customers", "default": 5}
                }
            },
            "function": query_crm_revenue
        },
        {
            "name": "query_erp_inventory",
            "description": "Query ERP system for current inventory levels by warehouse",
            "parameters": {
                "type": "object",
                "properties": {
                    "warehouse": {"type": "string", "description": "Warehouse name"}
                }
            },
            "function": query_erp_inventory
        },
        {
            "name": "get_customer_profile",
            "description": "Retrieve a specific customer profile by ID",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {"type": "string", "description": "Customer ID"}
                },
                "required": ["customer_id"]
            },
            "function": get_customer_profile
        }
    ]
