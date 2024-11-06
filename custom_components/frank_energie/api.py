from python_frank_energie import FrankEnergie

import logging
from aiohttp.client import ClientSession
from .const import DATA_URL as CONFIG_DATA_URL

LOGGER = logging.getLogger(__name__)

class FrankEnergieApi(FrankEnergie):
    def __init__(
            self,
            clientsession: ClientSession = None,
            auth_token: str | None = None,
            refresh_token: str | None = None,
    ):
        FrankEnergie.DATA_URL = CONFIG_DATA_URL
        super().__init__(clientsession, auth_token, refresh_token)
        LOGGER.debug(f"Using {FrankEnergie.DATA_URL} for queries")
