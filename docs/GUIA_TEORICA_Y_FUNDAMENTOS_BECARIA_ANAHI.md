# 🧬 GUÍA TEÓRICO-METODOLÓGICA DE BIOINFORMÁTICA E IA EN SALUD
## Plan de Beca de Estimulación a la Investigación Científica y Desarrollo Tecnológico (FaCENA - UNNE 2025-2026)

> **Título del Plan:** *Desarrollo de un modelo de Red Neuronal de Grafos (GNN) para la optimización de formulaciones basadas en compuestos naturales con potencial terapéutico*  
> **Proyecto Acreditado:** Integración de la Bioinformática y el Modelado Molecular para entender el mecanismo de acción de plantas etnomedicinales (PI 21F012, SeGCyT-UNNE)  
> **Lugar de Trabajo:** Laboratorio de Estructura Molecular y Propiedades (LEMyP), FaCENA - UNNE  
> **Director:** Dr. Emilio Luis Angelina  
> **Codirector:** Dirección de Beca FaCENA UNNE  
> **Becaria:** Anahí Ayelén Espinoza (Profesorado en Matemática)

---

## 📑 ÍNDICE GENERAL
1. **Introducción: De la Matemática Pura a la Bioinformática y Biología de Redes**
2. **Guía Práctica de Python para Matemáticos**
3. **Catálogo y Fundamentos de las Bases de Datos Bioinformáticas del Plan**
4. **Fundamentos Matemáticos y Arquitectura del Modelo (GNN / GAE)**
5. **Estrategia Metodológica: Perturbaciones Latentes, Cribado Virtual y Sinergia de Productos Naturales**
6. **Hoja de Ruta de los Cuadernos de Código (Google Colab / Jupyter)**

---

## 1. 📐 INTRODUCCIÓN: DE LA MATEMÁTICA PURA A LA BIOINFORMÁTICA Y BIOLOGÍA DE REDES

Bienvenida a esta guía, Anahí. Como profesional y estudiante avanzada de Matemática, posees un entrenamiento riguroso en abstracción, teoría de conjuntos, álgebra lineal, análisis de funciones, topología y probabilidad. La bioinformática moderna y la inteligencia artificial en salud no son más que la **aplicación de estos mismos principios matemáticos a sistemas de información biológica**.

### 1.1 El Flujo Central de la Biología Molecular como Transformación de Información
En biología molecular se estudia cómo la información fluye en un sistema vivo:
$$\text{ADN (Genoma)} \xrightarrow{\text{Transcripción}} \text{ARN (Transcriptoma)} \xrightarrow{\text{Traducción}} \text{Proteínas (Proteoma)} \xrightarrow{\text{Función}} \text{Fenotipo (Salud / Enfermedad)}$$

Desde nuestra perspectiva matemática:
* **El ADN** es una secuencia $S \in \{A, T, C, G\}^*$, es decir, una cadena sobre un alfabeto finito de 4 símbolos.
* **El ARN** resulta de una función de mapeo $f_{transcripcion}: \{A, T, C, G\}^* \to \{A, U, C, G\}^*$. La abundancia de este ARN en un momento dado se mide mediante cuantitativos de expresión génica ($z$-scores de ARN-seq o L1000).
* **Las Proteínas** son cadenas $P \in \mathcal{A}^*$ compuestas por 20 aminoácidos estándar $\mathcal{A} = \{A, R, N, D, C, E, Q, G, H, I, L, K, M, F, P, S, T, W, Y, V\}$. Estas cadenas se pliegan en el espacio tridimensional $\mathbb{R}^3$, adquiriendo una estructura espacial $\mathbf{R}_i \in \mathbb{R}^{3 \times N_{atomb}}$ indispensable para su función.

---

### 1.2 La Hipótesis de la Biología de Redes (Network Medicine)
Tradicionalmente, la farmacología buscaba una solución del tipo **"Un Gen / Una Proteína Blancas $\rightarrow$ Un Fármaco"**. Sin embargo, las enfermedades complejas (como el cáncer o las patologías crónicas) no se producen por la falla aislada de un elemento, sino por la **perturbación de un sistema interconectado**.

