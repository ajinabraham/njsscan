app.get('/', function (req, res) {
    try {
        foo;
    }
    catch (err) {
        res.statusCode = 500;
        res.setHeader("Content-Type", "text/plain");
        res.end("error happend");
        return;
    }
});

try {
    throw new Error("Something unexpected has occurred.");
} catch (e) {
    console.error("some error happend");
}