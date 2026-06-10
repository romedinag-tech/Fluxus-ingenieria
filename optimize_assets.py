# -*- coding: utf-8 -*-
"""Optimiza las imagenes del sitio Fluxus. Conserva originales en assets/_orig/."""
import os, shutil
from PIL import Image

ASSETS = os.path.join(os.path.dirname(__file__), "assets")
ORIG = os.path.join(ASSETS, "_orig")
os.makedirs(ORIG, exist_ok=True)
NAVY = (7, 27, 53)  # #071B35, fondo para aplanar transparencias

# Fotos/renders -> JPEG (sin transparencia necesaria)
TO_JPEG = [
    "keyvisual.png", "profesional.png", "cam-ia.png", "buses.png",
    "prod-terminal.png", "prod-puerto.png", "prod-recinto.png",
    "prod-estudios.png", "prod-infra.png", "prod-logistica.png", "prod-urbano.png",
]
# Logos -> mantener PNG (transparencia) pero redimensionar
TO_PNG_RESIZE = {
    "logo-hero.png": 760,            # se muestra a 430px max (2x)
    "logo-hero-horizontal.png": 480, # header (~68px alto) + footer (40px)
}
MAX_W = 1600  # cap de ancho para fotos


def backup(name):
    src = os.path.join(ASSETS, name)
    dst = os.path.join(ORIG, name)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copy2(src, dst)


def kb(path):
    return os.path.getsize(path) // 1024


def to_jpeg(name):
    src = os.path.join(ASSETS, name)
    if not os.path.exists(src):
        return None
    backup(name)
    before = kb(src)
    im = Image.open(src).convert("RGBA")
    if im.width > MAX_W:
        h = round(im.height * MAX_W / im.width)
        im = im.resize((MAX_W, h), Image.LANCZOS)
    bg = Image.new("RGB", im.size, NAVY)
    bg.paste(im, mask=im.split()[-1])
    out = os.path.join(ASSETS, os.path.splitext(name)[0] + ".jpg")
    bg.save(out, "JPEG", quality=80, optimize=True, progressive=True)
    os.remove(src)  # original ya respaldado en _orig
    return before, kb(out), os.path.basename(out)


def resize_png(name, target_w):
    src = os.path.join(ASSETS, name)
    if not os.path.exists(src):
        return None
    backup(name)
    before = kb(src)
    im = Image.open(src).convert("RGBA")
    if im.width > target_w:
        h = round(im.height * target_w / im.width)
        im = im.resize((target_w, h), Image.LANCZOS)
    im.save(src, "PNG", optimize=True)
    return before, kb(src), name


print("== JPEG ==")
tot_b = tot_a = 0
for n in TO_JPEG:
    r = to_jpeg(n)
    if r:
        b, a, out = r
        tot_b += b; tot_a += a
        print(f"  {n:24} {b:5}KB -> {a:4}KB  ({out})")

print("== PNG (resize) ==")
for n, w in TO_PNG_RESIZE.items():
    r = resize_png(n, w)
    if r:
        b, a, _ = r
        tot_b += b; tot_a += a
        print(f"  {n:24} {b:5}KB -> {a:4}KB")

print(f"\nTOTAL: {tot_b}KB -> {tot_a}KB  (ahorro {tot_b-tot_a}KB, {100*(tot_b-tot_a)//tot_b}%)")
