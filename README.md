<p align="center">
  <img src="./banner.png" width="100%" alt="Arnav Menon — computational radiation transport, proton therapy, ML surrogates"/>
</p>

<p align="center">
  <a href="https://github.com/amenon83"><img src="https://img.shields.io/badge/Ph.D.-Nuclear%20%26%20Radiological%20Eng%20%2B%20Medical%20Physics-22DAB0?style=flat-square&labelColor=0d1117" alt="PhD program"/></a>
  <img src="https://img.shields.io/badge/Georgia%20Tech-NRE%2FMP-B3A369?style=flat-square&labelColor=0d1117" alt="Georgia Tech"/>
  <img src="https://img.shields.io/badge/focus-proton%20therapy%20%C2%B7%20Monte%20Carlo%20%C2%B7%20ML-3987e5?style=flat-square&labelColor=0d1117" alt="focus"/>
</p>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?vCenter=true&center=true&color=22DAB0FF&width=1000&lines=Ph.D.+student+in+Medical+Physics+%40+Georgia+Tech;Accelerating+proton+therapy+with+GPU+%2B+ML;Monte+Carlo%2C+diffusion+models%2C+microdosimetry;A+showcase+of+my+PhD+research+%E2%80%94+take+a+look!)](https://git.io/typing-svg)

---

## 👋 About Me

I'm **Arnav Menon**, a Ph.D. student in the **Nuclear & Radiological Engineering and Medical Physics (NREMP)** program at **Georgia Tech**. I work at the intersection of **computational radiation transport** and **machine learning**, with the goal of making high-fidelity proton therapy simulation fast enough to use inside the clinical loop.

- 🔬 **Research focus** — GPU-accelerated Monte Carlo dose calculation and ML surrogate models (diffusion models, PINNs) for proton therapy.
- 🎯 **Why it matters** — proton therapy spares healthy tissue, but planning it well demands enormous simulation. I build methods that keep the physics accurate while cutting the compute from hours to seconds.
- 🧪 **Toolkit** — `TOPAS` / `Geant4` Monte Carlo, `CUDA`, `PyTorch`, inverse optimization, and microdosimetry.
- 🌱 **Currently** — connecting microdosimetric lineal-energy spectra to variable proton RBE, and accelerating ridge-filter design.
- 📫 **Reach me** — open an issue, or connect — always happy to talk medical physics, Monte Carlo, and ML for science.

---

## 🔬 Research & Project Showcase

<table border="0">
  <tr>
    <td width="33.3%" valign="top">
      <a href="https://github.com/amenon83/SIEMAC_card">
        <img src="./assets/siemac_card.png" width="100%" alt="Accelerated SIEMAC — ridge-filter SOBP optimization"/>
      </a>
      <p align="center">
        <a href="https://github.com/amenon83/SIEMAC_card"><b>⚡ Accelerated SIEMAC</b></a><br/>
        <sub>Inverse-optimized <b>sparse ridge filter</b> that shapes a pristine proton peak into a flat spread-out Bragg peak — GPU/ML-accelerated.</sub><br/><br/>
        <code>TOPAS</code> <code>CUDA</code> <code>PyTorch</code> <code>Optimization</code>
      </p>
    </td>
    <td width="33.3%" valign="top">
      <a href="https://github.com/amenon83/lineal-energy">
        <img src="./assets/lineal_card.png" width="100%" alt="Microdosimetric lineal-energy spectra for proton RBE"/>
      </a>
      <p align="center">
        <a href="https://github.com/amenon83/lineal-energy"><b>📈 Lineal Energy &amp; Proton RBE</b></a>
        <img src="https://img.shields.io/badge/-proposal-orange?style=flat-square" alt="proposal" valign="middle"/><br/>
        <sub>Microdosimetric <b>lineal-energy spectra</b> as a mechanistic input to variable proton RBE — a research proposal with a fast ML surrogate.</sub><br/><br/>
        <code>Microdosimetry</code> <code>TOPAS</code> <code>MKM</code> <code>ML</code>
      </p>
    </td>
    <td width="33.3%" valign="top">
      <a href="https://github.com/amenon83/compton-scattering">
        <img src="./assets/compton_card.png" width="100%" alt="Compton effect — scattered photon energy vs angle"/>
      </a>
      <p align="center">
        <a href="https://github.com/amenon83/compton-scattering"><b>🌀 Compton Scattering</b></a><br/>
        <sub>A small, runnable teaching sim of the <b>Compton effect</b>: kinematics, the Klein–Nishina cross section, and a Monte Carlo you can read line by line.</sub><br/><br/>
        <code>Python</code> <code>NumPy</code> <code>Monte&nbsp;Carlo</code> <code>Physics</code>
      </p>
    </td>
  </tr>
</table>

---

## 📡 Medical Physics Feed

<sub>The latest <b>physics.med-ph</b> preprints from <a href="https://arxiv.org/list/physics.med-ph/recent">arXiv</a>, auto-refreshed weekly by a GitHub Action. A snapshot of where the field is moving.</sub>

<!-- ARXIV-FEED:START -->
**[Fast ungated five-dimensional cardiac MRI on a 1.5 T MR-linac for MRI-guided radiotherapy](https://arxiv.org/abs/2607.16033v1)**  
_M. L. Terpstra, T. E. Olausson, M. M. N. Aubert et al. · 2026-07-17_  
Background: Stereotactic arrhythmia radio-ablation (STAR) for patients with ventricular tachycardia is currently limited by complex cardiorespiratory motion. Current 5D-MRI motion models require long…

**[Joint-decoupled iterative CBCT reconstruction with hybrid scatter estimation and voxel-adaptive beam hardening correction](https://arxiv.org/abs/2607.15812v1)**  
_Jianing Sun, Jean Michel Létang, Qixiang Sun et al. · 2026-07-17_  
Cone-beam computed tomography (CBCT) is fundamentally challenged by scatter and beam hardening artifacts, which originate from X-ray scattering and the polychromatic nature of the X-ray spectrum…

**[Differentiable Cardiac Electrophysiology Simulations for Dynamical State and Parameter Estimation](https://arxiv.org/abs/2607.15492v1)**  
_Adarsh Pashikanti, Shrey Chowdhary, Alex Ho et al. · 2026-07-16_  
The heart's contractions are triggered by action potential waves, which propagate through the cardiac muscle and exhibit diverse spatio-temporal dynamics during different heart rhythms. The dynamics…

**[Flow in a porous non-axisymmetric annular conduit: Coupling wall compliance and peristalsis](https://arxiv.org/abs/2607.15239v1)**  
_Nishanth Surianarayanan, Ivan C. Christov · 2026-07-16_  
Coenen \textit{et al.}\ (\textit{J. Fluid Mech.}, vol.~921, 2021, p.~R2) developed a reduced-order model of peristaltic pumping in non-axisymmetric annular conduits with rigid walls, in the context…

**[One-for-All Adaptive Radiotherapy Planning Agent: A Foundation Framework for Daily CBCT-guided Radiotherapy](https://arxiv.org/abs/2607.14870v1)**  
_Shaoyan Pan, Kirk Jon Luca, Yuan Gao et al. · 2026-07-16_  
In this work, we introduce the One-for-All Adaptive Radiotherapy Planning Agent, a unified foundation-model-based system that performs complete, treatment-specific online adaptive planning directly…

**[The Wulff bio-heat transfer model revisited: directional blood enthalpy transport, the biological Peclet number, and implications for laser-induced thermal therapy](https://arxiv.org/abs/2607.14017v1)**  
_Valerio D'Alessandro, Matteo Falone, Luca Giammichele et al. · 2026-07-15_  
Bio-heat transfer models play a fundamental role in predicting temperature fields during laser-induced thermal therapy (LITT). Among continuum bio-heat transfer models, the Pennes equation remains…

_Updated: 2026-07-20 · source: arXiv physics.med-ph_
<!-- ARXIV-FEED:END -->

---

## 🐍 My Contribution Trail
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/amenon83/amenon83/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/amenon83/amenon83/output/github-contribution-grid-snake.svg">
    <img alt="Arnav's GitHub Contribution Snake" src="https://raw.githubusercontent.com/amenon83/amenon83/output/github-contribution-grid-snake.svg" width="100%" style="max-width: 900px;" />
  </picture>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer&reversal=true" width="100%"/>
</p>
