# Game Box

A 6-year-old describes a game out loud (her dad types it), and we build it. Keep the back-and-forth
kid-sized: ask at most one simple question at a time, get something playable on screen fast, then tweak
what she asks for. Her ideas win, even weird ones.

This repo is PUBLIC (GitHub Pages). Never put her name, photos, voice, or any personal details in any file
or commit message.

## Every game

- One self-contained file: `games/<short-name>.html`. No libraries, no CDNs, no fonts or images from the
  internet: it must work offline. Art = emoji, CSS shapes, or inline SVG. Sound = Web Audio beeps
  (start audio on first tap, iOS needs it).
- `<meta name="robots" content="noindex, nofollow">` in the `<head>`.
- Works with touch (iPad/phone) AND mouse/keyboard. Big tap targets, nothing hover-only.
- Fills the screen, no scrolling or pinch-zoom: viewport meta with `user-scalable=no`,
  `touch-action: none` on the play area, resize with the window (portrait and landscape).
- Barely any reading: pictures, big emoji, sounds, a cheerful "🎉" when she wins.
- Gentle: easy to win, nothing scary, losing just restarts instantly.
- A big 🏠 button in the top-left corner linking to `../index.html`.
- Add its button to the `#games` list in `index.html`: `<a href="games/NAME.html"><span>EMOJI</span>Name</a>`
  (that list is also what gets pre-downloaded for offline play).
- Open it locally (`open games/NAME.html`) so she can play right away.
- When she's happy with it: `git add -A && git commit -m "Add NAME" && git push`.
  It's live on the iPad/phone/Mac about a minute later: https://alonp-od.github.io/game-box/
