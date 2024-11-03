import os
import datetime
import argparse

def main (pasta_arquivos_infectados: str, dt_infeccao: datetime.date, extensao: str):
    unidade = os.path.basename(pasta_arquivos_infectados)
    if pasta_arquivos_infectados.endswith(":/"):
        unidade = pasta_arquivos_infectados.replace(":/", "")
    
    f_infectados = open(f"arquivos_infectados_{unidade}.txt", "w")
    f_meta_alterados = open(f"arquivos_meta_alterados_{unidade}.txt", "w")
    f_seguros = open(f"arquivos_seguros_{unidade}.txt", "w")
    
    # Percorre o diretório e verifica os arquivos
    print(f"Escaneando arquivos...")
    for root, _, files in os.walk(pasta_arquivos_infectados):
        for file in files:
            file_path = os.path.join(root, file)
            
            if os.path.islink(file_path):
               if not os.path.exists(os.readlink(file_path)):
                   print(f"O arquivo aponta para um link invalido: {file}")
                   f_infectados.write(f"{file_path} \n")
                   continue
            
            try:
                stat_info = os.stat(file_path)

                dt_alteracao_metadados = datetime.datetime.fromtimestamp(stat_info.st_ctime)
                dt_modificacao = datetime.datetime.fromtimestamp(stat_info.st_mtime)
                
                if (extensao and file.endswith(extensao)) or dt_modificacao >= dt_infeccao:
                    print(f"Arquivo infectado localizado: {file} | Criado em: {dt_alteracao_metadados.isoformat()} | Modificado em: {dt_modificacao.isoformat()}")
                    f_infectados.write(f"{file_path} \n")
                else:
                    if dt_alteracao_metadados >= dt_infeccao:
                        print(f"Os metadados do arquivo foram modificados: {file}")
                        f_meta_alterados.write(f"{file_path} \n")
                    
                    print(f"O arquivo aparentemente está seguro: {file}")
                    f_seguros.write(f"{file_path} \n")
            except Exception as e:
                print(f"Ocorreu um erro ao analisar o arquivo: {file}\nConsiderando como corrompido\nErro: {e}\n")
                f_infectados.write(f"{file_path} \n")
                continue
    
    f_infectados.close()
    f_meta_alterados.close()
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