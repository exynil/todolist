import api from "./api";

const END_POINT = "tasks/";

export default {
  create(data) {
    return api.post(`${END_POINT}`, data);
  },
  update(id, data) {
    return api.patch(`${END_POINT}${id}/`, data);
  },
  list(params) {
    return api.get(END_POINT, { params: params });
  },
  delete(id) {
    return api.delete(`${END_POINT}${id}/`);
  },
  get(id) {
    return api.get(`${EDN_POINT}${id}/`);
  },
  toggleStatus(id) {
    return api.patch(`${END_POINT}${id}/toggle-status/`);
  }
  // getNumberOfUnverifiedWorks(id) {
  //   return api.get(`${EDN_POINT}/${id}/get-number-of-unverified-works/`);
  // },
  // getNumberOfRejectedWorks(id) {
  //   return api.get(`${EDN_POINT}/${id}/get-number-of-rejected-works/`);
  // },
  // getTotalHours(id) {
  //   return api.get(`${EDN_POINT}/${id}/get-total-hours/`);
  // },
  // recalculatePlanHours(id) {
  //   return api.patch(`${EDN_POINT}/${id}/recalculate-hours/`);
  // },
  // getUnverifiedPlans(params) {
  //   return api.get(`${EDN_POINT}/`, { params: params });
  // },
  // Comment: {
  //   list(params) {
  //     return api.get(`${EDN_POINT}/comments/`, { params: params });
  //   },
  //   create(data) {
  //     return api.post(`${EDN_POINT}/comments/`, data);
  //   },
  // },
  // History: {
  //   list(params = {}) {
  //     return api.get(`${EDN_POINT}/plan-histories/`, { params: params });
  //   },
  // },
};
