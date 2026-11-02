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
**[Quantitative Ultrasound Characterizes Perfusion Trajectories in Healthy and Inflamed Gingival Wound Healing](https://arxiv.org/abs/2610.41897v1)**  
_Haowei Tai, Oscar Duran-Garnica, Karen Villarreal et al. · 2026-10-30_  
Rationale and Objectives: Visual examination of extraction-site healing provides limited insight into underlying vascular recovery. We developed a quantitative ultrasound framework to assess gingival…

**[Roadmap: Image reconstruction in emission tomography for the era of fast Monte Carlo simulation](https://arxiv.org/abs/2610.41583v1)**  
_Georg Schramm, Benjamin Auer, Ane Etxebeste et al. · 2026-10-30_  
Quantitative image reconstruction in positron emission tomography and single photon emission computed tomography depends on how accurately the forward model describes photon emission, transport and…

**[A General-Purpose Adaptable Foundation Model for Total-Body PET Kinetic Modelling](https://arxiv.org/abs/2610.41093v1)**  
_Yun Zhao, Qinlin Gu, Andrew J. Reader et al. · 2026-10-30_  
Voxel-level kinetic modeling in total-body dynamic positron emission tomography (TB-PET) enables precise physiological quantification but complicates parameter uncertainty estimation. While…

**[Comparison of melanin subtypes using pump-probe microscopy](https://arxiv.org/abs/2610.40969v1)**  
_Emma Bao, David Grass, Martin C. Fischer et al. · 2026-10-29_  
Pump-probe microscopy (PPM) is used to probe excited state dynamics of endogenous chromophores to generate contrast that is unavailable in traditional forms of microscopy. Here we apply PPM to…

**[EPC-RawDC: Equivariant Physics Constrained 3D Diffusion with Raw Data Consistency for CBCT to CT Image Synthesis](https://arxiv.org/abs/2610.40046v1)**  
_Alzahra Altalib, Chunhui Li, Alessandro Perelli · 2026-10-29_  
Cone beam computed tomography (CBCT) is widely used for image guided and adaptive radiotherapy, but scatter, noise, reconstruction artifacts, and inaccurate Hounsfield units limit its quantitative…

**[Evaluation of attenuation-based simulated X-ray images for image-guided radiotherapy](https://arxiv.org/abs/2610.39647v1)**  
_Hannah Jungreuthmayer, Julius Arnold, Andreas Renner et al. · 2026-10-29_  
In image-guided radiation therapy (IGRT), in-room X-rays are often used for patient positioning and monitoring, however, usually default imaging settings are utilized for each indication. Obtaining…

_Updated: 2026-11-02 · source: arXiv physics.med-ph_
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
