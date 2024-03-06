import sys
import os

# Añade la carpeta /scripts al sys.path para permitir importaciones desde allí
script_dir = os.path.join(os.path.dirname(__file__), 'scripts')
sys.path.append(script_dir)

# Importa tus módulos de /scripts
from extract_abstracts import extract_abstract
from generate_wordcloud import generate_wordcloud
from extract_links import extract_links
from visualize_figures_count import visualize_figures_count

from grobid_client.grobid_client import GrobidClient

def process_xml_files(input_dir, output_dir):
    print("Iniciando el procesamiento de los archivos XML...")

    all_abstracts_file_path = os.path.join(output_dir, 'all_abstracts.txt')
    xml_files_for_figures = []

    with open(all_abstracts_file_path, 'w', encoding='utf-8') as all_abstracts_file:
        for filename in os.listdir(input_dir):
            if filename.endswith('.xml'):
                xml_file_path = os.path.join(input_dir, filename)
                xml_files_for_figures.append(xml_file_path)
                
                print(f"Procesando el archivo: {filename}")
                abstract_text = extract_abstract(xml_file_path)
                if abstract_text:
                    all_abstracts_file.write(abstract_text + "\n\n")
                
                links = extract_links(xml_file_path)
                links_file_path = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}_links.txt')
                with open(links_file_path, 'w', encoding='utf-8') as links_file:
                    for link in links:
                        links_file.write(link + "\n")

    generate_wordcloud(all_abstracts_file_path)
    figures_visualization_output_dir = os.path.join(output_dir, 'figures')
    visualize_figures_count(xml_files_for_figures, figures_visualization_output_dir)
    print("Procesamiento de archivos XML completado.")

if __name__ == "__main__":
    print("Iniciando el cliente GROBID...")
    client = GrobidClient(config_path="./config.json")
    client.process("processFulltextDocument", "./resources/test_pdf", output="./resources/test_out/", consolidate_citations=True, tei_coordinates=True, force=True)
    
    output_dir = "./processed_xmls"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    process_xml_files("./resources/test_out/", output_dir)

    # Listar todos los archivos generados al final del proceso
    print("\nArchivos generados en el directorio processed_xmls:")
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            print(os.path.join(root, file))


    # Al final del script, después de procesar los archivos XML y generar la nube de palabras

    # Ruta al archivo wordcloud.png en el directorio raíz del proyecto
    wordcloud_path = os.path.join(os.path.dirname(__file__), 'wordcloud.png')

    # Verificar si el archivo wordcloud.png ha sido generado
    if os.path.exists(wordcloud_path):
        print("\nEl archivo wordcloud.png ha sido generado exitosamente.")
    else:
        print("\nEl archivo wordcloud.png no se encuentra en el directorio esperado.")
