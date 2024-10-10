# coding: utf-8

"""
    SEC form 13F API

    API for SEC form filings such as 13F.

    The version of the OpenAPI document: 1.0.0
    Contact: forms13f@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiV1FormEntry(BaseModel):
    """
    ApiV1FormEntry
    """ # noqa: E501
    accession_number: Optional[StrictStr] = Field(default=None, description="The accession number of the form entry.")
    cik: Optional[StrictStr] = Field(default=None, description="The Central Index Key (CIK) of the form entry.")
    name_of_issuer: Optional[StrictStr] = Field(default=None, description="The name of the issuer.")
    title_of_class: Optional[StrictStr] = Field(default=None, description="The title of the class of securities.")
    cusip: Optional[StrictStr] = Field(default=None, description="The CUSIP number of the securities.")
    value: Optional[StrictInt] = Field(default=None, description="The value of the securities.")
    ssh_prnamt: Optional[StrictInt] = Field(default=None, description="The number of shares or principal amount.")
    ssh_prnamt_type: Optional[StrictStr] = Field(default=None, description="The type of shares or principal amount.")
    investment_discretion: Optional[StrictStr] = Field(default=None, description="The investment discretion.")
    voting_authority_sole: Optional[StrictInt] = Field(default=None, description="The sole voting authority.")
    voting_authority_shared: Optional[StrictInt] = Field(default=None, description="The shared voting authority.")
    voting_authority_none: Optional[StrictInt] = Field(default=None, description="The no voting authority.")
    __properties: ClassVar[List[str]] = ["accession_number", "cik", "name_of_issuer", "title_of_class", "cusip", "value", "ssh_prnamt", "ssh_prnamt_type", "investment_discretion", "voting_authority_sole", "voting_authority_shared", "voting_authority_none"]

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
        """Create an instance of ApiV1FormEntry from a JSON string"""
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
        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if ssh_prnamt (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_prnamt is None and "ssh_prnamt" in self.model_fields_set:
            _dict['ssh_prnamt'] = None

        # set to None if ssh_prnamt_type (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_prnamt_type is None and "ssh_prnamt_type" in self.model_fields_set:
            _dict['ssh_prnamt_type'] = None

        # set to None if investment_discretion (nullable) is None
        # and model_fields_set contains the field
        if self.investment_discretion is None and "investment_discretion" in self.model_fields_set:
            _dict['investment_discretion'] = None

        # set to None if voting_authority_sole (nullable) is None
        # and model_fields_set contains the field
        if self.voting_authority_sole is None and "voting_authority_sole" in self.model_fields_set:
            _dict['voting_authority_sole'] = None

        # set to None if voting_authority_shared (nullable) is None
        # and model_fields_set contains the field
        if self.voting_authority_shared is None and "voting_authority_shared" in self.model_fields_set:
            _dict['voting_authority_shared'] = None

        # set to None if voting_authority_none (nullable) is None
        # and model_fields_set contains the field
        if self.voting_authority_none is None and "voting_authority_none" in self.model_fields_set:
            _dict['voting_authority_none'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiV1FormEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accession_number": obj.get("accession_number"),
            "cik": obj.get("cik"),
            "name_of_issuer": obj.get("name_of_issuer"),
            "title_of_class": obj.get("title_of_class"),
            "cusip": obj.get("cusip"),
            "value": obj.get("value"),
            "ssh_prnamt": obj.get("ssh_prnamt"),
            "ssh_prnamt_type": obj.get("ssh_prnamt_type"),
            "investment_discretion": obj.get("investment_discretion"),
            "voting_authority_sole": obj.get("voting_authority_sole"),
            "voting_authority_shared": obj.get("voting_authority_shared"),
            "voting_authority_none": obj.get("voting_authority_none")
        })
        return _obj

