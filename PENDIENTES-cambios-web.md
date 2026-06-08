# Cambios pendientes para la web de Fluxus

> Lista de trabajo. NO ejecutar hasta tener todo definido y confirmado por Rodrigo.
> La publicación en GitHub/indexación queda en pausa hasta aplicar estos cambios.

## A. Estructura
1. **Estructura híbrida** (en vez de una sola página larga):
   - Home compacto que cuenta la historia (hero, producto bandera, diferenciador, método, resumen de productos, equipo, contacto).
   - El detalle de cada producto vive en **su propia página**, no en el home (evita el scroll infinito y mejora el SEO).
   - El menú "Productos" pasa a ser navegación real (lleva a las páginas de producto). "Inicio", "Quiénes somos" y "Contacto" pueden seguir como anclas del home.

## B. Identidad
2. **Agregar el logo oficial de Fluxus** al inicio, junto a "Fluxus ingeniería" en la barra superior. (Archivo `assets/logo-fluxus.png`; conviene optimizar/reducir su peso para web.) Revisar coherencia del wordmark.

## C. Productos (los 8, cada uno clickeable y con detalle)
3. **Cada producto debe ser un link en sí mismo**: al pincharlo, abre su descripción/página de detalle. Aplica a:
   - Demanda y evasión a bordo
   - Eficiencia de terminales
   - Acceso portuario
   - Afluencia en recintos
   - Estudios de demanda / IMIV
   - Evaluación de infraestructura
   - Logística y comercio exterior
   - Análisis urbano y territorial
4. **Cada producto con un ícono representativo** que lo refleje.
5. **Páginas de detalle por producto**: qué es, qué incluye, para quién, qué lo distingue, CTA. (Contenido extenso aún por redactar — paso ya acordado.)

## D. Recursos visuales (reutilizar lo ya creado para la web)
6. Integrar las láminas/gráficos ya generados, asignando cada uno a su sección o producto:
   - Mapa de buses en vivo (HTML) → demanda de transporte público / bandera.
   - Histograma de demanda y evasión (HTML) → demanda y evasión a bordo.
   - Dashboard de antepuerto ANPR (HTML) → acceso portuario.
   - Ilustración cámara con IA / ANPR (SVG) → sección de tecnología / productos en vivo.
   - Esquema "del dato a la decisión" (SVG) → sección método.
   - Hero "flujo continuo" (PNG/SVG) → hero o sección método.

## E. Contacto / formulario
7. **"Solicitar cotización"**: al enviar la consulta, debe llegar **automáticamente** a los correos de Rodrigo Medina y Rodrigo Valladares, **sin mostrar esos correos en la página** (no exponerlos públicamente).
   - Implica: usar un backend de formulario (Web3Forms/Formspree) configurado para enviar a ambos destinatarios; quitar los correos visibles de la sección de contacto y del pie de página.

## F. Contenido del detalle de productos (fuente: presentaciones)
8. Al redactar el detalle de cada producto, **usar la información de las presentaciones comerciales** (`Presentaciones clientes/Fluxus_Interurbano.pptx`, `Fluxus_Urbano_NoRegulado.pptx`, `Fluxus_Urbano_Regulado.pptx`), donde ya están identificados los dolores por segmento.
9. **Demanda y evasión a bordo — dolores a incorporar** (según Rodrigo / presentaciones):
   - Evasión en interurbanos y también en urbanos con prepago por tarjeta que no todos validan.
   - En interurbanos, frecuentes **pagos informales**.
   - Incluso el transporte público urbano **regulado** carece de información de la demanda que concentra actualmente.
   - En los **no regulados**, esa falta de información es un impedimento para **postular a créditos** e incluso para la **regulación** por parte del Ministerio de Transporte.

## G. Medición de demanda de transporte público (potenciar la analítica)
10. **Potenciar la dimensión analítica**, no solo el dashboard en vivo. Mostrar que Fluxus explica **dónde ocurre la demanda, dónde se generan viajes y dónde se atraen viajes**.
    - Crear una **figura esquemática, probablemente territorial** (zonas de generación/atracción de viajes), en HTML o apoyándose en Canvas si es posible. Mejorar la figura actual (que hoy solo insinúa "información en vivo").
11. **Explicación tecnológica + fotos del producto**:
    - Agregar **fotos del producto tecnológico**: una **cámara binocular con inteligencia artificial que se instala en la puerta de los buses**. (Falta conseguir las fotos — pendiente de Rodrigo o banco.)
    - Explicar **por qué es una herramienta distintiva**, con capacidades distintas a lo que existe hoy en el mercado, **sin entrar en marca ni especificaciones**.

## H. (continúa…)
- Rodrigo seguirá agregando cambios.
- Pendiente aclarar: "Margarita Bermientes" mencionado al inicio de un audio (¿nombre/dato a incorporar? — confirmar).

---

### Pendientes técnicos ya conocidos (de antes)
- Formulario: pegar clave de Web3Forms (hoy funciona con fallback a mailto a rmedina@ y rvalladares@fluxusingenieria.com).
- Dominio personalizado fluxusingenieria.com: conectar DNS y reactivar CNAME cuando esté listo (hoy se publicaría en romedinag-tech.github.io/fluxus-web/).
- Página de privacidad / tratamiento de datos (cámaras y ANPR).
- Permiso de dominio de la extensión Claude in Chrome para github.com y dominios de Google (bloqueó la publicación en el último intento).
