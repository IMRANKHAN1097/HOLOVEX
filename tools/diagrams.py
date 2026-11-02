"""SVG diagrams shared by the consoles (corrected labels: OBJECT beam, sync line)."""
def arrowhead(): return '<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#34d399"/></marker><linearGradient id="gg" x1="0" x2="1"><stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#22d3ee"/></linearGradient></defs>'
def setup(kind):
    if kind=='spray':
        sample='<rect x="505" y="70" width="14" height="30" rx="3" fill="#60a5fa"/><g fill="#93c5fd">'+''.join(f'<circle cx="{512+dx}" cy="{108+dy}" r="{r}"/>' for dx,dy,r in [(-14,10,3),(0,18,4),(14,12,3),(-6,30,5),(8,36,3),(-18,34,2.5),(16,30,2.5),(0,46,2.5)])+'</g>'
        slabel='<text x="512" y="62" text-anchor="middle" class="t">Spray nozzle</text><text x="512" y="165" text-anchor="middle" class="s">droplet field</text>'
        cap='z scanned numerically, 50 to 600 mm'
    else:
        sample='<rect x="480" y="72" width="64" height="76" rx="4" fill="rgba(34,211,238,.18)" stroke="#22d3ee" stroke-width="2"/><rect x="480" y="72" width="64" height="12" fill="rgba(244,114,182,.55)"/><path d="M500 84 C500 110 490 118 496 140 M514 84 C514 104 524 116 518 142 M528 84 C528 100 520 112 532 136" stroke="#f472b6" stroke-width="5" stroke-linecap="round" fill="none" opacity=".75"/>'
        slabel='<text x="512" y="62" text-anchor="middle" class="t">Glass cuvette, 10 mm path</text><text x="512" y="166" text-anchor="middle" class="s">water + IPA plumes</text>'
        cap='z = 45 mm, found empirically'
    return f'''<svg class="dg" viewBox="0 0 1100 470" role="img" aria-label="Optical setup of the off-axis Mach-Zehnder holographic recording">{arrowhead()}
<text x="24" y="30" class="t" style="font-size:16px">Optical setup · transmission Mach–Zehnder, 532 nm</text>
<rect x="24" y="218" width="120" height="54" rx="8" class="box"/><text x="84" y="241" text-anchor="middle" class="t">Laser</text><text x="84" y="259" text-anchor="middle" class="s">532 nm CW DPSS</text>
<path class="beam" d="M144 245 H198"/><path d="M198 227 L222 263" class="mir" style="stroke:var(--acc2)"/><text x="196" y="292" class="t">VBS</text><text x="196" y="308" class="s">variable beam splitter</text>
<path class="beam" d="M210 245 V122" marker-end="url(#ah)"/><path d="M196 122 L224 98" class="mir"/><text x="150" y="104" class="s">M1</text>
<rect x="224" y="108" width="520" height="28" class="bm"/><path class="beam" d="M224 122 H744"/>
<path d="M270 114 L292 122 L270 130 z" class="opt"/><text x="262" y="96" class="s">MO1</text><ellipse cx="340" cy="122" rx="9" ry="22" class="opt"/><text x="326" y="96" class="s">L1</text>
<text x="250" y="160" class="s">expanded, collimated OBJECT beam</text>
{sample}{slabel}
<path d="M730 108 L758 136" class="mir"/><text x="768" y="118" class="s">M2</text><path class="beam" d="M744 136 V232" marker-end="url(#ah)"/>
<path class="beam ref" d="M222 245 H270"/><path d="M276 237 L298 245 L276 253 z" class="opt"/><text x="268" y="224" class="s">MO2</text><ellipse cx="346" cy="245" rx="9" ry="22" class="opt"/><text x="332" y="212" class="s">L2</text>
<rect x="355" y="231" width="380" height="28" class="bm" style="fill:rgba(251,191,36,.16)"/><path class="beam ref" d="M355 245 H728"/><text x="372" y="292" class="s">REFERENCE beam (path folded in the lab to match length)</text>
<rect x="728" y="229" width="32" height="32" class="box hi"/><path d="M730 231 L758 259" stroke="var(--fg)" stroke-width="1.5"/><text x="722" y="284" class="t">CBS</text><text x="690" y="318" class="s">cube beam splitter</text>
<path class="beam" d="M760 245 H836"/><rect x="842" y="233" width="12" height="26" rx="3" class="opt"/><text x="826" y="224" class="s">NDF</text>
<rect x="880" y="205" width="150" height="80" rx="12" class="box" style="stroke:url(#gg)"/><text x="955" y="238" text-anchor="middle" class="t">High-speed camera</text><text x="955" y="256" text-anchor="middle" class="s">Photron FASTCAM SA-Z</text><text x="955" y="272" text-anchor="middle" class="s">1024 × 1024 px</text>
<rect x="905" y="372" width="100" height="50" rx="8" class="box"/><text x="955" y="402" text-anchor="middle" class="t">PC</text>
<path class="wire" d="M935 285 V372"/><text x="860" y="335" class="s">USB data</text><path class="wire" d="M975 285 V372" style="stroke:var(--acc)"/><text x="985" y="335" class="s">sync line</text>
<path class="dim" d="M512 190 V210 H880 V200"/><text x="640" y="202" class="t" style="fill:var(--acc3)">z: sample to sensor</text><text x="640" y="226" class="s" style="display:none"></text><text x="512" y="188" text-anchor="middle" class="s" style="fill:var(--acc3)">{cap}</text>
<text x="24" y="440" class="s">A small tilt between the two beams at the CBS creates the off-axis carrier, so the object term separates from the DC term and the twin image in Fourier space.</text></svg>'''
def pipe(steps, hi=()):
    w=250;h=92;gx=44;out=['<svg class="dg" viewBox="0 0 1180 330" role="img" aria-label="Processing pipeline">'+arrowhead()]
    for i,(t,s1,s2) in enumerate(steps):
        r,c=divmod(i,4);x=20+c*(w+gx);y=24+r*150
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" class="box{" hi" if i in hi else ""}"/><text x="{x+16}" y="{y+34}" class="t">{i+1}. {t}</text><text x="{x+16}" y="{y+58}" class="s">{s1}</text><text x="{x+16}" y="{y+75}" class="s">{s2}</text>')
        if c<3 and i<len(steps)-1: out.append(f'<path class="arr" d="M{x+w+4} {y+h/2} H{x+w+gx-6}" marker-end="url(#ah)"/>')
        if c==3 and i<len(steps)-1: out.append(f'<path class="arr" d="M{x+w/2} {y+h+4} V{y+h+20} H{20+w/2} V{y+150-4}" marker-end="url(#ah)"/>')
    out.append('</svg>');return ''.join(out)
