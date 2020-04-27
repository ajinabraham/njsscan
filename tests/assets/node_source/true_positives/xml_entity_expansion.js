app.get('/expat', function (req, res) {
    var parser = new expat.Parser();
    parser.write(req.param("xml"));
})