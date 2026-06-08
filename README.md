# Sitio web Fluxus — v1

Landing page autocontenida (un solo archivo `index.html`). Stack: HTML5 + Tailwind CSS (CDN) + Vanilla JS. Sin dependencias que instalar.

## Probar localmente
Abre `index.html` en el navegador (doble clic). Para servir como en producción:
```
python -m http.server 8000   # luego abre http://localhost:8000
```

## Publicar (hosting estático gratuito)
Sube esta carpeta a GitHub Pages, Netlify o Cloudflare Pages. No requiere build.

## ÚNICO pendiente de configuración — formulario
El formulario de contacto está listo pero apunta a un endpoint de ejemplo. Mientras no se configure, funciona en "modo demo" (muestra el mensaje de éxito sin enviar).

1. Crea una cuenta en [Formspree](https://formspree.io) o [Web3Forms](https://web3forms.com) (gratis).
2. En `index.html`, busca `action="https://formspree.io/f/TU_ENDPOINT"` y reemplaza por tu endpoint real.
   - Para Web3Forms: cambia el `action` a `https://api.web3forms.com/submit` y agrega un `<input type="hidden" name="access_key" value="TU_KEY">` dentro del `<form>`.

## Notas de marca
- Marca paraguas: **Fluxus**. Producto de cámaras: **Fluxus Analytics** (lema "Inteligencia conectada. Decisiones que transforman.").
- Paleta: azul marino `#0A1D3A`, azul `#2B7FD6`, cian `#22D3EE`, turquesa `#34E0C4`, naranja `#F39200` (uso puntual).
- Las cifras de impacto (30%, 98%, etc.) son **referenciales/ilustrativas** y llevan asterisco con nota al pie. Revisar antes de publicar.

## Por completar a futuro
- Reemplazar el isotipo SVG por el logo oficial (`assets/logo-fluxus.png` ya copiado) si se prefiere el PNG.
- Correo de contacto definitivo (hoy `contacto@fluxusingenieria.com`, placeholder).
- Validar/ajustar el copy con el equipo.
