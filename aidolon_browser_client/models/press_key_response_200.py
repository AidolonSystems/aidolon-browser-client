from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PressKeyResponse200")



@_attrs_define
class PressKeyResponse200:
    """ 
        Attributes:
            success (Union[Unset, bool]):  Example: True.
            action (Union[Unset, str]):  Example: press.
            selector (Union[Unset, str]): CSS selector for the element
            key (Union[Unset, str]): Key that was pressed
     """

    success: Union[Unset, bool] = UNSET
    action: Union[Unset, str] = UNSET
    selector: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        success = self.success

        action = self.action

        selector = self.selector

        key = self.key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if success is not UNSET:
            field_dict["success"] = success
        if action is not UNSET:
            field_dict["action"] = action
        if selector is not UNSET:
            field_dict["selector"] = selector
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        action = d.pop("action", UNSET)

        selector = d.pop("selector", UNSET)

        key = d.pop("key", UNSET)

        press_key_response_200 = cls(
            success=success,
            action=action,
            selector=selector,
            key=key,
        )


        press_key_response_200.additional_properties = d
        return press_key_response_200

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
