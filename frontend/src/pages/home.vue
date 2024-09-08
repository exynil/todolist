<template>

</template>

<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

const store = useStore();
const router = useRouter();

onMounted(async () => {
  if (localStorage.getItem("token")) {
    await store.dispatch("getUser");

    if (store.getters["isAuthenticated"]) {
      router.push("/tasks");
      return;
    }
  }
});

document.title = "Главная";
</script>
