// The same DOM values, written safely.

function renderFragment() {
    const raw = location.hash;
    document.getElementById('out').textContent = raw;
}

function renderNote(node) {
    const note = node.textContent;
    document.querySelector('#note').innerHTML = DOMPurify.sanitize('<b>' + note + '</b>');
}

function renderTitle(input) {
    const title = input.getAttribute('data-title');
    document.getElementById('title').insertAdjacentHTML('beforeend', sanitizeHtml(title));
}

function renderStatic() {
    document.write('<p>static markup</p>');
}
