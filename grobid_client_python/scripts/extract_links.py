from lxml import etree

def extract_links(xml_file):
    links = []
    with open(xml_file, 'rb') as file:
        tree = etree.parse(file)
        # Ignorando los espacios de nombres en la consulta XPath
        links_elements = tree.xpath('//*[local-name()="ptr"]/@target')
        links = [link for link in links_elements]
    return links


