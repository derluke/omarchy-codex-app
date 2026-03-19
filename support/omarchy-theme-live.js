(function () {
  const link = document.querySelector('link[href^="./assets/omarchy-theme.css"]');
  if (!link) return;

  let lastHref = link.getAttribute("href") || "./assets/omarchy-theme.css";

  function refresh() {
    const nextHref = "./assets/omarchy-theme.css?v=" + Date.now();
    if (nextHref === lastHref) return;
    lastHref = nextHref;
    link.setAttribute("href", nextHref);
  }

  async function poll() {
    try {
      const res = await fetch("./assets/omarchy-theme.css?ts=" + Date.now(), {
        cache: "no-store",
      });
      const text = await res.text();
      const hash = text.length + ":" + text.slice(0, 256);
      if (poll.lastHash && poll.lastHash !== hash) refresh();
      poll.lastHash = hash;
    } catch (_) {}
  }

  poll();
  window.setInterval(poll, 1500);
})();
