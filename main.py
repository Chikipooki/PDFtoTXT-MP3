from gtts import gTTS
import pdfplumber
from art import tprint 
from pathlib import Path

def PDFtoTextandMp3(file_path = 'test.pdf', language = 'en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f' - Original file: {Path(file_path).name}')
        print(' - Work in progress...')

        with pdfplumber.PDF(open(file = file_path, mode = 'rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        
        with open('Text.txt', 'w') as file:
            file.write(text)
        
        my_audio = gTTS(text = text, lang = language, slow = False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f' - {file_name}.mp3 and Text.txt saved succssefully!\n'
    else:
        return ' - File is not exist!, check the file path.'

def Main():
    tprint('PDF to TXT&MP3')
    file_path = input(" - Enter the file's path : ")
    language = input("Choose language - 'ru' or 'en': ")
    print(PDFtoTextandMp3(file_path = file_path, language = language))

if __name__ == '__main__':
    main()