Un sistema biológico se modela mediante un **Grafo No Dirigido y Ponderado**:
$$G = (V, E, W)$$

Donde:
* $V = \{v_1, v_2, \dots, v_N\}$ es el conjunto de **Nodos** (Proteínas o Genes humanos, $|V| \approx 20.000$).
* $E \subseteq V \times V$ es el conjunto de **Aristas** (Interacciones físicas Proteína-Proteína, conocidas como PPI - *Protein-Protein Interactions*).
* $W: E \to [0, 1]$ es una **Función de Peso** que asigna el grado de evidencia o intensidad de la interacción física entre la proteína $v_i$ y la proteína $v_j$.

```
[ Estado Sano (WT) ]            [ Estado Enfermo (Perturbado) ]         [ Acción Terapéutica / Fármaco ]
   (v1) --- (v2)                   (v1) === (v2) [Perturbado]               (v1) --- (v2) [Restaurado]
    |        |                        \\       |                               |        |
   (v3) --- (v4)                   (v3) --- (v4)                            (v3) --- (v4)
  Grafo Normal                     Reconfiguración de Aristas               Propagación del Efecto Terapéutico
```

> **Principio de Difusión Terapéutica:** Un compuesto no necesita unirse directamente a la proteína mutada o dañada. Si se une a proteínas vecinas en el grafo $G$, el efecto se propaga a través de la topología de la red hasta contrarrestar la perturbación de la enfermedad.

---

## 2. 🐍 GUÍA PRÁCTICA DE PYTHON PARA MATEMÁTICOS

Python es el lenguaje estándar en Inteligencia Artificial. Como matemática, te resultará natural entender Python pensando en términos de vectores, matrices, transformaciones y estructuras de datos.

### 2.1 Equivalencias entre Notación Matemática y Código Python

| Símbolo Matemático | Concepto | Equivalente en Python (NumPy / PyTorch) |
| :--- | :--- | :--- |
| $v \in \mathbb{R}^d$ | Vector de dimensión $d$ | `v = np.array([1.2, 0.5, -3.1])` o `v = torch.tensor(...)` |
| $A \in \mathbb{R}^{N \times N}$ | Matriz de Adyacencia | `A = np.zeros((N, N))` o `A = torch.sparse_coo_tensor(...)` |
| $A \cdot v$ | Producto Matriz-Vector | `np.dot(A, v)` o `torch.matmul(A, v)` |
| $u \cdot v$ | Producto Escalar (Dot Product) | `np.dot(u, v)` o `torch.dot(u, v)` |
| $\|v\|_2 = \sqrt{\sum v_i^2}$ | Norma Euclídea / $L_2$ | `np.linalg.norm(v)` o `torch.norm(v, p=2)` |
| $\cos(\theta) = \frac{u \cdot v}{\|u\| \|v\|}$ | Similitud de Coseno | `scipy.spatial.distance.cosine(u, v)` o `torch.nn.functional.cosine_similarity(u, v, dim=0)` |
| $G = (V, E)$ | Grafo no dirigido | `G = nx.Graph()` (Librería `networkx`) |

---

### 2.2 Estructura Fundamental en PyTorch Geometric (`torch_geometric`)
En Inteligencia Artificial de Grafos, no almacenamos matrices de adyacencia gigantas cuadradas $N \times N$ llenas de ceros (matrices dispersas). En su lugar, usamos el formato **COO (Coordinate Format)**:

1. `edge_index` $\in \mathbb{Z}^{2 \times |E|}$: Tensor de números enteros donde la primera fila contiene los nodos origen y la segunda fila contiene los nodos destino de cada interacción.
2. `x` $\in \mathbb{R}^{|V| \times d}$: Matriz de características de nodos (*Node Feature Matrix*). Cada fila $i$ representa a la proteína $v_i$ mediante un vector de características de dimensión $d$.
3. `edge_attr` $\in \mathbb{R}^{|E| \times k}$: Atributos o pesos asociados a cada arista (ejemplo: score de confianza de STRING).

