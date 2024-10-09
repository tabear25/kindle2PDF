import fitz  
import pytesseract
from PIL import Image
import io
import os

print("必要なライブラリのインストールが完了しました")

# Tesseract-OCRの正しいパスを設定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# PDFファイルのパスを正しく設定
pdf_path = r"C:\kindle-screenshot\40字要約で仕事はどんどんうまくいく_20240708215221.pdf"

lang = 'jpn_vert', 'jpn'

# OCRしたいファイル名をファイルパスで入力
if not os.path.exists(pdf_path):
    print("指定されたファイルが見つかりません。パスを確認してください。")
else:
    doc = fitz.open(pdf_path)
    output_file = 'コンサル一年目に学ぶこと.txt'
    print(f"{output_file}というファイル名で文字認識した結果をテキストファイルとして出力します。")

    with open(output_file, 'w', encoding='utf-8') as f:
        for page_number in range(len(doc)):
            page = doc[page_number]
            page_text = []

            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]

                image = Image.open(io.BytesIO(image_bytes))
                text = pytesseract.image_to_string(image, lang='jpn')
                page_text.append(text)

            if not page_text:  # テキストが空の場合のチェック
                print(f"Page {page_number + 1}: No text found.")
            else:
                f.write(f'Page {page_number + 1}:\n{" ".join(page_text)}\n')
                if page_number == 0:
                    print(f'Preview of Page {page_number + 1}:')
                    print(" ".join(page_text))

    doc.close()
print("文字の書き出しが完了しました")
