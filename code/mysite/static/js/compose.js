window.onload = () => {
  $('#tabs.tabs').tabs();
}

function parseMd() {
  let md = $('#markdown-content')[0].value;


  // in the response block
  let md_preview = $('#md-preview')[0];
  md_preview.innerHTML = `<h3>this should be h3</h3>
    <script src="https://gist.github.com/ishankhare07/ffc0d1dacfcec3c4a057aca22b4c9fe0.js"></script>
  `
}
