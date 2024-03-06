from lxml import etree

def extract_abstract(xml_file):
    try:
        with open(xml_file, 'rb') as file:
            tree = etree.parse(file)
            # Definir el espacio de nombres utilizado en el documento XML
            namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}
            # Actualizar el XPath para usar el espacio de nombres y extraer el abstract
            abstract_texts = tree.xpath('//tei:abstract//tei:p/text()', namespaces=namespaces)
            return ' '.join(abstract_texts).strip()
    except Exception as e:
        print(f"Error al procesar el archivo {xml_file}: {e}")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        xml_file = sys.argv[1]
        abstract_text = extract_abstract(xml_file)
        if abstract_text:
            print(f"Abstract: {abstract_text}")
        else:
            print("No se pudo extraer el abstract.")
    else:
        print("Por favor, proporciona la ruta del archivo XML como argumento.")
