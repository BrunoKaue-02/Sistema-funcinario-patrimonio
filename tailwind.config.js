/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",  // templates Flask
    "./app/**/*.html",            // caso use views fora da pasta templates
    "./**/*.py",                  // para detectar classes dentro de Jinja/Python
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
