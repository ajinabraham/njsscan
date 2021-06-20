module.exports = {
    local: {
        username: "AppUser",
        database: "AppDb",
        dialect: "postgres",
        host: "127.0.0.1",
        dialectOptions: {
        // ruleid: sequelize_weak_tls
        ssl: {
            minVersion: 'TLSv1'
        }
        }
    }
    };
    
    module.exports = {
    local: {
        username: "AppUser",
        database: "AppDb",
        dialect: "postgres",
        host: "127.0.0.1",
        dialectOptions: {
        // ruleid: sequelize_weak_tls
        ssl: {
            minVersion: 'TLSv1.1'
        }
        }
    }
    };
    
    module.exports = {
    local: {
        username: "AppUser",
        database: "AppDb",
        dialect: "mysql",
        host: "127.0.0.1",
        dialectOptions: {
        // ruleid: sequelize_weak_tls
        ssl: {
            minVersion: 'TLSv1.1'
        }
        }
    }
    };
    
    module.exports = {
    local: {
        username: "AppUser",
        database: "AppDb",
        dialect: "mariadb",
        host: "127.0.0.1",
        dialectOptions: {
        // ruleid: sequelize_weak_tls
        ssl: {
            minVersion: 'TLSv1.1'
        }
        }
    }
    };
    
    