
# Contribuciones de Bianca Grazia Merchan Torres

## Sprint 1

- **2025-06-10:** Implementé `adapter/main.tf` con un recurso `null_resource` que ejecuta `adapter_output.py`.  

  Commit:  
  - `feat(tf): agregar null_resource en main.tf para ejecutar adapter_output.py`

  Pull request grupal: [#3](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/3)

- **2025-06-10:** Creé `adapter/adapter_output.py` para emitir JSON dummy.  

  Commit:  
  - `feat(py): crear adapter_output.py para emitir JSON dummy`

  Pull request grupal: [#3](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/3)

- **2025-06-10:** Añadí `adapter/adapter_parse.sh` para capturar la salida y exportar variables.  

  Commit:  
  - `feat(sh): agregar adapter_parse.sh para capturar y exportar variables`

  Pull request grupal: [#3](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/3)

- **2025-06-10:** Registré logs de ejecución en `logs/adapter.log`.  

  Commit:  
  - `chore(log): registrar logs de ejecución en adapter.log`

  Pull request grupal: [#3](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/3)

---

## Sprint 2

- **2025-06-12:** Actualicé `adapter_parse.sh` para escribir `terraform.tfvars` y registrar logs.  

  Commit:  
  - `feat(sh): (Issue #21) actualizar adapter_parse.sh para escribir terraform.tfvars y registrar logs`

  Pull request grupal: [#27](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/27)

- **2025-06-12:** Cambié `main.tf` para poder leer variables desde `terraform.tfvars`.  

  Commit:  
  - `feat(tf): (Issue #21) hacer cambios a main.tf para poder leer variables desde terraform.tfvars`

  Pull request grupal: [#27](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/27)

- **2025-06-13:** Ajusté `parse.sh` para procesar datos según la hora.  

  Commit:  
  - `fix(sh): (Issue #21) ajustar parse.sh para procesar datos según la hora`

  Pull request grupal: [#27](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/27)

- **2025-06-14:** Desarrollé los scripts Cliente A y Cliente B, y documenté el flujo de interacción con el Mediator.  

  Commit:  
  - `feat(sh): (Issue #23) agrego send_message.sh para enviar JSON con mensaje`
  - `feat(sh): (Issue #23) agregar recibir_message.sh con la finalidad de leer mensaje del mediator`
  - `docs(readme): (Issue #23) documentar flujo de scripts y su interacción con el mediador`
  - `feat(sh): (Issue #23) modificar send_message.sh para crear archivo en cliente_a desde cualquier parte`
  - `docs(readme): (Issue #23) corregir error pequeño para la ejecucion de scripts de clientes`
  - `docs(readme): (Issue #23) ajustar detalle menor en documentación`
  - `fix(sh): (Issue #23) corregir ubicación de archivo generado por send_message.sh`

  Pull request grupal: [#29](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/29)

---

## Sprint 3

- **2025-06-19:** Implementé timeout y manejo de error para `message_b.txt`.  

  Commit:  
  - `feat(sh): (Issue #40) implementar timeout y error para message_b.txt`
  - `feat(sh): (Issue #40) crear script receive_message.sh con timeout de 5s`

  Pull request grupal: [#50](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/50)

- **2025-06-19:** Creé el script `adapter_validate.py` para validar que la salida de `adapter_output.py` esté en formato JSON.  

  Commit:  
  - `feat(py): (Issue #48) crear script de validación JSON para adapter`
  - `test(py): (Issue #48) pruebas unitarias para adapter_validate`

  Pull request grupal: [#52](http://github.com/Jharvichu/PC3_Grupo8_Proyecto4/pull/52)
