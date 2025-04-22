# Instalación de Miniconda en macOS M1 (Apple Silicon)

## 1.- Descargar Miniconda
Visita la página oficial:
👉 [Miniconda Official Site](https://docs.conda.io/en/latest/miniconda.html)

Descarga el instalador para **macOS (ARM64, Apple Silicon)**.

## 2.- Abrir la Terminal
Puedes encontrarla en **Aplicaciones > Utilidades > Terminal**.

## 3.- Ejecutar el Instalador
Navega a la carpeta donde se descargó Miniconda (generalmente `Descargas`):
```
cd ~/Downloads
```
Ejecuta el instalador (ajusta el nombre del archivo según la versión que descargaste):
```bash
bash Miniconda3-latest-MacOSX-arm64.sh
```
Acepta los términos y sigue las instrucciones en pantalla.

## 4.- Cargar Conda en la Terminal
Después de instalar, cierra y reabre la terminal o ejecuta:
```bash
source ~/.bashrc  # Si usas Bash
source ~/.zshrc   # Si usas Zsh (por defecto en macOS)
```

## 5.- Verificar la Instalación
Ejecuta:
```
conda --version
```
Si todo está bien, mostrará la versión instalada, por ejemplo:
```
conda 25.1.1

```
---

# 🔹 Comandos Útiles en Conda
Aquí tienes algunas funciones clave para manejar ambientes y paquetes en Miniconda.

## Crear un ambiente virtual
Para crear un nuevo ambiente llamado `mi_env` con Python 3.10:
```
conda create --name mi_env python=3.10
```
Después de crearlo, actívalo con:
```
conda activate mi_env
```

## Ver los ambientes instalados
Para ver todos los ambientes disponibles en tu sistema:
```
conda env list
```
o
```
conda info --envs
```
Salida esperada:
```
# conda environments:
#
base                  *  /Users/tu_usuario/miniconda3
mi_env                  /Users/tu_usuario/miniconda3/envs/mi_env
```

## Ver paquetes instalados en un ambiente
Si quieres ver qué paquetes están instalados dentro de un ambiente específico, usa:
```
conda list --name mi_env
```

## Instalar un paquete en un ambiente
Ejemplo: instalar `numpy` en `mi_env`:
```
conda install --name mi_env numpy
```
O si el ambiente ya está activado:
```
conda install numpy
```

## Eliminar un ambiente
Si ya no necesitas un ambiente y quieres borrarlo completamente:
```
conda remove --name mi_env --all
```
Esto eliminará todos los paquetes y dependencias dentro del ambiente.
