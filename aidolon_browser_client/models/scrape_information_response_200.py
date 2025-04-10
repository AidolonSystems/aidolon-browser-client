from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.scrape_information_response_200_data import ScrapeInformationResponse200Data





T = TypeVar("T", bound="ScrapeInformationResponse200")



@_attrs_define
class ScrapeInformationResponse200:
    """ 
        Attributes:
            success (Union[Unset, bool]):  Example: True.
            action (Union[Unset, str]):  Example: scrape_information.
            description (Union[Unset, str]): The description that was provided
            data (Union[Unset, ScrapeInformationResponse200Data]): The scraped information (structure varies based on
                content)
     """

    success: Union[Unset, bool] = UNSET
    action: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    data: Union[Unset, 'ScrapeInformationResponse200Data'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.scrape_information_response_200_data import ScrapeInformationResponse200Data
        success = self.success

        action = self.action

        description = self.description

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if success is not UNSET:
            field_dict["success"] = success
        if action is not UNSET:
            field_dict["action"] = action
        if description is not UNSET:
            field_dict["description"] = description
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scrape_information_response_200_data import ScrapeInformationResponse200Data
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        action = d.pop("action", UNSET)

        description = d.pop("description", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ScrapeInformationResponse200Data]
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = ScrapeInformationResponse200Data.from_dict(_data)




        scrape_information_response_200 = cls(
            success=success,
            action=action,
            description=description,
            data=data,
        )


        scrape_information_response_200.additional_properties = d
        return scrape_information_response_200

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
