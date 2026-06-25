from flask import Flask as f
app=f(__name__)
@app.route("/home")
def home():
    return "<h1> I am at home</h1>"
@app.route("/index")
def index():
  return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8Since "small and animated" is the goal, building a real-time multiplayer server is a bit heavy.">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pixel Duel Instead, here is a **Local PvP (Player vs Player) Battle** game. PvP</title>
    <style>
        body {
            background: #1a1a2e;
            color: white;
            font 

Two players can play on the same keyboard:
*   **Player 1 (Left):** Uses **`W`** to Jump, **`D-family: 'Segoe UI', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
`** to Attack.
*   **Player 2 (Right):** Uses **`Up Arrow`** to Jump            justify-content: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        , **`Left Arrow`** to Attack.
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mini PvP Duel</title>
    <style>
        body { background: #1a1a1a; display: flex; flex-direction: column; align-items: center; color: white; font-family: sans-serif; overflow: hidden; }
        #game { width: 600px; height: 300px; border-bottom: 4px solid #555; position: relative; overflow: hidden; background: linear-gradient(#1a1a1a, #2c3e50); }
        .player { width: 40px; height: 60px; position: absolute; bottom: 0; transition: transform 0.1s; border-radius: 4px; }
        #p1 { background: #ff4757; left: 50px; }
        #p2 { background: #2ed573; right: 50px; }
        .hp-bar { width: 200px; height: 20px; background: #333; border: 2px solid #fff; position: relative; }
        .hp-fill { height: 100%; width: 100%; transition: width 0.3s; }
        .ui { display: flex; gap: 50px; margin-bottom: 20px; margin-top: 20px; }
        .hit { animation: shake 0.2s; }
        @keyframes shake { 0% { margin-left: 0; } 25% { margin-left: 5px; } 50% { margin-left: -5px; } 100% { margin-left: 0; } }
        .sword { width: 40px; height: 10px; background: gold; position: absolute; top: 25px; display: none; }
        .p1-sword { right: -40px; }
        .p2-sword { left: -40px; }
    </style>
</head>
<body>
    <div class="ui">
        <div>P1: <div class="hp-bar"><div id="hp1" class="hp-fill" style="background: #ff4757;"></div></div></div>
        <div>P2: <div class="hp-bar"><div id="hp2" class="hp-fill" style="background: #2ed573;"></div></div></div>
    </div>
    <div id="game">
        <div id="p1" class="player"><div id="s1" class="sword p1-sword"></div></div>
        <div id="p2" class="player"><div id="s2" class="sword p2-sword"></div></div>
    </div>
    <p>P1: <b>W</b> Jump | <b>D</b> Attack &nbsp;&nbsp;&nbsp; P2: <b>↑</b> Jump | <b>←</b> Attack</p>

<script>
    const state = { p1: { hp: 100, pos: 50, jump: false }, p2: { hp: 100, pos: 50, jump: false } };

    window.addEventListener('keydown', (e) => {
        // Player 1 Actions
        if (e.key === 'w' && !state.p1.jump) jump('p1');
        if (e.key === 'd') attack('p1', 'p2');

        // Player 2 Actions
        if (e.key === 'ArrowUp' && !state.p2.jump) jump('p2');
        if (e.key === 'ArrowLeft') attack('p2', 'p1');
    });

    function jump(p) {
        state[p].jump = true;
        const el = document.getElementById(p);
        el.style.transform = "translateY(-100px)";
        setTimeout(() => { 
            el.style.transform = "translateY(0)";
            setTimeout(() => state[p].jump = false, 300);
        }, 300);
    }

    function attack(attacker, defender) {
        const sword = attacker === 'p1' ? document.getElementById('s1') : document.getElementById('s2');
        sword.style.display = 'block';
        
        // Simple hit detection (if both are on ground)
        if (!state[defender].jump) {
            state[defender].hp -= 10;
            updateUI();
            document.getElementById(defender).classList.add('hit');
            setTimeout(() => document.getElementById(defender).classList.remove('hit'), 200);
        }

        setTimeout(() => { sword.style.display = 'none'; }, 100);
    }

    function updateUI() {
        document.getElementById('hp1').style.width = state.p1.hp + "%";
        document.getElementById('hp2').style.width = state.p2.hp + "%";
        if (state.p1.hp <= 0) alert("Green Wins!");
        if (state.p2.hp <= 0) alert("Red Wins!");
        if (state.p1.hp <= 0 || state.p2.hp <= 0) location.reload();
    }
</script>
</body>
</html>
        
          """
app.run()