#!/usr/bin/env python3
"""
Bilim Tarihi ve Felsefesi ders notları için vektörel (SVG) diyagram üretici.
Bu betik ders notlarındaki kilit felsefi ve mantıksal kavramları görselleştiren
kristal netliğinde modern, koyu temalı SVG diyagramları üretir.
"""

import os

ASSETS_DIR = "/home/antigravity/yusufsanverdi/Ders_Notlari/Bilim_Tarihi_Ve_Felsefesi/assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def create_hukum_kategorileri_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500" width="100%" height="100%">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 22px; font-weight: 700; fill: #f8fafc; text-anchor: middle; }
      .subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; fill: #94a3b8; text-anchor: middle; }
      .box { rx: 12px; stroke-width: 2px; }
      .box-root { fill: #1e293b; stroke: #3b82f6; }
      .box-vacip { fill: #14532d; stroke: #22c55e; }
      .box-mumteni { fill: #7f1d1d; stroke: #ef4444; }
      .box-mumkun { fill: #1e3a8a; stroke: #60a5fa; }
      .box-sub { fill: #334155; stroke: #94a3b8; }
      .box-muhal { fill: #581c87; stroke: #a855f7; }
      .node-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 16px; font-weight: 700; fill: #ffffff; text-anchor: middle; }
      .node-desc { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 12px; fill: #cbd5e1; text-anchor: middle; }
      .node-formula { font-family: "Courier New", monospace; font-size: 13px; font-weight: 600; fill: #fef08a; text-anchor: middle; }
      .line { stroke: #64748b; stroke-width: 2px; stroke-dasharray: 4,4; }
      .line-solid { stroke: #38bdf8; stroke-width: 2.5px; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="16"/>

  <text x="450" y="45" class="title">Mantıksal Hüküm Kategorileri (Akli Varlık Mertebeleri)</text>
  <text x="450" y="70" class="subtitle">Klasik Mantık ve Kelam Epistemolojisinde Önermelerin Akli Değerleri</text>

  <!-- Root: Hüküm Çeşitleri -->
  <rect x="350" y="95" width="200" height="55" class="box box-root"/>
  <text x="450" y="122" class="node-title">AKLİ HÜKÜMLER</text>
  <text x="450" y="140" class="node-desc">Varlığın Akli Değerlendirmesi</text>

  <!-- Connectors from Root -->
  <path d="M 450 150 L 450 180 L 150 180 L 150 210" class="line-solid" fill="none"/>
  <path d="M 450 150 L 450 210" class="line-solid" fill="none"/>
  <path d="M 450 150 L 450 180 L 750 180 L 750 210" class="line-solid" fill="none"/>

  <!-- 1. VACİP -->
  <rect x="50" y="210" width="200" height="110" class="box box-vacip"/>
  <text x="150" y="240" class="node-title">1. VACİP (Zorunlu)</text>
  <text x="150" y="265" class="node-desc">Yokluğu Aklen İmkânsız</text>
  <text x="150" y="285" class="node-desc">Olmak Zorunda Olan</text>
  <text x="150" y="307" class="node-formula">2 + 2 = 4 | Bütün &gt; Parça</text>

  <!-- 2. MÜMTENÎ -->
  <rect x="350" y="210" width="200" height="110" class="box box-mumteni"/>
  <text x="450" y="240" class="node-title">2. MÜMTENÎ (İmkânsız)</text>
  <text x="450" y="265" class="node-desc">Varlığı Aklen İmkânsız</text>
  <text x="450" y="285" class="node-desc">Sebep Olsa Bile Olamaz</text>
  <text x="450" y="307" class="node-formula">2 + 2 = 5 | 4 Köşeli Üçgen</text>

  <!-- 3. MÜMKÜN -->
  <rect x="650" y="210" width="200" height="110" class="box box-mumkun"/>
  <text x="750" y="240" class="node-title">3. MÜMKÜN (Olabilir)</text>
  <text x="750" y="265" class="node-desc">Varlığı ve Yokluğu Eşit</text>
  <text x="750" y="285" class="node-desc">Varlık İçin SEBEP Şarttır</text>
  <text x="750" y="307" class="node-formula">Evren, İnsan, Olaylar</text>

  <!-- Connectors from Mümkün to Subcategories -->
  <path d="M 750 320 L 750 350 L 630 350 L 630 370" class="line-solid" fill="none"/>
  <path d="M 750 320 L 750 350 L 790 350 L 790 370" class="line-solid" fill="none"/>

  <!-- Mümkün -> Muhtemel -->
  <rect x="540" y="370" width="180" height="95" class="box box-sub"/>
  <text x="630" y="398" class="node-title" style="fill:#38bdf8;">MUHTEMEL</text>
  <text x="630" y="420" class="node-desc">Pratikte ve Fiziken</text>
  <text x="630" y="438" class="node-desc">Gerçekleşebilir Durumlar</text>
  <text x="630" y="455" class="node-formula">Zarda 2 Defa 6 Gelmesi</text>

  <!-- Mümkün -> Muhal -->
  <rect x="740" y="370" width="150" height="95" class="box box-muhal"/>
  <text x="815" y="398" class="node-title" style="fill:#c084fc;">MUHAL</text>
  <text x="815" y="420" class="node-desc">Teoride Mümkün ama</text>
  <text x="815" y="438" class="node-desc">Pratikte İMKÂNSIZ</text>
  <text x="815" y="455" class="node-formula">1000 Kere Çift 6 (36¹⁰⁰⁰)</text>
</svg>'''
    with open(os.path.join(ASSETS_DIR, "hukum_kategorileri.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def create_aristoteles_dort_neden_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500" width="100%" height="100%">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 22px; font-weight: 700; fill: #f8fafc; text-anchor: middle; }
      .subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; fill: #94a3b8; text-anchor: middle; }
      .card { rx: 12px; stroke-width: 2px; }
      .c-maddi { fill: #1e293b; stroke: #f59e0b; }
      .c-fail { fill: #1e293b; stroke: #3b82f6; }
      .c-sekli { fill: #1e293b; stroke: #10b981; }
      .c-gaye { fill: #1e293b; stroke: #ec4899; }
      .card-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 17px; font-weight: 700; text-anchor: middle; }
      .card-sub { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 12px; fill: #94a3b8; text-anchor: middle; }
      .item-bold { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; font-weight: 600; fill: #ffffff; }
      .item-val { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; fill: #cbd5e1; }
      .center-circle { fill: #0284c7; stroke: #38bdf8; stroke-width: 3px; }
      .center-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 15px; font-weight: 700; fill: #ffffff; text-anchor: middle; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="16"/>

  <text x="450" y="45" class="title">Aristoteles: Varlığın Dört Nedeni (Metafizik)</text>
  <text x="450" y="70" class="subtitle">Herhangi Bir Varlığın Meydana Gelmesi İçin Zorunlu 4 İlke</text>

  <!-- Central Target Object -->
  <circle cx="450" cy="270" r="65" class="center-circle"/>
  <text x="450" y="265" class="center-text">VARLIK</text>
  <text x="450" y="285" class="center-text">(Masa / Heykel)</text>

  <!-- 1. Maddî Neden (Sol Üst) -->
  <rect x="60" y="100" width="300" height="130" class="card c-maddi"/>
  <text x="210" y="130" class="card-title" style="fill:#f59e0b;">1. MADDÎ NEDEN (Causa Materialis)</text>
  <text x="210" y="150" class="card-sub">Nesnenin Hangi Maddeden Yapıldığı</text>
  <text x="80" y="180" class="item-bold">• Heykelde:</text><text x="175" y="180" class="item-val">Ahşap, Mermer, Tunç</text>
  <text x="80" y="205" class="item-bold">• Telefonda:</text><text x="175" y="205" class="item-val">Silikon, Bakır, Plastik, Lityum</text>

  <!-- 2. Fail Neden (Sağ Üst) -->
  <rect x="540" y="100" width="300" height="130" class="card c-fail"/>
  <text x="690" y="130" class="card-title" style="fill:#38bdf8;">2. FAİL NEDEN (Causa Efficiens)</text>
  <text x="690" y="150" class="card-sub">Maddeyi Şekillendiren Güç / Usta</text>
  <text x="560" y="180" class="item-bold">• Heykelde:</text><text x="655" y="180" class="item-val">Heykeltıraşın İradesi ve Eli</text>
  <text x="560" y="205" class="item-bold">• Telefonda:</text><text x="655" y="205" class="item-val">Mühendis, Fabrika, Tasarımcı</text>

  <!-- 3. Biçimsel Neden (Sol Alt) -->
  <rect x="60" y="310" width="300" height="130" class="card c-sekli"/>
  <text x="210" y="340" class="card-title" style="fill:#10b981;">3. BİÇİMSEL NEDEN (Causa Formalis)</text>
  <text x="210" y="360" class="card-sub">Nesnenin Aldığı Form ve Tasarım</text>
  <text x="80" y="390" class="item-bold">• Heykelde:</text><text x="175" y="390" class="item-val">İnsan Silüeti, Yüz Hissiyatı</text>
  <text x="80" y="415" class="item-bold">• Telefonda:</text><text x="175" y="415" class="item-val">Ekran, Kasa Geometrisi, Boyut</text>

  <!-- 4. Gayevî Neden (Sağ Alt) -->
  <rect x="540" y="310" width="300" height="130" class="card c-gaye"/>
  <text x="690" y="340" class="card-title" style="fill:#ec4899;">4. GAYEVÎ NEDEN (Causa Finalis)</text>
  <text x="690" y="360" class="card-sub">Varlığın Yapılış Amacı (Teleoloji)</text>
  <text x="560" y="390" class="item-bold">• Heykelde:</text><text x="655" y="390" class="item-val">Sanat, Anma, Ticaret</text>
  <text x="560" y="415" class="item-bold">• Telefonda:</text><text x="655" y="415" class="item-val">Haberleşme, Hesaplama, Ticaret</text>

  <!-- Connection Lines -->
  <line x1="360" y1="180" x2="410" y2="230" stroke="#f59e0b" stroke-width="2"/>
  <line x1="540" y1="180" x2="490" y2="230" stroke="#38bdf8" stroke-width="2"/>
  <line x1="360" y1="360" x2="410" y2="310" stroke="#10b981" stroke-width="2"/>
  <line x1="540" y1="360" x2="490" y2="310" stroke="#ec4899" stroke-width="2"/>
</svg>'''
    with open(os.path.join(ASSETS_DIR, "aristoteles_dort_neden.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def create_gercek_vs_hakikat_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <defs>
    <style>
      .bg { fill: #0b1329; }
      .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 22px; font-weight: 700; fill: #f8fafc; text-anchor: middle; }
      .subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; fill: #94a3b8; text-anchor: middle; }
      .col-box { rx: 14px; stroke-width: 2px; }
      .col-gercek { fill: #1e1b4b; stroke: #6366f1; }
      .col-hakikat { fill: #064e3b; stroke: #10b981; }
      .h-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 20px; font-weight: 700; text-anchor: middle; }
      .h-sub { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; fill: #cbd5e1; text-anchor: middle; }
      .row-label { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14px; font-weight: 700; fill: #facc15; }
      .row-content { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; fill: #e2e8f0; }
      .quote-box { rx: 8px; fill: #1e293b; stroke: #475569; stroke-width: 1px; }
      .quote-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 12px; fill: #f1f5f9; font-style: italic; }
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="16"/>

  <text x="450" y="40" class="title">Epistemolojik Karşılaştırma: Gerçek vs. Hakikat</text>
  <text x="450" y="65" class="subtitle">"Biz Hakikatçiyiz, Gerçekçi Değiliz — Ateist Gerçekliğe, İslam Hakikate Bakar"</text>

  <!-- Left: GERÇEK -->
  <rect x="50" y="90" width="370" height="350" class="col-box col-gercek"/>
  <text x="235" y="125" class="h-title" style="fill:#a5b4fc;">GERÇEK (Görünüş / Zahir)</text>
  <text x="235" y="148" class="h-sub">Beş Duyu Organıyla Algılanan İllüzyon</text>

  <text x="75" y="185" class="row-label">Kaynak:</text>
  <text x="145" y="185" class="row-content">Duyular (Göz, Kulak, Deri...)</text>

  <text x="75" y="215" class="row-label">Oda Örneği:</text>
  <text x="75" y="235" class="row-content">Duvarlar, masa ve sıralar hareketsiz,</text>
  <text x="75" y="255" class="row-content">sabit duruyor gibi görünür.</text>

  <text x="75" y="285" class="row-label">Güneş Örneği:</text>
  <text x="75" y="305" class="row-content">Güneş gökte dönüyor, sabah doğup</text>
  <text x="75" y="325" class="row-content">akşam batıyor gibi algılanır.</text>

  <rect x="70" y="345" width="330" height="75" class="quote-box"/>
  <text x="85" y="370" class="quote-text">Mahkeme Örneği: "Gördüğün gerçeği söyle,</text>
  <text x="85" y="390" class="quote-text">hakikate jüri ve hakim karar verir."</text>
  <text x="85" y="410" class="quote-text">Göz parmağı Güneş'ten büyük görebilir.</text>

  <!-- Right: HAKİKAT -->
  <rect x="480" y="90" width="370" height="350" class="col-box col-hakikat"/>
  <text x="665" y="125" class="h-title" style="fill:#34d399;">HAKİKAT (Asıl / Mahiyet)</text>
  <text x="665" y="148" class="h-sub">Akıl, Mantık ve Bilimle İdrak Edilen Asıl</text>

  <text x="505" y="185" class="row-label">Kaynak:</text>
  <text x="575" y="185" class="row-content">Akıl, Burhan ve Delil</text>

  <text x="505" y="215" class="row-label">Oda Örneği:</text>
  <text x="505" y="235" class="row-content">Dünya saniyede 30.5 km hızla top</text>
  <text x="505" y="255" class="row-content">güllesinden katbekat hızlı dönmektedir.</text>

  <text x="505" y="285" class="row-label">Güneş Örneği:</text>
  <text x="505" y="305" class="row-content">Güneş merkezdedir; Dünya kendi ekseninde</text>
  <text x="505" y="325" class="row-content">ve Güneş çevresinde dönmektedir.</text>

  <rect x="500" y="345" width="330" height="75" class="quote-box"/>
  <text x="515" y="370" class="quote-text">Kur'an Örneği (Neml Suresi, 88):</text>
  <text x="515" y="390" class="quote-text">"Sen dağları yerinde sabit görürsün (gerçek),</text>
  <text x="515" y="410" class="quote-text">oysa onlar bulutlar gibi geçmektedir (hakikat)."</text>
</svg>'''
    with open(os.path.join(ASSETS_DIR, "gercek_vs_hakikat.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def create_pil_sarj_mantigi_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 22px; font-weight: 700; fill: #f8fafc; text-anchor: middle; }
      .subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; fill: #94a3b8; text-anchor: middle; }
      .panel { rx: 12px; stroke-width: 2px; }
      .panel-sarj { fill: #1e293b; stroke: #38bdf8; }
      .panel-desarj { fill: #1e293b; stroke: #f43f5e; }
      .p-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 16px; font-weight: 700; text-anchor: middle; }
      .plate-pos { fill: #b91c1c; rx: 6px; }
      .plate-neg { fill: #1d4ed8; rx: 6px; }
      .plate-label { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 14px; font-weight: 700; fill: #ffffff; text-anchor: middle; }
      .desc-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 12px; fill: #cbd5e1; }
      .electron { fill: #facc15; stroke: #ca8a04; stroke-width: 1px; }
      .e-label { font-family: monospace; font-size: 10px; font-weight: 700; fill: #000; text-anchor: middle; }
      .arrow { stroke: #38bdf8; stroke-width: 3; fill: none; marker-end: url(#arrow-cyan); }
      .arrow-red { stroke: #f43f5e; stroke-width: 3; fill: none; marker-end: url(#arrow-rose); }
    </style>
    <marker id="arrow-cyan" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrow-rose" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#f43f5e"/>
    </marker>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="16"/>

  <text x="450" y="40" class="title">Şarj Yanılgısı: Piller Asla "Dolmaz" veya "Boşalmaz"</text>
  <text x="450" y="65" class="subtitle">Elektronlar Harcanmaz; Sadece İki Plaka Arasında Dengesizlik (Potansiyel Fark) Yaratılır</text>

  <!-- Left: ŞARJ DURUMU -->
  <rect x="50" y="90" width="370" height="350" class="panel panel-sarj"/>
  <text x="235" y="125" class="p-title" style="fill:#38bdf8;">1. ŞARJ EDİLİRKEN (Dış Güç Uygulanır)</text>
  <text x="75" y="150" class="desc-text">Şarj cihazı elektronları artı plakadan zorla çeker,</text>
  <text x="75" y="168" class="desc-text">eksi plakaya yığarak yüksek potansiyel fark üretir.</text>

  <!-- Plaka + (Fakir) -->
  <rect x="90" y="195" width="70" height="150" class="plate-pos"/>
  <text x="125" y="225" class="plate-label">+</text>
  <text x="125" y="245" class="plate-label">Kutup</text>
  <text x="125" y="275" class="desc-text" style="text-anchor:middle;">Elektron</text>
  <text x="125" y="295" class="desc-text" style="text-anchor:middle;">Fakiri</text>

  <!-- Flow Arrow -->
  <path d="M 175 240 Q 235 200 295 240" class="arrow"/>
  <text x="235" y="215" class="desc-text" style="fill:#38bdf8; text-anchor:middle; font-weight:700;">Dış Enerji İle Zorlama</text>

  <!-- Plaka - (Zengin) -->
  <rect x="310" y="195" width="70" height="150" class="plate-neg"/>
  <text x="345" y="225" class="plate-label">-</text>
  <text x="345" y="245" class="plate-label">Kutup</text>
  <text x="345" y="275" class="desc-text" style="text-anchor:middle;">Elektron</text>
  <text x="345" y="295" class="desc-text" style="text-anchor:middle;">Yığını</text>

  <text x="75" y="380" class="desc-text" style="font-weight:700; fill:#fef08a;">• Pilin ağırlığı 1 pikogram bile DEĞİŞMEZ!</text>
  <text x="75" y="405" class="desc-text">• Şarj = Bileşik kapta suyu pistonla tek tarafa yığmaktır.</text>

  <!-- Right: DEŞARJ (KULLANIM) DURUMU -->
  <rect x="480" y="90" width="370" height="350" class="panel panel-desarj"/>
  <text x="665" y="125" class="p-title" style="fill:#f43f5e;">2. DEŞARJ OLURKEN (Cihaz Çalışırken)</text>
  <text x="505" y="150" class="desc-text">Telefonu açtığınızda vanalar açılır; elektronlar</text>
  <text x="505" y="168" class="desc-text">eksi kutuptan artı kutba akarken lambayı/çipi çalıştırır.</text>

  <!-- Plaka + -->
  <rect x="520" y="195" width="70" height="150" class="plate-pos"/>
  <text x="555" y="225" class="plate-label">+</text>
  <text x="555" y="245" class="plate-label">Kutup</text>
  <text x="555" y="280" class="desc-text" style="text-anchor:middle;">Elektronlar</text>
  <text x="555" y="300" class="desc-text" style="text-anchor:middle;">Buraya Döner</text>

  <!-- Flow Arrow Reverse -->
  <path d="M 725 240 Q 665 200 605 240" class="arrow-red"/>
  <text x="665" y="215" class="desc-text" style="fill:#f43f5e; text-anchor:middle; font-weight:700;">Yüke İş Yaptırarak Akış</text>

  <!-- Plaka - -->
  <rect x="740" y="195" width="70" height="150" class="plate-neg"/>
  <text x="775" y="225" class="plate-label">-</text>
  <text x="775" y="245" class="plate-label">Kutup</text>
  <text x="775" y="280" class="desc-text" style="text-anchor:middle;">Elektronlar</text>
  <text x="775" y="300" class="desc-text" style="text-anchor:middle;">Boşalır</text>

  <text x="505" y="380" class="desc-text" style="font-weight:700; fill:#fef08a;">• "Pil Bitti" = İki kutuptaki elektronlar eşitlendi demektir.</text>
  <text x="505" y="405" class="desc-text">• Fatura elektrona değil, elektronu taşıma işine ödenir.</text>
</svg>'''
    with open(os.path.join(ASSETS_DIR, "pil_sarj_mantigi.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def create_kuhn_paradigma_dongusu_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500" width="100%" height="100%">
  <defs>
    <style>
      .bg { fill: #0f172a; }
      .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 22px; font-weight: 700; fill: #f8fafc; text-anchor: middle; }
      .subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 13px; fill: #94a3b8; text-anchor: middle; }
      .step-box { rx: 10px; stroke-width: 2px; }
      .step-title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 15px; font-weight: 700; text-anchor: middle; }
      .step-desc { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 11px; fill: #cbd5e1; text-anchor: middle; }
      .arrow-line { stroke: #38bdf8; stroke-width: 2.5; fill: none; marker-end: url(#arrowhead); }
    </style>
    <marker id="arrowhead" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="16"/>

  <text x="450" y="45" class="title">Thomas Kuhn: Paradigma Kayması ve Bilimsel Devrimler</text>
  <text x="450" y="70" class="subtitle">Bilim Doğrusal ve Birikimsel Değil; Krizler ve Devrimsel Sıçramalarla İlerler</text>

  <!-- 1. Aşama: Olağan Bilim -->
  <rect x="330" y="105" width="240" height="70" class="step-box" style="fill:#1e293b; stroke:#10b981;"/>
  <text x="450" y="132" class="step-title" style="fill:#34d399;">1. OLAĞAN BİLİM</text>
  <text x="450" y="152" class="step-desc">Hâkim Paradigma Sorunları Çözer</text>
  <text x="450" y="167" class="step-desc">(Örn: Batlamyus Yer-Merkezli Model)</text>

  <!-- Ok 1 -> 2 -->
  <path d="M 570 140 Q 680 140 700 200" class="arrow-line"/>

  <!-- 2. Aşama: Anomaliler -->
  <rect x="620" y="210" width="230" height="70" class="step-box" style="fill:#1e293b; stroke:#f59e0b;"/>
  <text x="735" y="237" class="step-title" style="fill:#fbbf24;">2. ANOMALİLER</text>
  <text x="735" y="257" class="step-desc">Modelin Açıklayamadığı Olgular Artar</text>
  <text x="735" y="272" class="step-desc">(Gezegenlerin Geri Hareketi vb.)</text>

  <!-- Ok 2 -> 3 -->
  <path d="M 735 280 L 735 340 L 600 375" class="arrow-line"/>

  <!-- 3. Aşama: Bunalım / Kriz -->
  <rect x="360" y="360" width="240" height="75" class="step-box" style="fill:#1e293b; stroke:#ef4444;"/>
  <text x="480" y="387" class="step-title" style="fill:#f87171;">3. KRİZ / BUNALIM</text>
  <text x="480" y="407" class="step-desc">Güven Sarsılır; Çözümler Yetmez</text>
  <text x="480" y="422" class="step-desc">Eski Paradigma İflas Eder</text>

  <!-- Ok 3 -> 4 -->
  <path d="M 360 400 L 220 400 L 170 330" class="arrow-line"/>

  <!-- 4. Aşama: Bilimsel Devrim -->
  <rect x="50" y="250" width="240" height="75" class="step-box" style="fill:#1e293b; stroke:#ec4899;"/>
  <text x="170" y="277" class="step-title" style="fill:#f472b6;">4. BİLİMSEL DEVRİM</text>
  <text x="170" y="297" class="step-desc">Yeni Bir Bakış Açısı / Model Doğar</text>
  <text x="170" y="312" class="step-desc">(Kopernik &amp; Bîrûnî: Güneş-Merkezli)</text>

  <!-- Ok 4 -> 1 -->
  <path d="M 170 250 L 170 170 L 320 145" class="arrow-line"/>

  <!-- Merkez Özet -->
  <circle cx="450" cy="265" r="50" style="fill:#0369a1; stroke:#38bdf8; stroke-width:2px;"/>
  <text x="450" y="260" class="step-title" style="fill:#ffffff; font-size:13px;">PARADİGMA</text>
  <text x="450" y="278" class="step-title" style="fill:#ffffff; font-size:13px;">KAYMASI</text>
</svg>'''
    with open(os.path.join(ASSETS_DIR, "kuhn_paradigma_dongusu.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    print("Diyagramlar üretiliyor...")
    create_hukum_kategorileri_svg()
    create_aristoteles_dort_neden_svg()
    create_gercek_vs_hakikat_svg()
    create_pil_sarj_mantigi_svg()
    create_kuhn_paradigma_dongusu_svg()
    print("Tüm diyagramlar başarıyla oluşturuldu:")
    for f in os.listdir(ASSETS_DIR):
        print(f" - {f}")
