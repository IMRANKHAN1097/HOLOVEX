# References and researchers, with the reason each is included

Generated from `tools/refdata.py`. Items marked *verify* need confirming on the publisher page.

## Researchers and groups

### Kaan Akşit
*University College London · Computational Light Laboratory*  
**Area:** Computer-generated holography, differentiable optics, displays, imaging  
Leads the laboratory behind the Odak toolkit (github.com/kaanaksit/odak, MPL-2.0). Recent work: Complex-Valued Holographic Radiance Fields (ACM TOG 2026) and Complex-Valued 2D Gaussian Representation for CGH (ECCV 2026).  
**Why I included this:** My two projects reconstruct holograms numerically; his lab optimises and learns them. Odak gives me a tested propagation and optimisation toolkit.  
Source: complightlab.com/publications

### Kedar Khare
*IIT Delhi · Physics*  
**Area:** Digital holographic microscopy, phase retrieval  
A low-cost digital holographic microscope developed at IIT Delhi was commercialised (press reports). With N. Singh: accurate carrier estimation for single-shot off-axis holography (Opt. Lett. 41, 2016).  
**Why I included this:** Indian work on exactly my planned Takeda step: choosing the carrier frequency decides the quality of off-axis phase recovery.  
Source: vidwan.inflibnet.ac.in/profile/70175; Deccan Herald archive

### Joby Joseph
*IIT Delhi · Physics*  
**Area:** Holographic storage, digital holography, 3D display  
With Samsheerali and Khare: single-shot quantitative phase imaging (Opt. Commun. 2014) and a 3D display using near on-axis, phase-only digital holography (Appl. Opt. 2015).  
**Why I included this:** Links my measurement side (phase imaging) to the display side of the same physics.  
Source: oeoc.iitd.ac.in faculty page

### Naveen K. Nishchal
*IIT Patna · Physics*  
**Area:** Optical information processing, optical cryptography, digital holography  
Professor at IIT Patna since Dec 2008, PhD IIT Delhi 2005. Author of Optical Cryptosystems (IOP, 2020), which includes phase retrieval with the Gerchberg–Saxton algorithm and digital-holography-based schemes. Program Chair of the Optica Digital Holography and 3D Imaging meeting (2024, 2026); organised a GIAN workshop on digital and dynamic holography (Dec 2022).  
**Why I included this:** Shows the Gerchberg–Saxton method I demonstrate being used in an Indian research group, and gives a route to Indian workshops and community.  
Source: iopscience.iop.org book preview; GIAN brochure; optica.org meeting pages

### Dr. Raj Kumar
*CSIR–Central Scientific Instruments Organisation (CSIO), Chandigarh*  
**Area:** Optical holography and metrology  
My internship supervisor: Scientist, Optical Holography, CSIR; Professor, AcSIR (Physics, Optics & Photonics). A 2025 IEEE TIM paper by M. Kumar, L. Pensia, R. Kumar and O. Matoba uses the same camera family (Photron FASTCAM); confirm whether R. Kumar is the same person before citing him.  
**Why I included this:** He guided both projects, and his group’s high-speed holography with the Photron camera is the direct context of my recordings.  
Source: my internship certificate; IEEE TIM 74, 5012510

### Osamu Matoba
*Kobe University (confirm)*  
**Area:** Digital holography, 3D information processing  
Co-author of the single-shot double field-of-view high-speed holography paper (IEEE TIM 2025) and of the survey on computational holographic imaging with Frauel, Javidi, Naughton and Tajahuerce.  
**Why I included this:** Connects my CSIO setup to an international group working on high-speed holography.  
Source: IEEE TIM 74, 5012510; ethw.org Javidi page

### Bahram Javidi
*University of Connecticut · ECE*  
**Area:** 3D imaging, digital holography, biophotonics  
Board of Trustees Distinguished Professor; more than 1,100 publications. Digital holographic microscopy for automated disease identification from blood cells; co-author of a survey on computational holographic imaging.  
**Why I included this:** A field leader whose reviews cover the whole chain I use: recording, numerical reconstruction, then analysis (classification, statistics).  
Source: mosis.engr.uconn.edu; ICFO colloquium page; ethw.org

