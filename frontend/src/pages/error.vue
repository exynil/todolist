<template>
  <div class="fullscreen bg-grey-2 text-center q-pa-md flex flex-center">
    <div>
      <div class="text-grey-9" style="font-size: 15vh;">
        <q-icon name="warning" />
      </div>

      <div class="text-grey-9">
        Не удалось подключиться к серверу.
      </div>

      <q-btn
        class="q-mt-xl"
        color="grey-9"
        unelevated
        to="/"
        label="Повторить"
        no-caps
      />
    </div>
  </div>
</template>