```python
import torch
from torch_geometric.data import Data

# Ejemplo: Un grafo con 4 proteínas (0: EGFR, 1: TP53, 2: BRCA1, 3: MYC)
# 3 Interacciones: (0-1), (1-2), (2-3)
edge_index = torch.tensor([
    [0, 1, 1, 2, 2, 3], # Nodo origen (bidireccional)
    [1, 0, 2, 1, 3, 2]  # Nodo destino
], dtype=torch.long)

# Matriz de Atributos nodales X (ej: 4 proteínas, vectores de dim 3)
x = torch.tensor([
    [0.1, 0.9, 0.4], # EGFR
    [0.8, 0.2, 0.1], # TP53
    [0.5, 0.5, 0.9], # BRCA1
    [0.3, 0.7, 0.2]  # MYC
], dtype=torch.float)

# Construcción del objeto Data de PyTorch Geometric
grafo_interactoma = Data(x=x, edge_index=edge_index)
print("Grafo creado exitosamente:", grafo_interactoma)
```

---

## 3. 📚 CATÁLOGO Y FUNDAMENTOS DE LAS BASES DE DATOS DEL PLAN

Tu plan de trabajo integra **5 fuentes de datos bioinformáticas de estándar internacional**. A continuación se detalla su rol matemático y biológico:

```
+-----------------------------------------------------------------------------------+
|                                  FUENTES DE DATOS                                 |
+--------------------------+--------------------------+-----------------------------+
| 1. STRING (v12.0)        | 2. UniProt + ESM-2       | 3. Connectivity Map (CMap)  |
| Grafo de la Red de       | Embeddings Estructurales | Firmas de Expresión (FEs)   |
| Interacciones Proteicas  | y Evolutivos de Nodos    | (z-scores de Perturbación)  |
| PPI -> Topologia (A)     | Proteínas -> Matriz (X)  | Modulación Dinámica (A_pert)|
+--------------------------+--------------------------+-----------------------------+
               \                        |                        /
                \                       |                       /
                 v                      v                      v
+-----------------------------------------------------------------------------------+
|                        4. COCONUT (Productos Naturales)                           |
| Quimioteca de fitocompuestos para filtrado, cribado virtual y sinergias (A3)      |
+-----------------------------------------------------------------------------------+
                                        |
                                        v
+-----------------------------------------------------------------------------------+
|                    5. Gene Ontology (GO) + GSEA / Enrichr                         |
| Anotación funcional y validación de vías biológicas en espacio latente            |
+-----------------------------------------------------------------------------------+
```

### 3.1 STRING Database (v12.0) — *The Search Tool for Recurring Proteins*
* **Propósito:** Construir la topología del interactoma humano (Matriz de Adyacencia $A$).
* **Filtro del Plan:** Se seleccionan interacciones de la especie *Homo sapiens* (TaxID `9606`) respaldadas por evidencia experimental directa (*experimental channel*) con un umbral de confianza combinado $\ge 700$ (escala de 0 a 1000).

### 3.2 UniProtKB & ESM-2 (Meta AI) — *Protein Language Model Embeddings*
* **Propósito:** Asignar a cada nodo (proteína) un vector de características inicial $x_i \in \mathbb{R}^{d}$ que resuma su química, plegamiento 3D y conservación evolutiva.
* **Modelo Utilizado:** `ESM-2` (`esm2_t30_150M_UR50D` o `esm2_t33_650M_UR50D`). Este modelo de aprendizaje profundo lee la secuencia aminoacídica de la proteína (ej. `MTEYKLVVVG...`) como si fuera un lenguaje natural y genera una representación numérica densa de dimensión $d=640$.

