const mainWindow = new BrowserWindow({
    webPreferences: {
        webSecurity: true
    }
})

const config = {
    webPreferences: {
        webSecurity: true
    }
}
var newwin = new BrowserWindow(config)

const mainWindow = new BrowserWindow({
    webPreferences: {
        allowRunningInsecureContent: false
    }
})

var x = new BrowserWindow({
    webPreferences: {
        webSecurity: true,
        allowRunningInsecureContent: false
    }
})


const mainWindow = new BrowserWindow({
    webPreferences: {
        allowRunningInsecureContent: false
    }
})

const mainWindow = new BrowserWindow({
    webPreferences: {
        nodeIntegration: false,
        nodeIntegrationInWorker: false
    }
})

