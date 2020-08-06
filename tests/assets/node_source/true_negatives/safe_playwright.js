const { chromium } = require('playwright');

app.post('/ok', async (req, res) => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    let url = 'https://hardcoded.url.com'
    // ok
    await page.goto('https://example.com');

    // ok
    await page.goto(url);


    await page.screenshot({ path: 'example.png' });
    await browser.close();
})

app.post('/ok', async (req, res) => {
    const browser = await chromium.launch();
    const page = await browser.newPage();

    // ok
    await page.setContent('<html></html>');

    await page.screenshot({ path: 'example.png' });
    await browser.close();
});

app.post('/ok', async (req, res) => {

    const browser = await chromium.launch();
    const page = await browser.newPage();

    // ok
    await page.evaluate(x => console.log(x), 5);


    await page.screenshot({ path: 'example.png' });
    await browser.close();
})

app.post('/ok', async (req, res) => {

    const browser = await chromium.launch();
    const page = await browser.newPage();

    // ok
    await page.evaluate(x => console.log(x), 5);

    await page.screenshot({ path: 'example.png' });
    await browser.close();
})