### 3.3 Connectivity Map (CMap / CLUE.io L1000) — *Gene Expression Signatures*
* **Propósito:** Obtener las Firmas de Expresión (FEs) provocadas por perturbaciones.
* **Estructura de Datos:** Un vector $\mathbf{z} \in \mathbb{R}^{978}$ de $z$-scores normalizados para los 978 genes *landmark* (hitos).
  * $z_i > 0$: El gen $i$ está **sobreexpresado** (aumentó su producción de ARN).
  * $z_i < 0$: El gen $i$ está **subexpresado** (reprimido o knockeado).
* **Firmas de Referencia:** Knockout genético mediante CRISPR (ej. eliminación del gen *BRAF* en líneas celulares de melanoma).

### 3.4 COCONUT — *COlleCtion of Open Natural ProdUcTs*
* **Propósito:** Base de datos abierta con más de 400.000 estructuras de productos naturales (metabolitos secundarios de plantas etnomedicinales, hongos, etc.). Se cruza con CMap para seleccionar los fitocompuestos evaluables.

### 3.5 Gene Ontology (GO) — *Ontología Génica y GSEA*
* **Propósito:** Validar qué funciones biológicas (*Biological Processes - BP*) son alteradas por las combinaciones optimizadas de productos naturales mediante análisis de enriquecimiento de conjuntos génicos (GSEA / ORA).

---

## 4. 🧮 FUNDAMENTOS MATEMÁTICOS Y ARQUITECTURA DEL MODELO (GAE)

En esta sección traduciremos el modelo **Graph Autoencoder (GAE)** de Kipf & Welling (2016) a notación matemática pura.

### 4.1 Definición Formal del Grafo
Sea $G = (V, E)$ el interactoma humano.
* Matriz de Adyacencia: $A \in \mathbb{R}^{N \times N}$, donde $A_{ij} = 1$ si existe interacción entre $v_i$ y $v_j$, y $0$ en caso contrario.
* Matriz de Grado: $D \in \mathbb{R}^{N \times N}$ es una matriz diagonal con $D_{ii} = \sum_{j=1}^N A_{ij}$.
* Matriz de Adyacencia Normalizada con Autobucle (Self-loops):
  $$\tilde{A} = A + I_N, \quad \tilde{D}_{ii} = \sum_{j=1}^N \tilde{A}_{ij}$$
  $$\hat{A}_{norm} = \tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2}$$

---

### 4.2 La Capa de Convolución en Grafos (GCN Layer)
A diferencia de una convolución en imágenes (que opera en una grilla regular 2D), la convolución en grafos agrega la información de los **vecinos de un nodo en el grafo**.

La regla de propagación de la capa $l$ a la capa $l+1$ es:
$$H^{(l+1)} = \sigma \left( \hat{A}_{norm} H^{(l)} W^{(l)} \right)$$

Donde:
* $H^{(0)} = X \in \mathbb{R}^{N \times d}$ es la matriz de atributos iniciales (Embeddings ESM-2).
* $W^{(l)} \in \mathbb{R}^{d_l \times d_{l+1}}$ es la **matriz de pesos entrenables** de la red.
* $\sigma(\cdot)$ es una función de activación no lineal (como $\text{ReLU}(x) = \max(0, x)$).

---

### 4.3 Arquitectura del Graph Autoencoder (GAE)

Un Autoencoder de Grafos consta de dos partes principales: **Codificador (Encoder)** y **Decodificador (Decoder)**.

```
       [ ENCODER GCN ]                              [ DECODER (Inner Product) ]
 Matriz de Entrada (X, A)                    Espacio Latente (Z)                      Matriz Reconstruida (Â)
 X ∈ ℝ^{N × 640}          ---> GCN Layer 1 ---> Z ∈ ℝ^{N × 64}  --->  Â = σ(Z · Zᵀ)  ---> Â ∈ ℝ^{N × N}
 A ∈ ℝ^{N × N}                 (Compresión)    (Representación)     (Predicción de bordes)   (Probabilidades)
```

