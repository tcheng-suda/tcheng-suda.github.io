This website is Tao Cheng’s personal academic website.
Tao Cheng is the copyright holder to all the contents published
on this website except the underlying theme, which is based on
the [Steve's No-Good-Very-Bad Jekyll Theme](https://github.com/esemble/esemble.github.io).
If you wish to use any copyright material on this website,
please contact me via the Email or address listed above to obtain
a permission.

Local development: run `./run.sh` or `./serve.sh`. Jekyll regenerates `_site/`
and `.jekyll-cache/`; `bundle exec jekyll clean` removes these generated files.

Gallery previews live in `images/thumbnails/`; clicking them opens the original
photo. After adding or replacing photos in `gallery.md`, regenerate the previews
on macOS with `python3 scripts/generate-gallery-thumbnails.py`.

People-card previews and homepage covers use WebP, with originals retained in
`images/`. Regenerate them with `python3 scripts/optimize-page-images.py` on macOS
(requires `sips` and `cwebp`; install the encoder with `brew install webp`).

Historical page/data backups are kept in `_archive/`, outside the published site.
Development scripts, tools, design notes and temporary files are excluded through
`_config.yml`. PDF and download links retain their existing paths.

