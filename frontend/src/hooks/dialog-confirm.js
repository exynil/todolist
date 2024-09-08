import { Dialog } from "quasar";

export default function dialogConfirm(message, event) {
  /**
   * Функция выводит диалоговое окно с подтверждением
   *  @param {string} message Сообщение
   *  @param {function} event Событие на случай подтверждения
   */
  Dialog.create({
    message: message,
    cancel: true,
    html: true,
    ok: {
      label: "Да",
    },
  })
    .onOk(() => {
      event();
    })
    .onCancel(() => {})
    .onDismiss(() => {});
}
