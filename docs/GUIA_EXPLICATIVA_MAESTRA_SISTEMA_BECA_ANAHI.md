# 📚 GUÍA EXPLICATIVA MAESTRA: SISTEMA INTEGRAL BECA FaCENA (UNNE 2025-2026)
## Manual de Arquitectura, Fundamentos Matemáticos, Ejecución y Defensa del Plan

> **Proyecto Acreditado:** Integración de la Bioinformática y el Modelado Molecular para entender el mecanismo de acción de plantas etnomedicinales (Código: PI 21F012, SeGCyT-UNNE)  
> **Lugar de Trabajo:** Laboratorio de Estructura Molecular y Propiedades (LEMyP), FaCENA - UNNE  
> **Directores:** Dr. Emilio Luis Angelina (Director) & Codirección de Beca (FaCENA UNNE)  
> **Becaria:** Anahí Ayelén Espinoza (Profesorado en Matemática)  
> **Estado del Código:** 🔒 **CONGELADO / CODE FREEZE** (Código finalizado, verificado al 100% en `pytest`, no requiere modificaciones).

---

## 📑 ÍNDICE GENERAL
1. **Directiva de Congelamiento de Código (Code Freeze Directive)**
2. **Resumen Ejecutivo y Visión General del Sistema**
3. **Mapeo Formal: De la Matemática Pura a la Bioinformática de Grafos**
4. **Desglose Exhaustivo del Pipeline y sus 4 Módulos**
5. **Guía Paso a Paso de Ejecución para Anahí (Google Colab vs. Local)**
6. **Estructura Interna del Paquete Python (`src/gnn_pharmacology/`)**
7. **Guía de Defensa y Preparación de Informes para FaCENA / UNNE**

---

## 1. 🔒 DIRECTIVA DE CONGELAMIENTO DE CÓDIGO (CODE FREEZE)


---

## 2. 🎯 RESUMEN EJECUTIVO Y VISIÓN GENERAL DEL SISTEMA

Las enfermedades complejas (como el cáncer) se producen por perturbaciones dinámicas en la topología de la **Red de Interacciones Proteína-Proteína (PPI)** humana. Un compuesto farmacéutico o producto natural induce **Firmas de Expresión Differential (FEs)** (medidas en ARN-seq o L1000) que modulan la intensidad de estas interacciones y propagan un efecto a través de la red.

El objetivo de este sistema es:
1. **Representar el interactoma humano** como un grafo ponderado $G = (V, E, W)$ dotado de atributos nodales vectoriales generados por **ESM-2** (Modelo de Lenguaje de Proteínas de Meta AI).
2. **Simular perturbaciones** de expresión génica (CMap L1000 z-scores) mediante la modulación dinámica de las aristas del grafo ($A_{pert}$).
3. **Aprender representaciones latentes** mediante un **Graph Autoencoder (GAE)** con capas de convolución en grafos (GCN).
4. **Cuantificar la respuesta terapéutica** en el espacio latente mediante el vector de desplazamiento $\Delta H = Z_{pert} - Z_{WT}$ y la Similitud Coseno respecto a una condición de referencia (Knockout CRISPR de un gen driver en cáncer).
5. **Optimizar formulaciones sinérgicas** de 2 y 3 productos naturales (ej. *Curcumina + EGCG Té Verde + Resveratrol*) y evaluar el enriquecimiento de vías biológicas (**Gene Ontology / GSEA**).

---

## 3. 📐 MAPEO FORMAL: DE LA MATEMÁTICA PURA A LA BIOINFORMÁTICA DE GRAFOS

Para Anahí (Matemática), cada componente del sistema se traduce a estructuras algebraicas puras:

