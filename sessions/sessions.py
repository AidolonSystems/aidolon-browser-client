from typing import Optional, Union

from aidolon_browser_client.client import AuthenticatedClient, Client
from aidolon_browser_client.api.session_management.list_browser_sessions import sync as list_sync
from aidolon_browser_client.api.session_management.close_all_browser_sessions import sync as close_all_sync
from aidolon_browser_client.models.error import Error
from aidolon_browser_client.models.list_browser_sessions_response_200 import ListBrowserSessionsResponse200
from aidolon_browser_client.models.close_all_browser_sessions_response_200 import CloseAllBrowserSessionsResponse200
from aidolon_browser_client.models.list_browser_sessions_status import ListBrowserSessionsStatus
from aidolon_browser_client.types import UNSET, Unset


def list_all_sessions(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, ListBrowserSessionsStatus] = UNSET,
) -> Optional[Union[Error, ListBrowserSessionsResponse200]]:
    """List all browser sessions

    Gets all browser sessions for the authenticated user with optional status filtering

    Args:
        client: The client instance to use for the request
        status: Optional filter for session status

    Returns:
        The response model containing session information or an error
    """
    return list_sync(client=client, status=status)


def close_all_sessions(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CloseAllBrowserSessionsResponse200, Error]]:
    """Close all browser sessions

    Closes all active browser sessions for the authenticated user

    Args:
        client: The client instance to use for the request

    Returns:
        The response model confirming sessions were closed or an error
    """
    return close_all_sync(client=client)
