from os import chdir, listdir, path, mkdir, rename, system

print('Organizador de Pastas v1.0')
print('')
diretorio = input('Digite o diretório: ')
print('')

try:
    chdir(diretorio)
    print("Caminho encontrado.")
    print('')
    
    arquivosDoDiretorio = listdir('.')
    
    tipos_arquivos = {
    "PDFs": [".pdf"],
    "Textos": [".txt"],
    "Word": [".docx"],
    "PowerPoint": [".pptx"],
    "Excel": [".xlsx"],
    "Imagens": [".jpeg", ".jpg", ".png"],
    "Videos": [".mp4", ".avi", ".mov", ".mpg", ".wmv"],
    "Audios": [".mp3", ".ogg", ".wav", ".flac", ".m4a", ".wma"]
}

    organizou_arquivos = False
    
    for pasta, extensoes in tipos_arquivos.items():
        existe_arquivo = any(arquivo.endswith(ext) for ext in extensoes for arquivo in arquivosDoDiretorio)
        
        if existe_arquivo:
            if not path.exists(pasta):
                mkdir(pasta)
            
            for arquivo in arquivosDoDiretorio:
                if any(arquivo.endswith(ext) for ext in extensoes):
                    rename(arquivo, path.join(pasta, arquivo))
                    print(f"Arquivo '{arquivo}' movido para a pasta '{pasta}'.")
                    print('')
                    organizou_arquivos = True
    if not organizou_arquivos:
        print("Não há arquivos para organizar no diretório.")
        print('')
        
except FileNotFoundError:
    print("Caminho não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

system("pause")