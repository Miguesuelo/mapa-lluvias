# Lluvia Bogotá en vivo

Mapa de lluvias de Bogotá en tiempo real con tu ubicación GPS precisa.

- **Pluviómetros del SAB (IDIGER):** 69 estaciones, acumulado del día y lectura actual, cada minuto.
- **Radar del SAB:** imagen de reflectividad sobre el mapa (requiere `servidor.py` o el proxy `worker.js`).
- **Tu ubicación:** localidad, estación más cercana y pronóstico de 2 horas (Open‑Meteo).

## Uso

- **En línea:** abre la página de GitHub Pages de este repositorio.
- **En el computador, con radar:** `python3 servidor.py` y abre http://localhost:8000.
- **Radar en el celular:** publica `worker.js` como Cloudflare Worker y pega su URL en *Capas → Configurar radar*.

Datos: [Sistema de Alerta de Bogotá](https://app.sab.gov.co/sab/lluvias.htm). Esta herramienta no es oficial.
