import os
import sys

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

files = ['index.html', 'style.css', 'config.js', 'script.js']
for f in files:
    assert os.path.exists(f), f'{f} missing!'
    size = os.path.getsize(f)
    print(f'[OK] {f} exists ({size} bytes)')

assets = [
    'assets/gold_ganesha.png',
    'assets/ganesha_line_clean.png',
    'assets/mangal_parinay_clean.png',
    'assets/palki_clean.png',
    'assets/elephant_right_clean.png',
    'assets/phere_clean.png'
]
for a in assets:
    assert os.path.exists(a), f'{a} missing!'
    print(f'[OK] {a} exists ({os.path.getsize(a)} bytes)')

# Check index.html for critical elements
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

required_ids = [
    'curtainOverlay', 'openCurtainBtn', 'curtainLeft', 'curtainRight', 'curtainCard',
    'welcomeSection',
    'brideDisplayName', 'groomDisplayName', 'familyWelcomeMsg',
    'countdownSection', 'timerGrid', 'cdDays', 'cdHours', 'cdMinutes', 'cdSeconds',
    'eventsSection', 'eventsTimelineContainer',
    'dinnerSection', 'dinnerTitle', 'dinnerTimeText',
    'venueSection', 'mainVenueName', 'googleMapsDirectionsBtn',
    'familySection', 'vineetList', 'swagataturList', 'visheshAagrahList', 'snehakankshiTags', 'balManuharPoem', 'nanihalText',
    'musicToggleBtn', 'addToCalendarBtn'
]

for rid in required_ids:
    assert f'id="{rid}"' in html, f'Missing ID in HTML: {rid}'

print('[OK] All required core IDs present in index.html')

# Verify that guest link generator elements are completely absent
removed_ids = [
    'personalizedGuestBadge', 'personalizedGuestName', 'curtainGuestBox', 'curtainGuestName',
    'guestToolSection', 'guestInputBox', 'generateLinkBtn', 'generatedLinkContainer',
    'generatedUrlText', 'copyLinkBtn', 'shareWhatsAppBtn', 'copySuccessToast'
]

for rid in removed_ids:
    assert f'id="{rid}"' not in html, f'Removed ID still present in HTML: {rid}'

print('[OK] Confirmed: All guest link generator elements completely removed from index.html')

# Verify script.js and style.css don't have guest generator logic
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

for term in ['initGuestPersonalization', 'initGuestLinkGenerator', 'getGuestInvitationBaseUrl', 'guestInputBox', 'shareWhatsAppBtn']:
    assert term not in js, f'Unwanted term {term} still in script.js'

print('[OK] Confirmed: script.js is completely clean of guest generator code')

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

for term in ['.guest-tool-section', '.guest-welcome-card', '.curtain-guest-box', '.btn-whatsapp-share']:
    assert term not in css, f'Unwanted term {term} still in style.css'

print('[OK] Confirmed: style.css is completely clean of guest generator styles')

# Verify Google Maps Link in config and html
with open('config.js', 'r', encoding='utf-8') as f:
    cfg = f.read()

assert 'https://maps.app.goo.gl/TqL9FSjMvaf4qETZ8' in cfg, 'Maps link missing in config!'
assert '2026-11-20T17:00:00+05:30' in cfg, 'Wedding ISO target date missing in config!'
print('[OK] Config verified with exact Maps link and ISO date')
print('ALL VERIFICATION CHECKS PASSED SUCCESSFULLY!')
