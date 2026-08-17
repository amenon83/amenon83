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
**[UMPIRE-Net: Unrolled Magnitude-Phase Regularization Network for Accelerated MRI](https://arxiv.org/abs/2608.14422v1)**  
_Mahdi Saberi, Toygan Kiliç, Mehmet Akçakaya · 2026-08-14_  
MRI reconstruction from undersampled k-space measurements is an ill-posed inverse problem. Physics-driven deep learning (PD-DL) methods have shown strong performance for this task by combining the…

**[MRI-guided cardiac radiotherapy using a 1.5 T MR-linac: surveying emerging patterns of care](https://arxiv.org/abs/2608.14213v1)**  
_O. Akdag, S. Mandija, J. Pomp et al. · 2026-08-14_  
Background: Cardiac tumours are rare and treated by surgical resections, which are complex, invasive and carry procedural risks. MRI-guided radiotherapy (MRgRT) noninvasively facilitates conformal…

**[Birth of the Coil: another Milestone towards a fully reproducible low-field MRI scanner for head-imaging](https://arxiv.org/abs/2608.14139v1)**  
_Umberto Zanovello, Julia Pfitzer, Ariane Ernst et al. · 2026-08-14_  
Low-field magnetic resonance imaging (MRI) provides an accessible, portable, and low-cost alternative to high-field scanners, expanding diagnostic imaging to point-of-care settings. However…

**[Focal-point scanning for dose delivery and optimization with focused laser-accelerated very-high-energy electron beams](https://arxiv.org/abs/2608.13919v1)**  
_Zhiyuan Guo, Yifei Pi, Junwei Zhou et al. · 2026-08-14_  
Focused very-high-energy electron (VHEE) beams can produce localized dose enhancement at selected depths, but irradiation of a finite target requires coordinated control of multiple focal positions…

**[Label-Free Deep-Tissue Peripheral Nerve Detection with a Handheld Multimodal OCT Probe and NerveDetNet](https://arxiv.org/abs/2608.13807v1)**  
_Yihan Wang, Ruilin You, Shaobai Li et al. · 2026-08-13_  
Peripheral nerves buried beneath intact tissue are difficult to visualize during surgery and remain inaccessible to white light wide-field imaging and other surface optical imaging methods. Existing…

**[Fully fiber-integrated endoscopic OCT probes by single-step two-photon 3D printing](https://arxiv.org/abs/2608.13772v1)**  
_Yihan Wang, Ruilin You, Jiabin Chen et al. · 2026-08-13_  
Optical coherence tomography (OCT) provides depth-resolved, label-free imaging of microstructure and has become a central modality for optical biopsy. Bringing this capability from bench-top…

_Updated: 2026-08-17 · source: arXiv physics.med-ph_
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