PIPE_MIX=[('Record','Photron, 1024×1024','frames saved as BMP'),('DC removal','subtract mean','removes |R|²+|O|²'),('FFT check','log spectrum','DC and ±1 orders visible'),('Fresnel h','exp[−iπΔx²(k²)/(λz)]','z = 45 mm'),('IFFT','complex field','amplitude and phase'),('Reference','subtract frame 1','phase subtraction'),('Metrics','visibility, RMS, SNR','one row per frame'),('Outputs','120 PNG, MP4, CSV','diagnostic plot')]
PIPE_SPR=[('Record','off-axis hologram','178-frame sequence'),('DC + window','mean removal','Tukey apodisation'),('ASM kernel H','band-limited','pre-computed once'),('Depth stack','50–600 mm','5 mm steps'),('Detect','min-projection','adaptive threshold'),('Focus + shape','Tenengrad','morphology'),('Filter + track','persistence 2 mm','k-d tree'),('Statistics','D32, R–R, bootstrap','velocity, CI')]
PIPE_COMP=[('Target / data','image or measured hologram','what we want to see'),('Forward model','angular spectrum, band-limited','differentiable (PyTorch)'),('Loss','amplitude error, PSNR','plus perceptual terms'),('Optimiser','Gerchberg–Saxton or SGD','Adam on the phase'),('Hologram','phase-only pattern','for an SLM or display'),('Verify','re-propagate, compare','sampling and aliasing checks'),('Close the loop','camera-in-the-loop, learned','sim-to-real gap'),('Use','display, metrology, compression','AR/VR, sprays, cells')]
PIPE_ODAK=[('wavenumber','k = 2π / λ','odak.learn.wave'),('generate_complex_field','amplitude + phase','→ complex field'),('propagate_beam','type: Angular Spectrum','or TR Fresnel, band-limited'),('calculate_amplitude','|field|','intensity = amplitude²'),('gerchberg_saxton','iterative phase retrieval','n_iterations, distance'),('stochastic_gradient_descent','differentiable optimiser','learning_rate, loss'),('save_image','odak.learn.tools','cmin, cmax scaling'),('Your next step','port my ASM pipeline','validate against Odak')]
