from lxml import etree
import matplotlib.pyplot as plt
import os

def count_figures(xml_file):
    with open(xml_file, 'rb') as file:
        tree = etree.parse(file)
        # Definir el espacio de nombres utilizado en el documento XML
        namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}
        # Contar las figuras usando XPath y el espacio de nombres
        figures = tree.xpath('//tei:figure', namespaces=namespaces)
        return len(figures)

def visualize_figures_count(xml_files, output_dir):
    # Asegúrate de que el directorio de salida existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Contar figuras en cada archivo XML
    figures_counts = [count_figures(file) for file in xml_files]
    articles = [os.path.basename(file).replace('.xml', '') for file in xml_files]
    
    # Generar y guardar la gráfica
    plt.figure(figsize=(10, 5))  # Ajusta el tamaño según necesites
    plt.bar(articles, figures_counts, color='skyblue')
    plt.xlabel('Article')
    plt.ylabel('Number of Figures')
    plt.title('Number of Figures in Each Article')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()  # Ajusta automáticamente los parámetros de la subtrama para dar espacio a las etiquetas
    plt.savefig(os.path.join(output_dir, 'figures_count.png'))
    plt.close()  # Cierra la figura para liberar memoria


