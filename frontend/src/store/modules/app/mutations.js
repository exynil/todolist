import { api } from "@/api";

export function SET_USER(state, user) {
  state.user = user;
  state.isAuthenticated = true;
}

export function RESET_STATE(state) {
  state.user = null;

  state.isAuthenticated = false;
  localStorage.removeItem("token");
  api.defaults.headers.Authorization = "";
}
