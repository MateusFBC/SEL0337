# SEL0337

Alunos: 

Antônio Duarte Pesqueira - 13677052 / Mateus Francisco Balesteros Cintra - 13676670

Nesta prática, foi implementado a execução de códigos em Python no BOOT da Raspberry Pi. Através do arquivo "blink.service", chamado de unit file, foi criado o serviço de execução dos códigos:

```
[Unit]
Description = Blink LED
After = multi-user.target

[Service]
ExecStart = /bin/python /home/sel/pratica5/blink1.py
ExecStop = /bin/python /home/sel/pratica5/blink2.py
user = SEL

[Install]
WantedBy = multi-user.target
```

Como o programa controla o acendimento de um LED, no bloco [Unit], é indicado o texto de inicialização no systemd, "Blink LED".

No bloco [Service], é indicado o programa a ser executado quando inicializado pelo 'ExecStart', e o programa que será executado quando o primeiro for interrompido em 'ExecStop'.

No último bloco, [Install], indica que esse processo será instalado em todos os usuários da máquina.

O código de inicialização (blink1.py) realiza o blink de um LED conectado ao GPIO23:

```
from gpiozero import LED
from time import sleep

pin = LED(23)

while 1:
	pin.on()
	sleep(1)
	pin.off()
	sleep(1)
```

O qual foi escolhido como verde na montagem prática.

E o código de encerramento (blink2.py) mantém um LED conectado ao GPIO18 aceso constantemente:

```
from gpiozero import LED

pin = LED(18)

while 1:
	pin.on()
```

Assim, na inicialização da Rasp (o LED pisca):

![image](https://github.com/user-attachments/assets/377abc6d-35ff-45be-9239-306d5cfd317f)

E no encerramento do código:

![image](https://github.com/user-attachments/assets/7b56175b-627e-44c2-be80-1ad0ef27104c)

OBS: Os códigos foram 'upados' diretamente da Rasp sem comentários. 

