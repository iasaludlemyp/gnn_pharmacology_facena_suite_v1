from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="GNN Pharmacology FaCENA UNNE - API",
    version="1.0.0",
    description="Sistema de Ingesta PPI, Embeddings ESM-2, Modulación CMap y Graph Autoencoders (GAE) para Farmacología Oncológica"
)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GNN Pharmacology FaCENA UNNE | Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #0D0F17;
            --card-bg: #161926;
            --primary: #1E40AF;
            --accent: #00A896;
            --text: #F3F4F6;
            --text-dim: #9CA3AF;
        }
        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 20px;
        }
        .card {
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 40px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        }
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(0, 168, 150, 0.15);
            color: #2DD4BF;
            padding: 6px 14px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 20px;
        }
        .dot {
            width: 8px;
            height: 8px;
            background: #2DD4BF;
            border-radius: 50%;
            box-shadow: 0 0 10px #2DD4BF;
        }
        h1 {
            font-size: 24px;
            margin: 0 0 10px 0;
            color: #FFF;
        }
        p {
            color: var(--text-dim);
            line-height: 1.6;
            font-size: 15px;
            margin-bottom: 30px;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 30px;
        }
        .btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 12px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.2s ease;
        }
        .btn-primary {
            background: linear-gradient(135deg, var(--primary), #1D4ED8);
            color: white;
        }
        .btn-secondary {
            background: rgba(255, 255, 255, 0.05);
            color: var(--text);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .btn:hover {
            transform: translateY(-2px);
            opacity: 0.9;
        }
        .footer {
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 20px;
            font-size: 13px;
            color: var(--text-dim);
            display: flex;
            justify-content: space-between;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge"><div class="dot"></div> SISTEMA ACTIVO (FaCENA UNNE)</div>
        <h1>GNN Natural Products Pharmacology Suite</h1>
        <p>Servicio biomédico de procesamiento de redes PPI, embeddings ESM-2 y modulación CMap para la beca FaCENA UNNE.</p>
        
        <div class="grid">
            <a href="/docs" class="btn btn-primary">📖 Probar API (/docs)</a>
            <a href="/health" class="btn btn-secondary">🩺 Estado (/health)</a>
        </div>
        
        <div class="footer">
            <span>Directores: <strong>Dr. Emilio Angelina & Dirección del Proyecto</strong></span>
            <span>Becaria: <strong>Anahí Ayelén Espinoza</strong></span>
        </div>
    </div>
</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
def root_dashboard():
    return HTML_TEMPLATE

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "gnn-pharmacology-facena-suite",
        "directors": "Dr. Emilio Angelina & Prof. FaCENA UNNE",
        "becaria": "Anahi Ayelen Espinoza",
        "institution": "FaCENA - UNNE"
    }

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": "Ocurrió un error interno en el servicio."}
    )
