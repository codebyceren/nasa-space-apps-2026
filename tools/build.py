#!/usr/bin/env python3
"""Mission Mars build script.

src/mission-mars.src.html  (ES-module source, Three.js from CDN import map,
                            texture placeholders like __MARS_TEX__)
        │ 1. embed textures from src/textures/ as data URIs
        ▼
dist/mission-mars-dev.html     (needs internet for Three.js CDN)
        │ 2. bundle the module script + Three.js with esbuild (IIFE, minified)
        ▼
dist/mission-mars-offline.html (one self-contained file, works offline)
        │ 3. add PWA manifest/meta + service-worker registration
        ▼
index.html + sw.js             (what GitHub Pages serves, repo root)

Usage:  npm install   then   npm run build   (or: python3 tools/build.py)
"""
import base64, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
VERSION = 'v17'

TEX = {'__MARS_TEX__': 'mars2k.jpg', '__MARS_N__': 'mars_n.jpg', '__EARTH_DAY__': 'earth_day.jpg',
       '__EARTH_CLOUDS2__': 'earth_clouds2.jpg', '__EARTH_SPEC2__': 'earth_spec2.jpg', '__EARTH_NIGHT__': 'earth_night.jpg'}

def main():
    os.makedirs(P('dist'), exist_ok=True)
    # 1. textures
    s = open(P('src', 'mission-mars.src.html'), encoding='utf-8').read()
    for key, f in TEX.items():
        data = base64.b64encode(open(P('src', 'textures', f), 'rb').read()).decode()
        s = s.replace(key, 'data:image/jpeg;base64,' + data)
    assert '__EARTH' not in s and '__MARS' not in s, 'a texture placeholder was not replaced'
    open(P('dist', 'mission-mars-dev.html'), 'w', encoding='utf-8').write(s)
    # 2. bundle
    a = s.index('<script type="module">'); b = s.index('</script>', a)
    open(P('dist', 'entry.js'), 'w', encoding='utf-8').write(s[a + len('<script type="module">'):b])
    esb = P('node_modules', '.bin', 'esbuild.cmd' if os.name == 'nt' else 'esbuild')
    if not os.path.exists(esb):
        sys.exit('esbuild not found: run "npm install" first')
    subprocess.run([esb, P('dist', 'entry.js'), '--bundle', '--format=iife', '--minify', '--outfile=' + P('dist', 'bundle.js'),
                    '--alias:three/addons=' + P('node_modules', 'three', 'examples', 'jsm'),
                    '--alias:three=' + P('node_modules', 'three', 'build', 'three.module.js'), '--log-level=warning'], check=True)
    bun = open(P('dist', 'bundle.js'), encoding='utf-8').read().replace('</script', '<\\/script')
    im0 = s.index('<script type="importmap">'); im1 = s.index('</script>', im0) + 9
    off = s[:im0] + s[im1:a] + '<script>' + bun + '</script>' + s[b + 9:]
    open(P('dist', 'mission-mars-offline.html'), 'w', encoding='utf-8').write(off)
    for f in ('entry.js', 'bundle.js'):
        os.remove(P('dist', f))
    # 3. PWA
    head = open(P('src', 'pwa-head.html'), encoding='utf-8').read()
    tail = open(P('src', 'pwa-tail.html'), encoding='utf-8').read()
    page = off.replace('<title>', head + '<title>', 1)
    i = page.rindex('</body>'); page = page[:i] + tail + page[i:]
    open(P('index.html'), 'w', encoding='utf-8').write(page)
    sw = open(P('src', 'sw.template.js'), encoding='utf-8').read().replace('__VERSION__', VERSION)
    open(P('sw.js'), 'w', encoding='utf-8').write(sw)
    print('built: index.html (%d KB), dist/mission-mars-offline.html, dist/mission-mars-dev.html' % (os.path.getsize(P('index.html')) // 1024))

if __name__ == '__main__':
    main()
