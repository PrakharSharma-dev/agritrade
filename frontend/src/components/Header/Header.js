/**
 * Header Component Logic
 */
export default {
  name: 'Header',
  props: {
    userEmail: {
      type: String,
      default: ''
    }
  },
  emits: ['logout'],
  setup(props, { emit }) {
    function handleLogout() {
      emit('logout');
    }

    return {
      handleLogout
    };
  }
};
