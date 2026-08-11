// DOM text read back into the page as HTML - DOM XSS.

function renderFragment() {
    const raw = location.hash;
    // ruleid:dom_xss
    document.getElementById('out').innerHTML = raw;
}

function renderNote(node) {
    const note = node.textContent;
    const wrapper = '<b>' + note + '</b>';
    // ruleid:dom_xss
    document.querySelector('#note').outerHTML = wrapper;
}

function renderTitle(input) {
    const title = input.getAttribute('data-title');
    // ruleid:dom_xss
    document.getElementById('title').insertAdjacentHTML('beforeend', title);
}

function renderReferrer() {
    // ruleid:dom_xss
    document.write(document.referrer);
}
