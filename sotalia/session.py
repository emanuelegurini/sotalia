import copy
from sotalia.configprovider import (SOTALIA_DEFAUT_SESSION_VARIABLES)
from sotalia import (__version__)

class Session:
    SESSION_VARIABLES = copy.copy(SOTALIA_DEFAUT_SESSION_VARIABLES)

    def __init__(
        self,
        session_vars=None,
        event_hooks=None,
        include_builtin_handlers=True,
        profile=None
    ):
        self.user_agent_name='sotalia'
        self.user_agent_version=__version__
        self._profile =None
        self._config =None
        self._credentials =None
        self._auth_token =None
        self._profile_map =None

        self._session_instance_vars = {}
        if profile is not None:
            self._session_instance_vars['profile'] = profile
        self._client_config = None
        self._last_client_region_used = None
