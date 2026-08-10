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
**[An Angular Spectrum Method for Nonlinear Propagation in Heterogeneous Tissue with Immersed Sources for Ultrasound](https://arxiv.org/abs/2608.07389v1)**  
_Gianmarco Pinton · 2026-08-07_  
A modified angular spectrum method (ASM) is developed for three-dimensional nonlinear acoustic propagation through heterogeneous tissue, targeting transcranial and therapeutic ultrasound. First, a…

**[Measurements Automatically Extracted from Zero Echo Time MRI Using Deep Learning Image Segmentation and Geometric Modeling Agree with Expert Manual Readings](https://arxiv.org/abs/2608.07368v1)**  
_Jack Consolini, Eric A. Bogner, Meghan Sahr et al. · 2026-08-07_  
Computed tomography (CT) remains the reference for 3D osseous morphometry in femoroacetabular impingement (FAI) but requires ionizing radiation and manual measurement. Zero echo time (ZTE) MRI…

**[Machine Learning-Based Inter-Crystal Scatter Recovery for Ultra-High Resolution PET Imaging](https://arxiv.org/abs/2608.07155v1)**  
_Alexandre Bernier, Roger Lecomte, Jean-Baptiste Michaud · 2026-08-07_  
Inter-crystal scatter (ICS) events pose a significant challenge in ultrahigh- resolution positron emission tomography (UHR-PET), especially as detector crystals become smaller and their readouts…

**[Lens-Aware Differentiable Beamforming for In Vivo Distributed Aberration Correction with Curvilinear Transducers](https://arxiv.org/abs/2608.06853v1)**  
_Benjamin N. Frey, Robin van Velzen, Hoda S. Hashemi et al. · 2026-08-07_  
This work extends ultrasound autofocusing via common midpoint phase error optimization to support curvilinear array geometries. Iterative model-based aberration correction via local sound speed…

**[108 ps coincidence time resolution through optimized scintillators, photodetectors, readout electronics, and DOI-based timing correction in orthogonally stacked detector configurations](https://arxiv.org/abs/2608.06746v1)**  
_Arisa Sanzen, Yuya Onishi, Takahiro Moriya et al. · 2026-08-07_  
Objective. Existing commercial time-of-flight positron emission tomography (TOF-PET) systems yield a coincidence time resolution (CTR) of ~200 ps or less full width at half maximum (FWHM). Recently…

**[An open-source framework for predicting ultrasound neuromodulation: bridging tissue elastomechanics and neuron firing dynamics](https://arxiv.org/abs/2608.06321v1)**  
_Gianmarco Pinton · 2026-08-06_  
Transcranial focused ultrasound is a non-invasive neuromodulation modality with millimetre-scale resolution, but its biophysical mechanism of action remains unresolved. Exposure is conventionally…

_Updated: 2026-08-10 · source: arXiv physics.med-ph_
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
