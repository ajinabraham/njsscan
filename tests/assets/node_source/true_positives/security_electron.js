const mainWindow = new BrowserWindow({
    webPreferences: {
        webSecurity: false
    }
})

const config = {
    webPreferences: {
        webSecurity: false
    }
}
var newwin = new BrowserWindow(config)

const mainWindow = new BrowserWindow({
    webPreferences: {
        allowRunningInsecureContent: true
    }
})

var x = new BrowserWindow({
    webPreferences: {
        webSecurity: false,
        allowRunningInsecureContent: true
    }
})

const mainWindow = new BrowserWindow({
    webPreferences: {
        enableBlinkFeatures: 'ExecCommandInJavaScript'
    }
})

const mainWindow = new BrowserWindow({
    webPreferences: {
        allowRunningInsecureContent: true
    }
})

const mainWindow = new BrowserWindow({
    webPreferences: {
        nodeIntegration: true,
        nodeIntegrationInWorker: true
    }
})

const mainWindow = new BrowserWindow({
    webPreferences: {
        contextIsolation: false,
        preload: path.join(app.getAppPath(), 'preload.js')
    }
})
const mainWindow = new BrowserWindow({
    webPreferences: {
        experimentalFeatures: true
    }
})