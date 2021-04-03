module.exports = {
local: {
    username: "AppUser",
    database: "AppDb",
    dialect: "postgres",
    host: "127.0.0.1",
    dialectOptions: {
    // ok: sequelize_weak_tls
    ssl: {
        minVersion: 'TLSv1.2'
    }
    }
}
};
// ok: sequelize_weak_tls
module.exports = {
local: {
    username: "AppUser",
    database: "AppDb",
    dialect: "postgres",
    host: "127.0.0.1",
    dialectOptions: {
        ssl: true
    }
}
};