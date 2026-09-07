from waste_collection_schedule import Collection, Icons
from waste_collection_schedule.service.OpenCities import (
    OpenCitiesClient,
    OpenCitiesConfig,
)

TITLE = "Palmerston North City Council"
DESCRIPTION = (
    "Source for Palmerston North City Council rubbish and recycling collections."
)
URL = "https://www.pncc.govt.nz/Services/Rubbish-and-recycling/Palmy-Collections/Rubbish-and-recycling-days"
COUNTRY = "nz"

HOW_TO_GET_ARGUMENTS_DESCRIPTION = {
    "en": (
        "Visit the Palmerston North City Council rubbish and recycling days page, "
        "search for your property, and enter the full address shown in the search results."
    )
}

TEST_CASES = {
    "Hancock Community House": {"address": "77 KING STREET PALMERSTON NORTH"},
}

ICON_MAP = {
    "Rubbish": Icons.GENERAL_WASTE,
    "Wheelie Bin": Icons.RECYCLING,
    "Glass Crate": Icons.GLASS,
}

_CONFIG = OpenCitiesConfig(
    domain="https://www.pncc.govt.nz",
    require_date_precise=True,
    icon_keywords=ICON_MAP,
    strict_address_matching=True,
    strict_single_result=True,
)


class Source:
    def __init__(self, address: str):
        self._address = " ".join(address.split())
        self._client = OpenCitiesClient(_CONFIG)

    def fetch(self) -> list[Collection]:
        return self._client.fetch(address=self._address)
