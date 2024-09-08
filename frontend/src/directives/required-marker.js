export default {
  // Директива вставляет внутрь элемента span с красной полужирной звёздочкой.
  // Используется для отметки полей обязательных к заполнению.
  mounted(el, binding, vnode) {
    let span = document.createElement("span");
    span.classList.add('text-red');
    span.classList.add('text-weight-bold');
    span.innerHTML = "* ";
    el.insertBefore(span, el.firstChild);
  },
};
