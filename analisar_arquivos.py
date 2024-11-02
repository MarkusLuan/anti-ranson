import os
import datetime
import argparse

def main (pasta_arquivos_infectados: str, dt_infeccao: datetime.date, extensao: str):
    unidade = os.path.basename(pasta_arquivos_infectados)
    if pasta_arquivos_infectados.endswith(":/"):
        unidade = pasta_arquivos_infectados.replace(":/", "")
    
    f_infectados = open(f"arquivos_infectados_{unidade}.txt", "w")
    f_seguros = open(f"arquivos_seguros_{unidade}.txt", "w")
    
    # Percorre o diretório e verifica os arquivos
    print(f"Escaneando arquivos...")
    for root, _, files in os.walk(pasta_arquivos_infectados):
        for file in files:
            file_path = os.path.join(root, file)
            dt_criacao = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            dt_modificacao = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if (extensao and file.endswith(extensao)) or (dt_criacao >= dt_infeccao or dt_modificacao >= dt_infeccao):
                print(f"Arquivo infectado localizado: {file}")
                f_infectados.write(f"{file_path} \n")
            else:
                print(f"O arquivo aparentemente está seguro: {file}")
                f_seguros.write(f"{file_path} \n")
    
    f_infectados.close()
    f_seguros.close()

    print(f"Escaneamento concluído!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Escanea arquivos infectados com RANSON")
    parser.add_argument("--caminho", required=True)
    parser.add_argument("--dt_infeccao", required=True)
    parser.add_argument("--extensao", default=None)

    args = parser.parse_args()
    
    try:
        dt_infeccao = datetime.datetime.strptime(args.dt_infeccao, "%d/%m/%Y")
    except:
        raise Exception ("Erro: A data de infecção deverá ser passada nesse formato: DIA/MES/ANO.\nExemplo 26/10/2024!")
    
    if not os.path.isdir(args.caminho):
        raise Exception ("Erro: O caminho informado não existe!\nO caminho deve ser a pasta onde os arquivos infectados estão!")
    
    main(args.caminho, dt_infeccao, args.extensao)