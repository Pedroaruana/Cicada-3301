(function() {
  var path = window.location.pathname;

  var fases = {
    '/fase/1': 1,
    '/fase/x7k2m9q3p5r8t4v6wz': 2,
    '/fase/p3n8w': 3,
    '/fase/sombra': 4,
    '/fase/nexus': 5
  };

  var faseAtual = fases[path];
  if (!faseAtual) return;

  var chaveTimer = 'cicada_fase' + faseAtual + '_inicio';
  var chaveVisitas = 'cicada_fase' + faseAtual + '_visitas';

  if (!sessionStorage.getItem(chaveTimer)) {
    sessionStorage.setItem(chaveTimer, Date.now());
  }

  var visitas = parseInt(sessionStorage.getItem(chaveVisitas) || '0') + 1;
  sessionStorage.setItem(chaveVisitas, visitas);

  var timer = document.createElement('div');
  timer.className = 'tracker-hud';
  timer.innerHTML =
    '<span class="tracker-item" id="tracker-tempo">00:00</span>' +
    '<span class="tracker-sep">|</span>' +
    '<span class="tracker-item">TENTATIVA ' + visitas + '</span>';
  document.body.appendChild(timer);

  var inicio = parseInt(sessionStorage.getItem(chaveTimer));

  function atualizarTempo() {
    var agora = Date.now();
    var diff = Math.floor((agora - inicio) / 1000);
    var min = String(Math.floor(diff / 60)).padStart(2, '0');
    var seg = String(diff % 60).padStart(2, '0');
    var el = document.getElementById('tracker-tempo');
    if (el) el.textContent = min + ':' + seg;
  }

  atualizarTempo();
  setInterval(atualizarTempo, 1000);
})();
