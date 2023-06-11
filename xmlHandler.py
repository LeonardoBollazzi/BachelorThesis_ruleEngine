import xml.etree.ElementTree as ET
from collections import defaultdict
def read_xml_files(file_paths):
    xml_data_list = []

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                xml_data = file.read()
                xml_data_list.append(xml_data)
        except FileNotFoundError:
            print(f"XML file not found: {file_path}")

    return xml_data_list

# Transform XML files to group them by same tags
def group_tags(xml_strings):
    grouped_tags = defaultdict(list)

    for xml_string in xml_strings:
        root = ET.fromstring(xml_string)
        added_tags = set()  # Track already added tags in the current XML string
        for element in root.iter():
            tag_name = element.tag
            text = element.text

            if text is not None and tag_name not in added_tags:
                grouped_tags[tag_name].append(text)
                added_tags.add(tag_name)  # Add the tag to the set of added tags

    result = []
    max_entries = max(len(entries) for entries in grouped_tags.values())

    for tag_name, entries in grouped_tags.items():
        xml_structure = f'<{tag_name}>'
        for i in range(max_entries):
            if i < len(entries):
                xml_structure += f'<value>{entries[i]}</value>'
        xml_structure += f'</{tag_name}>'
        result.append(xml_structure)

    return result