### Daniel R. Guildenbecher
*Purdue University (Sandia National Laboratories, 2011–2023)*  
**Area:** Digital in-line holography for sprays and multiphase flow  
High-speed (20 kHz) digital in-line holography for tracking and sizing fragments (Sandia publication); hybrid method for better transverse position and velocity (with Gao and Chen); 2014 ASME Robert T. Knapp award with Reu, Chen and Gao; 2026 webinar on holography diagnostics for 3D spray drop localization, velocimetry and sizing.  
**Why I included this:** His work is the closest published match to my spray project: 3D droplet position, size and velocity from holograms. It also explains the biases I should expect in my tracking.  
Source: sandia.gov publication page; osti.gov ILASS papers; ilass.org webinar

### Joseph Katz and Jian Sheng
*Johns Hopkins University (Katz)*  
**Area:** Holography in fluid mechanics  
Applications of holography in fluid mechanics and particle dynamics, Annu. Rev. Fluid Mech. 42, 531–555 (2010): the standard review cited in my spray report.  
**Why I included this:** Gives the fluid-mechanics reasons for 3D holographic particle tracking, which my report builds on.  
Source: my spray report, ref. [4]

### Etienne Cuche, Pierre Marquet, Christian Depeursinge
*EPFL, Lausanne*  
**Area:** Off-axis digital holographic microscopy  
Digital holography for quantitative phase-contrast imaging (Opt. Lett. 24, 291, 1999) and amplitude plus phase microscopy by numerical reconstruction of Fresnel off-axis holograms with phase-aberration correction (Appl. Opt. 38, 6994, 1999).  
**Why I included this:** The method behind my Fresnel reconstruction and the phase-subtraction idea in the mixing project.  
Source: infoscience.epfl.ch

### Gordon Wetzstein and Yifan Peng
*Stanford University*  
**Area:** Neural holography, computational displays  
Neural Holography with camera-in-the-loop training (ACM TOG 39(6), 2020): gradient-descent variants for CGH, camera-in-the-loop optimisation and HoloNet, full-colour 1080p holograms in real time, about 30 dB PSNR.  
**Why I included this:** The method family in my live Demo A, and the idea of using a camera to correct the model matches my measured recordings.  
Source: research.nvidia.com; computationalimaging.org

### Wojciech Matusik and Liang Shi
*MIT CSAIL*  
**Area:** Learned real-time 3D holography  
Tensor holography (Nature, 2021): a small convolutional network trained on 4,000 image pairs generates 3D holograms in milliseconds. Matusik is also a co-author of the lab’s multi-colour holograms paper.  
**Why I included this:** Shows learning-based CGH at real-time speed, the direction I list for AI-assisted holography.  
Source: MIT News; SIGGRAPH 2022 poster references

### Aydogan Ozcan
*UCLA*  
**Area:** Diffractive optical networks, computational microscopy  
Co-author with Akşit of All-optical image denoising using a diffractive visual processor (Light Sci. Appl. 13, 43, 2024).  
**Why I included this:** Optical computing for denoising is relevant to the speckle in my holograms.  
Source: complightlab.com/publications

### Hakan Ürey
*Koç University*  
**Area:** Displays, MEMS, holography  
Co-author of learned holographic light transport (Appl. Opt. 2022), realistic defocus blur (IEEE VR 2023), multi-colour holograms (SIGGRAPH Asia 2023) and AutoColor.  
**Why I included this:** Appears across the lab’s hologram papers I cite, linking learned models to real displays.  
Source: complightlab.com/publications

### Kyoji Matsushima and Tomoyoshi Shimobaba
*Japan*  
**Area:** Band-limited angular spectrum, fast CGH  
Band-limited angular spectrum method for numerical simulation of free-space propagation in far and near fields (Opt. Express 17, 19662, 2009).  
**Why I included this:** The aliasing control in my spray pipeline comes from this paper.  
Source: my spray report, ref. [15]

