# prowesstracker
app de seguimiento del mazo izzet

Abrí `index.html` en el navegador (ideal en el celular). No necesita instalación ni servidor.

## Instalar en el celular
1. Activá GitHub Pages: en el repo, **Settings → Pages → Build and deployment → Source: Deploy from a branch**, elegí la rama donde está la app y la carpeta `/ (root)`, y guardá.
2. En un minuto queda en `https://gabrielconforte.github.io/prowesstracker/`.
3. Abrí esa dirección en el celular:
   - **Android (Chrome)**: menú ⋮ → **Agregar a la pantalla principal** / **Instalar app**.
   - **iPhone (Safari)**: botón Compartir → **Agregar a inicio**.
4. Queda un ícono 🔥 que abre la app a pantalla completa. Funciona sin cuenta y guarda la partida en el celular.

## Uso
- **Criaturas**: tocá una criatura para ponerla en el campo (el número indica cuántas hay). Para sacarla, tocá la ✕ de su carta.
- **⚡ Hechizo no-criatura**: dispara el trigger de todas las criaturas a la vez (Swiftspear y Monk +1/+1, Slickshot +2/+0, DRC nada).
- **Prowess** en cada carta: dispara solo esa criatura.
- **+3 / +2 / +1** de fuerza y resistencia: pumps hasta fin de turno.
- **Delirium** (en DRC): pasa a 3/3 con vuelo.
- **Role token** (Monstrous Rage): Monster role, +1/+1 y arrolla. Permanente.
- **Equipar Cori-Steel**: +1/+1, arrolla y prisa. Permanente.
- **🌙 Fin de turno / ☀️ Fin turno rival**: alterna entre tu turno y el del rival. En los dos se limpian prowess, pumps y el contador de hechizos (role, equipo y delirium quedan). Al empezar tu turno siguiente se enderezan tus criaturas y sube el número de turno.
- **⚔️ Atacar** (en cada carta) o **💥 Atacar con todo**: las criaturas que atacan quedan **TAPEADAS** y su fuerza se resta a la vida del rival. Solo en tu turno, y respetando el mareo de invocación: DRC y los Monk no pueden atacar el turno en que entran, salvo que el Monk tenga Cori-Steel (que da prisa). Swiftspear y Slickshot tienen prisa. Tocando "TAPEADA" se endereza a mano.
- **📖 Historial**: eventos agrupados por turno (tuyo y del rival), con la vida perdida de cada lado en ese turno.
- **Vidas**: contador de vida tuyo y del rival (−1 y +1), arranca en 20.
- **💥 Pegar con todo**: resta al rival la fuerza total de tus criaturas. El contador del rival reacciona según el golpe: leve (menos de 5), se sacude (5 a 10), se sacude fuerte (más de 10) o se rompe si es letal.
- **🔄** (arriba a la derecha): nueva partida. Reinicia vidas, turnos, historial y campo; tocalo dos veces para confirmar.
- **↶**: deshacer.
- **🔊 / 🔇**: sonidos (sintetizados en el navegador, sin archivos). La elección queda guardada.
- **Imágenes**: la app busca en [Scryfall](https://scryfall.com) la ilustración de cada criatura (la del Monk sale de la ficha que crea Cori-Steel Cutter) y la guarda en el navegador por 30 días. Tocá la imagen de una carta en el campo para verla completa. Sin conexión se ven los emojis.

El estado se guarda en el navegador.
