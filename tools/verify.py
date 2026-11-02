"""Independent re-computation of every number quoted in the consoles and PDFs."""
import json, math, statistics as st, os
here=os.path.dirname(__file__); ok=True
def chk(name,got,exp,tol):
    global ok; p=abs(got-exp)<=tol; ok&=p
    print(('PASS ' if p else 'FAIL ')+f'{name}: computed {got:.6g}, reference {exp:.6g}')
# --- spray report
bins=[331,1867,706,205,72,35,18,9,1,2]
chk('Table 6.1 total',sum(bins),3246,0)
chk('Bins 1-3 share %',100*sum(bins[:3])/3246,89.4,0.1)
chk('Bins 7-9 count',sum(bins[6:9]),28,0)
chk('Bins 7-9 share %',100*28/3246,0.86,0.01)
chk('Persistence retained %',100*3246/4910,66.1,0.05)
chk('D32 = 6*sumV/sumA',6*1328.65/1763.00,4.5218,5e-5)
t=[2815.6,216.5,2768.9]
chk('Retained mean speed (m/s)',st.mean(t)/1000,1.934,5e-4)
chk('Retained sample SD (m/s)',st.stdev(t)/1000,1.487,5e-4)
raw=[2815.6,14137.6,216.5,2768.9]
chk('Raw mean speed (m/s)',st.mean(raw)/1000,4.98,5e-3)
chk('Raw sample SD (m/s)',st.stdev(raw)/1000,6.22,5e-3)
chk('Velocity error sqrt2*dx/dt (m/s)',math.sqrt(2)*0.1953125e-3/125e-6,2.2,0.02)
chk('Frame-46 displacement (mm)',14137.6*125e-6,1.77,0.01)
chk('Number density (stated params), 1/mm^3',28/(200*200*550),1.273e-6,5e-9)
chk('Reported / expected density',3.125e-6/(28/(200*200*550)),2.456,0.005)
chk('Pixel pitch ratio',0.1953125/0.1240,1.575,0.005)
chk('Sphericity -> perimeter ratio',1/0.272,3.7,0.05)
chk('b/a from e=0.697',math.sqrt(1-0.697**2),0.72,0.005)
# Weber number claimed in the report (0.34) -- recomputed
We=1.2*(1.934)**2*4.5e-3/0.072
print(f'NOTE We recomputed = {We:.3f} (report states 0.34)')
# --- fluid report
lam=532e-9; d=10e-3
chk('Fringe -> dn (1/118,100)',lam/d,5.32e-5,5e-8)
chk('2*pi*d/lambda',2*math.pi*d/lam,118100,20)
chk('Fringes across dn=0.044',0.044*d/lam,827,1)
chk('Diffusion length sqrt(2Dt), D=0.9e-9, t=7 s (mm)',math.sqrt(2*0.9e-9*7)*1e3,0.11,0.01)
chk('Min z for single-FFT chirp, N=1024, dx=20um (mm)',1024*(20e-6)**2/lam*1e3,770,1)
chk('Recon pixel lambda*z/(N dx) at 45 mm (um)',lam*0.045/(1024*20e-6)*1e6,1.17,0.01)
# --- droplet console dataset
D=json.load(open(os.path.join(here,'..','data','spray_droplets.json')))
x=[r['Deq_mm'] for r in D]
print(f'Console dataset: N={len(D)}, frames={len(set(r["frame"] for r in D))}, z unique={sorted(set(r["z_mm"] for r in D))}')
print(f'  D32={6*sum(math.pi/6*v**3 for v in x)/sum(math.pi*v*v for v in x):.4f} mm, mean={st.mean(x):.4f}, median={st.median(x):.4f}')
print('ALL CHECKS PASSED' if ok else 'SOME CHECKS FAILED')
