import { ref, onMounted, provide } from 'vue';
import Dashboard from './pages/Dashboard/Dashboard.vue';
import Login from './pages/Login/Login.vue';
import { getStoredAuth, logoutUser } from './services/api';
import { useI18n } from './i18n';

export default {
  name: 'App',
  components: {
    Dashboard,
    Login
  },
  setup() {
    const i18n = useI18n();
    provide('i18n', i18n);
    const isAuthenticated = ref(false);
    const currentUserEmail = ref('');

    onMounted(() => {
      const auth = getStoredAuth();
      if (auth.isAuthenticated) {
        isAuthenticated.value = true;
        currentUserEmail.value = auth.email || 'farmer@agritrade.in';
      }
    });

    function handleLoginSuccess({ token, email }) {
      isAuthenticated.value = true;
      currentUserEmail.value = email;
    }

    function handleLogout() {
      logoutUser();
      isAuthenticated.value = false;
      currentUserEmail.value = '';
    }

    return {
      isAuthenticated,
      currentUserEmail,
      handleLoginSuccess,
      handleLogout
    };
  }
};
