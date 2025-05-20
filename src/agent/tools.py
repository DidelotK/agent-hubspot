from typing import List

def get_hubspot_contacts() -> List[str]:
    """Get a HubSpot contacts."""
    return [{"id": "123", "full_name": "John Doe"}]

def get_hubspot_transactions() -> List[str]:
    """Get a HubSpot transactions."""
    return [{"id": "123", "name": "Total Saft : Infra deployment"}]

def get_hubspot_company_engagements() -> List[str]:
    """Get a HubSpot company engagements."""
    return [{"id": "123", "type": "call", "date": "2025-01-01"}]

def get_hubspot_users() -> List[str]:
    """Get a HubSpot users."""
    return [{"id": "123", "name": "John Doe", "email": "john.doe@example.com"}]
