import pytest  # Marco principal de pruebas
from unittest.mock import patch, MagicMock
from pathlib import Path # Para simular funciones y comportamientos
from adapter.adapter_validate import ejecutar_script, validar_salida_json, escribir # Importamos funciones a probar desde el módulo adaptor_validate
# -------------------------------------------------------
# TEST 1: Verifica que ejecutar_script funcione correctamente si el script devuelve salida válida
def test_ejecutar_script_exito():
    mock_result = MagicMock()
    mock_result.stdout = '{"status": "ok", "code": 200}'  # Salida simulada del comando

    # Parcho subprocess.run para que devuelva simulacro_resultado en vez de ejecutarse realmente
    with patch('subprocess.run', return_value=mock_result):
        salida, error = ejecutar_script()
        assert error is None  # No debe haber error
        assert salida == '{"status": "ok", "code": 200}'  # La salida debe ser la esperada

# TEST 2: Verifica el comportamiento cuando ejecuta_script falla
def test_ejecutar_script_falla():
    # Aca se simula que subprocess.run lanza una excepción
    with patch('subprocess.run', side_effect=Exception("falló el comando")):
        salida, error = ejecutar_script()
        assert salida is None  # No debe haber salida
        assert "falló el comando" in error  # El mensaje de error debe contener la excepción

# TEST 3: Valida varios casos de salida JSON usando parametrización
@pytest.mark.parametrize("salida,espera_error,espera_status", [
    ('{"status": "ok", "code": 200}', None, "ok"),  # Caso válido
    ('{"foo": "bar"}', "El JSON no contiene las claves", None),  # Faltan claves esperadas
    ('no es json', "JSON inválido", None),  # No es JSON
    ('[]', "La salida no es un objeto JSON", None),  # JSON pero no es un objeto
])
def test_validar_salida_json_casos(salida, espera_error, espera_status):
    datos, error = validar_salida_json(salida)
    if espera_error:
        # Si esperamos un error, datos debe ser None y el error debe estar en el mensaje
        assert datos is None
        assert espera_error in error
    else:
        # Si no esperamos error, el error debe ser None y los datos deben contener el status correcto
        assert error is None
        assert datos["status"] == espera_status

# TEST 4: Verifica que la función escribir() escriba el texto en el archivo
def test_escribir(tmp_path):
    file_path = tmp_path / "salida.txt"
    contenido = "Hola mundo"
    escribir(file_path, contenido)
    texto = file_path.read_text(encoding='utf-8')
    assert texto == contenido  # El contenido del archivo debe ser el mismo que el que escribimos

#  -------------------------------------------------------
# TEST 5: Verifica ejecución completa de main() cuando todo funciona correctamente
def test_main_exito(tmp_path):
    salida_valida = '{"status": "ok", "code": 200}'  # Salida simulada
    mock_result = MagicMock()
    mock_result.stdout = salida_valida

    report_path = tmp_path / "adapter_report.md"  # No se usa directamente, solo referencia

    # Simula subprocess.run y la función escribir
    with patch("subprocess.run", return_value=mock_result), \
        patch("adapter.adapter_validate.escribir") as mock_escribir:
        
        from adapter.adapter_validate import main
        main()

        # Verifica que escribirT fue llamado una vez y con el contenido esperado
        mock_escribir.assert_called_once()
        contenido = mock_escribir.call_args[0][1]
        assert "Validación exitosa" in contenido
        assert "- status: `ok`" in contenido
        assert "- code: `200`" in contenido

#
# TEST 6: Simula error al ejecutar el script -> main() debe capturarlo y salir
def test_main_error_ejecucion():
    # Simula que subprocess.run lanza una excepción
    with patch("subprocess.run", side_effect=Exception("falló el script")), \
        patch("adapter.adapter_validate.escribir") as mock_escribir:
        
        from adapter.adapter_validate import main
        with pytest.raises(SystemExit):  # Esperamos que el programa finalice con SystemExit
            main()
        
        # Verifica que el reporte contiene el mensaje de error
        contenido = mock_escribir.call_args[0][1]
        assert "Error al ejecutar" in contenido

# TEST 7: Simula error al ejecutar el script -> main() debe capturarlo y salir
def test_main_json_invalido():
    salida_invalida = 'no es json'  # Salida simulada inválida
    mock_result = MagicMock()
    mock_result.stdout = salida_invalida

    # Simula subprocess.run y la función escribir
    with patch("subprocess.run", return_value=mock_result), \
        patch("adapter.adapter_validate.escribir") as mock_escribir:
        
        from adapter.adapter_validate import main
        with pytest.raises(SystemExit):  # El programa debe terminar con SystemExit por el error
            main()
        
        # Verifica que el reporte contenga el mensaje de JSON inválido
        contenido = mock_escribir.call_args[0][1]
        assert "JSON inválido" in contenido
