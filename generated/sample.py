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

    start: Optional[Start] = field(
        default=None,
        metadata={
            "name": "START",
            "type": "Element",
        }
    )
    end: Optional[End] = field(
        default=None,
        metadata={
            "name": "END",
            "type": "Element",
        }
    )


@dataclass
class AssetGroups:
    class Meta:
        name = "ASSET_GROUPS"

    asset_group: Optional[AssetGroup] = field(
        default=None,
        metadata={
            "name": "ASSET_GROUP",
            "type": "Element",
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

    range: Optional[Range] = field(
        default=None,
        metadata={
            "name": "RANGE",
            "type": "Element",
        }
    )


@dataclass
class UserEnteredDomains:
    class Meta:
        name = "USER_ENTERED_DOMAINS"

    domain: Optional[Domain] = field(
        default=None,
        metadata={
            "name": "DOMAIN",
            "type": "Element",
        }
    )
    netblock: List[Netblock] = field(
        default_factory=list,
        metadata={
            "name": "NETBLOCK",
            "type": "Element",
        }
    )


@dataclass
class Header:
    class Meta:
        name = "HEADER"

    key: Optional[Key] = field(
        default=None,
        metadata={
            "name": "KEY",
            "type": "Element",
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
    ip: Optional[Ip] = field(
        default=None,
        metadata={
            "name": "IP",
            "type": "Element",
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
