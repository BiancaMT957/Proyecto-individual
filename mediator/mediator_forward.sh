#!/bin/bash

TMP_MSG="./tmp_message.txt"
MSG_B="./message_b.txt"

# Verifica si existe el archivo
if [ ! -f "$TMP_MSG" ]; then
  echo "[Mediator] ERROR: No se encontró $TMP_MSG."
  éxito 1
fi

# Pasa el contenido del archivo temporal a message_b.txt
echo "[Mediator] Reenviando el mensaje a $MSG_B..."
cp "$TMP_MSG" "$MSG_B"
echo "[Mediator] Mensaje reenviado exitosamente."