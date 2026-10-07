import os

svg_dir = 'frontend/public/assets/signs'
os.makedirs(svg_dir, exist_ok=True)

svgs = {
    'you.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#184562"/>
      <stop offset="100%" stop-color="#0e2b3d"/>
    </linearGradient>
  </defs>
  <rect width="320" height="200" rx="10" fill="url(#bg)"/>
  <g fill="#48cae4" stroke="#caf0f8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M40 135 L120 120 L120 160 L40 160 Z" fill="#0077b6"/>
    <rect x="120" y="110" width="55" height="50" rx="12" fill="#0096c7"/>
    <circle cx="145" cy="135" r="8" fill="#023e8a"/>
    <path d="M175 118 L245 118 C252 118 252 132 245 132 L175 132 Z" fill="#48cae4"/>
    <path d="M260 125 L285 125 M275 115 L285 125 L275 135" fill="none" stroke="#ffd166" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="160" y="42" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">ISL SIGN: YOU</text>
  <text x="160" y="65" fill="#90e0ef" font-size="12" font-family="sans-serif" text-anchor="middle">Direct index finger point toward partner</text>
</svg>''',

    'please.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#184562"/>
      <stop offset="100%" stop-color="#0e2b3d"/>
    </linearGradient>
  </defs>
  <rect width="320" height="200" rx="10" fill="url(#bg2)"/>
  <path d="M80 180 C80 120 120 95 180 95 C240 95 280 120 280 180 Z" fill="#0f3854" opacity="0.6"/>
  <g fill="#48cae4" stroke="#caf0f8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="130" y="110" width="60" height="55" rx="14" fill="#0096c7"/>
    <path d="M135 110 L135 75 C135 70 145 70 145 75 L145 110" fill="#48cae4"/>
    <path d="M148 110 L148 70 C148 65 158 65 158 70 L158 110" fill="#48cae4"/>
    <path d="M161 110 L161 73 C161 68 171 68 171 73 L171 110" fill="#48cae4"/>
    <path d="M174 110 L174 80 C174 75 184 75 184 80 L184 110" fill="#48cae4"/>
    <path d="M130 130 L110 120 C106 117 112 110 118 114 L130 122" fill="#48cae4"/>
    <path d="M210 115 A30 30 0 1 1 210 150" fill="none" stroke="#ffd166" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="4,3"/>
    <polygon points="215,110 210,122 202,114" fill="#ffd166"/>
  </g>
  <text x="160" y="38" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">ISL SIGN: PLEASE</text>
  <text x="160" y="58" fill="#90e0ef" font-size="12" font-family="sans-serif" text-anchor="middle">Open right palm rubbed in gentle circle on chest</text>
</svg>''',

    'hello.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#184562"/>
      <stop offset="100%" stop-color="#0e2b3d"/>
    </linearGradient>
  </defs>
  <rect width="320" height="200" rx="10" fill="url(#bg3)"/>
  <circle cx="110" cy="125" r="40" fill="#0f3854" opacity="0.7"/>
  <g fill="#48cae4" stroke="#caf0f8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M140 100 L200 85 C208 83 212 95 204 99 L145 120 Z" fill="#0096c7"/>
    <path d="M145 100 L215 85 C222 83 226 95 218 99 L150 120 Z" fill="#48cae4"/>
    <path d="M225 75 C245 78 260 90 270 105" fill="none" stroke="#ffd166" stroke-width="4" stroke-linecap="round"/>
    <polygon points="272,97 274,112 262,107" fill="#ffd166"/>
  </g>
  <text x="160" y="38" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">ISL SIGN: HELLO</text>
  <text x="160" y="58" fill="#90e0ef" font-size="12" font-family="sans-serif" text-anchor="middle">Open hand moved outward from temple/forehead</text>
</svg>''',

    'thank_you.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#184562"/>
      <stop offset="100%" stop-color="#0e2b3d"/>
    </linearGradient>
  </defs>
  <rect width="320" height="200" rx="10" fill="url(#bg4)"/>
  <g fill="#48cae4" stroke="#caf0f8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="90" cy="110" r="32" fill="#0f3854" opacity="0.7"/>
    <rect x="110" y="110" width="50" height="45" rx="10" fill="#0096c7"/>
    <path d="M120 110 L120 80 C120 74 130 74 130 80 L130 110" fill="#48cae4"/>
    <path d="M132 110 L132 76 C132 70 142 70 142 76 L142 110" fill="#48cae4"/>
    <path d="M144 110 L144 80 C144 74 154 74 154 80 L154 110" fill="#48cae4"/>
    <path d="M180 100 C215 95 245 105 270 125" fill="none" stroke="#ffd166" stroke-width="4" stroke-linecap="round"/>
    <polygon points="264,115 275,128 259,129" fill="#ffd166"/>
  </g>
  <text x="160" y="38" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">ISL SIGN: THANK YOU</text>
  <text x="160" y="58" fill="#90e0ef" font-size="12" font-family="sans-serif" text-anchor="middle">Fingertips touch chin, then extend flat toward person</text>
</svg>''',

    'sorry.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="100%">
  <defs>
    <linearGradient id="bg5" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#184562"/>
      <stop offset="100%" stop-color="#0e2b3d"/>
    </linearGradient>
  </defs>
  <rect width="320" height="200" rx="10" fill="url(#bg5)"/>
  <g fill="#48cae4" stroke="#caf0f8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="130" y="100" width="60" height="55" rx="18" fill="#0096c7"/>
    <circle cx="145" cy="118" r="7" fill="#48cae4"/>
    <circle cx="160" cy="118" r="7" fill="#48cae4"/>
    <circle cx="175" cy="118" r="7" fill="#48cae4"/>
    <path d="M205 105 A28 28 0 1 1 205 145" fill="none" stroke="#ffd166" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="4,3"/>
    <polygon points="210,100 205,112 197,104" fill="#ffd166"/>
  </g>
  <text x="160" y="38" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">ISL SIGN: SORRY</text>
  <text x="160" y="58" fill="#90e0ef" font-size="12" font-family="sans-serif" text-anchor="middle">Closed right fist rubbed in circle over center of chest</text>
</svg>''',

    'yes.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="100%">
  <defs>
    <linearGradient id="bg6" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#184562"/>
      <stop offset="100%" stop-color="#0e2b3d"/>
    </linearGradient>
  </defs>
  <rect width="320" height="200" rx="10" fill="url(#bg6)"/>
  <g fill="#48cae4" stroke="#caf0f8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="130" y="95" width="60" height="55" rx="18" fill="#0096c7"/>
    <path d="M220 85 L220 150 M210 140 L220 150 L230 140 M210 95 L220 85 L230 95" fill="none" stroke="#ffd166" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="160" y="38" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">ISL SIGN: YES</text>
  <text x="160" y="58" fill="#90e0ef" font-size="12" font-family="sans-serif" text-anchor="middle">Fist nodding vertically at wrist like a head nod</text>
</svg>''',

    'no.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="100%">
  <defs>
    <linearGradient id="bg7" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#184562"/>
      <stop offset="100%" stop-color="#0e2b3d"/>
    </linearGradient>
  </defs>
  <rect width="320" height="200" rx="10" fill="url(#bg7)"/>
  <g fill="#48cae4" stroke="#caf0f8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="130" y="115" width="60" height="50" rx="14" fill="#0096c7"/>
    <path d="M155 115 L155 75 C155 68 165 68 165 75 L165 115" fill="#48cae4"/>
    <path d="M130 65 L190 65 M140 55 L130 65 L140 75 M180 55 L190 65 L180 75" fill="none" stroke="#ffd166" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="160" y="38" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">ISL SIGN: NO</text>
  <text x="160" y="58" fill="#90e0ef" font-size="12" font-family="sans-serif" text-anchor="middle">Index finger waving side to side with slight head shake</text>
</svg>'''
}

for filename, content in svgs.items():
    path = os.path.join(svg_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Wrote {filename}')
