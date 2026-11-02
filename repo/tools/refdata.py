"""Researchers and references used in the consoles, each with the reason it was included.
Facts come from the pages listed in `src`. Items marked check=True need confirming on the publisher page."""
PEOPLE = [
 dict(n='Kaan Akşit', a='University College London · Computational Light Laboratory', area='Computer-generated holography, differentiable optics, displays, imaging',
  work='Leads the laboratory behind the Odak toolkit (github.com/kaanaksit/odak, MPL-2.0). Recent work: Complex-Valued Holographic Radiance Fields (ACM TOG 2026) and Complex-Valued 2D Gaussian Representation for CGH (ECCV 2026).',
  why='My two projects reconstruct holograms numerically; his lab optimises and learns them. Odak gives me a tested propagation and optimisation toolkit.', src='complightlab.com/publications'),
 dict(n='Kedar Khare', a='IIT Delhi · Physics', area='Digital holographic microscopy, phase retrieval',
  work='A low-cost digital holographic microscope developed at IIT Delhi was commercialised (press reports). With N. Singh: accurate carrier estimation for single-shot off-axis holography (Opt. Lett. 41, 2016).',
  why='Indian work on exactly my planned Takeda step: choosing the carrier frequency decides the quality of off-axis phase recovery.', src='vidwan.inflibnet.ac.in/profile/70175; Deccan Herald archive'),
 dict(n='Joby Joseph', a='IIT Delhi · Physics', area='Holographic storage, digital holography, 3D display',
  work='With Samsheerali and Khare: single-shot quantitative phase imaging (Opt. Commun. 2014) and a 3D display using near on-axis, phase-only digital holography (Appl. Opt. 2015).',
  why='Links my measurement side (phase imaging) to the display side of the same physics.', src='oeoc.iitd.ac.in faculty page', check=True),
 dict(n='Naveen K. Nishchal', a='IIT Patna · Physics', area='Optical information processing, optical cryptography, digital holography',
  work='Professor at IIT Patna since Dec 2008, PhD IIT Delhi 2005. Author of Optical Cryptosystems (IOP, 2020), which includes phase retrieval with the Gerchberg–Saxton algorithm and digital-holography-based schemes. Program Chair of the Optica Digital Holography and 3D Imaging meeting (2024, 2026); organised a GIAN workshop on digital and dynamic holography (Dec 2022).',
  why='Shows the Gerchberg–Saxton method I demonstrate being used in an Indian research group, and gives a route to Indian workshops and community.', src='iopscience.iop.org book preview; GIAN brochure; optica.org meeting pages'),
 dict(n='Dr. Raj Kumar', a='CSIR–Central Scientific Instruments Organisation (CSIO), Chandigarh', area='Optical holography and metrology',
  work='My internship supervisor: Scientist, Optical Holography, CSIR; Professor, AcSIR (Physics, Optics & Photonics). A 2025 IEEE TIM paper by M. Kumar, L. Pensia, R. Kumar and O. Matoba uses the same camera family (Photron FASTCAM); confirm whether R. Kumar is the same person before citing him.',
  why='He guided both projects, and his group’s high-speed holography with the Photron camera is the direct context of my recordings.', src='my internship certificate; IEEE TIM 74, 5012510'),
 dict(n='Osamu Matoba', a='Kobe University (confirm)', area='Digital holography, 3D information processing',
  work='Co-author of the single-shot double field-of-view high-speed holography paper (IEEE TIM 2025) and of the survey on computational holographic imaging with Frauel, Javidi, Naughton and Tajahuerce.',
  why='Connects my CSIO setup to an international group working on high-speed holography.', src='IEEE TIM 74, 5012510; ethw.org Javidi page', check=True),
 dict(n='Bahram Javidi', a='University of Connecticut · ECE', area='3D imaging, digital holography, biophotonics',
  work='Board of Trustees Distinguished Professor; more than 1,100 publications. Digital holographic microscopy for automated disease identification from blood cells; co-author of a survey on computational holographic imaging.',
  why='A field leader whose reviews cover the whole chain I use: recording, numerical reconstruction, then analysis (classification, statistics).', src='mosis.engr.uconn.edu; ICFO colloquium page; ethw.org'),
 dict(n='Daniel R. Guildenbecher', a='Purdue University (Sandia National Laboratories, 2011–2023)', area='Digital in-line holography for sprays and multiphase flow',
  work='High-speed (20 kHz) digital in-line holography for tracking and sizing fragments (Sandia publication); hybrid method for better transverse position and velocity (with Gao and Chen); 2014 ASME Robert T. Knapp award with Reu, Chen and Gao; 2026 webinar on holography diagnostics for 3D spray drop localization, velocimetry and sizing.',
  why='His work is the closest published match to my spray project: 3D droplet position, size and velocity from holograms. It also explains the biases I should expect in my tracking.', src='sandia.gov publication page; osti.gov ILASS papers; ilass.org webinar'),
 dict(n='Joseph Katz and Jian Sheng', a='Johns Hopkins University (Katz)', area='Holography in fluid mechanics',
  work='Applications of holography in fluid mechanics and particle dynamics, Annu. Rev. Fluid Mech. 42, 531–555 (2010): the standard review cited in my spray report.',
  why='Gives the fluid-mechanics reasons for 3D holographic particle tracking, which my report builds on.', src='my spray report, ref. [4]'),
 dict(n='Etienne Cuche, Pierre Marquet, Christian Depeursinge', a='EPFL, Lausanne', area='Off-axis digital holographic microscopy',
  work='Digital holography for quantitative phase-contrast imaging (Opt. Lett. 24, 291, 1999) and amplitude plus phase microscopy by numerical reconstruction of Fresnel off-axis holograms with phase-aberration correction (Appl. Opt. 38, 6994, 1999).',
  why='The method behind my Fresnel reconstruction and the phase-subtraction idea in the mixing project.', src='infoscience.epfl.ch'),
 dict(n='Gordon Wetzstein and Yifan Peng', a='Stanford University', area='Neural holography, computational displays',
  work='Neural Holography with camera-in-the-loop training (ACM TOG 39(6), 2020): gradient-descent variants for CGH, camera-in-the-loop optimisation and HoloNet, full-colour 1080p holograms in real time, about 30 dB PSNR.',
  why='The method family in my live Demo A, and the idea of using a camera to correct the model matches my measured recordings.', src='research.nvidia.com; computationalimaging.org'),
 dict(n='Wojciech Matusik and Liang Shi', a='MIT CSAIL', area='Learned real-time 3D holography',
  work='Tensor holography (Nature, 2021): a small convolutional network trained on 4,000 image pairs generates 3D holograms in milliseconds. Matusik is also a co-author of the lab’s multi-colour holograms paper.',
  why='Shows learning-based CGH at real-time speed, the direction I list for AI-assisted holography.', src='MIT News; SIGGRAPH 2022 poster references'),
 dict(n='Aydogan Ozcan', a='UCLA', area='Diffractive optical networks, computational microscopy',
  work='Co-author with Akşit of All-optical image denoising using a diffractive visual processor (Light Sci. Appl. 13, 43, 2024).',
  why='Optical computing for denoising is relevant to the speckle in my holograms.', src='complightlab.com/publications'),
 dict(n='Hakan Ürey', a='Koç University', area='Displays, MEMS, holography',
  work='Co-author of learned holographic light transport (Appl. Opt. 2022), realistic defocus blur (IEEE VR 2023), multi-colour holograms (SIGGRAPH Asia 2023) and AutoColor.',
  why='Appears across the lab’s hologram papers I cite, linking learned models to real displays.', src='complightlab.com/publications'),
 dict(n='Kyoji Matsushima and Tomoyoshi Shimobaba', a='Japan', area='Band-limited angular spectrum, fast CGH',
  work='Band-limited angular spectrum method for numerical simulation of free-space propagation in far and near fields (Opt. Express 17, 19662, 2009).',
  why='The aliasing control in my spray pipeline comes from this paper.', src='my spray report, ref. [15]'),
 dict(n='Ulf Schnars and Werner Jüptner', a='Germany', area='Digital holography foundations',
  work='First direct recording of holograms on a CCD with numerical reconstruction (1994); textbook Digital Holography and Wavefront Sensing.',
  why='The origin of the numerical reconstruction I use.', src='my reports, refs. [3]'),
 dict(n='Mitsuo Takeda', a='Japan (original work at the University of Electro-Communications)', area='Fourier-transform fringe analysis',
  work='Fourier-transform method of fringe-pattern analysis for computer-based topography and interferometry (J. Opt. Soc. Am. 72, 156, 1982).',
  why='The off-axis phase recovery I plan for the spray data and show in Demo B.', src='standard reference', check=True),
 dict(n='Grace Kuo', a='Meta Reality Labs Research', area='Holographic displays',
  work='Plenary speaker at the Optica Digital Holography and 3D Imaging meeting 2024: Holographic Displays, Past, Present and Future.',
  why='Shows where the field is heading and how measurement and display holography are converging.', src='optica.org meeting page'),
]
REFS = [
 ('Foundations of holography and diffraction', [
  ('Gabor, D. (1948). A new microscopic principle. <i>Nature</i> 161, 777–778.', 'Origin of holography and the twin-image problem.', True),
  ('Leith, E. N., Upatnieks, J. (1962–1964). Off-axis reference beam holography.', 'Solves the twin image; basis of my off-axis geometry.', True),
  ('Goodman, J. W. (2005). <i>Introduction to Fourier Optics</i>, 3rd ed. Roberts &amp; Company.', 'Diffraction theory used for every propagation formula.', False),
  ('Hariharan, P. (2002). <i>Basics of Holography</i>. Cambridge University Press.', 'Clear introduction for the explanation sections.', False),
  ('Schnars, U., Jüptner, W. (1994). Direct recording of holograms by a CCD target and numerical reconstruction. <i>Appl. Opt.</i> 33, 179–181.', 'Start of digital holography.', True),
  ('Schnars, U., Falldorf, C., Watson, J., Jüptner, W. (2015). <i>Digital Holography and Wavefront Sensing</i>, 2nd ed. Springer.', 'Reference book for reconstruction methods.', False),
  ('Kim, M. K. <i>Digital Holographic Microscopy: Principles, Techniques, and Applications</i>. Springer.', 'Listed in my reports for DHM principles.', True),
  ('Picart, P. (ed.) <i>New Techniques in Digital Holography</i>. Wiley-ISTE.', 'Listed in my reports for advanced techniques.', True)]),
 ('Numerical reconstruction and phase', [
  ('Takeda, M., Ina, H., Kobayashi, S. (1982). <i>J. Opt. Soc. Am.</i> 72, 156–160.', 'Off-axis phase recovery (Demo B).', True),
  ('Cuche, E., Bevilacqua, F., Depeursinge, C. (1999). Digital holography for quantitative phase-contrast imaging. <i>Opt. Lett.</i> 24(5), 291–293. doi:10.1364/OL.24.000291.', 'Off-axis digital holography giving amplitude and quantitative phase.', False),
  ('Cuche, E., Marquet, P., Depeursinge, C. (1999). Simultaneous amplitude-contrast and quantitative phase-contrast microscopy by numerical reconstruction of Fresnel off-axis holograms. <i>Appl. Opt.</i> 38(34), 6994–7001. doi:10.1364/AO.38.006994.', 'Fresnel reconstruction with phase-aberration correction.', False),
  ('Matsushima, K., Shimobaba, T. (2009). Band-limited angular spectrum method. <i>Opt. Express</i> 17, 19662–19673.', 'Band limit used in my spray pipeline.', False),
  ('Marquet, P., Depeursinge, C., Magistretti, P. J. (2014). Review of quantitative phase-digital holographic microscopy. <i>Neurophotonics</i> 1(2), 020901.', 'Review of quantitative phase DHM for transparent samples, like my liquids.', False),
  ('Singh, M., Khare, K. (2016). Accurate efficient carrier estimation for single-shot digital holographic imaging. <i>Opt. Lett.</i> 41, 4871–4874.', 'Carrier estimation for my planned Takeda step.', True),
  ('Samsheerali, P. T., Khare, K., Joseph, J. (2014). Quantitative phase imaging with single shot digital holography. <i>Opt. Commun.</i> 319, 85–89.', 'Single-shot phase imaging from IIT Delhi.', True),
  ('Samsheerali, P. T., Khare, K., Joseph, J. (2015). Three-dimensional display system using near on-axis, phase-only digital holography. <i>Appl. Opt.</i> 54(3), 451–457.', 'Bridge to phase-only display holography.', True)]),
 ('Sprays, particles and fluid mechanics', [
  ('Katz, J., Sheng, J. (2010). Applications of holography in fluid mechanics and particle dynamics. <i>Annu. Rev. Fluid Mech.</i> 42, 531–555.', 'Standard review behind my spray project.', False),
  ('Guildenbecher, D. R., Cooper, M., Sojka, P. E. High-speed (20 kHz) digital in-line holography for transient particle tracking and sizing in multiphase flows. Sandia publication.', 'Fast 3D droplet tracking by holography.', False),
  ('Guildenbecher, D. R., Engvall, L., Gao, J., Grasser, T. W., Reu, P. L., Chen, J. (2014). Digital in-line holography to quantify secondary droplets from the impact of a single drop on a thin film. <i>Exp. Fluids</i>.', 'Hybrid method and droplet quantification.', False),
  ('Chen, Y., Guildenbecher, D. R. (2017). Quantitative, bias-corrected measurements of droplet position, size and velocity with digital in-line holography. ILASS-Americas 29th Annual Conference.', 'Explains biases that affect my velocities.', False),
  ('Kumar, A., Guildenbecher, D., et al. (2019). Automated droplet size distribution measurements using digital inline holography. arXiv:1906.09634.', 'Automated sizing like my pipeline (cited in my report).', True),
  ('Shen, X., Kumar, A., Hong, J., et al. (2024). Visualization and characterization of agricultural sprays using machine learning based digital inline holography. <i>Comput. Electron. Agric.</i> 216, 108486.', 'Machine learning for sprays (cited in my report).', True),
  ('Kumar, M., Pensia, L., Kumar, R., Matoba, O. (2025). Vibration measurement of 3-D objects with single-shot double field-of-view high-speed digital holography. <i>IEEE Trans. Instrum. Meas.</i> 74, 5012510.', 'High-speed holography with the Photron platform at CSIO.', True),
  ('Rosin, P., Rammler, E. (1933). <i>J. Inst. Fuel</i> 7, 29–36; Sauter, J. (1926).', 'Size-distribution and D32 definitions.', True),
  ('Pilch, M., Erdman, C. A. (1987). <i>Int. J. Multiphase Flow</i> 13(6), 741–757; Ohnesorge, W. (1936). <i>ZAMM</i> 16, 355–358.', 'Breakup regimes for Weber and Ohnesorge numbers.', True)]),
 ('Computational and learned holography', [
  ('Gerchberg, R. W., Saxton, W. O. (1972). <i>Optik</i> 35, 237–246.', 'Iterative phase retrieval (Demo A).', True),
  ('Peng, Y., Choi, S., Padmanaban, N., Wetzstein, G. (2020). Neural holography with camera-in-the-loop training. <i>ACM Trans. Graph.</i> 39(6), Article 185. doi:10.1145/3414685.3417802.', 'SGD, camera-in-the-loop and HoloNet.', False),
  ('Shi, L., Li, B., Kim, C., Kellnhofer, P., Matusik, W. (2021). Towards real-time photorealistic 3D holography with deep neural networks. <i>Nature</i>.', 'Real-time learned CGH.', False),
  ('Chakravarthula, P., Peng, Y., Kollin, J., Fuchs, H., Heide, F. (2019). Wirtinger holography for near-eye displays. <i>ACM Trans. Graph.</i> 38(6).', 'Iterative CGH baseline used in comparisons.', False),
  ('Rivenson, Y., Zhang, Y., Günaydın, H., Teng, D., Ozcan, A. (2018). Phase recovery and holographic image reconstruction using deep learning. <i>Light Sci. Appl.</i> 7, 17141.', 'Deep learning for reconstruction (cited in my report).', True),
  ('Ren, Z., Xu, Z., Lam, E. Y. M. (2019). End-to-end deep learning framework for digital holographic reconstruction. <i>Adv. Photonics</i> 1(1), 016004.', 'End-to-end learning (cited in my report).', True),
  ('Frauel, Y., Javidi, B., Matoba, O., Naughton, T. J., Tajahuerce, E. Survey on computational holographic imaging and image processing of 3D objects.', 'Overview of computational holographic imaging.', True),
  ('Nishchal, N. K. (2020). <i>Optical Cryptosystems</i>. IOP Publishing.', 'Phase retrieval and digital-holography-based security.', False)]),
 ('Computational Light Laboratory publications used (from complightlab.com/publications)', [
  ('Zhan, Y., Shin, D.-H., Baek, S.-H., Akşit, K. Complex-Valued Holographic Radiance Fields. <i>ACM Trans. Graph.</i>, 2026 (SIGGRAPH 2026).', 'Complex-valued scene representation for holograms.', False),
  ('Zhan, Y., Gao, X., Quan, L., Akşit, K. Complex-Valued 2D Gaussian Representation for Computer-Generated Holography. <i>ECCV 2026</i>, 557–576. doi:10.1007/978-3-032-37574-2_31.', 'Compact complex Gaussians for CGH.', False),
  ('Wang, H., Zhan, Y., Akşit, K., Qiu, S. Hologram Representation via Quadratic Phase Gaussian Splatting. <i>SIGGRAPH Asia 2026 Technical Communications</i>. doi:10.1145/3829339.3847858.', 'Newest hologram-representation work.', False),
  ('Fan, X., Zhan, Y., Mazumdar, A., Akşit, K. Compressing Double Phase Holograms using 2D Gaussians. <i>Eurographics 2026 Posters</i>. doi:10.2312/egp.20261010.', 'Compression: my frame sequences are large.', False),
  ('Peng, Z., Zhan, Y., Spjut, J., Akşit, K. Assessing Learned Models for Phase-only Hologram Compression. <i>SIGGRAPH 2025 Posters</i>. doi:10.1145/3721250.3742993.', 'Compression benchmark.', False),
  ('Zheng, C., Zhan, Y., Shi, L., Cakmakci, O., Akşit, K. Focal Surface Holographic Light Transport using Learned Spatially Adaptive Convolutions. <i>SIGGRAPH Asia 2024 Technical Communications</i>. doi:10.1145/3681758.3697989.', 'Learned light transport on focal surfaces.', False),
  ('Zhan, Y., Urey, H., Sun, Q., Akşit, K. AutoColor: Learned Light Power Control for Multi-Color Holograms. arXiv:2305.01611.', 'Colour control for holograms.', False),
  ('Kavaklı, K., Shi, L., Urey, H., Matusik, W., Akşit, K. Multi-color Holograms Improve Brightness in Holographic Displays. <i>SIGGRAPH Asia 2023</i>. doi:10.1145/3610548.3618135.', 'Brightness through multi-colour optimisation.', False),
  ('Kavaklı, K., Itoh, Y., Urey, H., Akşit, K. Realistic Defocus Blur for Multiplane Computer-Generated Holography. <i>IEEE VR 2023</i>. arXiv:2205.07030.', 'Multiplane holograms relate to my depth stack.', False),
  ('Akşit, K., Itoh, Y. HoloBeam: Paper-Thin Near-Eye Displays. <i>IEEE VR 2023</i>. arXiv:2212.05057.', 'Display-side use of holography.', False),
  ('Walton, D. R., et al., Akşit, K. Metameric Varifocal Holograms. <i>IEEE VR 2022</i>. arXiv:2110.01981.', 'Perception-guided holograms.', False),
  ('Kavaklı, K., Urey, H., Akşit, K. Learned holographic light transport: invited. <i>Appl. Opt.</i> 61(5), B50–B55 (2022). doi:10.1364/AO.439401.', 'Closes the gap between simulated and captured holograms.', False),
  ('Işıl, Ç., et al., Akşit, K., Ozcan, A. All-optical image denoising using a diffractive visual processor. <i>Light Sci. Appl.</i> 13, 43 (2024). doi:10.1038/s41377-024-01385-6.', 'Optical computing for denoising.', False),
  ('Sahloul, M., Akşit, K., Toy, M. F. All-optical selective target highlighting for augmented reality microscopy. <i>Opt. Continuum</i> 5(8), 2708–2723 (2026). doi:10.1364/OPTCON.606265.', 'SLM phase maps used in microscopy.', False),
  ('Kingshott, O., Antipa, N., Bostan, E., Akşit, K. Unrolled Primal-Dual Networks for Lensless Cameras. <i>Opt. Express</i> (2022).', 'Computational imaging without lenses.', False),
  ('Chen, Z., Doğan, M. D., Spjut, J., Akşit, K. SpecTrack: Learned Multi-Rotation Tracking via Speckle Imaging. <i>SIGGRAPH Asia 2024 Posters</i>. doi:10.1145/3681756.3697875.', 'Uses speckle as a signal, not noise.', False),
  ('Dogan, M. D., et al., Akşit, K., Mueller, S. SensiCut: material-aware laser cutting using speckle sensing and deep learning. <i>UIST 2021</i>.', 'Speckle sensing.', False),
  ('Kavaklı, K., Walton, D. R., Antipa, N., Mantiuk, R., Lanman, D., Akşit, K. Optimizing vision and visuals: lectures on cameras, displays and perception. <i>ACM SIGGRAPH 2022 Courses</i>. doi:10.1145/3532720.3535650.', 'Teaching material for the whole pipeline.', False),
  ('Akşit, K., Kavaklı, K. (2023). Flexible modeling of next-generation displays using a differentiable toolkit. <i>Practical Holography XXXVII</i>, SPIE 12445; Kavaklı, K., Akşit, K. (2022). Introduction to Odak. <i>Frontiers in Optics</i>.', 'Describes the Odak toolkit.', False)]),
]
OTHER_LAB = ['Automatic Lens Placement for Personalized 3D Printed Eyewear (SCF 2026)','Heartian: Physiology-Aware Relightable Gaussian Head Avatar (SIGGRAPH Asia 2026 TC)','Gaussian Image Steganography via Parameter-Domain Keyed Embeddings (SIGGRAPH Asia 2026 TC)','Clustered Codebook Quantization for 2D Gaussian-based Image Compression (SIGGRAPH Posters 2026)','Editing Physiological Signals in Videos Using Latent Representations (CVPR Workshops 2026)','Text-guided Fine-Grained Video Anomaly Understanding (CVPR Workshops 2026)','Learned Display Radiance Fields with Lensless Cameras (SIGGRAPH Asia 2025 TC)','Foveation Improves Payload Capacity in Steganography (SIGGRAPH Asia 2025 Posters)','Learned Single-Pass Multitasking Perceptual Graphics for Immersive Displays (ACM MM 2025)','Efficient Proxy Raytracer for Optical Systems using Implicit Neural Representations (SIGGRAPH 2025 Posters)','ChromaCorrect: Prescription Correction in VR Headsets through Perceptual Guidance (Biomed. Opt. Express 2023)','Metameric Inpainting for Image Warping (IEEE TVCG 2022)','Telelife: the future of remote living (Front. VR 2021)','Beyond blur: ventral metamers for foveated rendering (SIGGRAPH 2021)','Beaming displays (IEEE VR 2021)','Optical gaze tracking with spatially-sparse single-pixel detectors (ISMAR 2020)','Patch scanning displays (Opt. Express 2020)','Near-eye display and tracking technologies for VR and AR (CGF 2019)','Foveated AR (SIGGRAPH 2019)','FocusAR (ISMAR 2018)','Manufacturing application-driven foveated near-eye displays (IEEE VR 2018)','Near-eye varifocal AR display using see-through screens (SIGGRAPH Asia 2017)','Wide field of view varifocal near-eye display using deformable membrane mirrors (IEEE VR 2017)','Gaze-sensing LEDs for head mounted displays (arXiv)','Slim near-eye display using pinhole aperture arrays (Appl. Opt. 2015)','Head-worn mixed reality projection display application (ACE 2014)','Super stereoscopy technique (Opt. Lett. 2014)','Dynamic exit pupil trackers for autostereoscopic displays (Opt. Express 2013)','Multi-view autostereoscopic projection display using rotating screen (Opt. Express 2013)','Portable 3D Laser Projector Using Mixed Polarization Technique (J. Display Technol. 2012)','Heart rate monitoring via remote photoplethysmography (Opt. Express 2010)']
def html_people():
    out=[]
    for p in PEOPLE:
        chk=' <span class="tag">confirm details</span>' if p.get('check') else ''
        out.append(f'<div class="pc"><h3>{p["n"]}{chk}</h3><div class="aff">{p["a"]}</div><p><b>Area:</b> {p["area"]}</p><p>{p["work"]}</p><div class="why"><b>Why I included this:</b> {p["why"]}<br><span class="hint">Source: {p["src"]}</span></div></div>')
    return '<div class="pgrid">'+''.join(out)+'</div>'
def html_refs():
    out=[]
    for g,items in REFS:
        out.append(f'<h3 style="margin:14px 0 8px;font-size:15px;color:var(--acc)">{g}</h3>')
        for c,w,chk in items:
            out.append(f'<div class="rf">{c}{" <span class=\"tag\">verify</span>" if chk else ""}<div class="why"><b>Why:</b> {w}</div></div>')
    out.append('<details class="more"><summary>Other publications from the laboratory (graphics, VR and perception; listed for completeness)</summary><ul>'+''.join(f'<li>{t}</li>' for t in OTHER_LAB)+'</ul></details>')
    out.append('<p class="hint">“Verify” marks details I took from my reports or standard knowledge: confirm volume, pages and DOI on the publisher page before citing. Items without the tag were checked against a library record, the publisher or the laboratory’s own list.</p>')
    return ''.join(out)
