#!/usr/bin/env python3
""" Create function who serailize and deserialyse an alternative format to json"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save to a file.
    
    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The name of the file to save the XML data
    """
    root = ET.Element('data')
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        
        if isinstance(value, bool):
            child.text = str(value)
            child.set('type', 'bool')
        elif isinstance(value, int):
            child.text = str(value)
            child.set('type', 'int')
        elif isinstance(value, float):
            child.text = str(value)
            child.set('type', 'float')
        elif isinstance(value, (list, tuple)):
            child.set('type', 'list')
            for item in value:
                item_element = ET.SubElement(child, 'item')
                item_element.text = str(item)
        elif isinstance(value, dict):
            child.set('type', 'dict')
            for nested_key, nested_value in value.items():
                nested_element = ET.SubElement(child, nested_key)
                nested_element.text = str(nested_value)
        else:
            child.text = str(value)
            child.set('type', 'str')
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file back into a Python dictionary.
    
    Args:
        filename (str): The name of the file to read XML data from
        
    Returns:
        dict: The deserialized Python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    
    result_dict = {}
    
    for child in root:
        key = child.tag
        value_type = child.get('type', 'str')
        
        if value_type == 'bool':
            result_dict[key] = child.text == 'True'
        elif value_type == 'int':
            result_dict[key] = int(child.text)
        elif value_type == 'float':
            result_dict[key] = float(child.text)
        elif value_type == 'list':
            result_dict[key] = [item.text for item in child.findall('item')]
        elif value_type == 'dict':
            nested_dict = {}
            for nested_child in child:
                nested_dict[nested_child.tag] = nested_child.text
            result_dict[key] = nested_dict
        else:
            result_dict[key] = child.text if child.text is not None else ''
    
    return result_dict

