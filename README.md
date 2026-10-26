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
**[U-NeXt: General-purpose event detection for neonatal EEG](https://arxiv.org/abs/2610.32811v1)**  
_Robert Hogan, Sean R. Mathieson, Aurel Luca et al. · 2026-10-23_  
We developed U-NeXt, a general framework for neonatal electroencephalography (EEG) event detection based on semantic segmentation. Its convolutional encoder-decoder directly segments individual…

**[OPTARI: An open-source software framework for clinical translation of optoacoustic imaging](https://arxiv.org/abs/2610.32468v1)**  
_Moritz Schillinger, Maximilian Bader, Adrian Buehler et al. · 2026-10-23_  
Combined optoacoustic (OptA) and ultrasound imaging is a promising modality across a wide range of pathologies. Its use in clinical research, however, is limited by a lack of analysis software…

**[Interactive image diagnosis using test-time backpropagation from the auxiliary task](https://arxiv.org/abs/2610.32396v1)**  
_Takuro Shimaya · 2026-10-23_  
Multi-task deep learning has been developed to ensure explainability in computer-aided diagnosis (CAD) systems. These systems simultaneously predict interpretable characteristics of findings in…

**[Sam-Correction: Fully Adaptive Label Noise Reduction for Medical Image Segmentation](https://arxiv.org/abs/2610.32377v1)**  
_Takuro Shimaya, Masahiro Saiko · 2026-10-23_  
The quality of the teacher label has a dramatic impact on the outcome of the machine learning process. Medical image segmentation often suffers from a noisy ground truth (GT) mask due to difficulties…

**[Geometry-Dependent Properties of Physically Crosslinked PPy-PVA Hydrogels Enable Tunable Iontophoretic Drug Delivery](https://arxiv.org/abs/2610.31567v1)**  
_Heather Jin Hee Kim, Mohsen Alishahi, Kyuin Park et al. · 2026-10-22_  
Objective: Iontophoretic drug delivery has primarily relied on current modulation to regulate drug transport. Here, we investigate hydrogel geometry, microstructure, and local electric fields as…

**[Direct Production of Ultra-High Radioisotopic Pure $^{64}$Cu from Natural Zinc Metal via D-D Fusion Narrowband Fast Neutron Source Irradiation](https://arxiv.org/abs/2610.31340v1)**  
_Jeremy M. C. Brown, Mantas Grigalavicius, Tibor Gilinger et al. · 2026-10-22_  
Copper-64 radiopharmaceuticals have seen limited clinical deployment primarily due to the high cost of the isotopically enriched $^{64}$Ni metal required for its production. In this work we…

_Updated: 2026-10-26 · source: arXiv physics.med-ph_
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
