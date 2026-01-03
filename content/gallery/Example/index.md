---
title: 📈 Communicate your results effectively with the best data visualizations
summary: Use popular tools such as HuggingFace, Plotly, Mermaid, and data frames.
date: 2023-10-25
draft: true
authors:
  - me


---


## Image Gallery

Here you can add your gallery code. Below are examples of different gallery layouts:

### Grid Gallery (3 columns)

<div class="gallery" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <figure style="margin: 0;">
    <img src="/media/example1.jpg" alt="Description 1" style="width: 100%; height: auto; border-radius: 0.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <figcaption style="text-align: center; margin-top: 0.5rem; font-size: 0.9rem; color: var(--bs-secondary, #6c757d);">Caption 1</figcaption>
  </figure>
  <figure style="margin: 0;">
    <img src="/media/example2.jpg" alt="Description 2" style="width: 100%; height: auto; border-radius: 0.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <figcaption style="text-align: center; margin-top: 0.5rem; font-size: 0.9rem; color: var(--bs-secondary, #6c757d);">Caption 2</figcaption>
  </figure>
  <figure style="margin: 0;">
    <img src="/media/example3.jpg" alt="Description 3" style="width: 100%; height: auto; border-radius: 0.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <figcaption style="text-align: center; margin-top: 0.5rem; font-size: 0.9rem; color: var(--bs-secondary, #6c757d);">Caption 3</figcaption>
  </figure>
</div>

### Instructions

1. **Place your images** in one of these locations:
   - `assets/media/` folder (for site-wide access)
   - `content/gallery/` folder (for gallery-specific images)
   - `static/uploads/` folder (for downloadable files)

2. **Update the image paths** in the gallery code above:
   - Replace `/media/example1.jpg` with your actual image path
   - For images in `assets/media/`, use: `/media/your-image.jpg`
   - For images in the gallery folder, use: `your-image.jpg` (relative path)

3. **Add more images** by copying the `<figure>` block and updating the image source and caption

### Alternative: Simple Grid Layout

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 2rem 0;">
  ![Image 1](/media/example1.jpg)
  ![Image 2](/media/example2.jpg)
  ![Image 3](/media/example3.jpg)
</div>

### Using Hugo Figure Shortcode

You can also use Hugo's built-in figure shortcode:

{{< figure src="/media/example1.jpg" title="Image Title" >}}

{{< figure src="/media/example2.jpg" title="Another Image" >}}