### Ulf Schnars and Werner Jüptner
*Germany*  
**Area:** Digital holography foundations  
First direct recording of holograms on a CCD with numerical reconstruction (1994); textbook Digital Holography and Wavefront Sensing.  
**Why I included this:** The origin of the numerical reconstruction I use.  
Source: my reports, refs. [3]

### Mitsuo Takeda
*Japan (original work at the University of Electro-Communications)*  
**Area:** Fourier-transform fringe analysis  
Fourier-transform method of fringe-pattern analysis for computer-based topography and interferometry (J. Opt. Soc. Am. 72, 156, 1982).  
**Why I included this:** The off-axis phase recovery I plan for the spray data and show in Demo B.  
Source: standard reference

### Grace Kuo
*Meta Reality Labs Research*  
**Area:** Holographic displays  
Plenary speaker at the Optica Digital Holography and 3D Imaging meeting 2024: Holographic Displays, Past, Present and Future.  
**Why I included this:** Shows where the field is heading and how measurement and display holography are converging.  
Source: optica.org meeting page

## References

### Foundations of holography and diffraction

- Gabor, D. (1948). A new microscopic principle. Nature 161, 777–778. *(verify)*  
  *Why:* Origin of holography and the twin-image problem.
- Leith, E. N., Upatnieks, J. (1962–1964). Off-axis reference beam holography. *(verify)*  
  *Why:* Solves the twin image; basis of my off-axis geometry.
- Goodman, J. W. (2005). Introduction to Fourier Optics, 3rd ed. Roberts & Company.  
  *Why:* Diffraction theory used for every propagation formula.
- Hariharan, P. (2002). Basics of Holography. Cambridge University Press.  
  *Why:* Clear introduction for the explanation sections.
- Schnars, U., Jüptner, W. (1994). Direct recording of holograms by a CCD target and numerical reconstruction. Appl. Opt. 33, 179–181. *(verify)*  
  *Why:* Start of digital holography.
- Schnars, U., Falldorf, C., Watson, J., Jüptner, W. (2015). Digital Holography and Wavefront Sensing, 2nd ed. Springer.  
  *Why:* Reference book for reconstruction methods.
- Kim, M. K. Digital Holographic Microscopy: Principles, Techniques, and Applications. Springer. *(verify)*  
  *Why:* Listed in my reports for DHM principles.
- Picart, P. (ed.) New Techniques in Digital Holography. Wiley-ISTE. *(verify)*  
  *Why:* Listed in my reports for advanced techniques.

### Numerical reconstruction and phase

- Takeda, M., Ina, H., Kobayashi, S. (1982). J. Opt. Soc. Am. 72, 156–160. *(verify)*  
  *Why:* Off-axis phase recovery (Demo B).
- Cuche, E., Bevilacqua, F., Depeursinge, C. (1999). Digital holography for quantitative phase-contrast imaging. Opt. Lett. 24(5), 291–293. doi:10.1364/OL.24.000291.  
  *Why:* Off-axis digital holography giving amplitude and quantitative phase.
- Cuche, E., Marquet, P., Depeursinge, C. (1999). Simultaneous amplitude-contrast and quantitative phase-contrast microscopy by numerical reconstruction of Fresnel off-axis holograms. Appl. Opt. 38(34), 6994–7001. doi:10.1364/AO.38.006994.  
  *Why:* Fresnel reconstruction with phase-aberration correction.
- Matsushima, K., Shimobaba, T. (2009). Band-limited angular spectrum method. Opt. Express 17, 19662–19673.  
  *Why:* Band limit used in my spray pipeline.
- Marquet, P., Depeursinge, C., Magistretti, P. J. (2014). Review of quantitative phase-digital holographic microscopy. Neurophotonics 1(2), 020901.  
  *Why:* Review of quantitative phase DHM for transparent samples, like my liquids.
- Singh, M., Khare, K. (2016). Accurate efficient carrier estimation for single-shot digital holographic imaging. Opt. Lett. 41, 4871–4874. *(verify)*  
  *Why:* Carrier estimation for my planned Takeda step.
- Samsheerali, P. T., Khare, K., Joseph, J. (2014). Quantitative phase imaging with single shot digital holography. Opt. Commun. 319, 85–89. *(verify)*  
  *Why:* Single-shot phase imaging from IIT Delhi.
