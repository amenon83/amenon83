<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&text=A+GitHub+Portfolio&fontSize=50&fontAlignY=85&fontColor=22DAB0FF&height=100&section=header" width="100%"/>
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
**[Numerical Simulation of Electrical Properties in Cortical and Trabecular Bone: A Simplified Model](https://arxiv.org/abs/2609.31584v1)**  
_María José Cervantes, Catalina A. Cely-Ortíz, C. Manuel Carlevaro et al. · 2026-09-25_  
The electrical properties of biological tissues depend on their composition and microstructure and determine their response to applied electric fields. In bone tissue, these properties are closely…

**[Improving Multi-Delay-ASL through specialized reconstruction](https://arxiv.org/abs/2609.30923v1)**  
_Ingmar Sorgenfrei, Qinyang Shou, Ingrid Barth et al. · 2026-09-25_  
Purpose: Although image reconstruction has received relatively little attention in ASL research to date, it has the potential to address several challenges in ASL. As well as speeding up measurements…

**[A 2D autocorrelation-based frequency estimator reflecting spatial tissue distribution to improve Ultrasound H-scan tissue characterization](https://arxiv.org/abs/2609.30686v1)**  
_Jihye Baek, Thurston Brevett, Dongwoon Hyun et al. · 2026-09-25_  
H-scan is a promising quantitative ultrasound technique that estimates the frequency content of backscattered signals and maps the estimated frequencies onto a red/blue color scale to reflect…

**[MBFormer: Microbubble Transformer for 3D Time-Series Da-ta Processing to Improve Bound Bubble Detection in Nonde-structive Ultrasound Molecular Imaging](https://arxiv.org/abs/2609.30618v1)**  
_Jihye Baek, Jeong Hoon Lee, Hoda Hashemi et al. · 2026-09-24_  
Development of nondestructive ultrasound molecular imaging (UMI) is essential for early cancer detection through real-time screening using clinical ultrasound systems. Current techniques face…

**[PGDM-MRSRGAN: Physics-Guided Degradation Model with an SRGAN Framework for Magnetic Resonance Image Super-Resolution: Applications in Low-Field MRI](https://arxiv.org/abs/2609.30431v1)**  
_Yashwant Kurmi, Charlotte R. Sappo, Sai Abitha Srinivas et al. · 2026-09-24_  
Magnetic Resonance Imaging (MRI) often suffers from low signal-to-noise ratio (SNR) and limited spatial resolution, which compromise clinical precision. This study aims to address these challenges by…

**[Cone-beam artifact reduction in Gamma Knife CBCT images using a line-arc-line scan trajectory](https://arxiv.org/abs/2609.30169v1)**  
_Alexandra Alain-Beaudoin, Håkan Nordström, Luc Beaulieu et al. · 2026-09-24_  
Objective. Gamma Knife cone-beam computed tomography (CBCT) images suffer from distinct cone-beam artifacts for some patients, due to the conical X-ray beam which is oriented to intersect the…

_Updated: 2026-09-28 · source: arXiv physics.med-ph_
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
