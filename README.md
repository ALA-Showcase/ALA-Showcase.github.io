# [ALA Showcase](https://ala-showcase.github.io)
Showcase website for the UTS Animal Logic Academy 2023 cohort.

## Setup
1. Install Jekyll. [Use this guide for Windows](https://jekyllrb.com/docs/installation/windows/).
2. Open a terminal and navigate to the base of this repository.
3. Type `bundle exec jekyll serve`.
4. Open the URL in your browser, usually http://127.0.0.1:4000.

## Libraries
This website uses a couple of libraries to make things easier. Try to use them where you can:

### [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
Bootstrap has a bunch of CSS classes which adjust for mobile and make styling easier.

For example it's good for [margins and padding](https://getbootstrap.com/docs/5.3/utilities/spacing/#margin-and-padding):
```html
<!-- Bootstrap version -->
<div class="mb-3">Hello</div>

<!-- Regular version -->
<div style="margin-bottom: 1rem">Hello</div>
```

### [Bootstrap Icons](https://icons.getbootstrap.com/)
A large pack of icons, used for the [navigation bar](_includes/navbar_bottom.html).

### [Leaflet](https://leafletjs.com/)
A map library used for the [studio map page](_pages/map.md).

## Structure

### Variables
A couple of global variables like pages for the navigation bar are in [`_config.yml`](_config.yml)

### Styles
Try to use [Bootstrap classes](https://getbootstrap.com/docs/5.3/getting-started/introduction/) to avoid manual styling when possible.

I mainly used inline CSS for custom styling, with a few general styles in [`style.scss`](assets/css/style.scss).

The base style for fonts and colours is [`base.scss`](_sass/base.scss).

### Scripts
Most pages use inline JavaScript, so check the [`_pages`](_pages) folder.

### Pages
Pages are located in the [`_pages`](_pages) folder.

Pages use [Liquid syntax](https://jekyllrb.com/docs/step-by-step/02-liquid/), which adds helpers like for loops and variables on top of HTML.

### Components
Jekyll doesn't have React-style components, but it lets you reuse HTML with [includes](https://jekyllrb.com/docs/includes/).

Includes are located in the [`_includes`](_includes) folder.

This is good for elements shared between pages, like the navigation bar.

### Images
Images are located in the [`assets`](assets/images) folder.

To make the website load faster on mobile, make sure to compress images. Either `.webp` or `.jpg` is good.

I included the original version of each image in the `hires` folder in case it's needed later.
