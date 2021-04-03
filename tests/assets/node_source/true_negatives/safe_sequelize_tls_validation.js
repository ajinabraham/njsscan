// Example for postgresql
module.exports = {

  // ok: sequelize_tls_cert_validation
  dev: {
    username: "0xdbe",
    database: "app_db",
    dialect: "postgres",
    host: "127.0.0.1",
    dialectOptions: {
      ssl: true
      }
  }
};
