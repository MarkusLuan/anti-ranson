import os
import argparse
import shutil

import constantes

def get_lista_arquivos(arquivo: str):
    if not os.path.isfile(arquivo):
        raise Exception (f"{constantes.COLOR_RED}O arquivo '{arquivo}' não existe!\nCertifique-se de que executou o escaner antes e de que o arquivo esteja na mesma pasta do script!")
    
    arquivos = []
    with open(arquivo, "r") as f:
        arquivos = f.readlines()
    return arquivos

def main (unidade: str, destino: str):
    arquivos_seguros = get_lista_arquivos(f"arquivos_seguros_{unidade}.txt")
    arquivos_meta_alterados = get_lista_arquivos(f"arquivos_meta_alterados_{unidade}.txt")
    
    print(f"{constantes.COLOR_BLUE}Copiando arquivos...{constantes.COLOR_RESET}")
    for arquivo in arquivos_seguros:
        print(f"{constantes.COLOR_GREEN}Copiando {arquivo}...{constantes.COLOR_RESET}")
        
        if arquivo in arquivos_meta_alterados:
            print(f"{constantes.COLOR_YELLOW}{os.path.basename(arquivo)} teve os metadados alterados!\nMantendo separado!{constantes.COLOR_RESET}")
            pass
        
        break
        # shutil.copy()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copia os arquivos que foram considerados seguros pelo escaner.")
    parser.add_argument("--origem", help="HD onde estão os arquivos infectados", required=True)
    parser.add_argument("--destino", help="Pasta onde deseja salvar os arquivos", required=True)

    args = parser.parse_args()
    
    if not os.path.isdir(args.origem):
        raise Exception (f"{constantes.COLOR_RED}Erro: O arquivo informado não existe!\nO argumento --i deve ser o arquivo que foi gerado após realizar o scan!{constantes.COLOR_RESET}")
    
    if not os.path.isdir(args.destino):
        raise Exception (f"{constantes.COLOR_RED}Erro: O destino informado não existe!\nO destino deve ser a pasta para onde deseja salvar os arquivos!{constantes.COLOR_RESET}")
    
    pasta_origem = os.path.basename(args.origem)
    unidade = pasta_origem
    if args.origem.endswith(":/"):
        unidade = args.origem.replace(":/", "")
    
    main(unidade, args.destino)