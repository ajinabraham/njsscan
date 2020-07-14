
function testOk1() {
    // ok
    var { credentials, Client } = require('grpc');
    var channel_creds = credentials.createSsl(root_certs);
    var client = new Client(address, channel_creds);

    client.list({}, function (error, books) {
        if (error)
            console.log('Error: ', error);
        else
            console.log(books);
    });
}