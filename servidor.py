#!/usr/bin/env python3
"""Servidor local para "Lluvia Bogotá en vivo".

- Sirve index.html en http://localhost:8000 (el GPS del navegador funciona en localhost).
- Reenvía el radar del SAB en /radar.kmz, porque su servidor no permite leerlo desde otra página.

Uso:  python3 servidor.py        (luego abre http://localhost:8000)
"""
import http.server
import os
import time
import urllib.request

RADAR = "https://evp.sire.gov.co/radar_animate/datos/kml/reflectividad.kmz"
PORT = int(os.environ.get("PORT", "8000"))
_cache = {"t": 0, "data": b""}


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] == "/radar.kmz":
            return self.radar()
        return super().do_GET()

    def radar(self):
        try:
            if time.time() - _cache["t"] > 60:  # como máximo una descarga por minuto
                req = urllib.request.Request(RADAR, headers={"User-Agent": "lluvia-bogota-local"})
                with urllib.request.urlopen(req, timeout=20) as r:
                    _cache["data"] = r.read()
                    _cache["t"] = time.time()
            self.send_response(200)
            self.send_header("Content-Type", "application/vnd.google-earth.kmz")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(_cache["data"])
        except Exception as e:  # noqa: BLE001
            self.send_error(502, f"No se pudo leer el radar: {e}")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Abre http://localhost:{PORT}  (Ctrl+C para salir)")
    http.server.ThreadingHTTPServer(("", PORT), Handler).serve_forever()
