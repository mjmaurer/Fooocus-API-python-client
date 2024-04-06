# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from fooocusapi_client.models.cn_img import CnImg
from fooocusapi_client.models.cn_stop import CnStop
from fooocusapi_client.models.cn_weight import CnWeight
from fooocusapi_client.models.control_net_type import ControlNetType
from typing import Optional, Set
from typing_extensions import Self

class ImagePrompt(BaseModel):
    """
    ImagePrompt
    """ # noqa: E501
    cn_img: Optional[CnImg] = None
    cn_stop: Optional[CnStop] = None
    cn_weight: Optional[CnWeight] = None
    cn_type: Optional[ControlNetType] = None
    __properties: ClassVar[List[str]] = ["cn_img", "cn_stop", "cn_weight", "cn_type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ImagePrompt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cn_img
        if self.cn_img:
            _dict['cn_img'] = self.cn_img.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cn_stop
        if self.cn_stop:
            _dict['cn_stop'] = self.cn_stop.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cn_weight
        if self.cn_weight:
            _dict['cn_weight'] = self.cn_weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImagePrompt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cn_img": CnImg.from_dict(obj["cn_img"]) if obj.get("cn_img") is not None else None,
            "cn_stop": CnStop.from_dict(obj["cn_stop"]) if obj.get("cn_stop") is not None else None,
            "cn_weight": CnWeight.from_dict(obj["cn_weight"]) if obj.get("cn_weight") is not None else None,
            "cn_type": obj.get("cn_type")
        })
        return _obj

