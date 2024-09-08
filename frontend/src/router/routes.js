import Home from "@/pages/home.vue";
import Tasks from "@/pages/tasks/tasks.vue";

export default [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { layout: "empty", needsAuthorization: true },
  },
  {
    path: "/tasks",
    name: "Tasks",
    component: Tasks,
    meta: { layout: "default", needsAuthorization: true },
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: () => import("../pages/sign-up/sign-up.vue"),
    meta: { layout: "empty", needsAuthorization: false },
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: () => import("../pages/log-in/log-in.vue"),
    meta: { layout: "empty", needsAuthorization: false },
  },
  {
    path: "/error",
    component: () => import("@/pages/error.vue"),
    meta: { layout: "empty", needsAuthorization: false },
  },
  {
    path: "/:catchAll(.*)",
    component: () => import("@/pages/error-404.vue"),
    meta: { layout: "empty", needsAuthorization: false },
  },
];
