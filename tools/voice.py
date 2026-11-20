"""Record a game's voice lines with a macOS voice and embed them in the game file (so they work offline, on any device).

Usage: python3 tools/voice.py games/NAME.html ["Voice Name"]

Lines live in the game's <script id="voice-lines" type="application/json"> block; the audio goes into
<script id="voice-data">. With no voice given, the best installed English voice is used (Premium > Enhanced).
"""
import base64, json, pathlib, re, subprocess, sys, tempfile

game = pathlib.Path(sys.argv[1])
installed = re.findall(r'^(.+?)\s+en_\w+\s+#', subprocess.run(['say', '-v', '?'], capture_output=True, text=True).stdout, re.M)
voice = sys.argv[2] if len(sys.argv) > 2 else next((v for tag in ('(Premium)', '(Enhanced)') for v in installed if tag in v), 'Samantha')

html = game.read_text()
lines = json.loads(re.search(r'<script id="voice-lines" type="application/json">(.*?)</script>', html, re.S).group(1))
clips = {}
with tempfile.TemporaryDirectory() as d:
    for key, text in lines.items():
        aiff, m4a = f'{d}/{key}.aiff', f'{d}/{key}.m4a'
        subprocess.run(['say', '-v', voice, '-o', aiff, text], check=True)
        subprocess.run(['afconvert', '-f', 'm4af', '-d', 'aac', '-c', '1', '-b', '48000', aiff, m4a], check=True)
        clips[key] = base64.b64encode(pathlib.Path(m4a).read_bytes()).decode()

data = '<script id="voice-data">window.VOICE = ' + json.dumps(clips) + ';</script>'
game.write_text(re.sub(r'<script id="voice-data">.*?</script>', lambda _: data, html, flags=re.S))
print(f'{len(clips)} lines, {sum(map(len, clips.values())) // 1024} KB, voice: {voice}')