- Samsheerali, P. T., Khare, K., Joseph, J. (2015). Three-dimensional display system using near on-axis, phase-only digital holography. Appl. Opt. 54(3), 451–457. *(verify)*  
  *Why:* Bridge to phase-only display holography.

### Sprays, particles and fluid mechanics

- Katz, J., Sheng, J. (2010). Applications of holography in fluid mechanics and particle dynamics. Annu. Rev. Fluid Mech. 42, 531–555.  
  *Why:* Standard review behind my spray project.
- Guildenbecher, D. R., Cooper, M., Sojka, P. E. High-speed (20 kHz) digital in-line holography for transient particle tracking and sizing in multiphase flows. Sandia publication.  
  *Why:* Fast 3D droplet tracking by holography.
- Guildenbecher, D. R., Engvall, L., Gao, J., Grasser, T. W., Reu, P. L., Chen, J. (2014). Digital in-line holography to quantify secondary droplets from the impact of a single drop on a thin film. Exp. Fluids.  
  *Why:* Hybrid method and droplet quantification.
- Chen, Y., Guildenbecher, D. R. (2017). Quantitative, bias-corrected measurements of droplet position, size and velocity with digital in-line holography. ILASS-Americas 29th Annual Conference.  
  *Why:* Explains biases that affect my velocities.
- Kumar, A., Guildenbecher, D., et al. (2019). Automated droplet size distribution measurements using digital inline holography. arXiv:1906.09634. *(verify)*  
  *Why:* Automated sizing like my pipeline (cited in my report).
- Shen, X., Kumar, A., Hong, J., et al. (2024). Visualization and characterization of agricultural sprays using machine learning based digital inline holography. Comput. Electron. Agric. 216, 108486. *(verify)*  
  *Why:* Machine learning for sprays (cited in my report).
- Kumar, M., Pensia, L., Kumar, R., Matoba, O. (2025). Vibration measurement of 3-D objects with single-shot double field-of-view high-speed digital holography. IEEE Trans. Instrum. Meas. 74, 5012510. *(verify)*  
  *Why:* High-speed holography with the Photron platform at CSIO.
- Rosin, P., Rammler, E. (1933). J. Inst. Fuel 7, 29–36; Sauter, J. (1926). *(verify)*  
  *Why:* Size-distribution and D32 definitions.
- Pilch, M., Erdman, C. A. (1987). Int. J. Multiphase Flow 13(6), 741–757; Ohnesorge, W. (1936). ZAMM 16, 355–358. *(verify)*  
  *Why:* Breakup regimes for Weber and Ohnesorge numbers.

### Computational and learned holography

- Gerchberg, R. W., Saxton, W. O. (1972). Optik 35, 237–246. *(verify)*  
  *Why:* Iterative phase retrieval (Demo A).
- Peng, Y., Choi, S., Padmanaban, N., Wetzstein, G. (2020). Neural holography with camera-in-the-loop training. ACM Trans. Graph. 39(6), Article 185. doi:10.1145/3414685.3417802.  
  *Why:* SGD, camera-in-the-loop and HoloNet.
- Shi, L., Li, B., Kim, C., Kellnhofer, P., Matusik, W. (2021). Towards real-time photorealistic 3D holography with deep neural networks. Nature.  
  *Why:* Real-time learned CGH.
- Chakravarthula, P., Peng, Y., Kollin, J., Fuchs, H., Heide, F. (2019). Wirtinger holography for near-eye displays. ACM Trans. Graph. 38(6).  
  *Why:* Iterative CGH baseline used in comparisons.
- Rivenson, Y., Zhang, Y., Günaydın, H., Teng, D., Ozcan, A. (2018). Phase recovery and holographic image reconstruction using deep learning. Light Sci. Appl. 7, 17141. *(verify)*  
  *Why:* Deep learning for reconstruction (cited in my report).
- Ren, Z., Xu, Z., Lam, E. Y. M. (2019). End-to-end deep learning framework for digital holographic reconstruction. Adv. Photonics 1(1), 016004. *(verify)*  
  *Why:* End-to-end learning (cited in my report).
