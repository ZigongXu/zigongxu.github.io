---
title: Selected Publications

date: 2024-05-19
type: landing
cms_exclude: true
design:
  # Section spacing
  spacing: '5rem'

# Page sections
sections:
  - block: collection
    content:
      title: Featured Publications
      filters:
        folders:
          - selectedpublications
        featured_only: true
    design:
      view: article-grid
      columns: 3
  - block: collection
    content:
      title: Recent/Selected Publications
      text: 'Full list of Paper <a href=" https://ui.adsabs.harvard.edu/public-libraries/c6ahuEHzQ82MrHBbTvhEYw" style="color: blue; text-decoration: underline;">ADS</a>'
      filters:
        folders:
          - selectedpublications
        exclude_featured: false
    design:
      view: citation
      
---

    

