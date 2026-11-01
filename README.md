# Skills de Lushows para Claude Code

18 skills: 12 de negocios, 3 de diseño y 3 de investigación.

| Grupo | Skills |
|---|---|
| Negocios | `economist_lushows`, `ventas_lushows`, `abogado_lushows`, `contador_lushows`, `ecommerce_lushows`, `dropshipping_lushows`, `mercadolibre_lushows`, `facebook_ads_lushows`, `google_ads_lushows`, `tiktok_ads_lushows`, `SDR_OUTBOUND_LUSHOW`, `Matematicas_lushows` |
| Diseño | `directorcreativo_lushows`, `desingweb-lushows`, `editpro_lushows` |
| Investigación | `engineer_visualopen_lushows`, `Quimico_lushows`, `optimizer_tokens_lushows` |

## Instalar en otro PC (Windows)

**Opción A, sin Git:**
1. En esta página de GitHub: botón verde **Code** → **Download ZIP**.
2. Descomprime el ZIP.
3. En la carpeta descomprimida: clic derecho en un espacio vacío → **Abrir en Terminal** y pega:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\instalar.ps1
   ```

**Opción B, con Git:**
```powershell
git clone https://github.com/Lushows/skills-lushows.git
cd skills-lushows
powershell -ExecutionPolicy Bypass -File .\instalar.ps1
```

Las skills quedan en `%USERPROFILE%\.claude\skills`. Si ya había una con el mismo nombre, la vieja se guarda
en `%USERPROFILE%\.claude\skills-respaldo`. Al terminar, cierra y vuelve a abrir Claude Code.

**Para comprobarlo:** en Claude Code escribe `/` y busca, por ejemplo, `ventas_lushows`.

Algunas herramientas de `Matematicas_lushows` y `Quimico_lushows` usan Python 3. Instálalo si Claude te lo pide.
