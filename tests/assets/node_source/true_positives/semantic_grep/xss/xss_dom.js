// DOM text read back into the page as HTML - DOM XSS.

function renderFragment() {
    const raw = location.hash;
    document.getElementById('out').innerHTML = raw;
}

function renderNote(node) {
    const note = node.textContent;
    const wrapper = '<b>' + note + '</b>';
    document.querySelector('#note').outerHTML = wrapper;
}

function renderTitle(input) {
    const title = input.getAttribute('data-title');
    document.getElementById('title').insertAdjacentHTML('beforeend', title);
}

function renderReferrer() {
    document.write(document.referrer);
}
