import api from "./api";

const EDN_POINT = "auth";

export default {
  login(data) {
    api.defaults.headers.Authorization = "";
    return api.post(`${EDN_POINT}/token/login/`, data);
  },
  signup(data) {
    return api.post(`${EDN_POINT}/users/`, data);
  },
  logout() {
    return api.post(`${EDN_POINT}/token/logout/`);
  },
  User: {
    me(params) {
      const TOKEN = localStorage.getItem("token");
      api.defaults.headers.Authorization = `Token ${TOKEN}`;
      return api.get(`${EDN_POINT}/users/me/`, { params: params });
    },
  },
};
