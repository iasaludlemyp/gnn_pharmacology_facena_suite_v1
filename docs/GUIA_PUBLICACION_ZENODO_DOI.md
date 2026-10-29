# 🏛️ GUÍA OFICIAL PARA DEPÓSITO Y OBTENCIÓN DE DOI EN ZENODO
## Repositorio: `gnn-pharmacology-v1-becaria` (FaCENA - UNNE)

> **Propósito:** Asignar un identificador de objeto digital persistente (**DOI**) a través de **Zenodo (CERN / OpenAIRE)** para convalidar la producción de software científico y datos del plan de beca en el sistema **SIGEVA (CONICET / UNNE)** y en informes de la **SeGCyT-UNNE (Proyecto PI 21F012)**.

---

## 📌 ¿Qué archivos se prepararon en el repositorio?

1. `.zenodo.json`: Archivo de metadatos oficial que Zenodo lee de forma automática (autores, afiliaciones, resumen académico, palabras clave, licencias y subvención PI 21F012).
2. `CITATION.cff`: Archivo estándar de citación que habilita el botón *"Cite this repository"* en GitHub y permite exportar la cita en formatos BibTeX, APA y CFF.

---

## 🚀 Método A: Vinculación Automática GitHub $\leftrightarrow$ Zenodo (Recomendado)

Este método archiva el repositorio automáticamente en los servidores seguros del CERN cada vez que se emite un nuevo release:

### Paso 1: Iniciar sesión en Zenodo con GitHub
1. Ingresar a [https://zenodo.org](https://zenodo.org).
2. Hacer clic en **Log in** (Iniciar sesión) y seleccionar **Log in with GitHub**.
3. Autorizar el acceso con la cuenta `iasaludlemyp`.

### Paso 2: Activar el repositorio en Zenodo
1. Ir al menú superior derecho (avatar de usuario) $\to$ **GitHub** (o acceder a [https://zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/)).
2. Buscar en la lista el repositorio `iasaludlemyp/gnn-pharmacology-v1-becaria`.
3. Cambiar el interruptor de **OFF** a **ON** (se pondrá verde).

### Paso 3: Publicar el Release
1. Ir a la pestaña **Releases** de tu repositorio en GitHub:  
   [https://github.com/iasaludlemyp/gnn-pharmacology-v1-becaria/releases](https://github.com/iasaludlemyp/gnn-pharmacology-v1-becaria/releases)
2. En unos segundos, Zenodo detectará el release `v1.0.0`, generará un snapshot del código y le asignará un **DOI oficial** (ej. `10.5281/zenodo.14XXXXXX`).
3. Zenodo te entregará un *badge* oficial en formato Markdown para incrustar en el `README.md`:
   ```markdown
   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
   ```

---

## 📦 Método B: Depósito Manual en Zenodo (1-Clic vía ZIP)

Si prefieres no vincular la cuenta de GitHub o requieres el DOI de forma inmediata e independiente:

1. Ingresar a [https://zenodo.org/deposit/new](https://zenodo.org/deposit/new).
2. En la sección **Files**, arrastrar y soltar el archivo pre-empaquetado:  
   `gnn_pharmacology_v1.0.0_zenodo_deposit.zip`  
   *(Generado en `c:\Users\rafae\.gemini\01_PROYECTOS\0034_gnn_pharmacology_facena_suite/`)*.
3. **Tipo de Recurso:** Seleccionar **Software**.
4. **Título:**  
   `GNN Natural Products Pharmacology Suite: Redes Neuronales de Grafos y Modelado Molecular en Etnomedicina (FaCENA - UNNE)`
5. **Autores:**
   * **Pérez, Rafael Ernesto** (LEMyP, FaCENA - UNNE / CONICET)
   * **Angelina, Emilio Luis** (LEMyP, FaCENA - UNNE / IQUIBA-NEA)
   * **Espinoza, Anahí Ayelén** (FaCENA - UNNE)
6. **Descripción:** Copiar la descripción incluida en el archivo `.zenodo.json`.
7. **Licencia:** MIT License.
8. Hacer clic en **Publish**. ¡Listo! Zenodo emitirá el DOI permanente de inmediato.

---

## 📋 Cómo Citar en SIGEVA (CONICET / UNNE) y Memoria de Beca

En el sistema SIGEVA, registrar bajo el rubro **Desarrollo Tecnológico y Social $\to$ Producción de Software**:

* **Título del Software:** GNN Natural Products Pharmacology Suite (FaCENA - UNNE) v1.0
* **Autores:** Pérez, Rafael E.; Angelina, Emilio L.; Espinoza, Anahí A.
* **Año:** 2026
* **Institución Responsable:** LEMyP, FaCENA - Universidad Nacional del Nordeste (UNNE).
* **Marco:** Proyecto Acreditado SeGCyT PI 21F012.
* **URL / Repositorio:** [https://github.com/iasaludlemyp/gnn-pharmacology-v1-becaria](https://github.com/iasaludlemyp/gnn-pharmacology-v1-becaria)
* **Identificador Persistente:** DOI de Zenodo emitido tras la publicación.