| Concepto Biológico / IA | Concepto Matemático Puro | Expresión Formal / Código |
| :--- | :--- | :--- |
| **Proteína / Gen** | Nodo $v_i \in V$ de un conjunto finito | $V = \{v_1, v_2, \dots, v_N\}, |V| = N$ |
| **Interacción Proteica (PPI)** | Arista no dirigida $(v_i, v_j) \in E$ | Matriz de Adyacencia $A \in \mathbb{R}^{N \times N}, A_{ij} \in [0,1]$ |
| **Plegamiento / Evolución Proteica** | Vector de características en $\mathbb{R}^d$ | Embedding ESM-2 $x_i \in \mathbb{R}^{640}, X \in \mathbb{R}^{N \times 640}$ |
| **Firma de Expresión (CMap L1000)** | Vector de perturbación $\mathbf{z} \in \mathbb{R}^N$ | $z_i \in \mathbb{R}$ ($z_i > 0$ sobreexpresión, $z_i < 0$ represión) |
| **Modulación Dinámica de Aristas** | Producto Hadamard ponderado | $A_{ij}^{(pert)} = A_{ij} \cdot \exp(-\alpha |z_i - z_j|)$ |
| **Convolución de Grafos (GCN)** | Transformación Lineal sobre Grafo Normalizado | $H^{(l+1)} = \text{ReLU}\left( \tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2} H^{(l)} W^{(l)} \right)$ |
| **Decodificador Latente** | Producto Interno de Vectores Latentes | $\hat{A} = \sigma(Z Z^T), \quad \hat{A}_{ij} = \frac{1}{1 + e^{-\mathbf{z}_i \cdot \mathbf{z}_j}}$ |
| **Pérdida de Entrenamiento** | Entropía Cruzada Binaria (BCE) | $\mathcal{L}_{BCE} = -\frac{1}{N^2} \sum \left[ A_{ij} \log \hat{A}_{ij} + (1 - A_{ij}) \log (1 - \hat{A}_{ij}) \right]$ |
| **Desplazamiento Latente ($\Delta H$)** | Resta de Matrices / Desplazamiento Vectorial | $\Delta H = Z_{pert} - Z_{WT} \in \mathbb{R}^{N \times 64}$ |
| **Similitud Terapéutica** | Coseno del Ángulo entre Vectores | $\cos(\theta) = \frac{\mathbf{v}_{ref} \cdot \mathbf{v}_{combo}}{\|\mathbf{v}_{ref}\|_2 \|\mathbf{v}_{combo}\|_2} \in [-1, 1]$ |

---

## 4. 🔬 DESGLOSE EXHAUSTIVO DE LOS 4 MÓDULOS Y CUADERNOS

### 📓 Módulo 1: Ingesta del Interactoma y Embeddings ESM-2 (`notebooks/01_...ipynb`)
* **Qué hace:** Conecta con STRING API v12.0 para extraer las interacciones físicas de *Homo sapiens* ($score \ge 700$). Asocia las secuencias aminoacídicas de UniProtKB y las procesa en **ESM-2** (Meta AI) para obtener vectores de $d=640$ por proteína.
* **Salida:** Grafo PyTorch Geometric `ppi_human_esm2.pt`.

### 📓 Módulo 2: CMap L1000 y Modulación Dinámica (`notebooks/02_...ipynb`)
* **Qué hace:** Carga los $z$-scores de expresión de CMap. Configura la referencia de enfermedad (Knockout CRISPR de *BRAF*) y las firmas de los productos naturales (Curcumina, Resveratrol, Quercetina, EGCG, Berberina). Modula la adyacencia mediante $A_{ij}^{(pert)} = A_{ij} \cdot \exp(-\alpha |z_i - z_j|)$.
* **Salida:** Dataset de grafos perturbados `graph_perturbations_dataset.pt`.

### 📓 Módulo 3: Modelo Graph Autoencoder (`notebooks/03_...ipynb`)
* **Qué hace:** Construye la red `GraphAutoencoderModel` con 2 capas `GCNConv`. Entrena sobre el interactoma salvaje ($WT$) hasta converger. Proyecta los grafos perturbados al espacio latente $Z \in \mathbb{R}^{N \times 64}$ y calcula el desplazamiento $\Delta H$.
* **Salida:** Model state y vectores latentes `gae_inference_results.pt`.

