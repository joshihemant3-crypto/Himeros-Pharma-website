import zipfile
import xml.etree.ElementTree as ET

def extract_text(docx_file):
    try:
        with zipfile.ZipFile(docx_file) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.XML(xml_content)
            
            # The namespace for w:t (text elements)
            WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
            PARA = WORD_NAMESPACE + 'p'
            TEXT = WORD_NAMESPACE + 't'
            
            paragraphs = []
            for paragraph in tree.iter(PARA):
                texts = [node.text for node in paragraph.iter(TEXT) if node.text]
                if texts:
                    paragraphs.append(''.join(texts))
                    
            print('\n'.join(paragraphs))
    except Exception as e:
        print(f"Error reading docx: {e}")

extract_text('E:/himros web/docs/Our Segments (1).docx')
