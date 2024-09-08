import { Loading } from "quasar";
import router from "@/router";
import { Auth } from "@/api";

export const getUser = async (ctx) => {
  Loading.show();

  await Auth.User.me()
    .then((r) => ctx.commit("SET_USER", r.data))
    .catch((e) => {});

  Loading.hide();
};

export const logout = async (ctx) => {
  Loading.show();

  await Auth.logout()
    .then((r) => {
      ctx.commit("RESET_STATE");
      router.push("/");
    })
    .catch((e) => {});

  Loading.hide();
};