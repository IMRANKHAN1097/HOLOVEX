# Methods in one page

**Hologram formation.** I = |R + O|² = |R|² + |O|² + R\*O + R O\*. Mean subtraction removes the first two terms.

**Angular spectrum (spray, Project 2).** U(x,y,z) = F⁻¹{ F{U₀} · exp[i k z √(1 − (λfₓ)² − (λf_y)²)] }, with evanescent components set to zero and the Matsushima–Shimobaba band limit.

**Fresnel single-FFT (mixing, Project 1).** h = exp[−iπ Δx² (kₓ² + k_y²) / (λ z)], applied to the DC-removed hologram, then inverse FFT. Sampling check: z ≥ N Δx² / λ. Reconstructed pixel Δx′ = λ z / (N Δx).

**Refractive index from phase.** Δn = λ Δφ / (2π d). One fringe corresponds to Δn = λ / d (5.32 × 10⁻⁵ for d = 10 mm).

**Focus metric.** S(z) = Σ [(∂I/∂x)² + (∂I/∂y)²] (Tenengrad); z_focus = argmax S.

**Droplet statistics.** D32 = Σ D³ / Σ D² = 6 ΣV / ΣA; Rosin–Rammler Q(D) = 1 − exp[−(D/D̄)ⁿ]; bootstrap 95% intervals.

**Off-axis demodulation (Takeda).** Isolate the +f₀ lobe, shift to the origin, take the argument of the inverse transform.

**Gerchberg–Saxton and gradient descent.** See the live demos. Gradient: ∂L/∂φ = −2 Im(u · conj(h)), h = Pᴴ[(|v| − t) v/|v|], u = e^{iφ}, v = P u.