#### A) Codificador (Encoder)
El codificador comprime la información topológica y secuencial a un **Espacio Latente** de baja dimensionalidad $Z \in \mathbb{R}^{N \times d_{latente}}$ (por ejemplo, $d_{latente} = 64$):
$$Z = \text{GCN}_2 \left( \hat{A}_{norm}, \text{ReLU} \left( \hat{A}_{norm} X W^{(0)} \right) W^{(1)} \right)$$

#### B) Decodificador (Decoder)
El decodificador reconstruye la estructura de la red mediante el **producto interno** de las representaciones latentes:
$$\hat{A} = \sigma (Z Z^T)$$
$$\hat{A}_{ij} = \frac{1}{1 + e^{-\mathbf{z}_i \cdot \mathbf{z}_j}}$$

Donde $\hat{A}_{ij} \in [0, 1]$ representa la probabilidad reconstruida de que la proteína $v_i$ e interaccione físicamente con la proteína $v_j$.

#### C) Función de Pérdida (Loss Function)
El modelo se entrena minimizando la entropía cruzada binaria (Binary Cross-Entropy Loss) entre la adyacencia real $A$ y la reconstruida $\hat{A}$:
$$\mathcal{L} = -\frac{1}{N^2} \sum_{i=1}^N \sum_{j=1}^N \left[ A_{ij} \log \hat{A}_{ij} + (1 - A_{ij}) \log (1 - \hat{A}_{ij}) \right]$$

---

## 5. 🔬 ESTRATEGIA METODOLÓGICA: PERTURBACIONES, CRIBADO Y SINERGIA

### 5.1 Modulación Dinámica del Grafo por Perturbaciones ($A_{pert}$)
Cuando una célula es tratada con un compuesto o sufre un knockout de un gen driver, la expresión de sus genes cambia. Esto altera la intensidad de las interacciones físicas.

Modelamos la matriz de adyacencia perturbada $A^{(pert)}$ mediante una modulación probabilística de las aristas basada en las firmas de expresión $\mathbf{z}$:
$$A_{ij}^{(pert)} = A_{ij} \cdot \exp \left( -\alpha |z_i - z_j| \right)$$

Donde $\alpha > 0$ es un hiperparámetro de atenuación. Si dos proteínas interactuantes cambian drásticamente su co-expresión en sentidos opuestos, la fuerza de su arista en el interactoma se debilita.

---

### 5.2 Cuantificación del Desplazamiento en el Espacio Latente ($\Delta H$)
Una vez entrenado el GAE en el estado salvaje (Wild Type, WT), pasamos el grafo perturbado por el Encoder congelado para obtener la matriz latente perturbada $Z_{pert}$.

Definimos el **Vector de Desplazamiento Latente Global ($\Delta H$)**:
$$\Delta H = Z_{pert} - Z_{WT} \in \mathbb{R}^{N \times d_{latente}}$$

Para una condición de referencia de enfermedad/terapéutica (ej. Knockout del gen driver *BRAF*):
$$\Delta H_{ref} = Z_{KO\_BRAF} - Z_{WT}$$

Para un producto natural candidato $k$:
$$\Delta H_{comp\_k} = Z_{compound\_k} - Z_{WT}$$

---

### 5.3 Métrica de Similitud de Coseno en el Espacio Latente
Bajo la hipótesis central de nuestro proyecto: **"Un compuesto con potencial terapéutico debe inducir un perfil de desplazamiento en el espacio latente similar al de la condición de referencia"**.

Medimos la orientación de los vectores de desplazamiento flattenizados $\mathbf{v}_{ref} = \text{vec}(\Delta H_{ref})$ y $\mathbf{v}_{comp} = \text{vec}(\Delta H_{comp})$ mediante la **Similitud Coseno**:

