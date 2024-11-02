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

### Algumas informações que descobri
Os IPs responsaveis por isso foram:
```
85.209.11.191 - on - Rusia
92.51.2.56 - off - Rusia
185.234.216.19 - on - Rusia
77.83.38.206 - off - Bulgaria
149.28.146.16 - on - Singapura
119.201.140.94 - off - Corea do Sul
185.9.55.64 - off - Latvia - SERVER-PC
```

Nos logs também encontrei isto aqui, mas não sei exatamente o que significa
```
WindowsLive:target=virtualapp/didlogical
MicrosoftAccount:user=02ritameipukcera
WindowsLive:(token):name=02nieralseklqqxy;serviceuri=*
WindowsLive:(token):name=02ritameipukcera;serviceuri=*
```
