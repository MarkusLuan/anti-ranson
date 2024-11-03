# Anti-RANSON

Fui infectado por RANSON, então acabei criando este projeto a fim de tentar descobrir quais arquivos foram infectados e se possivel tentar recuperá-los. E estou deixando publico a fim de poder ajudar a outras pessoas também.

Descobriram meu usuário, senha e IP, entraram no RDP e instalaram alguns Softwares como o "Proceess Hacker 2" e criptografaram meus arquivos do HD do windows.

O vírus que me infectou, tem como descrição ELPACO-TEAM.

### Funcionamento dos meus scripts
Até o momento só criei um script em python para escanear os arquivos para listar os arquivos que estão infectados e os que não estão. O script verifica com base na data de modificação dos arquivos ou com base na extenção (que o ranson modifica).

Recomendo executar o meu script no linux e montar a partição infectada como apenas leitura
```shell
mount -o ro /dev/sda1 /mnt/c
```

Para executar o script de analise basta passar os parametros
```shell
python3 analisar_arquivos.py --caminho /mnt/c --dt_infeccao 26/04/2024 --extensao ELPACO-TEAM-ID
```

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
