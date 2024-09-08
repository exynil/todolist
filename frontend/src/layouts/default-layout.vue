<template>
  <q-layout view="hHh Lpr lff" class="shadow-2 rounded-borders" v-if="currentUser !== null">
    <q-header elevated class="bg-primary">
      <q-toolbar>
        <q-toolbar-title>
          <q-btn flat :label="`${currentUser.username}`" />
        </q-toolbar-title>

        <q-btn flat icon="logout" @click="$store.dispatch('logout')">
        </q-btn>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { computed, ref } from "vue";
import { useStore } from "vuex";

const store = useStore();

const currentUser = computed(() => store.getters["user"]);
</script>
