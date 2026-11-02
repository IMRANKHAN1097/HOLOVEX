(function(){
var K='hl-theme',PALS={aurora:['#22d3ee','#8b5cf6','#f472b6'],ocean:['#38bdf8','#3b82f6','#22d3ee'],sunset:['#fbbf24','#fb7185','#f97316'],emerald:['#34d399','#10b981','#a3e635'],royal:['#a78bfa','#6366f1','#f0abfc'],mono:['#cbd5e1','#94a3b8','#e2e8f0']},
FONTS={sans:'Inter,-apple-system,Segoe UI,Roboto,Arial,sans-serif',serif:'Georgia,"Times New Roman",serif',mono:'ui-monospace,SFMono-Regular,Menlo,Consolas,monospace'},
st={mode:'auto',pal:'aurora',font:'sans',size:100};
try{var s=JSON.parse(localStorage.getItem(K)||'null');if(s)st=Object.assign(st,s)}catch(e){}
var R=document.documentElement,emb=window.parent!==window;
function apply(x,fromParent){if(x)st=Object.assign(st,x);if(st.mode==='auto')R.removeAttribute('data-theme');else R.setAttribute('data-theme',st.mode);
var p=PALS[st.pal]||PALS.aurora;R.style.setProperty('--p1',p[0]);R.style.setProperty('--p2',p[1]);R.style.setProperty('--p3',p[2]);R.style.setProperty('--font',FONTS[st.font]||FONTS.sans);document.body.style.zoom=st.size/100;
if(!fromParent){try{localStorage.setItem(K,JSON.stringify(st))}catch(e){}}
mark();window.dispatchEvent(new Event('themechange'));if(!emb)document.querySelectorAll('iframe').forEach(function(f){try{f.contentWindow.postMessage({hl:'theme',state:st},'*')}catch(e){}})}
var pan;function mark(){if(!pan)return;pan.querySelectorAll('[data-k]').forEach(function(b){b.classList.toggle('on',String(st[b.dataset.k])===b.dataset.v)})}
function build(){var b=document.createElement('button');b.className='thm-btn';b.textContent='🎨 Theme';b.setAttribute('aria-label','Theme settings');pan=document.createElement('div');pan.className='thm-pan';
var h='<h4>Mode</h4><div class="thm-row">'+['auto','light','dark'].map(function(m){return '<button data-k="mode" data-v="'+m+'">'+m[0].toUpperCase()+m.slice(1)+'</button>'}).join('')+'</div><h4>Colours</h4><div class="thm-row">'+Object.keys(PALS).map(function(k){var c=PALS[k];return '<button class="sw" title="'+k+'" data-k="pal" data-v="'+k+'" style="background:linear-gradient(135deg,'+c[0]+','+c[1]+' 55%,'+c[2]+')"></button>'}).join('')+'</div><h4>Font</h4><div class="thm-row">'+['sans','serif','mono'].map(function(m){return '<button data-k="font" data-v="'+m+'">'+m+'</button>'}).join('')+'</div><h4>Text size</h4><div class="thm-row">'+[90,100,115].map(function(m){return '<button data-k="size" data-v="'+m+'">'+(m==90?'A−':m==100?'A':'A+')+'</button>'}).join('')+'</div>';
pan.innerHTML=h;document.body.appendChild(b);document.body.appendChild(pan);b.onclick=function(){pan.classList.toggle('on')};
pan.addEventListener('click',function(e){var t=e.target.closest('[data-k]');if(!t)return;var o={};o[t.dataset.k]=t.dataset.k==='size'?+t.dataset.v:t.dataset.v;apply(o)})}
window.addEventListener('message',function(e){if(e.data&&e.data.hl==='theme')apply(e.data.state,true)});
function go(){if(!emb)build();apply();if(!emb)document.querySelectorAll('iframe').forEach(function(f){f.addEventListener('load',function(){f.contentWindow.postMessage({hl:'theme',state:st},'*')})})}
if(document.body)go();else document.addEventListener('DOMContentLoaded',go);
})();
