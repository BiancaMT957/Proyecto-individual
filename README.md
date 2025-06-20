# Proyecto 4: "Gestión de dependencias en IaC con patrones Facade, Adapter y Mediator"
#### Alumna: Bianca Merchán Torres.
#### código: 20220425E
#### correo: bianca.merchan.t@uni.pe
#### Repositorio: https://github.com/Jharvichu/PC3_Grupo8_Proyecto4

### Rol: 

Contribuí a la creación de el módulo adapter haciendo sus implementaciones en `terraform`, `Python` y `bash` asi tambien me encargue de crear los archivos `Bash` de envio de mensaje y recibimiento de mensaje que estan dentro de las carpetas `cliente_a`  y `cliente_b. 


### Herramientas necesarias:
```
 
# terraform
$ sudo apt update
$ sudo apt install terraform
# python
$ sudo apt update
$ sudo apt install python3 python3-pip -y
# jq
$ sudo apt install jq
```

### Instrucciones

Para crear entorno virtual y activarlo.
```
python3 -m venv .venv
```

```
 source venv/bin/activate
 ```


## Ejecución
```
##  Cómo clonar y ejecutar este proyecto

```bash
git clone https://github.com/BiancaMT957/mi_proyecto_individual.git
cd mi_proyecto_individual

# Si hay scripts Python:
python3 -m venv .venv
source .venv/bin/activate

## Dentro de adapter

# Ejemplo de ejecución de adapter_output.py
cd adapter
python3 adapter_output.py

# Ejemplo de ejecución de adapter_validate.py
python3 adapter_validate.py

# Ejemplo de ejecución de adapter_parse.sh
chmod +x adapter_parse.sh
./adapter_parse.sh

# Ejemplo de uso con Terraform del adapter/main.tf
# Primero genera el .tfvars  con  ./adapter_parse.sh, luego se ejecuta esto:
# Luego ejecuta Terraform
terraform init
terraform apply

## Dentro de clientes

# Ejemplo de ejecución de cliente_a/send_message.sh
cd cliente_a
chmod +x send_message.sh

bash send_message.sh "hola que tal"

##desde la raiz del proyecto

cp cliente_a/message_a.txt mediator/tmp_message.txt

## dentro de mediator
cd mediator

./mediator_forward.sh


# Ejemplo de ejecución de cliente_b/receive_message.sh
cd cliente_b

chmod +x receive_message.sh

./receive_message.sh

## Para el test
# Ejecución de los tests
cd tests
pytest test_adapter_validate.py