- Frauel, Y., Javidi, B., Matoba, O., Naughton, T. J., Tajahuerce, E. Survey on computational holographic imaging and image processing of 3D objects. *(verify)*  
  *Why:* Overview of computational holographic imaging.
- Nishchal, N. K. (2020). Optical Cryptosystems. IOP Publishing.  
  *Why:* Phase retrieval and digital-holography-based security.

### Computational Light Laboratory publications used (from complightlab.com/publications)

- Zhan, Y., Shin, D.-H., Baek, S.-H., Akşit, K. Complex-Valued Holographic Radiance Fields. ACM Trans. Graph., 2026 (SIGGRAPH 2026).  
  *Why:* Complex-valued scene representation for holograms.
- Zhan, Y., Gao, X., Quan, L., Akşit, K. Complex-Valued 2D Gaussian Representation for Computer-Generated Holography. ECCV 2026, 557–576. doi:10.1007/978-3-032-37574-2_31.  
  *Why:* Compact complex Gaussians for CGH.
- Wang, H., Zhan, Y., Akşit, K., Qiu, S. Hologram Representation via Quadratic Phase Gaussian Splatting. SIGGRAPH Asia 2026 Technical Communications. doi:10.1145/3829339.3847858.  
  *Why:* Newest hologram-representation work.
- Fan, X., Zhan, Y., Mazumdar, A., Akşit, K. Compressing Double Phase Holograms using 2D Gaussians. Eurographics 2026 Posters. doi:10.2312/egp.20261010.  
  *Why:* Compression: my frame sequences are large.
- Peng, Z., Zhan, Y., Spjut, J., Akşit, K. Assessing Learned Models for Phase-only Hologram Compression. SIGGRAPH 2025 Posters. doi:10.1145/3721250.3742993.  
  *Why:* Compression benchmark.
- Zheng, C., Zhan, Y., Shi, L., Cakmakci, O., Akşit, K. Focal Surface Holographic Light Transport using Learned Spatially Adaptive Convolutions. SIGGRAPH Asia 2024 Technical Communications. doi:10.1145/3681758.3697989.  
  *Why:* Learned light transport on focal surfaces.
- Zhan, Y., Urey, H., Sun, Q., Akşit, K. AutoColor: Learned Light Power Control for Multi-Color Holograms. arXiv:2305.01611.  
  *Why:* Colour control for holograms.
- Kavaklı, K., Shi, L., Urey, H., Matusik, W., Akşit, K. Multi-color Holograms Improve Brightness in Holographic Displays. SIGGRAPH Asia 2023. doi:10.1145/3610548.3618135.  
  *Why:* Brightness through multi-colour optimisation.
- Kavaklı, K., Itoh, Y., Urey, H., Akşit, K. Realistic Defocus Blur for Multiplane Computer-Generated Holography. IEEE VR 2023. arXiv:2205.07030.  
  *Why:* Multiplane holograms relate to my depth stack.
- Akşit, K., Itoh, Y. HoloBeam: Paper-Thin Near-Eye Displays. IEEE VR 2023. arXiv:2212.05057.  
  *Why:* Display-side use of holography.
- Walton, D. R., et al., Akşit, K. Metameric Varifocal Holograms. IEEE VR 2022. arXiv:2110.01981.  
  *Why:* Perception-guided holograms.
- Kavaklı, K., Urey, H., Akşit, K. Learned holographic light transport: invited. Appl. Opt. 61(5), B50–B55 (2022). doi:10.1364/AO.439401.  
  *Why:* Closes the gap between simulated and captured holograms.
- Işıl, Ç., et al., Akşit, K., Ozcan, A. All-optical image denoising using a diffractive visual processor. Light Sci. Appl. 13, 43 (2024). doi:10.1038/s41377-024-01385-6.  
  *Why:* Optical computing for denoising.
- Sahloul, M., Akşit, K., Toy, M. F. All-optical selective target highlighting for augmented reality microscopy. Opt. Continuum 5(8), 2708–2723 (2026). doi:10.1364/OPTCON.606265.  
  *Why:* SLM phase maps used in microscopy.
