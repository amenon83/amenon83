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
**[Full-field fluorescence computed tomography (F3CT) using a calibrated virtual cone-beam pinhole geometry](https://arxiv.org/abs/2608.28275v1)**  
_Thomas Zillhardt, Yunhui Chen, Alexander Rack et al. · 2026-08-28_  
We present F3CT, a synchrotron-based hyperspectral full-field fluorescence computed tomography technique that avoids raster scanning by combining a pinhole aperture with an energy-resolving 2D…

**[Physics-Assisted Deep Learning Denoising for Stabilized IMPULSED dMRI Microenvironment Parameter Fitting](https://arxiv.org/abs/2608.27681v1)**  
_Wen Li, Yan Dai, Arely Perez Rodriguez et al. · 2026-08-27_  
Diffusion-weighted MRI (dMRI) is a powerful tool for quantifying cellular microenvironment parameters. This study proposes a physics-assisted deep learning (DL)-based denoising framework designed to…

**[Constrained estimation of rotational invariants of the cumulant expansion (RICE) for rapid tensor-valued diffusion MRI](https://arxiv.org/abs/2608.27212v1)**  
_Jinyang Yu, Oliver Gödicke, Frederik B. Laun et al. · 2026-08-27_  
Purpose: To complement 1.5-minute measurements of common tensor-valued diffusion MRI (dMRI) markers with rapid constrained fitting. Methods: Fast dMRI protocols for obtaining rotational invariants of…

**[Dose-PlanNet: Physics Based Radiotherapy Dose Prediction with Deep Learning](https://arxiv.org/abs/2608.26901v1)**  
_Ankit Bhattacharjee, Sougata Maity, Santam Chakraborty et al. · 2026-08-27_  
Automating prostate radiotherapy treatment planning is dosimetrically complex, particularly for extreme hypofractionated regimens. In this study, we introduce Dose-PlanNet, a physics-guided 3D deep…

**[Sparse Delta Integration method for the calculation of spatiotemporal pressure fields of arbitrary ultrasound transducer geometries](https://arxiv.org/abs/2608.26891v1)**  
_Deyver E. Rivera, Charlie Demene, Mickael Tanter · 2026-08-27_  
Accurate and efficient simulation of ultrasound pressure fields and pulse-echo responses is essential for transducer design, beamforming optimization, and model-based imaging research. Conventional…

**[Adapting the TG-43 formalism for use in Diffusing alpha-emitters Radiation Therapy](https://arxiv.org/abs/2608.26330v1)**  
_Guy Heger, Lior Epstein, Lior Arazi · 2026-08-26_  
Background: Diffusing alpha-emitters Radiation Therapy ("Alpha DaRT") enables the treatment of solid tumors using alpha particles. In Alpha DaRT, the tumor dose distribution is mainly dictated by the…

_Updated: 2026-08-31 · source: arXiv physics.med-ph_
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