### 📓 Módulo 4: Virtual Screening, Sinergias y GSEA (`notebooks/04_...ipynb`)
* **Qué hace:** Realiza el Virtual Screening masivo contra decoys (midiendo ROC-AUC). Implementa la búsqueda combinatoria de tríos de productos naturales, selecciona la mezcla óptima y ejecuta el análisis de ontología génica (GO Biological Processes) con `gseapy`.
* **Salida:** Ranking de formulaciones y gráficos de enriquecimiento.

---

## 5. 💻 GUÍA PASO A PASO DE EJECUCIÓN PARA ANAHÍ

### Opción A: Ejecución en Google Colab (Recomendado para Aprendizaje e Interacción)
1. Entrar a [Google Colab](https://colab.research.google.com/).
2. Subir cualquiera de los 4 cuadernos desde la carpeta `notebooks/`.
3. Ejecutar la primera celda (`!pip install ...`) para preparar las dependencias en la nube.
4. Correr celda por celda leyendo los comentarios pedagógicos en español.

### Opción B: Ejecución Local Automática en 1-Clic
Para ejecutar todo el pipeline de principio a fin localmente sin intervención manual:
```bash
python pipeline_beca_anahi_master.py
```
* **Resultado:** El script detecta el entorno, ejecuta las 4 fases, entrena el GAE, evalúa las sinergias y genera automáticamente el archivo CSV [`RESULTADOS_OPTIMIZACION_BECA_ANAHI.csv`](file:///C:/Users/usuario/OneDrive/Bioinformatica/becaria_2026/2026-classroom/RESULTADOS_OPTIMIZACION_BECA_ANAHI.csv).

---

## 6. 🏛️ ESTRUCTURA INTERNA DEL PAQUETE PYTHON (`src/gnn_pharmacology/`)

El paquete Python modular permite importar cada etapa directamente en scripts externos:

* `src/gnn_pharmacology/ppi_loader.py`: Función `fetch_string_ppi()` para consultar STRING API.
* `src/gnn_pharmacology/protein_embedder.py`: Función `generate_protein_embeddings()` para ESM-2.
* `src/gnn_pharmacology/cmap_modulator.py`: Función `modulate_adjacency()` para modificar aristas con $z$-scores.
* `src/gnn_pharmacology/gae_model.py`: Clase PyTorch `SimpleGCN` (Autoencoder de Grafos).
* `src/gnn_pharmacology/synergy_optimizer.py`: Función `evaluate_synergies()` para evaluar tríos combinatorios.

---

## 7. 🎓 GUÍA PARA LA DEFENSA Y PRESENTACIÓN DE LA BECA FaCENA

Para la presentación del informe de avance/final ante FaCENA (UNNE):

1. **Documento Base:** Utilizar la plantilla pre-redactada [`docs/PLANTILLA_INFORME_BECA_FACENA_ANAHI.md`](file:///./docs/PLANTILLA_INFORME_BECA_FACENA_ANAHI.md).
2. **Puntos Clave a Enfatizar en la Exposición:**
   * **Innovación:** Pasar del paradigma simplista de "un blanco único" al modelado de la red de interactoma completa mediante IA.
   * **Aporte de la Matemática:** Resaltar cómo el álgebra matricial y la convolución de grafos permiten transformar secuencias complejas en espacios latentes comparables mediante Similitud Coseno.
   * **Resultado Farmacológico:** Demostrar que las mezclas sinérgicas (como *Curcumina + EGCG + Resveratrol*) logran una respuesta de difusión latente superior a cualquiera de los compuestos por separado.

---

`[VINCIT_OMNIA_VERITAS]`
