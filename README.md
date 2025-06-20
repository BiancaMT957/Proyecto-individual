# Proyecto 4: "Gestión de dependencias en IaC con patrones Facade, Adapter y Mediator"
#### Alumna: Bianca Merchán Torres.
#### código: 20220425E
#### correo: bianca.merchan.t@uni.pe
#### Repositorio: https://github.com/Jharvichu/PC3_Grupo8_Proyecto4

### Rol: 

Contribuí a la creación de el módulo adapter haciendo sus implementaciones en `terraform`, `Python` y `bash` asi tambien me encargue de crear los archivos `Bash` de envio de mensaje y recibimiento de mensaje que estan dentro de las carpetas `cliente_a`  y `cliente_b.


### Herramientas necesarias:
```
$ cd ~
# shellcheck
$ sudo apt install shellcheck
# tflint
$ curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
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

Instalar requirements:

```
pip install -r requirements
```


## Ejecución
```
## 🛠 Cómo clonar y ejecutar este proyecto

```bash
git clone https://github.com/BiancaMT957/mi_proyecto_individual.git
cd mi_proyecto_individual

# Si hay scripts Python:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # Si aplica

## Dentro de adapter

# Ejemplo de ejecución de adapter_output.py
cd adapter
python3 adapter_output.py

# Ejemplo de ejecución de adapter_validate.py
python3 adapter_validate.py

# Ejemplo de ejecución de adapter_parse.sh
chmod +x adapter_parse.sh
./adapter_parse.sh

# Ejemplo de uso con Terraform
# Primero genera el .tfvars  con  ./adapter_parse.sh, luego se ejecuta esto:
# Luego ejecuta Terraform
terraform init
terraform apply

## Dentro de clientes

# Ejemplo de ejecución de cliente_a/send_message.sh
cd cliente_a
chmod +x send_message.sh
./send_message.sh

# Ejemplo de ejecución de cliente_b/receive_message.sh
cd cliente_b
chmod +x receive_message.sh
./receive_message.sh

## Para el test
# Ejecución de los tests
cd tests
pytest test_adapter_validate.py





