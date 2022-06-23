import sys
from typing import List, Union

from lxml.etree import DTD

from xsdata.codegen.models import Class, Attr, AttrType, Restrictions
from xsdata.models.enums import Tag, DataType

class ElementType:
    UNDEFINED = "undefined"
    EMPTY = "empty"
    ANY = "any"
    MIXED = "mixed"
    ELEMENT = "element"


class AttributeDefault:
    REQUIRED = "required"
    IMPLIED = "implied"
    FIXED = "fixed"
    NONE = "none"

class AttributeType:
    CDATA = "cdata"
    ID = "id"
    IDREF = "idref"
    IDREFS = "idrefs"
    ENTITY = "entity"
    ENTITIES = "entities"
    NMTOKEN = "nmtoken"
    NMTOKENS = "nmtokens"
    ENUMERATION = "enumeration"
    NOTATION = "notation"


class ContentType:
    PCDATA = "pcdata"
    ELEMENT = "element"
    SEQ = "seq"
    OR = "or"


class Occur:
    ONCE = "once"
    OPT = "opt"
    MULT = "mult"
    PLUS = "plus"




class DtdMapper:

    @classmethod
    def map(cls, dtd: DTD, location: str) -> List[Class]:
        for element in dtd.iterelements():
            yield cls.build_class(element, location)

    @classmethod
    def build_class(cls, element, location: str) -> Class:
        target = Class(qname=element.name, tag=Tag.ELEMENT, location=location)

        cls.build_attributes(target, element)
        cls.build_elements(target, element)

        return target

    @classmethod
    def append_attr(cls, target: Class, attr: Attr):
        attr.index = len(target.attrs)
        target.attrs.append(attr)

    @classmethod
    def build_attributes(cls, target, element):
        for attribute in element.iterattributes():
            cls.build_attribute(target, attribute)

    @classmethod
    def build_attribute(cls, target, attribute) -> Attr:

        if attribute.type == AttributeType.ENUMERATION:
            attr_type = AttrType(qname=attribute.name, forward=True)
            cls.build_enumeration(target, attribute.name, attribute.values())
        else:
            data_type = DataType.from_type(attribute.type.lower())
            attr_type = AttrType(qname=str(data_type), native=True)

        attr = Attr(name=attribute.name, tag=Tag.ATTRIBUTE, types=[attr_type])
        attr.restrictions.max_occurs = 1

        if attribute.default == AttributeDefault.REQUIRED:
            attr.restrictions.min_occurs = 1
        elif attribute.default == AttributeDefault.IMPLIED:
            attr.restrictions.min_occurs = 0
        elif attribute.default == AttributeDefault.FIXED:
            attr.fixed = True
            attr.restrictions.min_occurs = 1
            attr.default = attribute.default_value
        elif attribute.default:
            attr.restrictions.min_occurs = 1
            attr.default = attribute.default_value
        else:
            attr.restrictions.min_occurs = 0

        attr.index = len(target.attrs)
        target.attrs.append(attr)

    @classmethod
    def build_elements(cls, target, element):

        # "undefined", "empty", "any", "mixed", or "element";

        if element.type == ElementType.ELEMENT:
            cls.build_content(target, element.content)

        elif element.type == ElementType.MIXED:
            target.mixed = True
        elif element.type == ElementType.ANY:
            pass
        else: #element.type == ElementType.EMPTY:
            pass


    @classmethod
    def build_content(cls, target, content, **kwargs):
        content_type = content.type
        if content_type == ContentType.ELEMENT:
            restrictions = cls.build_restrictions(content.occur, **kwargs)
            cls.build_element(target, content.name, restrictions)
        elif content_type == ContentType.SEQ:
            cls.build_content_tree(target, content, sequential=True)
        elif content_type == ContentType.OR:
            cls.build_content_tree(target, content, choice=str(id(content)))
        else:
            # ContentType.PCDATA
            foo = 5


    @classmethod
    def build_content_tree(cls, target: Class, content, **kwargs):
        if content.left:
            cls.build_content(target, content.left, **kwargs)

        if content.right:
            cls.build_content(target, content.right, **kwargs)

    @classmethod
    def build_restrictions(cls, occur: str, **kwargs):
        restrictions = Restrictions(**kwargs)
        if occur == Occur.ONCE:
            restrictions.min_occurs = 1
            restrictions.max_occurs = 1
        elif occur == Occur.OPT:
            restrictions.min_occurs = 0
            restrictions.max_occurs = 1
        elif occur == Occur.MULT:
            restrictions.min_occurs = 0
            restrictions.max_occurs = sys.maxsize
        elif occur == Occur.PLUS:
            restrictions.min_occurs = 1
            restrictions.max_occurs = sys.maxsize

        return restrictions

    @classmethod
    def build_element(cls, target, name: str, restrictions: Restrictions):
        types = AttrType(qname=name, native=False)
        attr = Attr(name=name, tag=Tag.ELEMENT, types=[types], restrictions=restrictions)
        attr.index = len(target.attrs)
        target.attrs.append(attr)

    @classmethod
    def build_enumeration(cls, target: Class, name: str, values: list[str]):

        inner = Class(qname=name, tag=Tag.SIMPLE_TYPE, location=target.location)
        attr_type = AttrType(qname=str(DataType.STRING), native=True)

        for value in values:
            inner.attrs.append(Attr(
                fixed=True,
                default=value,
                name=value,
                tag=Tag.ENUMERATION,
                types=[attr_type.clone()]
            ))

        target.inner.append(inner)
