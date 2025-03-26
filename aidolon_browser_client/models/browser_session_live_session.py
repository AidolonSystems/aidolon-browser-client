from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.browser_session_live_session_viewport import BrowserSessionLiveSessionViewport





T = TypeVar("T", bound="BrowserSessionLiveSession")



@_attrs_define
class BrowserSessionLiveSession:
    """ Information about the live browser session

        Attributes:
            url (Union[Unset, str]): Current URL of the browser
            title (Union[Unset, str]): Current page title
            is_loading (Union[Unset, bool]): Whether the page is currently loading
            viewport (Union[Unset, BrowserSessionLiveSessionViewport]):
     """

    url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    is_loading: Union[Unset, bool] = UNSET
    viewport: Union[Unset, 'BrowserSessionLiveSessionViewport'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.browser_session_live_session_viewport import BrowserSessionLiveSessionViewport
        url = self.url

        title = self.title

        is_loading = self.is_loading

        viewport: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.viewport, Unset):
            viewport = self.viewport.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if is_loading is not UNSET:
            field_dict["is_loading"] = is_loading
        if viewport is not UNSET:
            field_dict["viewport"] = viewport

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.browser_session_live_session_viewport import BrowserSessionLiveSessionViewport
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        title = d.pop("title", UNSET)

        is_loading = d.pop("is_loading", UNSET)

        _viewport = d.pop("viewport", UNSET)
        viewport: Union[Unset, BrowserSessionLiveSessionViewport]
        if isinstance(_viewport,  Unset):
            viewport = UNSET
        else:
            viewport = BrowserSessionLiveSessionViewport.from_dict(_viewport)




        browser_session_live_session = cls(
            url=url,
            title=title,
            is_loading=is_loading,
            viewport=viewport,
        )


        browser_session_live_session.additional_properties = d
        return browser_session_live_session

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
