const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});

module.exports = {
  e2e: {
    setupNodeEvents(on, config) {
      // Configura o tamanho da viewport globalmente
      config.viewportWidth = 1920;
      config.viewportHeight = 1080;
      return config;
    },
  },
};