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
**[Consistency Models for Fast MRI Reconstruction Using Regularization by Denoising](https://arxiv.org/abs/2608.20561v1)**  
_Merve Gülle, Junno Yun, Yaşar Utku Alçalar et al. · 2026-08-20_  
Diffusion models (DMs) have emerged as powerful generative priors for MRI reconstruction with promising results. Yet DM-based methods require extensive iterative refinement, limiting their practical…

**[An integrated diffusion-weighted imaging processing and interpretation platform for MR-guided radiotherapy](https://arxiv.org/abs/2608.20519v1)**  
_Yunxiang Li, Yan Dai, Yen-Peng Liao et al. · 2026-08-20_  
Background: Magnetic resonance imaging-guided linear accelerators (MR-Linacs) allow diffusion-weighted imaging (DWI) to be acquired at every treatment fraction, but converting these…

**[Flow Matching-Based PET Image Reconstruction](https://arxiv.org/abs/2608.20112v1)**  
_Fumio Hashimoto, Ziqian Huang, Tatsuya Yokota et al. · 2026-08-20_  
Generative models have shown strong potential for positron emission tomography (PET) image reconstruction. Although diffusion model-based reconstruction methods have demonstrated promising…

**[Simultaneous 3D co-registered perfusion and oxygenation with ULM, photoacoustic imaging, and a planar matrix array](https://arxiv.org/abs/2608.19823v1)**  
_Léa Davenet, Jacques Battaglia, Franck Lager et al. · 2026-08-20_  
Objective. Joint assessment of tissue oxygenation and microvascular perfusion could offer valuable insights into vascular function across a wide range of biomedical applications. Multispectral…

**[A Reference System for Open Source Portable Low-Field MRI](https://arxiv.org/abs/2608.19062v2)**  
_David Schote, Helge Herthum, Umberto Zanovello et al. · 2026-08-19_  
Despite its renewed attention, the pathway to point-of-care portable low-field MRI systems remains challenging, limiting adoption across research groups. Incomplete documentation limits…

**[Ultra-wideband MRE of the human liver and spleen for viscoelastic model identification in hepatic inflammation](https://arxiv.org/abs/2608.18867v1)**  
_Jakob Schattenfroh, Michael Fedders, Steffen P. Häseli et al. · 2026-08-19_  
Magnetic resonance elastography (MRE) is established for noninvasive assessment of liver fibrosis. Conventional abdominal MRE is typically limited to 40-60 Hz. Lower frequencies remain largely…

_Updated: 2026-08-24 · source: arXiv physics.med-ph_
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
