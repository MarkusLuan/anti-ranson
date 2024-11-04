import os
import argparse

import constantes

def get_programas(raiz_os: str, tipo: str):
    if tipo not in ["x86", "x64"]:
        raise Exception (f"{constantes.COLOR_RED}Erro: Bytes não reconhecido - '{tipo}'{constantes.COLOR_RESET}")
    
    pasta_pf = "Program Files"
    if tipo != "x64":
        pasta_pf += f" ({tipo})"
    
    pasta = os.path.join(raiz_os, pasta_pf)
    programas = []
    
    if os.path.isdir(pasta):
        programas = os.listdir(pasta)
    
    return programas

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lista os programas que estavam instalados no PC")
    parser.add_argument("--caminho", required=True)
    args = parser.parse_args()
    
    for tipo in ["x86", "x64"]:
        programas = get_programas(args.caminho, tipo)
        with open(f"programas_{tipo}", "w") as f:
            for programa in programas:
                f.write(f"{programa}\n")