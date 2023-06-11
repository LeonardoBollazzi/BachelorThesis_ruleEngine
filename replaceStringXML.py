from lxml import etree

def replaceStringValues(xml_data, stringValues):

    # Parse XML using lxml
    root = etree.fromstring(xml_data)

    # Function to replace values
    def replace_values(brief, element):
        parent_tag = element.getparent().tag
        tag = element.tag
        text = element.text

        brief = brief.replace(text, f"<{parent_tag}><{tag}>")

        return brief

    modified_paragraph = stringValues

    # Iterate over the elements in the XML
    for element in root.iter():
        if element.text is not None and element.text in modified_paragraph:
            modified_paragraph = replace_values(modified_paragraph, element)

    # returns modified paragraphs
    return modified_paragraph