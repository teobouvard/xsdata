from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


@dataclass
class AssetGroupTitle:
    class Meta:
        name = "ASSET_GROUP_TITLE"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class Discovery:
    class Meta:
        name = "DISCOVERY"

    method: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class Domain:
    class Meta:
        name = "DOMAIN"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class End:
    class Meta:
        name = "END"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class Error:
    class Meta:
        name = "ERROR"

    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class Key:
    class Meta:
        name = "KEY"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


class LinkType(Enum):
    CHECK = "check"
    CASH = "cash"


@dataclass
class OptionProfileTitle:
    class Meta:
        name = "OPTION_PROFILE_TITLE"

    option_profile_default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class Port:
    class Meta:
        name = "PORT"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class Start:
    class Meta:
        name = "START"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class AssetGroup:
    class Meta:
        name = "ASSET_GROUP"

    asset_group_title: Optional[AssetGroupTitle] = field(
        default=None,
        metadata={
            "name": "ASSET_GROUP_TITLE",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Link:
    class Meta:
        name = "LINK"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: LinkType = field(
        default=LinkType.CASH,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OptionProfile:
    class Meta:
        name = "OPTION_PROFILE"

    option_profile_title: Optional[OptionProfileTitle] = field(
        default=None,
        metadata={
            "name": "OPTION_PROFILE_TITLE",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Range:
    class Meta:
        name = "RANGE"

    start: List[Start] = field(
        default_factory=list,
        metadata={
            "name": "START",
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    end: List[End] = field(
        default_factory=list,
        metadata={
            "name": "END",
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )


@dataclass
class AssetGroups:
    class Meta:
        name = "ASSET_GROUPS"

    asset_group: List[AssetGroup] = field(
        default_factory=list,
        metadata={
            "name": "ASSET_GROUP",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Ip:
    class Meta:
        name = "IP"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    network_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    network: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    account: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    netbios: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    os: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    port: List[Port] = field(
        default_factory=list,
        metadata={
            "name": "PORT",
            "type": "Element",
            "sequential": True,
        }
    )
    discovery: List[Discovery] = field(
        default_factory=list,
        metadata={
            "name": "DISCOVERY",
            "type": "Element",
            "sequential": True,
        }
    )
    link: List[Link] = field(
        default_factory=list,
        metadata={
            "name": "LINK",
            "type": "Element",
            "sequential": True,
        }
    )


@dataclass
class Netblock:
    class Meta:
        name = "NETBLOCK"

    range: List[Range] = field(
        default_factory=list,
        metadata={
            "name": "RANGE",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class UserEnteredDomains:
    class Meta:
        name = "USER_ENTERED_DOMAINS"

    domain: List[Domain] = field(
        default_factory=list,
        metadata={
            "name": "DOMAIN",
            "type": "Element",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    netblock: List[Netblock] = field(
        default_factory=list,
        metadata={
            "name": "NETBLOCK",
            "type": "Element",
            "sequential": True,
        }
    )


@dataclass
class Header:
    class Meta:
        name = "HEADER"

    key: List[Key] = field(
        default_factory=list,
        metadata={
            "name": "KEY",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    asset_groups: Optional[AssetGroups] = field(
        default=None,
        metadata={
            "name": "ASSET_GROUPS",
            "type": "Element",
        }
    )
    user_entered_domains: Optional[UserEnteredDomains] = field(
        default=None,
        metadata={
            "name": "USER_ENTERED_DOMAINS",
            "type": "Element",
        }
    )
    option_profile: Optional[OptionProfile] = field(
        default=None,
        metadata={
            "name": "OPTION_PROFILE",
            "type": "Element",
        }
    )


@dataclass
class Map:
    class Meta:
        name = "MAP"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    header: Optional[Header] = field(
        default=None,
        metadata={
            "name": "HEADER",
            "type": "Element",
        }
    )
    ip: List[Ip] = field(
        default_factory=list,
        metadata={
            "name": "IP",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    error: Optional[Error] = field(
        default=None,
        metadata={
            "name": "ERROR",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class MapRequest:
    class Meta:
        name = "MAP_REQUEST"

    map: List[Map] = field(
        default_factory=list,
        metadata={
            "name": "MAP",
            "type": "Element",
        }
    )
    error: List[Error] = field(
        default_factory=list,
        metadata={
            "name": "ERROR",
            "type": "Element",
        }
    )
