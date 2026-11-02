"""Rebuild the three HTML files from the templates. Run: python3 tools/build.py"""
import base64, html, io, json, os, sys
from PIL import Image
root = os.path.join(os.path.dirname(__file__), '..')
rd = lambda p: open(os.path.join(root, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(root, p), 'w', encoding='utf-8').write(s)
def img(path, mx):
    im = Image.open(os.path.join(root, 'assets', path)).convert('RGB')
    if im.width > mx: im = im.resize((mx, int(im.height * mx / im.width)))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=82)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
sys.path.insert(0, os.path.join(root, 'tools')); import diagrams
css = rd('tools/shared.css')
d = json.load(open(os.path.join(root, 'data', 'spray_droplets.json')))
for r in d: r['orientation_deg'] = round(r['orientation_deg'], 2)
sp_t = rd('tools/spray_template.html').replace('/*__CSS__*/', css).replace('__SETUP__', diagrams.setup('spray')).replace('__PIPE__', diagrams.pipe(diagrams.PIPE_SPR, hi=(2,)))
wr('spray_console.html', sp_t.replace('__DATA__', json.dumps(d, separators=(',', ':'))))
m = rd('tools/mixing_template.html').replace('/*__CSS__*/', css).replace('__SETUP__', diagrams.setup('mixing')).replace('__PIPE__', diagrams.pipe(diagrams.PIPE_MIX, hi=(3,)))
for tok, f, w in [('__RAW__','fluid_raw.png',500),('__REC__','fluid_recon.png',500),('__IMG_FFT__','pp_s8_17.png',1100),('__IMG_PS__','pp_s10_22.png',560),('__IMG_DYN__','pp_s10_23.png',820),('__IMG_CSV__','pp_s10_24.jpg',560),('__IMG_FILES__','pp_s10_21.jpg',560),('__IMG_CFG__','pp_s4_4.jpg',320),('__IMG_SET__','pp_s5_7.jpg',520),('__IMG_REC2__','pp_s6_13.jpg',460)]:
    m = m.replace(tok, img(f, w))
wr('mixing_console.html', m)

import refdata
c = rd('tools/comp_template.html').replace('/*__CSS__*/', css).replace('__PEOPLE__', refdata.html_people()).replace('__REFS__', refdata.html_refs())
for tok, v in [('__SETUP_MIX2__', diagrams.setup('mixing')), ('__SETUP_SPR2__', diagrams.setup('spray'))]: c = c.replace(tok, v)
c = c.replace('__SETUP_MIX__', diagrams.setup('mixing')).replace('__SETUP_SPR__', diagrams.setup('spray')).replace('__PIPE_COMP__', diagrams.pipe(diagrams.PIPE_COMP, hi=(1,3))).replace('__PIPE_ODAK__', diagrams.pipe(diagrams.PIPE_ODAK, hi=(4,5))).replace('__PIPE_MIX__', diagrams.pipe(diagrams.PIPE_MIX, hi=(3,))).replace('__PIPE_SPR__', diagrams.pipe(diagrams.PIPE_SPR, hi=(2,)))
for tok, f, w in [('__IMG_FFT__','pp_s8_17.png',900),('__IMG_DYN__','pp_s10_23.png',760),('__IMG_SIX__','sixpanel.png',900)]:
    c = c.replace(tok, img(f, w))
wr('computational_console.html', c)
wr('internship_console.html', rd('tools/profile_template.html').replace('/*__CSS__*/', css))
THEME = '<script>' + rd('tools/theme.js') + '</script>'
for f in ['spray_console.html','mixing_console.html','computational_console.html','internship_console.html']:
    s = rd(f)
    if THEME not in s: wr(f, s.replace('</body>', THEME + '</body>'))
sp, mx, cc, pf = rd('spray_console.html'), rd('mixing_console.html'), rd('computational_console.html'), rd('internship_console.html')
q = lambda s: html.escape(s, quote=True)
index_css = css
index_html = '''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><link rel="icon" type="image/svg+xml" href="assets/holovex-logo.svg">
<meta name="theme-color" content="#071629">
<title>HOLOVEX — Research &amp; Innovation Lab</title>
<style>/*__CSS__*/
body{display:flex;flex-direction:column;height:100vh}
nav{display:flex;gap:8px;align-items:center;padding:10px 120px 10px 14px;background:var(--panel);backdrop-filter:blur(14px);border-bottom:1px solid var(--line);flex-wrap:wrap}
.hvx-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  margin-right: 15px;
}

.hvx-brand img {
  width: 46px;
  height: 46px;
  filter: drop-shadow(0 0 12px #00c8f0);
}

.hvx-brand span {
  display: flex;
  flex-direction: column;
}

.hvx-brand strong {
  color: var(--fg);
  font-size: 21px;
  letter-spacing: 4px;
}

.hvx-brand small {
  color: var(--mut);
  font-size: 9px;
  letter-spacing: 2px;
  margin-top: 4px;
}
nav button{width:auto;margin:0;border-radius:999px;padding:8px 16px}
nav button.on{background:linear-gradient(90deg,var(--acc2),var(--acc));color:#fff;border-color:transparent;font-weight:700}
iframe{flex:1;border:0;width:100%;background:transparent}</style></head>
<body><nav><a class="hvx-brand" href="index.html">
  <img src="assets/holovex-logo.svg" alt="HOLOVEX Logo">
  <span>
    <strong>HOLOVEX</strong>
    <small>RESEARCH &amp; INNOVATION LAB</small>
  </span>
</a><button id="b0" class="on">Internship &amp; research</button><button id="b1">Project 1 · Liquid mixing</button><button id="b2">Project 2 · Spray droplets</button><button id="b3">Computational holography</button></nav>
<iframe id="f0" srcdoc="__F0__"></iframe><iframe id="f1" srcdoc="__F1__" style="display:none"></iframe><iframe id="f2" srcdoc="__F2__" style="display:none"></iframe><iframe id="f3" srcdoc="__F3__" style="display:none"></iframe>
<script>[0,1,2,3].forEach(function(i){document.getElementById('b'+i).onclick=function(){[0,1,2,3].forEach(function(j){document.getElementById('f'+j).style.display=i===j?'block':'none';document.getElementById('b'+j).className=i===j?'on':''});window.dispatchEvent(new Event('resize'))}})</script>
__THEME__</body></html>'''
index_html = index_html.replace('/*__CSS__*/', css).replace('__F0__', q(pf)).replace('__F1__', q(mx)).replace('__F2__', q(sp)).replace('__F3__', q(cc)).replace('__THEME__', THEME)
wr('index.html', index_html)
print('built', len(sp), len(mx), len(cc), len(pf))
