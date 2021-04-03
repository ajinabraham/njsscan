module.exports = {
// ok: sequelize_tls
local: {
    username: "AppUser",
    database: "AppDb",
    dialect: "postgres",
    host: "127.0.0.1",
    dialectOptions: {
    ssl: {
        minVersion: 'TLSv1.3'
    }
    }
}
};

module.exports = {
// ok: sequelize_tls
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
