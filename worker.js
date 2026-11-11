// Cloudflare Worker (gratis) para usar el radar del SAB desde el celular o desde GitHub Pages.
// 1. https://dash.cloudflare.com → Workers & Pages → Create → "Hello World" → Edit code.
// 2. Pega este archivo, pulsa Deploy y copia la URL (https://<nombre>.<cuenta>.workers.dev).
// 3. En la herramienta: Capas → Configurar radar → pega la URL → Guardar.
const RADAR = "https://evp.sire.gov.co/radar_animate/datos/kml/reflectividad.kmz";

export default {
  async fetch() {
    const r = await fetch(RADAR, { cf: { cacheTtl: 60, cacheEverything: true } });
    return new Response(r.body, {
      status: r.status,
      headers: {
        "Content-Type": "application/vnd.google-earth.kmz",
        "Cache-Control": "no-store",
        "Access-Control-Allow-Origin": "*",
      },
    });
  },
};
