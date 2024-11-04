# Anti-RANSON

Fui infectado por RANSON, então acabei criando este projeto a fim de tentar descobrir quais arquivos foram infectados e se possivel tentar recuperá-los. E estou deixando publico a fim de poder ajudar a outras pessoas também.

Descobriram meu usuário, senha e IP, entraram no RDP e instalaram alguns Softwares como o "Proceess Hacker 2" e criptografaram meus arquivos do HD do windows.

O vírus que me infectou, tem como descrição ELPACO-TEAM.

### Funcionamento dos meus scripts
Recomendo executar os meus scripts no linux e montar a partição infectada como apenas leitura
```shell
mount -o ro /dev/sda1 /mnt/c
```

#### Escaner de arquivos - [analisar_arquivos.py](./analisar_arquivos.py)
Escaneia os arquivos e indica os que foram infectados, os que estão seguros e os que tiveram metadados alterados.
O escaner é feito com base na data de modificação dos arquivos ou com base na extenção (que o ranson modifica).

Para executar o script:
```shell
python3 analisar_arquivos.py --caminho /mnt/c --dt_infeccao 26/04/2024 \[--extensao ELPACO-TEAM-ID\]
```

* Caminho é a pasta onde está montado o HD
* dt_infeccao é a Data de quando o primeiro arquivo foi corrompido
* Extensao é um argumento opcional e indica qual foi a extensão criada pelo RANSON

#### Copia de arquivos seguros - [cp_arquivos_seguros.py](./cp_arquivos_seguros.py)
<b>Executar apenas após o escaner.</b>
Faz a cópia dos arquivos que estão seguros, permitindo fazer uma formatação sem perder os arquivos que não foram infectados

Para executar o script:
```shell
python3 cp_arquivos_seguros.py --origem /mnt/c --destino /bkp \[--ignorar pasta\|arquivo\]
```
por exemplo
```shell
python3 cp_arquivos_seguros.py --origem /mnt/c --destino bkp --ignorar 'Program Files' --ignorar 'Program Files (x86)' --ignorar 'System Volume Information' --ignorar Tesseract-OCR --ignorar Recovery --ignorar DumpStack.log --ignorar_pasta AMD --ignorar '$Recycle.Bin' --ignorar Intel
```

* Origem é a pasta onde está montado o HD
* Destino é a pasta onde será salvo o backup
* Ignorar é usado para indicar quais pastas ou arquivos ignorar e pode ser repetido quantas vezes necessário

#### Listar Programas Instalados - [listar_programas.py](./listar_programas.py)
Lista os programas instalados com base na pasta
- C:/Program Files
- C:/Program Files (x86)

Para executar o script:
```shell
python3 listar_programas.py --caminho /mnt/c
```

* O caminho é a pasta onde está montado o HD

---

### Algumas informações que descobri sobre o RANSON
* Os crackers (Hackers do mal) instalaram no meu computador um software chamado 'Process Hacker 2', que roda em segundo plano alguns serviços em modo de kernel. Aparentemente esse processo inicia quando o usuário loga e baixa uma chave publica em c:/Users/{usuario}/Downloads/encryption_public_key.pem para realizar a criptografia.

* Aparentemente eles também usaram uma maquina virtual através do VmWare. Acredito que foi para monitorar o input de senhas ou algo do genero (mas graças a Deus nos dias que eles estavam com essa maquina aberta não fiz login nenhum - afinal estava focado em entregar um projeto para uma vaga de programador). E de qualquer forma alterei todas minhas senhas.

* Por algum motivo antes de criptografar os arquivos eles modificam algumas coisas no metadados dos arquivos (não consegui identificar ainda o que foi alterado nos metadados).

* Além de criptografar os arquivos eles também geram ou tornam "arquivos fantasmas", que aparecem no ls ou dir, porém ao tentar ler ou ver a data de modificação do arquivo informa que o arquivo não existe.

* A chave fornecida pelo ELPACO-TEAM não é bem uma chave, pelo que eu vi... Na verdade é só informando qual a extensão que os arquivos terão após o ataque. 

* Os arquivos são criptografados conforme o tamanho e formato dos mesmos (Por exemplo, se um arquivo tiver 2kb (vamos supor), ele não seria criptografado). E um executavel não é renomeado, embora tenha sido alterado o conteudo do mesmo.

* Os IPs responsaveis por isso foram:
```
85.209.11.191 - ONLINE - Rusia
92.51.2.56 - OFFLINE - Rusia
185.234.216.19 - ONLINE - Rusia
77.83.38.206 - OFFLINE - Bulgaria
149.28.146.16 - ONLINE - Singapura
119.201.140.94 - OFFLINE - Corea do Sul
185.9.55.64 - OFFLINE - Latvia - SERVER-PC
```
Entenda o ONLINE/OFFLINE como se retornou ping ou não

* Nos logs também encontrei isto aqui, mas não sei exatamente o que significa
```
WindowsLive:target=virtualapp/didlogical
MicrosoftAccount:user=02ritameipukcera
WindowsLive:(token):name=02nieralseklqqxy;serviceuri=*
WindowsLive:(token):name=02ritameipukcera;serviceuri=*
```
