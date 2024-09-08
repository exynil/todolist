import { version } from '../../package.json';

const CONF = Object.freeze({
  VERSION: version,
  NODE_ENV: import.meta.env.VITE_APP_NODE_ENV,
  TEST: import.meta.env.VITE_APP_TEST === "true",
  VUEX_STRICT: import.meta.env.VITE_APP_VUEX_STRICT === "true",
  WSGI_BASE_URL: import.meta.env.VITE_APP_WSGI_BASE_URL,
});

export default CONF;