- Kingshott, O., Antipa, N., Bostan, E., Akşit, K. Unrolled Primal-Dual Networks for Lensless Cameras. Opt. Express (2022).  
  *Why:* Computational imaging without lenses.
- Chen, Z., Doğan, M. D., Spjut, J., Akşit, K. SpecTrack: Learned Multi-Rotation Tracking via Speckle Imaging. SIGGRAPH Asia 2024 Posters. doi:10.1145/3681756.3697875.  
  *Why:* Uses speckle as a signal, not noise.
- Dogan, M. D., et al., Akşit, K., Mueller, S. SensiCut: material-aware laser cutting using speckle sensing and deep learning. UIST 2021.  
  *Why:* Speckle sensing.
- Kavaklı, K., Walton, D. R., Antipa, N., Mantiuk, R., Lanman, D., Akşit, K. Optimizing vision and visuals: lectures on cameras, displays and perception. ACM SIGGRAPH 2022 Courses. doi:10.1145/3532720.3535650.  
  *Why:* Teaching material for the whole pipeline.
- Akşit, K., Kavaklı, K. (2023). Flexible modeling of next-generation displays using a differentiable toolkit. Practical Holography XXXVII, SPIE 12445; Kavaklı, K., Akşit, K. (2022). Introduction to Odak. Frontiers in Optics.  
  *Why:* Describes the Odak toolkit.

### Other publications from the Computational Light Laboratory
- Automatic Lens Placement for Personalized 3D Printed Eyewear (SCF 2026)
- Heartian: Physiology-Aware Relightable Gaussian Head Avatar (SIGGRAPH Asia 2026 TC)
- Gaussian Image Steganography via Parameter-Domain Keyed Embeddings (SIGGRAPH Asia 2026 TC)
- Clustered Codebook Quantization for 2D Gaussian-based Image Compression (SIGGRAPH Posters 2026)
- Editing Physiological Signals in Videos Using Latent Representations (CVPR Workshops 2026)
- Text-guided Fine-Grained Video Anomaly Understanding (CVPR Workshops 2026)
- Learned Display Radiance Fields with Lensless Cameras (SIGGRAPH Asia 2025 TC)
- Foveation Improves Payload Capacity in Steganography (SIGGRAPH Asia 2025 Posters)
- Learned Single-Pass Multitasking Perceptual Graphics for Immersive Displays (ACM MM 2025)
- Efficient Proxy Raytracer for Optical Systems using Implicit Neural Representations (SIGGRAPH 2025 Posters)
- ChromaCorrect: Prescription Correction in VR Headsets through Perceptual Guidance (Biomed. Opt. Express 2023)
- Metameric Inpainting for Image Warping (IEEE TVCG 2022)
- Telelife: the future of remote living (Front. VR 2021)
- Beyond blur: ventral metamers for foveated rendering (SIGGRAPH 2021)
- Beaming displays (IEEE VR 2021)
- Optical gaze tracking with spatially-sparse single-pixel detectors (ISMAR 2020)
- Patch scanning displays (Opt. Express 2020)
- Near-eye display and tracking technologies for VR and AR (CGF 2019)
- Foveated AR (SIGGRAPH 2019)
- FocusAR (ISMAR 2018)
- Manufacturing application-driven foveated near-eye displays (IEEE VR 2018)
- Near-eye varifocal AR display using see-through screens (SIGGRAPH Asia 2017)
- Wide field of view varifocal near-eye display using deformable membrane mirrors (IEEE VR 2017)
- Gaze-sensing LEDs for head mounted displays (arXiv)
- Slim near-eye display using pinhole aperture arrays (Appl. Opt. 2015)
- Head-worn mixed reality projection display application (ACE 2014)
- Super stereoscopy technique (Opt. Lett. 2014)
- Dynamic exit pupil trackers for autostereoscopic displays (Opt. Express 2013)
- Multi-view autostereoscopic projection display using rotating screen (Opt. Express 2013)
- Portable 3D Laser Projector Using Mixed Polarization Technique (J. Display Technol. 2012)
- Heart rate monitoring via remote photoplethysmography (Opt. Express 2010)