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
**[Attention-guided super-resolution of 4D flow MRI in carotid arteries](https://arxiv.org/abs/2609.04891v1)**  
_Ali Mokhtari, Dominik Obrist · 2026-09-04_  
Four-dimensional (4D) flow magnetic resonance imaging (MRI) is a powerful non-invasive technique for visualizing and quantifying complex blood flow patterns in vivo. Despite its clinical promise…

**[BEAM3R: Beam's-eye-view architecture with Mamba-3 for implicit dose reconstruction](https://arxiv.org/abs/2609.04747v1)**  
_Chen Cheng, Michael Ferraro, James Grover et al. · 2026-09-04_  
To enable accurate and rapid photon control point and proton beamlet dose calculation in the DoseRAD2026 challenge, we present BEAM3R, a dose estimation framework operating in beam's-eye-view (BEV)…

**[3D scattered light imaging: extracting 3D fiber orientations from 1D line profiles in brain imaging](https://arxiv.org/abs/2609.03764v1)**  
_Dennis Scheidt, Charlotte Voß, Cristian Rosero Arias et al. · 2026-09-03_  
Understanding the 3D fiber architecture of the brain at the microscopic scale is essential for revealing its structural connectivity and function. Polarization-based optical imaging (3D-PLI)…

**[HPC Modeling of Coupled Elastic-Acoustic Wave Propagation in Biological Media: Numerical Validation](https://arxiv.org/abs/2609.03644v1)**  
_Fawad Ali, Carlos García, Lapo Boschi · 2026-09-03_  
Accurate numerical models of sound propagation through biological media are an important tool for many applications, from medical physics to studying the auditory system of humans or other animals…

**[Fast Patient-Specific Breast CT Dosimetry: 22-Fold Acceleration of Monte Carlo MGD Estimation](https://arxiv.org/abs/2609.03263v1)**  
_Amir Entezam, Ashkan Pakzad, Christopher J. Hall et al. · 2026-09-03_  
Accurate patient-specific mean glandular dose (MGD) estimation in breast computed tomography (BCT) requires anatomically realistic models, but high-resolution patient-derived phantoms impose high…

**[Improving Clinical Target Volume Segmentation Accuracy using Anatomical Priors and Active Learning for the AGITG TOPGEAR Clinical Trial](https://arxiv.org/abs/2609.03186v1)**  
_Phillip Chlap, Mark Lee, Trevor Leong et al. · 2026-09-02_  
Training deep learning-based medical image segmentation models is challenging with limited curated datasets. For AGITG TOPGEAR, a gastric cancer trial, the Clinical Target Volume (CTV) is complex and…

_Updated: 2026-09-07 · source: arXiv physics.med-ph_
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
