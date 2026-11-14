---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  spacing: '5rem'

sections:
  - block: hero-heliosphere
    content:
      kicker: Space physicist · Caltech
      name: Zigong Xu
      tagline: I follow **energetic particles from the Sun to the Moon**, with data from Parker Solar Probe, Solar Orbiter, IMAP and Chang'E-4.
      topics:
        - Solar energetic particles
        - CME-driven shocks
        - Cosmic rays in the heliosphere
        - The lunar radiation environment
        - Space weather and machine learning
      buttons:
        - text: Explore my research
          url: '#research'
          style: primary
        - text: Download CV
          url: uploads/cv.pdf
          style: ghost
      missions:
        - Parker Solar Probe
        - Solar Orbiter
        - IMAP
        - Chang'E-4
      hint: Click anywhere to launch a CME

  - block: resume-biography-3
    content:
      username: me
      text: ''
      button:
        text: Download CV
        url: uploads/cv.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle

  - block: stats
    content:
      items:
        - statistic: "50"
          description: Publications
          sub_metric: 7 first / co-first author · 2 in Science Advances
          icon: hero/document-text
        - statistic: "1,300+"
          description: Citations
          sub_metric: h-index 20 · Google Scholar
          icon: hero/chart-bar
        - statistic: "4"
          description: Space missions
          sub_metric: PSP · Solar Orbiter · IMAP · Chang'E-4
          icon: hero/rocket-launch
        - statistic: "3"
          description: Invited talks
          sub_metric: AGU 2025 & 2026 · Solar Orbiter WG
          icon: hero/presentation-chart-bar
    design:
      layout: cards

  - block: research-areas
    id: research
    content:
      title: Research Areas
      text: From the Sun's corona to the surface of the Moon — following energetic particles through the heliosphere.
      items:
        - name: Solar Energetic Particles
          description: How CME-driven shocks and flares accelerate particles, seen by spacecraft at different distances from the Sun.
          emoji: ☀️
          gradient: from-orange-400 to-red-500
          status: active
          topics: [Inverse velocity arrival, Heavy-ion composition, Multi-spacecraft events]
          cta:
            text: Parker Solar Probe work
            url: projects/parkersolarprobe/
        - name: Cosmic Rays in the Heliosphere
          description: Radial gradients and modulation of anomalous and galactic cosmic rays between 0.3 and 1 au.
          emoji: 🌌
          gradient: from-indigo-400 to-purple-600
          status: active
          topics: [Anomalous cosmic rays, Galactic cosmic rays, Solar modulation]
          cta:
            text: Solar Orbiter work
            url: projects/solarorbiter/
        - name: Lunar Radiation Environment
          description: Primary and albedo particles, SEPs and cosmic-ray shadowing measured on the Moon's far side.
          emoji: 🌕
          gradient: from-slate-400 to-gray-600
          status: active
          topics: [Chang'E-4 LND, Albedo protons, Earth-Moon cosmic-ray cavity]
          cta:
            text: LND work
            url: projects/lnd/
        - name: Space Weather & Machine Learning
          description: Radiation-risk assessment for exploration and data-driven SEP forecasting.
          emoji: 🤖
          gradient: from-teal-400 to-cyan-600
          status: emerging
          topics: [SEP prediction, Deep learning, Radiation risk]
          cta:
            text: IMAP/HIT
            url: projects/imap/
        - name: Instruments & Simulation
          description: Calibrating particle telescopes and modelling their response with Geant4 — from LND on the Moon to HET and EPI-Hi in space.
          emoji: 🔬
          gradient: from-amber-400 to-yellow-600
          status: active
          topics: [Geant4, Cross-calibration, Data products]
          cta:
            text: Experience
            url: experience/#missions
        - name: Flares & Coronal Shocks
          description: Where SEPs start — coronal shock waves, flare statistics and radio bursts, the topic of my first papers at Nanjing.
          emoji: 🔥
          gradient: from-rose-400 to-pink-600
          status: completed
          topics: [CME shocks, Flare waiting times, Remote sensing]
          cta:
            text: Publications
            url: publications/
    design:
      layout: cards

  - block: mission-map
    id: missions
    content:
      title: Where my instruments fly
      text: I work with particle detectors on four missions, from 9.86 solar radii to the far side of the Moon. Pick one to see where it flies and what I do with its data.
      missions:
        - key: psp
          name: Parker Solar Probe
          short: PSP
          agency: NASA · launched 2018
          color: '#fb923c'
          orbit: { q: 0.046, Q: 0.73, w: 200, m0: 140 }
          facts: Closer to the Sun than any spacecraft before it, 9.86 solar radii (0.046 au), once every 88 days.
          role: Member of the IS⊙IS/EPI-Hi team since 2023. I study solar energetic particle events with inverse velocity arrival, and events seen by several spacecraft at once.
          url: projects/parkersolarprobe/
        - key: solo
          name: Solar Orbiter
          short: SolO
          agency: ESA & NASA · launched 2020
          color: '#a78bfa'
          orbit: { q: 0.29, Q: 0.91, w: 60, m0: 250 }
          facts: Comes within about 0.3 au of the Sun on an increasingly tilted orbit, carrying the Energetic Particle Detector (EPD).
          role: EPD/HET team member, 2020–2023. Cross-calibration, cosmic-ray radial gradients, and the first observations of anomalous cosmic-ray helium in the inner heliosphere.
          url: projects/solarorbiter/
        - key: imap
          name: IMAP
          agency: NASA · launched 2025
          color: '#34d399'
          at: l1
          facts: Watches the solar wind and energetic particles from the Sun–Earth L1 point, 1.5 million km sunward of Earth.
          role: Member of the High-Energy Ion Telescope (HIT) team since launch.
          url: projects/imap/
        - key: ce4
          name: Chang'E-4
          short: Moon · Chang'E-4
          agency: CNSA · landed 2019
          color: '#e2e8f0'
          at: moon
          facts: The first landing on the far side of the Moon, carrying the Lunar Lander Neutron and Dosimetry experiment (LND) built at Kiel University.
          role: LND project manager, 2019–2023. The first solar energetic particle event measured on the far side, albedo protons, and a cosmic-ray cavity in Earth–Moon space.
          url: projects/lnd/

  - block: collection
    id: news
    content:
      title: Latest News
      count: 4
      filters:
        folders:
          - newsblog
      order: desc
      archive:
        enable: true
        text: All news
        link: newsblog/
    design:
      view: date-title-summary

  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - selectedpublications
        featured_only: true
    design:
      view: article-grid
      columns: 3

  - block: pub-chart
    content:
      title: Publications by Year
      text: 'Complete list on [NASA ADS](https://ui.adsabs.harvard.edu/public-libraries/c6ahuEHzQ82MrHBbTvhEYw) · [Google Scholar](https://scholar.google.com/citations?user=o1RDduwAAAAJ&hl=en)'
      button:
        text: Browse all publications
        url: publications/

  - block: space-weather
    id: space-weather
    content:
      title: 🛰️ Space Weather Right Now
      text: Live readings from NOAA's GOES satellites — the same kind of energetic-particle data I work with every day. Toggle energy channels to compare.

  - block: career-timeline
    id: timeline
    content:
      title: Journey So Far
      items:
        - date: Sep 2026
          emoji: ⭐
          title: Senior Postdoctoral Scholar, Caltech
          text: Promoted to Senior Postdoctoral Scholar Research Associate in Physics.
          url: newsblog/2026-senior-postdoc/
        - date: 2026
          emoji: 📄
          title: Three first / co-first-author papers
          text: 'Inverse-velocity-arrival SEP events (A&A), anomalous cosmic-ray helium (A&A), and a cosmic-ray cavity in Earth-Moon space (*Science Advances*).'
          url: newsblog/
        - date: Jun 2026
          emoji: 🎤
          title: Co-convened a session at SHINE 2026
          text: 'Session 13, *Dynamics of Particle Populations Throughout the Inner Heliosphere*; my ACR helium result featured as an ESA Solar Orbiter Science Nugget.'
          url: newsblog/2026-shine-session/
        - date: Sep 2025
          emoji: 🛰️
          title: Joined NASA IMAP / HIT team
          url: projects/imap/
        - date: Sep 2023
          emoji: 🌴
          title: Postdoc at Caltech — Parker Solar Probe IS⊙IS/EPI-Hi
          url: projects/parkersolarprobe/
        - date: 2023
          emoji: 🎓
          title: PhD (Dr. rer. nat., cum laude), Kiel University
          text: Project manager of Chang'E-4/LND and member of the Solar Orbiter EPD/HET team.
        - date: 2015 – 2018
          emoji: 🔭
          title: B.S. & M.S., Nanjing University
          text: First paper on coronal shocks and solar energetic particles (ApJ 2017).
      
  - block: collection
    id: talks
    content:
      title: Recent Talks
      count: 3
      filters:
        folders:
          - events
      order: desc
      archive:
        enable: true
        text: All talks
        link: events/
    design:
      view: date-title-summary

  - block: contact-info
    id: contact
    content:
      title: Get in Touch
      subtitle: Open to collaborations on energetic particles, space radiation and space weather.
      visit_title: Where to find me
      connect_title: Connect
      address:
        lines:
          - Space Radiation Laboratory
          - California Institute of Technology
          - Pasadena, CA, United States
      email: zgxu@caltech.edu
      social:
        - icon: brands/github
          url: https://github.com/zigongxu
        - icon: brands/linkedin
          url: https://www.linkedin.com/in/zigongxu/
        - icon: brands/x
          url: https://x.com/zigong_xu
        - icon: academicons/google-scholar
          url: https://scholar.google.com/citations?user=o1RDduwAAAAJ&hl=en
        - icon: academicons/orcid
          url: https://orcid.org/0000-0002-9246-996X
      show_form: false
---
