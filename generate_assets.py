#!/usr/bin/env python3
"""
Gerador de Assets Visuais para AquaPlay Deluxe 4U
Gera ícones PWA e Banner 16:9 oficial
"""

import math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    pad = size * 0.04
    corner = size * 0.18

    # Carcaça amarela vintage do brinquedo
    toy_box = [pad, pad, size - pad, size - pad]
    # Sombra externa
    shadow_box = [pad + size * 0.02, pad + size * 0.03, size - pad + size * 0.02, size - pad + size * 0.03]
    draw.rounded_rectangle(shadow_box, radius=corner, fill=(0, 20, 40, 100))

    # Corpo de plástico amarelo
    for i in range(int(size * 0.06)):
        alpha_val = int(255 - i * 2)
        inset_box = [pad + i, pad + i, size - pad - i, size - pad - i]
        draw.rounded_rectangle(inset_box, radius=max(2, corner - i), fill=(255, 190 + int(i * 0.8), 20 + i))

    # Visor acrílico de água
    screen_pad = size * 0.14
    screen_box = [screen_pad, screen_pad, size - screen_pad, size - screen_pad]
    # Moldura interna do visor
    draw.rounded_rectangle(screen_box, radius=corner * 0.7, fill=(210, 150, 20))
    
    inner_screen_pad = size * 0.16
    inner_screen_box = [inner_screen_pad, inner_screen_pad, size - inner_screen_pad, size - inner_screen_pad]
    draw.rounded_rectangle(inner_screen_box, radius=corner * 0.6, fill=(28, 140, 215))

    # Gradiente de profundidade da água
    for y in range(int(inner_screen_box[1]), int(inner_screen_box[3])):
        ratio = (y - inner_screen_box[1]) / (inner_screen_box[3] - inner_screen_box[1])
        r = int(70 * (1 - ratio) + 15 * ratio)
        g = int(180 * (1 - ratio) + 110 * ratio)
        b = int(245 * (1 - ratio) + 200 * ratio)
        draw.line([(inner_screen_box[0], y), (inner_screen_box[2], y)], fill=(r, g, b, 255))

    # Reflexo de vidro acrílico
    refl_box = [inner_screen_pad + 4, inner_screen_pad + 4, size - inner_screen_pad - 4, inner_screen_pad + size * 0.22]
    draw.ellipse(refl_box, fill=(255, 255, 255, 45))

    # Haste central (Spike)
    spike_x = size * 0.5
    spike_base_y = inner_screen_box[3] - size * 0.04
    spike_top_y = inner_screen_box[1] + size * 0.18
    draw.line([(spike_x, spike_base_y), (spike_x, spike_top_y)], fill=(240, 240, 240, 230), width=int(size * 0.025))
    # Braços da haste
    arm_w = size * 0.07
    draw.line([(spike_x - arm_w, spike_top_y + size * 0.04), (spike_x, spike_top_y + size * 0.08), (spike_x + arm_w, spike_top_y + size * 0.04)], fill=(240, 240, 240, 230), width=int(size * 0.02))

    # Bolhas decorativas
    random.seed(42)
    for _ in range(18):
        bx = random.uniform(inner_screen_box[0] + 15, inner_screen_box[2] - 15)
        by = random.uniform(inner_screen_box[1] + 15, inner_screen_box[3] - 15)
        br = random.uniform(size * 0.012, size * 0.028)
        draw.ellipse([bx - br, by - br, bx + br, by + br], fill=(255, 255, 255, 120), outline=(255, 255, 255, 180), width=1)
        draw.ellipse([bx - br * 0.4, by - br * 0.4, bx - br * 0.1, by - br * 0.1], fill=(255, 255, 255, 220))

    # Argolas flutuantes coloridas (Toróides em 3D)
    ring_colors = [
        ((235, 45, 45), size * 0.5, spike_top_y + size * 0.09, 0),       # Vermelha na haste
        ((250, 210, 30), size * 0.5, spike_top_y + size * 0.13, 0),      # Amarela na haste
        ((60, 210, 80), size * 0.34, size * 0.48, -0.3),                 # Verde flutuando
        ((160, 50, 220), size * 0.66, size * 0.42, 0.4),                 # Roxa flutuando
        ((250, 130, 30), size * 0.38, size * 0.65, 0.2),                 # Laranja flutuando
    ]

    for col, rx, ry, tilt in ring_colors:
        outer_r = size * 0.065
        inner_r = size * 0.035
        # Sombra da argola
        draw.ellipse([rx - outer_r + 2, ry - outer_r * 0.6 + 3, rx + outer_r + 2, ry + outer_r * 0.6 + 3], fill=(0, 40, 80, 80))
        # Corpo da argola
        draw.ellipse([rx - outer_r, ry - outer_r * 0.6, rx + outer_r, ry + outer_r * 0.6], fill=col, outline=(255, 255, 255, 140), width=max(1, int(size * 0.008)))
        # Furo da argola (mostra o fundo)
        furo_color = (40, 150, 225)
        draw.ellipse([rx - inner_r, ry - inner_r * 0.6, rx + inner_r, ry + inner_r * 0.6], fill=furo_color, outline=(col[0] // 2, col[1] // 2, col[2] // 2, 160), width=1)

    # Botões inferiores (Pistões de borracha vermelho escuro)
    btn_r = size * 0.05
    # Botão Esquerdo
    btn_l_x = pad + size * 0.12
    btn_y = size - pad - size * 0.06
    draw.ellipse([btn_l_x - btn_r, btn_y - btn_r, btn_l_x + btn_r, btn_y + btn_r], fill=(210, 35, 35), outline=(150, 15, 15), width=2)
    draw.ellipse([btn_l_x - btn_r * 0.7, btn_y - btn_r * 0.7, btn_l_x + btn_r * 0.7, btn_y + btn_r * 0.7], fill=(235, 55, 55))
    
    # Botão Direito
    btn_r_x = size - pad - size * 0.12
    draw.ellipse([btn_r_x - btn_r, btn_y - btn_r, btn_r_x + btn_r, btn_y + btn_r], fill=(210, 35, 35), outline=(150, 15, 15), width=2)
    draw.ellipse([btn_r_x - btn_r * 0.7, btn_y - btn_r * 0.7, btn_r_x + btn_r * 0.7, btn_y + btn_r * 0.7], fill=(235, 55, 55))

    # Parafusos nas 4 quinas
    screw_r = size * 0.016
    screws = [
        (pad + size * 0.06, pad + size * 0.06),
        (size - pad - size * 0.06, pad + size * 0.06),
        (pad + size * 0.06, size - pad - size * 0.06),
        (size - pad - size * 0.06, size - pad - size * 0.06)
    ]
    for sx, sy in screws:
        draw.ellipse([sx - screw_r, sy - screw_r, sx + screw_r, sy + screw_r], fill=(180, 180, 180), outline=(120, 120, 120), width=1)
        draw.line([(sx - screw_r * 0.7, sy), (sx + screw_r * 0.7, sy)], fill=(100, 100, 100), width=max(1, int(size * 0.005)))

    return img

def create_banner():
    w, h = 1024, 576
    img = Image.new('RGB', (w, h), (12, 28, 48))
    draw = ImageDraw.Draw(img)

    # Fundo oceânico com degradê
    for y in range(h):
        ratio = y / h
        r = int(10 * (1 - ratio) + 4 * ratio)
        g = int(45 * (1 - ratio) + 20 * ratio)
        b = int(95 * (1 - ratio) + 55 * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Bolhas de luz no fundo (Bokeh)
    random.seed(1985)
    for _ in range(40):
        bx = random.randint(0, w)
        by = random.randint(0, h)
        br = random.randint(15, 80)
        alpha = random.randint(10, 30)
        draw.ellipse([bx - br, by - br, bx + br, by + br], fill=(30 + alpha, 100 + alpha, 180 + alpha))

    # Ilustração do AquaPlay no lado direito
    icon_sub = create_icon(440)
    img.paste(icon_sub, (530, 68), icon_sub)

    # Textos e Badges no lado esquerdo
    # Badge topo: NOSTALGIA ANOS 80 & 90
    draw.rounded_rectangle([60, 65, 340, 98], radius=8, fill=(235, 45, 45))
    draw.text((75, 74), "★ NOSTALGIA RETRÔ ANOS 80 & 90 ★", fill=(255, 255, 255))

    # Título Principal
    # Carregar fontes TrueType caso existam, senão default
    title_text = "AQUAPLAY"
    sub_title = "DELUXE 4U"
    
    # Desenho estilizado do título
    draw.text((60, 125), title_text, fill=(255, 205, 30))
    draw.text((60, 205), sub_title, fill=(50, 215, 255))
    
    desc_lines = [
        "O clássico brinquedo aquático portátil da Estrela & Tomy",
        "recriado com física de água realista, bombas duplas,",
        "modos Argolas & Basquete, sons sintetizados e PWA!"
    ]
    y_off = 280
    for line in desc_lines:
        draw.text((60, y_off), line, fill=(210, 230, 245))
        y_off += 24

    # Recursos (Pills/Badges)
    badges = [
        ("💨 BOMBA DUPLA 3D", (40, 140, 210)),
        ("🏀 ARGOLAS & BASQUETE", (230, 120, 25)),
        ("🌊 FÍSICA & GIROSCÓPIO", (40, 185, 120)),
        ("🔊 WEB AUDIO REALISTA", (160, 50, 220)),
        ("📱 PWA 100% OFFLINE", (235, 45, 75))
    ]

    bx_start, by_start = 60, 385
    cur_x, cur_y = bx_start, by_start
    for text, bg_col in badges:
        bw = len(text) * 8 + 24
        if cur_x + bw > 500:
            cur_x = bx_start
            cur_y += 38
        draw.rounded_rectangle([cur_x, cur_y, cur_x + bw, cur_y + 28], radius=6, fill=bg_col)
        draw.text((cur_x + 12, cur_y + 8), text, fill=(255, 255, 255))
        cur_x += bw + 12

    # Rodapé institucional
    draw.text((60, 515), "4U.IA.BR • Ecossistema de Aplicações de Alta Performance", fill=(140, 175, 205))

    return img

def main():
    base_dir = '/home/fabiano/public_html/app/aquaplay'
    print("🎨 Gerando ícones PWA e Banner...")
    
    # 512x512
    icon512 = create_icon(512)
    icon512.save(f"{base_dir}/icon-512.png")
    print("  ✓ icon-512.png")

    # 192x192
    icon192 = icon512.resize((192, 192), Image.Resampling.LANCZOS)
    icon192.save(f"{base_dir}/icon-192.png")
    print("  ✓ icon-192.png")

    # apple-touch-icon 180x180
    icon180 = icon512.resize((180, 180), Image.Resampling.LANCZOS)
    icon180.save(f"{base_dir}/apple-touch-icon.png")
    print("  ✓ apple-touch-icon.png")

    # favicon 64x64
    icon64 = icon512.resize((64, 64), Image.Resampling.LANCZOS)
    icon64.save(f"{base_dir}/favicon.png")
    print("  ✓ favicon.png")

    # Banner 16:9 1024x576
    banner = create_banner()
    banner.save(f"{base_dir}/banner-16-9.jpg", quality=92)
    print("  ✓ banner-16-9.jpg")

    print("🎉 Todos os assets visuais foram gerados com sucesso!")

if __name__ == '__main__':
    main()
