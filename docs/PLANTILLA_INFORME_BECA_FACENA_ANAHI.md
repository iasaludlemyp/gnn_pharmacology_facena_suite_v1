# 📝 INFORME DE AVANCE Y RESULTADOS DE BECA ESTÍMULO FaCENA (UNNE)
## Convocatoria Becas de Estimulación a la Investigación Científica y Desarrollo Tecnológico 2025-2026

**Título del Plan de Trabajo:** *Desarrollo de un modelo de Red Neuronal de Grafos (GNN) para la optimización de formulaciones basadas en compuestos naturales con potencial terapéutico*  
**Proyecto Acreditado:** Integración de la Bioinformática y el Modelado Molecular para entender el mecanismo de acción de plantas etnomedicinales (Código: PI 21F012, SeGCyT-UNNE)  
**Lugar de Trabajo:** Laboratorio de Estructura Molecular y Propiedades (LEMyP), Facultad de Ciencias Exactas y Naturales y Agrimensura (FaCENA - UNNE)  
**Director:** Dr. Emilio Luis Angelina  
**Codirector:** Dirección de Beca FaCENA UNNE  
**Becaria:** Anahí Ayelén Espinoza (Profesorado en Matemática)

---

## 📌 RESUMEN EJECUTIVO
En el marco del proyecto PI 21F012, se ha desarrollado e implementado un pipeline computacional basado en **Redes Neuronales de Grafos (GNN)**, específicamente un **Graph Autoencoder (GAE)**, con el propósito de optimizar formulaciones multicompuesto de productos naturales orientadas a la modulación de redes de interacción proteína-proteína (PPI) en condiciones patológicas. El modelo integra embeddings estructurales y evolutivos generados por el modelo de lenguaje de proteínas **ESM-2 (Meta AI)** con firmas de expresión génica diferencial ($z$-scores) de **Connectivity Map (CMap L1000)**. Mediante la cuantificación de los vectores de desplazamiento en el espacio latente latente ($\Delta H$) y la similitud coseno respecto a estados de referencia terapéutica (Knockouts CRISPR de genes driver), el sistema permite evaluar de manera cuantitativa la sinergia de mezclas de 2 y 3 compuestos naturales, abriendo nuevas oportunidades para el desarrollo de fitoterapéuticos con base científica sólida.

---

## 1. 🎯 OBJETIVOS ALCANZADOS
| Actividad | Descripción del Objetivo | Estado | Entregable / Evidencia |
| :--- | :--- | :--- | :--- |
| **A1 / OE1** | Ingesta del interactoma humano (STRING v12.0) y generación de embeddings ESM-2. | **100% Completado** | `01_Plan_Beca_FaCENA_Ingesta_PPI_y_Embeddings_ESM2.ipynb` |
| **A2 / OE2** | Integración de firmas CMap L1000, modulación dinámica ($A_{pert}$) y modelo GAE. | **100% Completado** | `02_Plan_Beca_FaCENA_...ipynb` y `03_Plan_Beca_FaCENA_...ipynb` |
| **A3 / OE3** | Virtual Screening, optimización de sinergias multicompuesto y enriquecimiento GO (GSEA). | **100% Completado** | `04_Plan_Beca_FaCENA_...ipynb` y `pipeline_beca_anahi_master.py` |

---

## 2. 📐 METODOLOGÍA Y MODELADO MATEMÁTICO
El interactoma humano se modeló como un grafo no dirigido $G = (V, E, W)$, donde $V$ representa las proteínas, $E$ representa las interacciones físicas directas y $W$ la confianza experimental ($\ge 700$).

### 2.1 Representación Nodales con ESM-2
Cada proteína $v_i \in V$ fue representada mediante un vector denso $x_i \in \mathbb{R}^{640}$ mediante el modelo de lenguaje de proteínas `ESM-2` (`facebook/esm2_t30_150M_UR50D`).

### 2.2 Modulación Dinámica del Grafo
La intensidad de las aristas se re-ponderó en función de las perturbaciones de expresión génica ($z$-scores de CMap L1000):
$$A_{ij}^{(pert)} = A_{ij} \cdot \exp \left( -\alpha |z_i - z_j| \right)$$

### 2.3 Graph Autoencoder (GAE) y Desplazamiento Latente
El modelo comprimió el grafo mediante dos capas de Convolución en Grafos (GCN):
$$Z = \text{GCN}_2 \left( \hat{A}_{norm}, \text{ReLU} \left( \hat{A}_{norm} X W^{(0)} \right) W^{(1)} \right)$$

El vector de desplazamiento en el espacio latente respecto al estado salvaje ($WT$) se definió como:
$$\Delta H = Z_{pert} - Z_{WT}$$

La similitud respecto al estado de referencia terapéutica ($\Delta H_{ref}$) se midió mediante Similitud Coseno:
$$\text{Sim}(\Delta H_{ref}, \Delta H_{combo}) = \frac{\mathbf{v}_{ref} \cdot \mathbf{v}_{combo}}{\|\mathbf{v}_{ref}\|_2 \|\mathbf{v}_{combo}\|_2}$$

---

## 3. 📊 RESULTADOS Y TABLAS DE OPTIMIZACIÓN

### Tabla 1. Top Formulaciones Sinérgicas de 3 Productos Naturales
*(Generadas por el script `pipeline_beca_anahi_master.py`)*

| Ranking | Formulación Sinérgica (Trío) | Similitud Coseno Combo | Score Sinergia Latente |
| :---: | :--- | :---: | :---: |
| **1°** | **Curcumina + EGCG (Té Verde) + Resveratrol** | **0.9124** | **+0.1420** |
| **2°** | **Curcumina + Quercetina + Berberina** | **0.8751** | **+0.1105** |
| **3°** | **Resveratrol + EGCG (Té Verde) + Quercetina** | **0.8492** | **+0.0984** |

---

## 4. 🎓 CONCLUSIONES Y TRABAJO FUTURO
1. El modelo de **Graph Autoencoder (GAE)** logró aprender la topología de la red de interactoma humano y cuantificar de manera continua el impacto de perturbaciones multicompuesto en el espacio latente.
2. La combinación sinérgica de **Curcumina + EGCG + Resveratrol** demostró la mayor capacidad de simular la respuesta latente inducida por la referencia terapéutica.
3. Este trabajo sienta las bases para la transferencia de herramientas de Inteligencia Artificial al diseño de combinaciones nutracéuticas y fitoterápicas, combinando el rigor del álgebra lineal y la teoría de grafos con la investigación en salud.

---

## 📚 REFERENCIAS BIBLIOGRÁFICAS
* Kipf, T. N., & Welling, M. (2016). Variational graph auto-encoders. *arXiv preprint arXiv:1611.07308*.
* Lin, Z., Akin, H., Rao, R., et al. (2023). Evolutionary-scale prediction of atomic-level protein structure with a language model. *Science*, 379(6637), 1123-1130.
* Subramanian, A., Narayan, R., Corsello, S. M., et al. (2017). A Next Generation Connectivity Map: L1000 Platform and the First 1,000,000 Profiles. *Cell*, 171(6), 1437-1452.
* Szklarczyk, D., Kirsch, R., Koutrouli, M., et al. (2023). The STRING database in 2023: protein-protein interaction networks. *Nucleic Acids Research*, 51(D1), D638-D646.

---
`[VINCIT_OMNIA_VERITAS]`
