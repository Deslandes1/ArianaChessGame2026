"""
Ariana — smiling 19-year-old Black Haitian girl.
Returned as a self-contained SVG string so it can be embedded anywhere.
"""

_ARIANA_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <radialGradient id="avBg" cx="50%" cy="32%" r="80%">
      <stop offset="0%" stop-color="#4ab0ff"/>
      <stop offset="100%" stop-color="#0d4c80"/>
    </radialGradient>
    <linearGradient id="avSkin" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#a5714a"/>
      <stop offset="55%"  stop-color="#8a5636"/>
      <stop offset="100%" stop-color="#6b3f22"/>
    </linearGradient>
    <radialGradient id="avHair" cx="50%" cy="40%" r="70%">
      <stop offset="0%"   stop-color="#3a2010"/>
      <stop offset="60%"  stop-color="#1e0f08"/>
      <stop offset="100%" stop-color="#0a0503"/>
    </radialGradient>
  </defs>

  <circle cx="100" cy="100" r="97" fill="url(#avBg)"/>
  <circle cx="100" cy="100" r="97" fill="none" stroke="#ffd93b" stroke-width="3.5"/>

  <circle cx="100" cy="100" r="72" fill="url(#avHair)"/>
  <circle cx="34"  cy="78"  r="16" fill="#0a0503"/>
  <circle cx="40"  cy="118" r="15" fill="#0a0503"/>
  <circle cx="166" cy="78"  r="16" fill="#0a0503"/>
  <circle cx="160" cy="118" r="15" fill="#0a0503"/>
  <circle cx="46"  cy="46"  r="15" fill="#0a0503"/>
  <circle cx="154" cy="46"  r="15" fill="#0a0503"/>
  <circle cx="74"  cy="30"  r="15" fill="#0a0503"/>
  <circle cx="126" cy="30"  r="15" fill="#0a0503"/>
  <circle cx="100" cy="26"  r="16" fill="#0a0503"/>
  <ellipse cx="80" cy="58" rx="24" ry="12" fill="#4a2a15" opacity="0.55"/>
  <ellipse cx="120" cy="58" rx="18" ry="9"  fill="#4a2a15" opacity="0.4"/>

  <path d="M 34 200 C 40 168, 68 148, 100 148 L 100 200 Z" fill="#d21034"/>
  <path d="M 100 200 L 100 148 C 132 148, 160 168, 166 200 Z" fill="#00209f"/>
  <rect x="93" y="148" width="14" height="52" fill="#ffffff"/>
  <path d="M 82 152 L 100 174 L 118 152" fill="none" stroke="#ffffff"
        stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>

  <path d="M 86 128 L 86 152 Q 100 160, 114 152 L 114 128 Z" fill="#6b3f22"/>
  <path d="M 86 128 Q 100 140, 114 128 L 114 136 Q 100 148, 86 136 Z"
        fill="#4a2a15" opacity="0.55"/>

  <ellipse cx="100" cy="102" rx="40" ry="44" fill="url(#avSkin)"/>
  <ellipse cx="60"  cy="106" rx="7.5" ry="10.5" fill="#7a4828"/>
  <ellipse cx="140" cy="106" rx="7.5" ry="10.5" fill="#7a4828"/>
  <circle cx="60"  cy="118" r="4.5" fill="none" stroke="#ffd93b" stroke-width="2"/>
  <circle cx="140" cy="118" r="4.5" fill="none" stroke="#ffd93b" stroke-width="2"/>

  <path d="M 60 92 C 58 60, 78 40, 100 40 C 122 40, 142 60, 140 92
           C 136 76, 128 66, 120 62 C 116 74, 108 82, 100 82
           C 92 82, 84 74, 80 62 C 72 66, 64 76, 60 92 Z" fill="url(#avHair)"/>
  <path d="M 60 92 C 54 118, 52 148, 56 178 L 72 178
           C 66 148, 66 120, 68 100 Z" fill="url(#avHair)"/>
  <path d="M 140 92 C 146 118, 148 148, 144 178 L 128 178
           C 134 148, 134 120, 132 100 Z" fill="url(#avHair)"/>

  <path d="M 72 86 Q 80 80, 90 85"   stroke="#0a0503" stroke-width="3.8" fill="none" stroke-linecap="round"/>
  <path d="M 110 85 Q 120 80, 128 86" stroke="#0a0503" stroke-width="3.8" fill="none" stroke-linecap="round"/>

  <ellipse cx="82"  cy="102" rx="9.5" ry="10.5" fill="#ffffff"/>
  <ellipse cx="118" cy="102" rx="9.5" ry="10.5" fill="#ffffff"/>
  <ellipse cx="82"  cy="103" rx="6.4" ry="7.6"  fill="#2a1a0e"/>
  <ellipse cx="118" cy="103" rx="6.4" ry="7.6"  fill="#2a1a0e"/>
  <circle  cx="82"  cy="104" r="3.2" fill="#0a0503"/>
  <circle  cx="118" cy="104" r="3.2" fill="#0a0503"/>
  <circle  cx="84"  cy="100" r="2.4" fill="#ffffff"/>
  <circle  cx="120" cy="100" r="2.4" fill="#ffffff"/>
  <circle  cx="80"  cy="106" r="1.2" fill="#ffffff" opacity="0.85"/>
  <circle  cx="116" cy="106" r="1.2" fill="#ffffff" opacity="0.85"/>
  <path d="M 72 95 Q 82 89, 92 95"   stroke="#0a0503" stroke-width="2.8" fill="none" stroke-linecap="round"/>
  <path d="M 108 95 Q 118 89, 128 95" stroke="#0a0503" stroke-width="2.8" fill="none" stroke-linecap="round"/>

  <path d="M 99 108 Q 96 117, 99 119.5 Q 101 120.5, 103 119"
        stroke="#4a2a15" stroke-width="2.4" fill="none"
        stroke-linecap="round" stroke-linejoin="round"/>

  <ellipse cx="69"  cy="118" rx="10" ry="6" fill="#c25a3a" opacity="0.42"/>
  <ellipse cx="131" cy="118" rx="10" ry="6" fill="#c25a3a" opacity="0.42"/>

  <path d="M 83 124 Q 100 132, 117 124 Q 100 146, 83 124 Z" fill="#5a1f2a"/>
  <path d="M 85 125 Q 100 131.5, 115 125 Q 100 137, 85 125 Z" fill="#ffffff"/>
  <path d="M 87 133 Q 100 142, 113 133" stroke="#7a2a3a" stroke-width="1.4"
        fill="none" stroke-linecap="round"/>

  <g transform="translate(138 58) rotate(12)">
    <rect x="-11" y="-7" width="22" height="14" rx="3" fill="#00209f"/>
    <rect x="-11" y="0"  width="22" height="7"  rx="3" fill="#d21034"/>
    <rect x="-11" y="-7" width="22" height="14" rx="3" fill="none"
          stroke="#ffd93b" stroke-width="1.5"/>
    <circle cx="0" cy="0" r="1.8" fill="#ffffff"/>
  </g>
</svg>
"""


def get_ariana_svg() -> str:
    """Return Ariana's cartoon avatar as an inline SVG string."""
    return _ARIANA_SVG.strip()