$$\text{Sim}(\Delta H_{ref}, \Delta H_{comp}) = \frac{\mathbf{v}_{ref} \cdot \mathbf{v}_{comp}}{\|\mathbf{v}_{ref}\|_2 \|\mathbf{v}_{comp}\|_2} \in [-1, 1]$$

* Si $\text{Sim} \approx 1$: El compuesto induce un patrón de respuesta latente **altamente análogo** al estado terapéutico deseado.
* Si $\text{Sim} \approx -1$: El compuesto produce un efecto opuesto.

---

### 5.4 Algoritmo de Optimización Combinatoria de Sinergias (Formulaciones de 2 y 3 Productos Naturales)
Los productos naturales suelen actuar mediante mezclas complejas (sinergia multicompuesto).

Para evaluar una formulación combinada de dos productos naturales $(C_a, C_b)$, superponemos sus firmas de expresión ponderadas:
$$\mathbf{z}_{combo(a,b)} = w_a \mathbf{z}_a + w_b \mathbf{z}_b$$

Calculamos la modulación del grafo $A^{(pert\_combo)}$, obtenemos $Z_{combo}$ a través del GAE y evaluamos el score de sinergia latente:

$$S(C_a, C_b) = \text{Sim} \left( \Delta H_{ref}, \Delta H_{combo(a,b)} \right) - \max \left( \text{Sim}(\Delta H_{ref}, \Delta H_a), \text{Sim}(\Delta H_{ref}, \Delta H_b) \right)$$

* Si $S(C_a, C_b) > 0$: La combinación produce un **efecto sinérgico positivo en el espacio latente**, superando a cualquiera de los compuestos por separado.

---

## 6. 🗺️ HOJA DE RUTA DE LOS CUADERNOS DE CÓDIGO (GOOGLE COLAB)

Para acompañar esta base teórica, hemos desarrollado **4 cuadernos interactivos de Jupyter / Google Colab** con código real aplicable a tu plan de trabajo:

```
 📂 2026-classroom/
 ├── 📘 GUIA_TEORICA_Y_FUNDAMENTOS_BECARIA_ANAHI.md (Este documento)
 ├── 📓 01_Plan_Beca_FaCENA_Ingesta_PPI_y_Embeddings_ESM2.ipynb
 ├── 📓 02_Plan_Beca_FaCENA_Integracion_CMap_y_Perturbaciones.ipynb
 ├── 📓 03_Plan_Beca_FaCENA_Modelo_Graph_Autoencoder_GAE.ipynb
 └── 📓 04_Plan_Beca_FaCENA_Cribado_Virtual_y_Optimizacion_Sinergias.ipynb
```

### Resumen de Actividades por Cuaderno:
1. **Cuaderno 01:** Ingesta de la red PPI humana desde STRING API ($score \ge 700$) y extracción de embeddings evolutivos de secuencias UniProt usando el modelo de lenguaje de proteínas `ESM-2` (Meta AI).
2. **Cuaderno 02:** Ingesta y normalización de firmas L1000 de CMap (z-scores), definición de la firma de referencia (CRISPR KO driver) y construcción de matrices de adyacencia dinámicas $A_{pert}$.
3. **Cuaderno 03:** Implementación del modelo Graph Autoencoder (GAE) en `torch_geometric`, bucle de entrenamiento con función de pérdida BCE y proyección de estados latentes perturbados $\Delta H$.
4. **Cuaderno 04:** Virtual Screening masivo sobre quimioteca de productos naturales (COCONUT), optimización combinatoria de sinergias de 2 y 3 compuestos, y enriquecimiento funcional de vías biológicas (Gene Ontology / GSEA).

---

> **Mensaje de Tus Directores (Dirección de Investigación):**  
> *"Anahí, tu perspectiva matemática es tu mayor fortaleza. No te abrumes por los términos biológicos o la sintaxis de Python: cada concepto de este plan tiene una contraparte clara en el álgebra lineal y la teoría de grafos. ¡Estamos listos para hacer ciencia de vanguardia juntos!"*

---
`[VINCIT_OMNIA_VERITAS]`
